import gc
import json
import os
import platform
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

import pytest
from compare_excel import compare_excel_files
from loguru import logger
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMessageBox

# добавим возможность импорта из директории выше
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# главный класс MainWindowProcessingApp
from main_window_processing_app import MainWindowProcessingApp

# ----------------------------------------------- #
logger.remove()

try:
    logger.add(
        sys.stderr, format="<green>{time:HH:mm:ss}</green> | {level} | {message}", level="INFO"
    )
except Exception as e:
    print(f"Нельзя импортировать: {e}")
# ----------------------------------------------- #

"""
===============
Общее для всех тестов
===============
"""


def get_abs_path(path: str) -> str:
    return str(Path(__file__).parent / path)


def auto_close_message_box(timeout: int = 1) -> None:
    """Monkey patch для сообщений."""
    original_exec = QMessageBox.exec

    def patched_exec(self):
        timer = QTimer(self)
        timer.timeout.connect(self.close)
        timer.start(timeout * 1000)
        return original_exec(self)

    QMessageBox.exec = patched_exec


@pytest.fixture(autouse=True)
def auto_close_message_boxes() -> None:
    auto_close_message_box(timeout=3)


@pytest.fixture(scope="session")
def app() -> QApplication:
    # создаем один QApplication для всей сессии
    application = QApplication.instance()
    if application is None:
        application = QApplication(sys.argv)
    yield application
    logger.info("------ application.quit()")
    # завершаем работу
    application.quit()


@pytest.fixture(scope="session")
def data_folder() -> str:
    # сегодняшняя дата
    now_date = datetime.now().strftime("%Y-%m-%d")  # noqa: DTZ005
    # путь к новой папке
    path_to_test_folder = get_abs_path(f"temp_data_{now_date}")

    # копируем папку с данными и в ней будем проводить тесты
    shutil.copytree(get_abs_path("data"), path_to_test_folder, dirs_exist_ok=True)
    return path_to_test_folder


@pytest.fixture(scope="session")
def window() -> None:
    window = MainWindowProcessingApp()
    return window


@pytest.fixture(scope="session", autouse=True)
def cleanup_folder_after_app(pytestconfig, data_folder, app) -> None:
    """Отдельный fixture для очистки папки ПОСЛЕ закрытия app."""
    yield  # Все тесты выполняются здесь

    # завершаем работу -- проверим, не было ли ошибок
    session = pytestconfig.pluginmanager.get_plugin("terminalreporter")
    if session is not None and hasattr(session.stats, "get"):
        failed = len(session.stats.get("failed", []))

        if failed == 0:  # все тесты прошли
            if os.path.exists(data_folder):
                logger.info("✓ Все тесты прошли -- очистка папки...")

                # Добавляем retry логику с принудительным закрытием файлов
                max_retries = 5
                for attempt in range(max_retries):
                    try:
                        shutil.rmtree(data_folder)
                        logger.info(f"✓ Папка успешно удалена (попытка {attempt + 1})")
                        break
                    except PermissionError as e:
                        if attempt == max_retries - 1:
                            logger.error(
                                f"✗ Не удалось удалить папку после {max_retries} попыток: {e}"
                            )
                            raise

                        logger.warning(
                            f"Попытка {attempt + 1}: файлы все еще открыты, жду 0.5 сек..."
                        )
                        time.sleep(0.5)
                        gc.collect()  # Принудительный сбор мусора
        else:
            logger.info("✗ Тесты упали - папка не будет очищена")


"""
===============
Тесты
===============
"""


def test_rheo_scan_1_level(
    app: QApplication, window: MainWindowProcessingApp, data_folder: str
) -> None:
    logger.info("--- RheoScan: level=1  ---")

    # выставляем нужные переменные
    window.ui.main_path.setText(str(Path(data_folder) / "RheoScan_1_level"))
    window.ui.spinBox_level.setValue(1)

    window.ui.check_save_RheoScan_overall.setChecked(True)

    # выполняем обработку данных
    window.RheoScan()

    logger.info("Все проверки для RheoScan прошли (level=1)")


