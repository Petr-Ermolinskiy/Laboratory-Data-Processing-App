import os
import sys

import numpy as np
import pandas as pd
from loguru import logger

# ----------------------------------------------- #
logger.remove()

try:
    logger.add(sys.stderr, format="<green>{time:HH:mm:ss}</green> | {level} | {message}", level="INFO")
except Exception as e:
    print(f"Нельзя импортировать: {e}")
# ----------------------------------------------- #


def compare_excel_files(  # noqa: C901, PLR0912, PLR0915
    file1_path: str,
    file2_path: str,
    *,
    check_index: bool = False,
    tolerance: float = 1e-10,
) -> tuple[bool, dict]:
    """
    Сравнивает два Excel файла на наличие одинаковых данных во ВСЕХ листах.

    :param file1_path: Путь к первому файлу Excel
    :param file2_path: Путь ко второму файлу Excel
    :param check_index: Сравнивать ли индексы DataFrame (по умолчанию: False)
    :param tolerance: Допуск для сравнения чисел с плавающей точкой
    :return: Кортеж (all_sheets_match: bool, comparison_details: dict)
    """
    if not os.path.exists(file1_path):
        return False, {
            "error": f"Файл не найден: {file1_path}",
            "file1": file1_path,
            "file2": file2_path,
            "file1_exists": False,
            "file2_exists": os.path.exists(file2_path) if file2_path else False,
        }

    if not os.path.exists(file2_path):
        return False, {
            "error": f"Файл не найден: {file2_path}",
            "file1": file1_path,
            "file2": file2_path,
            "file1_exists": os.path.exists(file1_path),
            "file2_exists": False,
        }

    try:
        # Читаем оба Excel файла со всеми листами
        excel1 = pd.read_excel(file1_path, sheet_name=None, dtype=object)
        excel2 = pd.read_excel(file2_path, sheet_name=None, dtype=object)

        # Получаем названия листов из каждого файла
        sheets1 = set(excel1.keys())
        sheets2 = set(excel2.keys())

        # Создаем словарь для хранения результатов сравнения
        comparison_result = {
            "file1": file1_path,
            "file2": file2_path,
            "sheets_match": False,
            "same_sheet_names": (sheets1 == sheets2),
            "sheet_count_match": (len(sheets1) == len(sheets2)),
            "sheet_comparisons": {},
            "differences": [],
        }

        # Объединяем все названия листов для последовательного сравнения
        all_sheets = sheets1.union(sheets2)

        all_sheets_match = True

        # Проходим по каждому листу
        for sheet_name in all_sheets:
            # Создаем словарь для результатов сравнения текущего листа
            sheet_comparison = {
                "exists_in_both": False,
                "shape_match": False,
                "columns_match": False,
                "data_match": False,
                "dtypes_match": False,
                "differences": [],
            }

            # Проверяем, существует ли лист в обоих файлах
            if sheet_name in excel1 and sheet_name in excel2:
                sheet_comparison["exists_in_both"] = True

                df1 = excel1[sheet_name]
                df2 = excel2[sheet_name]

                # Проверяем размерность данных (количество строк и столбцов)
                sheet_comparison["shape_match"] = df1.shape == df2.shape

                # Проверяем названия столбцов
                cols1 = set(df1.columns)
                cols2 = set(df2.columns)
                sheet_comparison["columns_match"] = cols1 == cols2

                # Проверяем типы данных (необязательная проверка)
                try:
                    # Пытаемся привести к одинаковым типам данных для сравнения
                    df1_comparison = df1.convert_dtypes()
                    df2_comparison = df2.convert_dtypes()
                    sheet_comparison["dtypes_match"] = df1_comparison.dtypes.equals(
                        df2_comparison.dtypes
                    )
                except Exception:
                    sheet_comparison["dtypes_match"] = "Сравнение пропущено"

                # Сравниваем содержимое данных, если размерность и столбцы совпадают
                if sheet_comparison["shape_match"] and sheet_comparison["columns_match"]:
                    try:
                        # Упорядочиваем столбцы в одинаковом порядке
                        df2_aligned = df2[df1.columns]

                        # Сбрасываем индексы, если не нужно их сравнивать
                        if not check_index:
                            df1_reset = df1.reset_index(drop=True)
                            df2_reset = df2_aligned.reset_index(drop=True)
                        else:
                            df1_reset = df1
                            df2_reset = df2_aligned

                        # Сравниваем DataFrame с помощью встроенного метода
                        if df1_reset.equals(df2_reset):
                            sheet_comparison["data_match"] = True
                        else:
                            # Более детальное сравнение с учетом числового допуска
                            try:
                                # Используем numpy для точного сравнения чисел с плавающей точкой

                                # Конвертируем в numpy массивы для сравнения
                                arr1 = df1_reset.to_numpy()
                                arr2 = df2_reset.to_numpy()

                                # Обрабатываем NaN значения отдельно
                                mask1 = pd.isna(arr1)
                                mask2 = pd.isna(arr2)

                                # Проверяем, совпадают ли позиции NaN значений
                                nan_match = np.array_equal(mask1, mask2, equal_nan=True)

                                if nan_match:
                                    # Для не-NaN значений сравниваем с допуском
                                    non_nan_mask = ~mask1
                                    if non_nan_mask.any():
                                        # Сравниваем числовые значения с указанным допуском
                                        numerical_close = np.allclose(
                                            arr1[non_nan_mask].astype(float),
                                            arr2[non_nan_mask].astype(float),
                                            rtol=tolerance,
                                            atol=tolerance,
                                            equal_nan=True,
                                        )
                                        sheet_comparison["data_match"] = numerical_close
                                    else:
                                        # Все значения NaN
                                        sheet_comparison["data_match"] = True
                                else:
                                    sheet_comparison["data_match"] = False

                            except (ValueError, TypeError):
                                logger.info(
                                    "Сравнение данных в excel: сравнение через numpy не удалось"
                                )

                                # Резервный вариант: точное сравнение, если сравнение через numpy не удалось
                                sheet_comparison["data_match"] = False

                            # Если данные не совпадают, находим конкретные различия
                            if not sheet_comparison["data_match"]:
                                # Создаем маску различий -- заполняем изначально пропуски
                                diff_mask = ~(df1_reset.fillna(-1) == df2_reset.fillna(-1))
                                diff_locations = diff_mask.stack()  # noqa: PD013
                                diff_cells = diff_locations[diff_locations].index.tolist()

                                if diff_cells:
                                    sample_diffs = []
                                    # Ограничиваем вывод 10 различиями для читаемости
                                    for row_idx, col_name in diff_cells[:10]:
                                        val1 = df1_reset.at[row_idx, col_name]
                                        val2 = df2_reset.at[row_idx, col_name]

                                        if (
                                            isinstance(val1, float)
                                            and isinstance(val2, float)
                                            and np.allclose(
                                                val1,
                                                val2,
                                                rtol=tolerance,
                                                atol=tolerance,
                                                equal_nan=True,
                                            )
                                        ):
                                            continue

                                        sample_diffs.append({
                                            "row": row_idx,
                                            "column": col_name,
                                            "file1_value": val1,
                                            "file2_value": val2,
                                        })
                                    # может быть такая ситуация, что нет ошибок, тогда все данные идентичны
                                    if len(sample_diffs) == 0:
                                        sheet_comparison["data_match"] = True
                                    else:
                                        sheet_comparison["differences"] = sample_diffs

                    except Exception as e:
                        sheet_comparison["data_match"] = False
                        sheet_comparison["differences"].append(f"Ошибка сравнения: {e}")

                # Обновляем общий статус сравнения
                sheet_match = (
                    sheet_comparison["exists_in_both"]
                    and sheet_comparison["shape_match"]
                    and sheet_comparison["columns_match"]
                    and sheet_comparison["data_match"]
                )

                # Если листы не совпадают, добавляем информацию о различии
                if not sheet_match:
                    all_sheets_match = False
                    diff_msg = f"Лист '{sheet_name}' отличается"
                    if sheet_comparison["differences"]:
                        diff_msg += f" - Пример различий: {sheet_comparison['differences'][:3]}"
                    comparison_result["differences"].append(diff_msg)

            else:
                # Лист отсутствует в одном из файлов
                all_sheets_match = False
                missing_in = "file2" if sheet_name in excel1 else "file1"
                sheet_comparison["differences"].append(f"Лист отсутствует в {missing_in}")
                comparison_result["differences"].append(
                    f"Лист '{sheet_name}' существует только в {missing_in}"
                )

            # Сохраняем результаты сравнения для текущего листа
            comparison_result["sheet_comparisons"][sheet_name] = sheet_comparison

        # Сохраняем общий результат сравнения всех листов
        comparison_result["sheets_match"] = all_sheets_match

        return all_sheets_match, comparison_result  # noqa: TRY300

    except Exception as e:
        # Обработка ошибок при чтении файлов или сравнении
        error_msg = f"Ошибка при сравнении файлов: {e!s}"
        return False, {"error": error_msg, "file1": file1_path, "file2": file2_path}
