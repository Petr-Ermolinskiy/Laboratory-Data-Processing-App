from pathlib import Path

import pandas as pd
from PySide6.QtWidgets import QMessageBox

from ..utils_dop.const_vals import COLS_MNOI_RHEOSCAN_DICT


def rheo_scan_describe_file_or_files(self):
    dlg = QMessageBox(self)
    # путь
    path = self.ui.path_for_RheoScan_describe.text()
    if path == "":
        dlg.setWindowTitle("Обработка файлов RheoScan")
        dlg.setText("Не введен путь к excel файлу")
        dlg.exec()
        return

    # флаг, что будем смотреть только колонки как в файле
    make_as_remote = self.ui.checkBox_save_additional_excel_list_rheoscan.isChecked()

    if self.ui.RheoScan_describe_mask_sheets.text() == "":
        mask = None
    else:
        try:
            mask = self.ui.RheoScan_describe_mask_sheets.text()
            mask = mask.split(" ")
            mask = [bool(strtobool(i)) for i in mask]
        except Exception as e:
            dlg.setWindowTitle("Обработка файлов RheoScan")
            dlg.setText("В поле <Расчет SD на разных листах> неправильный ввод.\n" + str(e))
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()
            return

    try:
        if self.ui.comboBox_RheoScan_describe.currentText() == "Один файл - один образец":
            _describe_all_multiple_files(path, mask, make_as_remote)
        else:
            _describe_all_one_file(path, mask, make_as_remote)
    except Exception as e:
        dlg.setWindowTitle("Обработка файлов RheoScan")
        dlg.setText("Ошибка в обработке: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    dlg.setWindowTitle("Обработка файлов RheoScan")
    dlg.setText("Все данные успешно обработаны")
    dlg.exec()
    return


# функция, когда файлов много и один файл == один образец
def _describe_all_multiple_files(
    path: str,
    mask_sheet_main=None,
    make_as_remote: bool = False,
) -> None:
    path_obj = Path(path)
    summary_file = path_obj / "RheoScan_summary.xlsx"

    files_all = list(path_obj.glob("*.xlsx"))
    if summary_file in files_all:
        files_all.remove(summary_file)

    describe_all_files = pd.DataFrame()

    for file in files_all:
        # читаем exel файл
        try:
            sheets = pd.ExcelFile(file).sheet_names
        except Exception as e:
            msg = f"Не удаётся открыть файл -- скорее всего он открыт в другой программе: {e}"
            raise ValueError(msg)  # noqa: B904

        if mask_sheet_main is None:
            mask_sheet = [True] * len(sheets)
        elif not isinstance(mask_sheet_main, list) or len(mask_sheet_main) > len(sheets):
            msg = "Переданная строка по маске не может конвертироваться в список или кол-во больше, чем кол-во листов."
            raise ValueError(msg)
        elif len(mask_sheet_main) < len(sheets):
            mask_sheet = [*mask_sheet_main, *[False] * (len(sheets) - len(mask_sheet_main))]
        else:
            mask_sheet = [False] * len(sheets)
        describe_data_frame = pd.DataFrame()
        # file name
        file_path = Path(file)
        name_of_file = file_path.stem
        for one_sheet, mask in zip(sheets, mask_sheet, strict=False):
            # -- если есть какая-то статистика, то просто пропускаем эти листы -- #
            if "-Stat" in one_sheet or one_sheet == "данные_таблица_мноц":
                continue

            # читаем exel файл
            try:
                df = pd.read_excel(str(file_path), one_sheet)
            except Exception as e:
                msg = f"Не удаётся открыть файл -- скорее всего он открыт в другой программе: {e}"
                raise ValueError(msg)  # noqa: B904

            mean_vals = df[df.columns[2:]].mean()
            if mask:
                std_vals = df[df.columns[2:]].std()
                std_vals.index = std_vals.index + "_SD"
                data_from_sheet = pd.DataFrame(
                    [pd.concat([mean_vals, std_vals])],
                    index=[name_of_file],
                )
                data_from_sheet = data_from_sheet[data_from_sheet.columns.sort_values()]
            else:
                data_from_sheet = pd.DataFrame([mean_vals], index=[name_of_file])
            describe_data_frame = pd.concat([describe_data_frame, data_from_sheet], axis=1)
        # сохраняем в основной DataFrame
        describe_all_files = pd.concat([describe_all_files, describe_data_frame], axis=0)

    # сохраняем в excel файл
    with pd.ExcelWriter(str(summary_file)) as writer:
        describe_all_files.to_excel(writer, sheet_name="Sheet1")
        if make_as_remote:
            describe_all_files[list(COLS_MNOI_RHEOSCAN_DICT.keys())].rename(
                columns=COLS_MNOI_RHEOSCAN_DICT
            )[list(COLS_MNOI_RHEOSCAN_DICT.values())].to_excel(
                writer, sheet_name="данные_таблица_мноц"
            )



# функция, когда файл один и один файл == много образцов -- причем колонка с индексами -- первая
def _describe_all_one_file(
    path: str,
    mask_sheet: list | None = None,
    make_as_remote: bool = False,
) -> None:
    describe_file = pd.DataFrame()
    sheets = pd.ExcelFile(path).sheet_names
    if mask_sheet is None:
        mask_sheet = [True] * len(sheets)
    elif not isinstance(mask_sheet, list) or len(mask_sheet) > len(sheets):
        msg = "Переданная строка по маске не может конвертироваться в список или кол-во больше, чем кол-во листов."
        raise ValueError(msg)
    elif len(mask_sheet) < len(sheets):
        mask_sheet = [*mask_sheet, *[False] * (len(sheets) - len(mask_sheet))]

    for one_sheet, mask in zip(sheets, mask_sheet, strict=False):
        # читаем exel файл
        df = pd.read_excel(path, one_sheet)

        mean_df = df.groupby(df.columns[0]).mean()

        if mask:
            std_df = df.groupby(df.columns[0]).std()
            std_df.columns = std_df.columns + "_SD"
            df_describe_for_one_sheet = pd.concat([mean_df, std_df], axis=1)
            df_describe_for_one_sheet = df_describe_for_one_sheet[
                df_describe_for_one_sheet.columns.sort_values()
            ]
        else:
            df_describe_for_one_sheet = mean_df

        # статистика
        describe_file = pd.concat([describe_file, df_describe_for_one_sheet], axis=1)

    # сохраняем в excel файл
    path_obj = Path(path)
    with pd.ExcelWriter(str(path_obj.parent / "RheoScan_summary.xlsx")) as writer:
        describe_file.to_excel(writer, sheet_name="Sheet1")
        if make_as_remote:
            describe_file[list(COLS_MNOI_RHEOSCAN_DICT.keys())].rename(
                columns=COLS_MNOI_RHEOSCAN_DICT
            )[list(COLS_MNOI_RHEOSCAN_DICT.values())].to_excel(
                writer, sheet_name="данные_таблица_мноц"
            )


def strtobool(val: str) -> int:
    """Функция для правильной интерпретации введенных значений -- 0 или 1 на выходе."""
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return 1
    if val in ("n", "no", "f", "false", "off", "0"):
        return 0
    return 1