def test_rheo_scan_2_level(
    app: QApplication, window: MainWindowProcessingApp, data_folder: str
) -> None:
    logger.info("--- RheoScan: level=2  ---")

    # выставляем нужные переменные
    window.ui.main_path.setText(str(Path(data_folder) / "RheoScan_2_level"))
    window.ui.spinBox_level.setValue(2)

    window.ui.check_approx_agg.setChecked(True)
    window.ui.check_approx_deform.setChecked(True)
    window.ui.check_dop_CSS_parameter.setChecked(True)
    window.ui.check_stat_for_column.setChecked(True)
    window.ui.vibros_delete.setChecked(True)
    window.ui.check_save_csv.setChecked(True)
    window.ui.check_approx_deform_raw_data.setChecked(True)
    window.ui.check_save_RheoScan_overall.setChecked(False)

    window.ui.comboBox_RheoScan_path_save.setCurrentText("Сохранить excel/cvs файлы в одном месте")

    # выполняем обработку данных
    window.RheoScan()

    logger.info("Все проверки для RheoScan прошли (level=2)")


def test_lt(app: QApplication, window: MainWindowProcessingApp, data_folder: str) -> None:
    logger.info("--- Лазерный пинцет  ---")

    # выставляем нужные переменные
    window.ui.path_for_LT.setText(str(Path(data_folder) / "Лазерный_пинцет"))

    # выполняем обработку данных
    window.LT()

    # проверка на файлы
    check_, diff = compare_excel_files(
        str(Path(data_folder) / "Лазерный_пинцет" / "Лазерный_пинцет.xlsx"),
        str(Path(data_folder) / "check_" / "Лазерный_пинцет_check.xlsx"),
    )

    if not check_:
        # сохраняем файл
        with open(
            str(Path(data_folder) / "Лазерный_пинцет" / "отличие.json"), "w", encoding="utf-8"
        ) as file:
            json.dump(diff, file, indent=4, ensure_ascii=False)

        msg = "Файлы отличаются"
        raise AssertionError(msg)

    logger.info("Все проверки для Лазерного пинцета прошли")


def test_biola(app: QApplication, window: MainWindowProcessingApp, data_folder: str) -> None:
    logger.info("--- Biola  ---")

    # выставляем нужные переменные
    window.ui.path_for_biola.setText(str(Path(data_folder) / "Biola"))
    window.ui.comboBox_biola.setCurrentText("test.txt")

    # выполняем обработку данных
    window.biola_do()

    # проверка на файлы
    check_, diff = compare_excel_files(
        str(Path(data_folder) / "Biola" / "test_agg.xlsx"),
        str(Path(data_folder) / "check_" / "test_agg_check.xlsx"),
    )

    if not check_:
        # сохраняем файл
        with open(str(Path(data_folder) / "Biola" / "отличие.json"), "w", encoding="utf-8") as file:
            json.dump(diff, file, indent=4, ensure_ascii=False)

        msg = "Файлы отличаются"
        raise AssertionError(msg)

    logger.info("Все проверки для Биола прошли")


def test_figs(app: QApplication, window: MainWindowProcessingApp, data_folder: str) -> None:
    logger.info("--- Обработка данных: графики  ---")

    # выставляем нужные переменные
    window.ui.path_for_plot.setText(str(Path(data_folder) / "Обработка_данных"))
    window.ui.comboBox.setCurrentText("test.xlsx")
    window.ui.comboBox_2.setCurrentText("пол")

    window.ui.check_corr_matrix.setChecked(True)
    window.ui.check_corr_figs.setChecked(True)
    window.ui.check_box_pairplot.setChecked(True)
    window.ui.check_jointplot.setChecked(True)

    # выполняем обработку данных
    window.figures_and_stuff()

    # корреляция по одному параметру
    window.ui.comboBox.setCurrentText("test2.xlsx")
    window.ui.comboBox_2.setCurrentText("par1")
    window.ui.check_corr_one_parameter.setChecked(True)
    window.ui.check_corr_one_parameter_plot_sep_wind.setChecked(False)
    window.ui.doubleSpinBox_one_correlation.setValue(0)
    # выполняем обработку данных
    window.figures_and_stuff()

    logger.info("Все проверки для построения рисунков прошли")


