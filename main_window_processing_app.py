import os
import sys
from pathlib import Path

import pandas as pd
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from vcolorpicker import getColor, rgb2hex

from app.ui.ui_main import Ui_MainWindow  # UI приложения, созданный в QT Designer
from scripts.Biola.biola_concentration import conentration_to_excel

# Biola
from scripts.Biola.biola_main import biola_result

# Расчет p-value для 2 колонок
from scripts.Data_Processing.calculation_of_p_value import p_value_calc_for_two_columns
from scripts.Data_Processing.catplot_figures import plot_catplot

# Рисунки
from scripts.Data_Processing.figures import figs_plot

# Микрореологический профиль
from scripts.Data_Processing.microrheological_profile import prifile_plot

# Сводные таблицы
from scripts.Data_Processing.pivot_table_and_correlation import (
    corr_for_sheet,
    pivot_do_for_sheet,
    pivot_or_melt_excel_file,
)

# Лазерный пинцет
from scripts.Laser_Tweezers.laser_tweezers import laser_tweezers
from scripts.RheoScan.rheo_scan_describe import rheo_scan_describe_file_or_files

# обработка RheoScan
from scripts.RheoScan.rheo_scan_main import all_rheo_scan_level
from scripts.RheoScan.rheo_scan_sort import sort_rheo_scan_data

#  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  #


def get_name_out_of_path(files: list) -> list:
    """Функция, чтобы разделить путь до файла на название файла без расширений."""
    return [Path(i).name for i in files]


def resource_path(relative_path: str) -> str:
    """Получить абсолютный путь к ресурсу, нужно для PyInstaller."""
    try:
        # PyInstaller создает временную папку и сохраняет путь в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  #


