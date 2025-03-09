# библиотеки для создания приложения
from PySide6.QtWidgets import (QMainWindow, QFileDialog)
from PySide6.QtCore import Slot
############################
# обработка RheoScan
from RheoScan.__RheoScan__ import *
from RheoScan.__RheoScan__describe import *
from RheoScan.__RheoScan_sort__ import *
# Biola
from Biola.__Biola__ import *
from Biola.__Biola_concentration__ import *
# Лазерный пинцет
from Laser_Tweezers.__LT__ import *
# Микрореологический профиль
from Data_Processing.__Profile__ import *
# Рисунки
from Data_Processing.__Figs__ import *
from Data_Processing.__Catplot__ import *
# Сводные таблицы
from Data_Processing.__Pivot_table_and_corr__ import *
# Расчет p-value для 2 колонок
from Data_Processing.__Calc_p_value__ import *
############################
# основное окно приложения
from ui.ui_main import Ui_MainWindow
############################
# дополнительные библиотеки - pandas нужен для добавления листов excel в соответствующие окна
import pandas as pd
############################
# узнать цвет HEX - color picker
from vcolorpicker import getColor, rgb2hex


class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #################################
        # Buttons
        #################################
        # для кнопки из вкладки RheoScan
        self.ui.btn_save_exel_csv.pressed.connect(self.RheoScan)
        # для кнопки из вкладки RheoScan
        self.ui.btn_sort_data_RheoScan.pressed.connect(self.RheoScan_sort_data)
        # для кнопки по построению микрореологического профиля
        self.ui.btn_plot_and_save_profile.pressed.connect(self.Profile)
        # для кнопки по построению графиков
        self.ui.btn_plot_and_save_figs.pressed.connect(self.Figs_and_stuff)
        # для кнопки по расчету сводных таблиц
        self.ui.btn_plot_and_save_pivot_table.pressed.connect(self.pivot_table)
        # для кнопки по построению корреляционной матрицы
        self.ui.btn_plot_and_save_corr_table.pressed.connect(self.corr_table)
        # для кнопки по обработки данных Biola
        self.ui.btn_biola.pressed.connect(self.biola_do)
        # для кнопки по обработки данных Biola
        self.ui.btn_biola_concentration.pressed.connect(self.biola_concentration)
        # для кнопки по обработки данных лазерного пинцета
        self.ui.btn_LT.pressed.connect(self.LT)
        # для кнопки по catplot
        self.ui.btn_plot_and_save_catplot.pressed.connect(self.cat_plot)
        # для кнопки по доп. обработке данных - RheoScan - описать
        self.ui.btn_RheoScan_describe_file_or_files.pressed.connect(self.RheoScan_describe)
        # для кнопки по доп. обработке данных - RheoScan - описать
        self.ui.btn_dop_stat_calc.pressed.connect(self.p_value_calc)
        # для кнопки по расчету сводных таблиц - перевести данные в индексируемые или в по столбцам
        self.ui.btn_save_pivot_or_melt.pressed.connect(self.pivot_or_melt)
        # для кнопки выбора HEX цветов BOX
        self.ui.pushButton_HEX_box.pressed.connect(self.HEX_box)
        # для кнопки выбора HEX цветов точек
        self.ui.pushButton_HEX_points.pressed.connect(self.HEX_points)
        # для кнопки выбора папки
        self.ui.toolButton_RheoScan.pressed.connect(self.toolButton_RheoScan_file)
        # для инфо
        self.ui.label_info.mousePressEvent = self.info_about_programme

        #########################################
        # путь к папке с файлами - графики
        self.ui.path_for_plot.textChanged.connect(self.add_excel_files_to_combobox)
        # обновим какие есть sheets - графики
        self.ui.comboBox.currentTextChanged.connect(self.figs_add_sheets_to_combobox)
        # обновим, какие есть колонки
        self.ui.comboBox_figs_sheets.currentTextChanged.connect(self.add_columns_sheets_to_combobox)

        #########################################
        # путь к папке с файлами - pivot
        self.ui.path_for_pivot_table.textChanged.connect(self.add_excel_files_to_combobox_pivot)
        # обновим какие есть sheets - pivot
        self.ui.comboBox_pivot_table.currentTextChanged.connect(self.add_sheets_to_combobox_pivot)
        # обновим какие есть колонки - pivot
        self.ui.comboBox_pivot_table_excel_sheet.currentTextChanged.connect(self.add_columns_to_combobox_pivot)

        #########################################
        # для нахождения файла Biola
        self.ui.path_for_biola.textChanged.connect(self.add_biola_file)

        #########################################
        # catplot
        self.ui.path_for_catplot.textChanged.connect(self.add_excel_catplot)
        self.ui.comboBox_excel_catplot.currentTextChanged.connect(self.catplot_add_sheets)
        self.ui.comboBox_excel_sheet_catplot.currentTextChanged.connect(self.catplot_add_x_y_hue)

        #########################################
        # дополнительная статистика - расчет p-value
        self.ui.path_for_dop_stat.textChanged.connect(self.add_excel_dop_stat)
        self.ui.comboBox_excel_dop_stat.currentTextChanged.connect(self.dop_stat_add_sheets)
        self.ui.comboBox_excel_sheet_dop_stat.currentTextChanged.connect(self.dop_stat_add_x_y_hue)

        self.ui.comboBox_stat_test_dop_stat.currentTextChanged.connect(self.p_value_calc)
        self.ui.comboBox_alter_hep_dop_stat.currentTextChanged.connect(self.p_value_calc)

        #########################################
        # изменяем каллибровку
        self.ui.comboBox_LT_calibration.currentTextChanged.connect(self.LT_change_calibration)

        #########################################
        # для цветов box plot
        self.ui.color_box.textChanged.connect(self.box_pallete_off)
        self.ui.color_points.textChanged.connect(self.point_pallete_off)

    def info_about_programme(self, _):
        info_message = QMessageBox(self)
        info_message.setWindowTitle("Информация про программу")
        first_message = 'Программа написана на языке Python с применением ряда библиотек Ермолинским Петром Борисовичем - аспирантом лаборатории <Биомедицинской фотоники> Физического факультета МГУ имени М.В. Ломоносова. Исходный код доступен в репозитории GitHub на странице:'
        url_message = 'https://github.com/Petr-Ermolinskiy'
        message = first_message + '\n' + url_message
        info_message.setText(message)
        info_message.exec()

    ##############################
    # изменим стиль - светлая или темная тема
    ##############################
    @Slot(int)
    def on_comboBox_style_sheet_currentIndexChanged(self, index):
        # меняем стили, как перчатки
        if index == 1:
            with open("style/style_dark.qss", "r") as f:
                _style = f.read()
            self.setStyleSheet(_style)
        else:
            self.setStyleSheet('')

    ##############################
    ##############################
    # функции при нажатии на кнопки
    ##############################
    ##############################

    ############
    # RheoScan
    ############
    def RheoScan(self):
        all_RheoScan_level(self)

    # сортировка данных RheoScan
    def RheoScan_sort_data(self):
        sort_RheoScan_data(self)

    # этот метод находится в отделе обработки данных
    def RheoScan_describe(self):
        RheoScan_describe_file_or_files(self)

    ############
    # Biola
    ############
    # основная функция извлечения данных из txt файла
    def biola_do(self):
        biola_result(self)

    # извлечение данных из PDF файла для "Счета"
    def biola_concentration(self):
        conentration_to_excel(self, self.ui.path_for_biola.text(), self.ui.comboBox_biola_concentration.currentText())

    ############
    # Лазерный пинцет
    ############
    def LT(self):
        laser_tweezers(self)

    ############
    # Обработка данных
    ############
    # Рисунки
    def Figs_and_stuff(self):
        # основная функция - comboBox и comboBox2 -- это для excel файла
        figs_plot(self)

    # Микрореологический профиль
    def Profile(self):
        prifile_plot(self)

    # сводная таблица
    def pivot_table(self):
        pivot_do_for_sheet(self)

    # корреляционная матрица
    def corr_table(self):
        corr_for_sheet(self)

    # перевести данные в индексируемые или по столбцам
    def pivot_or_melt(self):
        pivot_or_melt_excel_file(self)

    # Catplot
    def cat_plot(self):
        plot_catplot(self)

    # дополнительная обработка данных -- расчет p-value
    def p_value_calc(self):
        p_value_calc_for_two_columns(self)

    ################################################
    ###
    # добавление списка файлов в папке в comboBox'ы
    ###
    ################################################

    ############
    # Catplot
    ############
    def add_excel_catplot(self):
        # files = get_name_out_of_path(glob.glob(self.ui.path_for_plot.text() + '//' +'*.xlsx'))
        files = glob.glob(self.ui.path_for_catplot.text() + '//' + '*.xlsx')
        files = get_name_out_of_path(files)
        self.ui.comboBox_excel_catplot.clear()  # удалить все элементы из combobox
        self.ui.comboBox_excel_catplot.addItems(files)

    def catplot_add_sheets(self):
        path_file = self.ui.path_for_catplot.text() + '//' + self.ui.comboBox_excel_catplot.currentText()
        try:
            sheets = pd.ExcelFile(path_file).sheet_names
            self.ui.comboBox_excel_sheet_catplot.clear()  # удалить все элементы из combobox
            self.ui.comboBox_excel_sheet_catplot.addItems(sheets)
        except:
            self.ui.comboBox_excel_sheet_catplot.clear()  # удалить все элементы из combobox

    def catplot_add_x_y_hue(self):
        path_file = self.ui.path_for_catplot.text() + '//' + self.ui.comboBox_excel_catplot.currentText()
        try:
            df = pd.read_excel(path_file, sheet_name=self.ui.comboBox_excel_sheet_catplot.currentText())
            self.ui.comboBox_catplot_x.clear()  # удалить все элементы из combobox
            self.ui.comboBox_catplot_y.clear()  # удалить все элементы из combobox
            self.ui.comboBox_catplot_hue.clear()  # удалить все элементы из combobox

            self.ui.comboBox_catplot_x.addItems(df.columns)
            self.ui.comboBox_catplot_y.addItems(df.columns)
            self.ui.comboBox_catplot_hue.addItems(df.columns.insert(0, '--без подгруппы'))
        except:
            self.ui.comboBox_catplot_x.clear()  # удалить все элементы из combobox
            self.ui.comboBox_catplot_y.clear()  # удалить все элементы из combobox
            self.ui.comboBox_catplot_hue.clear()  # удалить все элементы из combobox

    ############
    # Дополнительная статистика
    ############
    def add_excel_dop_stat(self):
        files = glob.glob(self.ui.path_for_dop_stat.text() + '//' + '*.xlsx')
        files = get_name_out_of_path(files)
        self.ui.comboBox_excel_dop_stat.clear()  # удалить все элементы из combobox
        self.ui.comboBox_excel_sheet_dop_stat.clear()  # удалить все элементы из combobox
        self.ui.comboBox_dop_stat_x.clear()  # удалить все элементы из combobox
        self.ui.comboBox_dop_stat_y.clear()  # удалить все элементы из combobox
        self.ui.comboBox_excel_dop_stat.addItems(files)

    def dop_stat_add_sheets(self):
        path_file = self.ui.path_for_dop_stat.text() + '//' + self.ui.comboBox_excel_dop_stat.currentText()
        try:
            sheets = pd.ExcelFile(path_file).sheet_names
            self.ui.comboBox_excel_sheet_dop_stat.clear()  # удалить все элементы из combobox
            self.ui.comboBox_excel_sheet_dop_stat.addItems(sheets)
        except:
            self.ui.comboBox_excel_sheet_dop_stat.clear()  # удалить все элементы из combobox

    def dop_stat_add_x_y_hue(self):
        path_file = self.ui.path_for_dop_stat.text() + '//' + self.ui.comboBox_excel_dop_stat.currentText()
        try:
            df = pd.read_excel(path_file, sheet_name=self.ui.comboBox_excel_sheet_dop_stat.currentText())
            self.ui.comboBox_dop_stat_x.clear()  # удалить все элементы из combobox
            self.ui.comboBox_dop_stat_y.clear()  # удалить все элементы из combobox

            self.ui.comboBox_dop_stat_x.addItems(df.columns)
            self.ui.comboBox_dop_stat_y.addItems(df.columns)
        except:
            self.ui.comboBox_dop_stat_x.clear()  # удалить все элементы из combobox
            self.ui.comboBox_dop_stat_y.clear()  # удалить все элементы из combobox

    ############
    # Графики
    ############
    def add_excel_files_to_combobox(self):
        # files = get_name_out_of_path(glob.glob(self.ui.path_for_plot.text() + '//' +'*.xlsx'))
        files = glob.glob(self.ui.path_for_plot.text() + '//' + '*.xlsx')
        files = get_name_out_of_path(files)
        self.ui.comboBox.clear()  # удалить все элементы из combobox
        self.ui.comboBox.addItems(files)

    def figs_add_sheets_to_combobox(self):
        path_file = self.ui.path_for_plot.text() + '//' + self.ui.comboBox.currentText()
        try:
            sheets = pd.ExcelFile(path_file).sheet_names
            self.ui.comboBox_figs_sheets.clear()  # удалить все элементы из combobox
            self.ui.comboBox_figs_sheets.addItems(sheets)
        except:
            self.ui.comboBox_figs_sheets.clear()  # удалить все элементы из combobox

    def add_columns_sheets_to_combobox(self):
        path_file = self.ui.path_for_plot.text() + '//' + self.ui.comboBox.currentText()
        try:
            sheets = pd.ExcelFile(path_file).sheet_names
            # прочитаем файл
            df = pd.read_excel(path_file, sheet_name=self.ui.comboBox_figs_sheets.currentText())
            self.ui.comboBox_2.clear()  # удалить все элементы из combobox
            self.ui.comboBox_2.addItems(df.columns)
        except:
            self.ui.comboBox_2.clear()  # удалить все элементы из combobox

    ############
    # Сводные таблицы
    ############
    def add_excel_files_to_combobox_pivot(self):
        files = glob.glob(self.ui.path_for_pivot_table.text() + '//' + '*.xlsx')
        files = get_name_out_of_path(files)
        self.ui.comboBox_pivot_table.clear()  # удалить все элементы из combobox
        self.ui.comboBox_pivot_table.addItems(files)

    def add_sheets_to_combobox_pivot(self):
        path_file = self.ui.path_for_pivot_table.text() + '//' + self.ui.comboBox_pivot_table.currentText()
        try:
            sheets = pd.ExcelFile(path_file).sheet_names
            self.ui.comboBox_pivot_table_excel_sheet.clear()  # удалить все элементы из combobox
            self.ui.comboBox_pivot_table_excel_sheet.addItems(sheets)
        except:
            self.ui.comboBox_pivot_table_excel_sheet.clear()  # удалить все элементы из combobox

    def add_columns_to_combobox_pivot(self):
        # прочитаем файл
        path_file = self.ui.path_for_pivot_table.text() + '//' + self.ui.comboBox_pivot_table.currentText()
        try:
            df = pd.read_excel(path_file, sheet_name=self.ui.comboBox_pivot_table_excel_sheet.currentText())
            self.ui.comboBox_pivot_hue.clear()  # удалить все элементы из combobox
            self.ui.comboBox_pivot_hue.addItems([str(i) for i in df.columns])
        except:
            self.ui.comboBox_pivot_hue.clear()  # удалить все элементы из combobox

    ############
    # Биола -- одновременно добавляем файлы txt и pdf
    ############
    def add_biola_file(self):
        files = glob.glob(self.ui.path_for_biola.text() + '//' + '*.txt')
        files = get_name_out_of_path(files)
        self.ui.comboBox_biola.clear()  # удалить все элементы из combobox
        self.ui.comboBox_biola.addItems(files)

        files2 = glob.glob(self.ui.path_for_biola.text() + '//' + '*.pdf')
        files2 = get_name_out_of_path(files2)
        self.ui.comboBox_biola_concentration.clear()  # удалить все элементы из combobox
        self.ui.comboBox_biola_concentration.addItems(files2)

    ############
    # Лазерный пинцет -- изменим калибровку
    ############
    def LT_change_calibration(self):
        if self.ui.comboBox_LT_calibration.currentText() == 'Линейная':
            self.ui.hhhhh.setEnabled(True)
            self.ui.hhhhh_exp.setEnabled(False)
        else:
            self.ui.hhhhh.setEnabled(False)
            self.ui.hhhhh_exp.setEnabled(True)

    ############
    # Добавить цвета к BOX или точкам
    ############
    def HEX_box(self):
        color = getColor(True if self.ui.comboBox_style_sheet.currentText() == 'Основная тема' else False)
        if color is not None:
            self.ui.color_box.setText(self.ui.color_box.text() + '#' + rgb2hex(color) + '&')

    def HEX_points(self):
        color = getColor(True if self.ui.comboBox_style_sheet.currentText() == 'Основная тема' else False)
        if color is not None:
            self.ui.color_points.setText(self.ui.color_points.text() + '#' + rgb2hex(color) + '&')

    ############
    # Сделаем disabled у box и точек для палитр
    ############
    @Slot()
    def box_pallete_off(self):
        if self.ui.color_box.text() == '':
            self.ui.comboBox_color_pal_box.setEnabled(True)
        else:
            self.ui.comboBox_color_pal_box.setEnabled(False)

    @Slot()
    def point_pallete_off(self):
        if self.ui.color_points.text() == '':
            self.ui.comboBox_color_pal_points.setEnabled(True)
        else:
            self.ui.comboBox_color_pal_points.setEnabled(False)

    ############
    # Нажатие кнопки toolButton_RheoScan и получение имени папки/файла
    ############
    def toolButton_RheoScan_file(self):
        dialog = QFileDialog()
        path = 'ошибка'
        if self.ui.comboBox_RheoScan_describe.currentText() == 'Один файл - один образец':
            path = dialog.getExistingDirectory(None, "Путь к папке с файлами RheoScan пациентов/образцов")
            path = path.replace('/', '\\')
        elif self.ui.comboBox_RheoScan_describe.currentText() == 'Один файл - много образцов':
            path = dialog.getOpenFileName(None, "Путь к папке с файлом RheoScan", filter="Text Files (*.xlsx)")
            path = path[0]
            path = path.replace('/', '\\')
        self.ui.path_for_RheoScan_describe.setText(path)


# функция, чтобы разделить путь до файла на название файла без расширений
def get_name_out_of_path(files):
    out = [0] * (len(files))
    for i in range(len(files)):
        out[i] = files[i].split('\\')[-1]
    return out