def test_profile(app: QApplication, window: MainWindowProcessingApp, data_folder: str) -> None:
    logger.info("--- Обработка данных: микрореологический профиль  ---")

    # выставляем нужные переменные
    window.ui.path_for_profile.setText(str(Path(data_folder) / "Обработка_данных"))

    window.ui.patient_data.setText("norm")
    window.ui.norm_data.setText("norm")

    # выполняем обработку данных
    window.profile_of_patient()

    logger.info("Все проверки для построения микрореологического профиля прошли")


def test_table(app: QApplication, window: MainWindowProcessingApp, data_folder: str) -> None:
    logger.info("--- Обработка данных: сводные таблицы  ---")

    # выставляем нужные переменные
    window.ui.path_for_pivot_table.setText(str(Path(data_folder) / "Обработка_данных"))
    window.ui.comboBox_pivot_table.setCurrentText("test2.xlsx")

    # выполняем обработку данных
    window.pivot_table()
    window.corr_table()
    window.pivot_or_melt()

    logger.info("Все проверки для сводных таблиц прошли")


def test_catplot(app: QApplication, window: MainWindowProcessingApp, data_folder: str) -> None:
    logger.info("--- Обработка данных: catplot  ---")

    # выставляем нужные переменные
    window.ui.path_for_catplot.setText(str(Path(data_folder) / "Обработка_данных"))
    window.ui.comboBox_excel_catplot.setCurrentText("test.xlsx")

    # выполняем обработку данных
    window.pivot_table()
    window.corr_table()
    window.pivot_or_melt()

    logger.info("Все проверки для сводных таблиц прошли")


def test_calc_stat_significance(
    app: QApplication, window: MainWindowProcessingApp, data_folder: str
) -> None:
    logger.info("--- Обработка данных: стат.значимость  ---")
    # выставляем нужные переменные
    window.ui.path_for_dop_stat.setText(str(Path(data_folder) / "Обработка_данных"))
    window.ui.comboBox_excel_dop_stat.setCurrentText("test2.xlsx")

    # выполняем обработку данных
    window.p_value_calc()

    p_value = window.ui.p_value_dop_stat.text()

    assert float(p_value) == 1.0, "p_value должен быть 1.0"

    logger.info("Все проверки по расчету стат.значимости прошли")


def test_rheo_scan_post_processing(
    app: QApplication, window: MainWindowProcessingApp, data_folder: str
) -> None:
    logger.info("--- RheoScan: сводные таблицы  ---")

    # выставляем нужные переменные
    window.ui.path_for_RheoScan_describe.setText(str(Path(data_folder) / "RheoScan_2_level"))

    # выполняем обработку данных
    window.RheoScan_describe()

    # на Windows и Mac могут быть различия в Numpy обработки данных с точки зрения аппроксимации
    # поэтому надо сделать разный порог для сравнения -- tolerance
    tolerance = 1e-10 if platform.system() == "Windows" else 1e-6

    # проверка на файлы
    check_, diff = compare_excel_files(
        str(Path(data_folder) / "RheoScan_2_level" / "RheoScan_summary.xlsx"),
        str(Path(data_folder) / "check_" / "RheoScan_summary_check.xlsx"),
        tolerance=tolerance,
    )

    if not check_:
        # сохраняем файл
        with open(
            str(Path(data_folder) / "RheoScan_2_level" / "отличие.json"), "w", encoding="utf-8"
        ) as file:
            json.dump(diff, file, indent=4, ensure_ascii=False)

        msg = "Файлы отличаются"
        raise AssertionError(msg)

    logger.info("Все проверки по обработки данных RheoScan прошли")