class MainWindowProcessingApp(QMainWindow):
    """Главный класс, весь UI которого от Ui_MainWindow."""

    def __init__(self, version: str = "v0.0.0") -> None:
        """Инициализация -- определения UI и связка кнопок."""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # выставим необходимую версию
        self.ui.label_version.setText(version)

        #  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  #
        # КНОПКИ
        #  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  #

        # RheoScan
        self.ui.btn_save_exel_csv.pressed.connect(self.RheoScan)  # для кнопки из вкладки RheoScan
        self.ui.btn_sort_data_RheoScan.pressed.connect(
            self.RheoScan_sort_data,
        )  # для кнопки из вкладки RheoScan
        self.ui.btn_RheoScan_describe_file_or_files.pressed.connect(
            self.RheoScan_describe,
        )  # для кнопки по дополнительной обработке данных RheoScan
        self.ui.btn_dop_stat_calc.pressed.connect(
            self.p_value_calc,
        )  # для кнопки по дополнительной обработке данных - RheoScan - описать

        # Biola
        self.ui.btn_biola.pressed.connect(self.biola_do)  # для кнопки по обработки данных Biola
        self.ui.btn_biola_concentration.pressed.connect(
            self.biola_concentration,
        )  # для кнопки по обработки данных Biola

        # Лазерный пинцет
        self.ui.btn_LT.pressed.connect(self.LT)  # для кнопки по обработки данных лазерного пинцета

        # Графики
        self.ui.btn_plot_and_save_profile.pressed.connect(
            self.profile_of_patient,
        )  # для кнопки по построению микро реологического профиля
        self.ui.btn_plot_and_save_figs.pressed.connect(
            self.figures_and_stuff,
        )  # для кнопки по построению графиков
        self.ui.btn_plot_and_save_pivot_table.pressed.connect(
            self.pivot_table,
        )  # для кнопки по расчету сводных таблиц
        self.ui.btn_plot_and_save_corr_table.pressed.connect(
            self.corr_table,
        )  # для кнопки по построению корреляционной матрицы
        self.ui.btn_plot_and_save_catplot.pressed.connect(self.cat_plot)  # для кнопки по catplot
        self.ui.btn_save_pivot_or_melt.pressed.connect(
            self.pivot_or_melt,
        )  # для кнопки по расчету сводных таблиц
        self.ui.pushButton_HEX_box.pressed.connect(self.HEX_box)  # для кнопки выбора HEX цветов BOX
        self.ui.pushButton_HEX_points.pressed.connect(
            self.HEX_points,
        )  # для кнопки выбора HEX цветов точек
        self.ui.toolButton_RheoScan.pressed.connect(
            self.toolButton_RheoScan_file
        )  # для кнопки выбора папки

        # Дополнительные кнопки
        self.ui.label_info.mousePressEvent = self.info_about_programme  # для инфо

        #  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  #
        # Текстовые и другие поля
        #  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  #
        # -----------------------------------------------------#
        # путь к папке с файлами - графики
        self.ui.path_for_plot.textChanged.connect(self.add_excel_files_to_combobox)
        # обновим какие есть sheets - графики
        self.ui.comboBox.currentTextChanged.connect(self.figs_add_sheets_to_combobox)
        # обновим, какие есть колонки
        self.ui.comboBox_figs_sheets.currentTextChanged.connect(self.add_columns_sheets_to_combobox)

        # -----------------------------------------------------#
        # путь к папке с файлами - pivot
        self.ui.path_for_pivot_table.textChanged.connect(self.add_excel_files_to_combobox_pivot)
        # обновим какие есть sheets - pivot
        self.ui.comboBox_pivot_table.currentTextChanged.connect(self.add_sheets_to_combobox_pivot)
        # обновим какие есть колонки - pivot
        self.ui.comboBox_pivot_table_excel_sheet.currentTextChanged.connect(
            self.add_columns_to_combobox_pivot,
        )

        # -----------------------------------------------------#
        # для нахождения файла Biola
        self.ui.path_for_biola.textChanged.connect(self.add_biola_file)

        # -----------------------------------------------------#
        # catplot
        self.ui.path_for_catplot.textChanged.connect(self.add_excel_catplot)
        self.ui.comboBox_excel_catplot.currentTextChanged.connect(self.catplot_add_sheets)
        self.ui.comboBox_excel_sheet_catplot.currentTextChanged.connect(self.catplot_add_x_y_hue)

        # -----------------------------------------------------#
        # дополнительная статистика - расчет p-value
        self.ui.path_for_dop_stat.textChanged.connect(self.add_excel_dop_stat)
        self.ui.comboBox_excel_dop_stat.currentTextChanged.connect(self.dop_stat_add_sheets)
        self.ui.comboBox_excel_sheet_dop_stat.currentTextChanged.connect(self.dop_stat_add_x_y_hue)

        self.ui.comboBox_stat_test_dop_stat.currentTextChanged.connect(self.p_value_calc)
        self.ui.comboBox_alter_hep_dop_stat.currentTextChanged.connect(self.p_value_calc)

        # -----------------------------------------------------#
        # изменяем калибровку
        self.ui.comboBox_LT_calibration.currentTextChanged.connect(self.LT_change_calibration)

        # -----------------------------------------------------#
        # для цветов box plot
        self.ui.color_box.textChanged.connect(self.box_palette_off)
        self.ui.color_points.textChanged.connect(self.point_palette_off)

    def info_about_programme(self, _) -> None:  # noqa: ANN001
        """Информация про программу.

        :param _: Нужен этот параметр, так как передается 2 параметра функции.
        """
        info_message = QMessageBox(self)
        info_message.setWindowTitle("Информация про программу")
        first_message = (
            "Программа написана на языке Python с применением ряда библиотек Ермолинским Петром Борисовичем"
            "- аспирантом лаборатории <Биомедицинской фотоники> Физического факультета МГУ имени М.В. Ломоносова."
            " Исходный код доступен в репозитории GitHub на странице:"
        )
        url_message = "https://github.com/Petr-Ermolinskiy"
        message = first_message + "\n" + url_message
        info_message.setText(message)
        info_message.exec()

    @Slot(int)
    def on_comboBox_style_sheet_currentIndexChanged(self, index: int) -> None:  # noqa: N802
        """Изменим стиль - светлая или темная тема. См. 'comboBox_style_sheet' в UI.

        :param index: Индекс файла qss. Пока только один.
        :return:
        """
        if index == 1:
            with open(resource_path("app/style/style_dark.qss")) as f:
                _style = f.read()
            self.setStyleSheet(_style)
        else:
            self.setStyleSheet("")

    """
    = = = = = = = = = = = = = = =
    Функции при нажатии на кнопки
    = = = = = = = = = = = = = = =
    """

    # - - - - - - - - - #
    # RheoScan
    # - - - - - - - - - #
    def RheoScan(self) -> None:  # noqa: N802
        """Основная обработка данных RheoScan."""
        all_rheo_scan_level(self)

    def RheoScan_sort_data(self) -> None:  # noqa: N802
        """Сортировка данных RheoScan."""
        sort_rheo_scan_data(self)

    def RheoScan_describe(self) -> None:  # noqa: N802
        """Описание -- статистика по данным. Этот метод находится в отделе обработки данных."""
        rheo_scan_describe_file_or_files(self)

    # - - - - - - - - - #
    # Biola
    # - - - - - - - - - #
    def biola_do(self) -> None:
        """Основная функция извлечения данных Biola из txt файла."""
        biola_result(self)

    def biola_concentration(self) -> None:
        """Извлечение данных Biola из PDF файла для "Счета."""
        conentration_to_excel(
            self,
            self.ui.path_for_biola.text(),
            self.ui.comboBox_biola_concentration.currentText(),
        )

    # - - - - - - - - - #
    # Лазерный пинцет
    # - - - - - - - - - #
    def LT(self) -> None:  # noqa: N802
        """Обработка данных лазерного пинцета."""
        laser_tweezers(self)

    # - - - - - - - - - #
    # Обработка данных
    # - - - - - - - - - #
    def figures_and_stuff(self) -> None:
        """Рисунки. Основная функция - comboBox и comboBox2 -- это для excel файла."""
        figs_plot(self)

    def profile_of_patient(self) -> None:
        """Микрореологический профиль."""
        prifile_plot(self)

    def pivot_table(self) -> None:
        """Сводная таблица."""
        pivot_do_for_sheet(self)

    def corr_table(self) -> None:
        """Корреляционная матрица."""
        corr_for_sheet(self)

    def pivot_or_melt(self) -> None:
        """Перевести данные в индексируемые или по столбцам."""
        pivot_or_melt_excel_file(self)

    def cat_plot(self) -> None:
        """Catplot."""
        plot_catplot(self)

    def p_value_calc(self) -> None:
        """Дополнительная обработка данных -- расчет p-value."""
        p_value_calc_for_two_columns(self)

    # -----------------------------------------------------#
    """
    Добавление списка файлов в папке в comboBox'ы
    """
    # -----------------------------------------------------#

    # - - - - - - - - - #
    # Catplot
    # - - - - - - - - - #
    def add_excel_catplot(self) -> None:
        path = Path(self.ui.path_for_catplot.text())
        files = list(path.glob("*.xlsx"))
        files = get_name_out_of_path([str(f) for f in files])
        self.ui.comboBox_excel_catplot.clear()  # удалить все элементы из combobox
        self.ui.comboBox_excel_catplot.addItems(files)

    def catplot_add_sheets(self) -> None:
        path_file = (
            Path(self.ui.path_for_catplot.text()) / self.ui.comboBox_excel_catplot.currentText()
        )
        try:
            sheets = pd.ExcelFile(str(path_file)).sheet_names
            self.ui.comboBox_excel_sheet_catplot.clear()  # удалить все элементы из combobox
            self.ui.comboBox_excel_sheet_catplot.addItems(sheets)
        except:  # noqa: E722
            self.ui.comboBox_excel_sheet_catplot.clear()  # удалить все элементы из combobox

    def catplot_add_x_y_hue(self) -> None:
        path_file = (
            Path(self.ui.path_for_catplot.text()) / self.ui.comboBox_excel_catplot.currentText()
        )
        try:
            df = pd.read_excel(
                str(path_file),
                sheet_name=self.ui.comboBox_excel_sheet_catplot.currentText(),
            )
            self.ui.comboBox_catplot_x.clear()  # удалить все элементы из combobox
            self.ui.comboBox_catplot_y.clear()  # удалить все элементы из combobox
            self.ui.comboBox_catplot_hue.clear()  # удалить все элементы из combobox

            self.ui.comboBox_catplot_x.addItems(df.columns)
            self.ui.comboBox_catplot_y.addItems(df.columns)
            self.ui.comboBox_catplot_hue.addItems(df.columns.insert(0, "--без подгруппы"))
        except:  # noqa: E722
            self.ui.comboBox_catplot_x.clear()  # удалить все элементы из combobox
            self.ui.comboBox_catplot_y.clear()  # удалить все элементы из combobox
            self.ui.comboBox_catplot_hue.clear()  # удалить все элементы из combobox

    # - - - - - - - - - #
    # Дополнительная статистика
    # - - - - - - - - - #
    def add_excel_dop_stat(self) -> None:
        path = Path(self.ui.path_for_dop_stat.text())
        files = list(path.glob("*.xlsx"))
        files = get_name_out_of_path([str(f) for f in files])
        self.ui.comboBox_excel_dop_stat.clear()  # удалить все элементы из combobox
        self.ui.comboBox_excel_sheet_dop_stat.clear()  # удалить все элементы из combobox
        self.ui.comboBox_dop_stat_x.clear()  # удалить все элементы из combobox
        self.ui.comboBox_dop_stat_y.clear()  # удалить все элементы из combobox
        self.ui.comboBox_excel_dop_stat.addItems(files)

    def dop_stat_add_sheets(self) -> None:
        path_file = (
            Path(self.ui.path_for_dop_stat.text()) / self.ui.comboBox_excel_dop_stat.currentText()
        )
        try:
            sheets = pd.ExcelFile(str(path_file)).sheet_names
            self.ui.comboBox_excel_sheet_dop_stat.clear()  # удалить все элементы из combobox
            self.ui.comboBox_excel_sheet_dop_stat.addItems(sheets)
        except:  # noqa: E722
            self.ui.comboBox_excel_sheet_dop_stat.clear()  # удалить все элементы из combobox

    def dop_stat_add_x_y_hue(self) -> None:
        path_file = (
            Path(self.ui.path_for_dop_stat.text()) / self.ui.comboBox_excel_dop_stat.currentText()
        )
        try:
            df = pd.read_excel(
                str(path_file),
                sheet_name=self.ui.comboBox_excel_sheet_dop_stat.currentText(),
            )
            self.ui.comboBox_dop_stat_x.clear()  # удалить все элементы из combobox
            self.ui.comboBox_dop_stat_y.clear()  # удалить все элементы из combobox

            self.ui.comboBox_dop_stat_x.addItems(df.columns)
            self.ui.comboBox_dop_stat_y.addItems(df.columns)
        except:  # noqa: E722
            self.ui.comboBox_dop_stat_x.clear()  # удалить все элементы из combobox
            self.ui.comboBox_dop_stat_y.clear()  # удалить все элементы из combobox

    # - - - - - - - - - #
    # Графики
    # - - - - - - - - - #
    def add_excel_files_to_combobox(self) -> None:
        path = Path(self.ui.path_for_plot.text())
        files = list(path.glob("*.xlsx"))
        files = get_name_out_of_path([str(f) for f in files])
        self.ui.comboBox.clear()  # удалить все элементы из combobox
        self.ui.comboBox.addItems(files)

    def figs_add_sheets_to_combobox(self) -> None:
        path_file = Path(self.ui.path_for_plot.text()) / self.ui.comboBox.currentText()
        try:
            sheets = pd.ExcelFile(str(path_file)).sheet_names
            self.ui.comboBox_figs_sheets.clear()  # удалить все элементы из combobox
            self.ui.comboBox_figs_sheets.addItems(sheets)
        except:  # noqa: E722
            self.ui.comboBox_figs_sheets.clear()  # удалить все элементы из combobox

    def add_columns_sheets_to_combobox(self) -> None:
        path_file = Path(self.ui.path_for_plot.text()) / self.ui.comboBox.currentText()
        try:
            # прочитаем файл
            df = pd.read_excel(
                str(path_file), sheet_name=self.ui.comboBox_figs_sheets.currentText()
            )
            self.ui.comboBox_2.clear()  # удалить все элементы из combobox
            self.ui.comboBox_2.addItems(df.columns)
        except:  # noqa: E722
            self.ui.comboBox_2.clear()  # удалить все элементы из combobox

    # - - - - - - - - - #
    # Сводные таблицы
    # - - - - - - - - - #
    def add_excel_files_to_combobox_pivot(self) -> None:
        path = Path(self.ui.path_for_pivot_table.text())
        files = list(path.glob("*.xlsx"))
        files = get_name_out_of_path([str(f) for f in files])
        self.ui.comboBox_pivot_table.clear()  # удалить все элементы из combobox
        self.ui.comboBox_pivot_table.addItems(files)

    def add_sheets_to_combobox_pivot(self) -> None:
        path_file = (
            Path(self.ui.path_for_pivot_table.text()) / self.ui.comboBox_pivot_table.currentText()
        )
        try:
            sheets = pd.ExcelFile(str(path_file)).sheet_names
            self.ui.comboBox_pivot_table_excel_sheet.clear()  # удалить все элементы из combobox
            self.ui.comboBox_pivot_table_excel_sheet.addItems(sheets)
        except:  # noqa: E722
            self.ui.comboBox_pivot_table_excel_sheet.clear()  # удалить все элементы из combobox

    def add_columns_to_combobox_pivot(self) -> None:
        # прочитаем файл
        path_file = (
            Path(self.ui.path_for_pivot_table.text()) / self.ui.comboBox_pivot_table.currentText()
        )
        try:
            df = pd.read_excel(
                str(path_file),
                sheet_name=self.ui.comboBox_pivot_table_excel_sheet.currentText(),
            )
            self.ui.comboBox_pivot_hue.clear()  # удалить все элементы из combobox
            self.ui.comboBox_pivot_hue.addItems([str(i) for i in df.columns])
        except:  # noqa: E722
            self.ui.comboBox_pivot_hue.clear()  # удалить все элементы из combobox

    # - - - - - - - - - #
    # Биола -- одновременно добавляем файлы txt и pdf
    # - - - - - - - - - #
    def add_biola_file(self) -> None:
        path = Path(self.ui.path_for_biola.text())
        files = list(path.glob("*.txt"))
        files = get_name_out_of_path([str(f) for f in files])
        self.ui.comboBox_biola.clear()  # удалить все элементы из combobox
        self.ui.comboBox_biola.addItems(files)

        files2 = list(path.glob("*.pdf"))
        files2 = get_name_out_of_path([str(f) for f in files2])
        self.ui.comboBox_biola_concentration.clear()  # удалить все элементы из combobox
        self.ui.comboBox_biola_concentration.addItems(files2)

    # - - - - - - - - - #
    # Лазерный пинцет -- изменим калибровку
    # - - - - - - - - - #
    def LT_change_calibration(self) -> None:  # noqa: N802
        if self.ui.comboBox_LT_calibration.currentText() == "Линейная":
            self.ui.hhhhh.setEnabled(True)
            self.ui.hhhhh_exp.setEnabled(False)
        else:
            self.ui.hhhhh.setEnabled(False)
            self.ui.hhhhh_exp.setEnabled(True)

    # - - - - - - - - - #
    # Добавить цвета к BOX или точкам
    # - - - - - - - - - #
    def HEX_box(self) -> None:
        color = getColor(self.ui.comboBox_style_sheet.currentText() == "Основная тема")
        if color is not None:
            self.ui.color_box.setText(self.ui.color_box.text() + "#" + rgb2hex(color) + "&")

    def HEX_points(self) -> None:
        color = getColor(self.ui.comboBox_style_sheet.currentText() == "Основная тема")
        if color is not None:
            self.ui.color_points.setText(self.ui.color_points.text() + "#" + rgb2hex(color) + "&")

    # - - - - - - - - - #
    # Сделаем disabled у box и точек для палитр
    # - - - - - - - - - #
    @Slot()
    def box_palette_off(self):
        if self.ui.color_box.text() == "":
            self.ui.comboBox_color_pal_box.setEnabled(True)
        else:
            self.ui.comboBox_color_pal_box.setEnabled(False)

    @Slot()
    def point_palette_off(self):
        if self.ui.color_points.text() == "":
            self.ui.comboBox_color_pal_points.setEnabled(True)
        else:
            self.ui.comboBox_color_pal_points.setEnabled(False)

    # - - - - - - - - - #
    # Нажатие кнопки toolButton_RheoScan и получение имени папки/файла
    # - - - - - - - - - #
    def toolButton_RheoScan_file(self) -> None:
        dialog = QFileDialog()
        path = "ошибка"
        if self.ui.comboBox_RheoScan_describe.currentText() == "Один файл - один образец":
            path = dialog.getExistingDirectory(
                None,
                "Путь к папке с excel файлами RheoScan пациентов/образцов",
            )
            path = str(Path(path))
        elif self.ui.comboBox_RheoScan_describe.currentText() == "Один файл - много образцов":
            path = dialog.getOpenFileName(
                None,
                "Путь к excel файлу RheoScan",
                filter="Text Files (*.xlsx)",
            )
            path = path[0]
            path = str(Path(path))
        self.ui.path_for_RheoScan_describe.setText(path)
