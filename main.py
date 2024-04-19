##############
import sys
############################
# библиотеки для создания приложения
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot
############################
# обработка RheoScan
from __RheoScan__ import *
from __RheoScan_sort__ import *
# Biola
from __Biola__ import *
from __Biola_concentration__ import *
# Лазерный пинцет
from __LT__ import *
# Микрореологический профиль
from __Profile__ import *
# Рисунки
from __Figs__ import *
from __Catplot__ import *
# Сводные таблицы
from __Pivot_table_and_corr__ import *
############################
# основное окно приложения
from ui_main import Ui_MainWindow
############################
#дополнительные библиотеки - pandas нужен для добавления листов excel в соответствующие окна
import pandas as pd
import os
############################
#чтобы Лого показывалось - https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
############################

class Main_window(QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #################################
        #Buttons
        #################################
        #для кнопки из вкладки RheoScan
        self.ui.btn_save_exel_csv.pressed.connect(self.RheoScan)
        #для кнопки из вкладки RheoScan
        self.ui.btn_sort_data_RheoScan.pressed.connect(self.RheoScan_sort_data)
        #для кнопки по построению микрореологического профиля
        self.ui.btn_plot_and_save_profile.pressed.connect(self.Profile)
        #для кнопки по построению графиков
        self.ui.btn_plot_and_save_figs.pressed.connect(self.Figs_and_stuff)
        #для кнопки по расчету сводных таблиц
        self.ui.btn_plot_and_save_pivot_table.pressed.connect(self.pivot_table)
        #для кнопки по построению корреляционной матрицы
        self.ui.btn_plot_and_save_corr_table.pressed.connect(self.corr_table)
        #для кнопки по обработки данных Biola
        self.ui.btn_biola.pressed.connect(self.biola_do)
        #для кнопки по обработки данных Biola
        self.ui.btn_biola_concentration.pressed.connect(self.biola_concentration)
        #для кнопки по обработки данных лазерного пинцета
        self.ui.btn_LT.pressed.connect(self.LT)
        #catplot
        self.ui.btn_plot_and_save_catplot.pressed.connect(self.cat_plot)

        #########################################
        #путь к папке с файлами - графики
        self.ui.path_for_plot.textChanged.connect(self.add_excel_files_to_combobox)
        #обновим какие есть sheets - графики
        self.ui.comboBox.currentTextChanged.connect(self.add_sheets_to_combobox)

        #путь к папке с файлами - pivot
        self.ui.path_for_pivot_table.textChanged.connect(self.add_excel_files_to_combobox_pivot)
        #обновим какие есть sheets - pivot
        self.ui.comboBox_pivot_table.currentTextChanged.connect(self.add_sheets_to_combobox_pivot)
        # обновим какие есть колонки - pivot
        self.ui.comboBox_pivot_table_excel_sheet.currentTextChanged.connect(self.add_columns_to_combobox_pivot)

        #для нахождения файла Biola
        self.ui.path_for_biola.textChanged.connect(self.add_biola_file)

        #catplot
        self.ui.path_for_catplot.textChanged.connect(self.add_excel_catplot)
        self.ui.comboBox_excel_catplot.currentTextChanged.connect(self.catplot_add_sheets)
        self.ui.comboBox_excel_sheet_catplot.currentTextChanged.connect(self.catplot_add_x_y_hue)

    ##############################
    #изменим стиль - светлая или темная тема
    ##############################
    @Slot(int)
    def on_comboBox_style_sheet_currentIndexChanged(self, index):
        #меняем стили, как перчатки
        if index == 1:
            with open("style_dark.qss", "r") as f:
                _style = f.read()
            self.setStyleSheet(_style)
        else:
            self.setStyleSheet('')

    ##############################
    ##############################
    #функции при нажатии на кнопки
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

    ############
    # Biola
    ############
    # основная функция извлечения данных из txt файла
    def biola_do(self):
        biola_result(self)
    # извлечение данных из PDF файла для "Счета"
    def biola_concentration(self):
        conentration_to_excel(self.ui.path_for_biola.text(), self.ui.comboBox_biola_concentration.currentText())

    ############
    # Лазерный пинцет
    ############
    def LT(self):
        laser_tweezers(self)

    ############
    # Обработка данных
    ############
    #Рисунки
    def Figs_and_stuff(self):
        #дополнительные настройки
        plot_feature_data__ = self.ui.comboBox_color_pal_box.currentText(), self.ui.comboBox_color_pal_points.currentText(), self.ui.color_box.text(), self.ui.color_points.text(), self.ui.comboBox_sd_or_minmax.currentText(), self.ui.bottom_lim.text(), self.ui.comboBox_color_pal_corr.currentText(), self.ui.del_hue.text(), self.ui.corr_mat_figsize.text(), self.ui.font_for_in.text(), self.ui.font_for_out.text(), self.ui.name_of_corr_matrix.text(), self.ui.comboBox_stat_test.currentText(), self.ui.comboBox_alter_hep.currentText(), self.ui.comboBox_spin_x_.currentText(), self.ui.check_sort_or_not.isChecked(), self.ui.check_stat_znachimost.isChecked(), self.ui.spinBox_x_label.value(), self.ui.spinBox_y_label.value(), self.ui.spinBox_x_val.value(), self.ui.spinBox_y_vals.value(), self.ui.comboBox_fonts.currentText(), self.ui.spinBox_mean_val_size.value(), self.ui.check_N_.isChecked(), self.ui.check_background.isChecked(), self.ui.check_change_corr_fig_down_limit.isChecked(), self.ui.doubleSpinBox_corr_figs.value(), self.ui.spinBox_points_corrFIGS.value(), self.ui.doubleSpinBox_corr_figs_fontscale.value(), self.ui.check_sort_or_not_corr_figs.isChecked(), self.ui.check_setka.isChecked(), self.ui.order_box_plot.text(), self.ui.STAT_znachimost_order_box_plot.text()
        #основная функция - comboBox и comboBox2 -- это для excel файла
        figs_plot(plot_feature_data__, self.ui.path_for_plot.text(), self.ui.comboBox.currentText(), self.ui.comboBox_2.currentText(),
                  self.ui.check_box_plot.isChecked(), self.ui.check_corr_matrix.isChecked(), self.ui.check_corr_figs.isChecked())
    # Микрореологический профиль
    def Profile(self):
        prifile_plot(self)

    #сводная таблица
    def pivot_table(self):
        pivot_do_for_sheet(self)
    # корреляционная матрица
    def corr_table(self):
        corr_for_sheet(self)
    # Catplot
    def cat_plot(self):
        plot_catplot(self)

    ################################################
    ###
    #добавление списка файлов в папке в comboBox'ы
    ###
    ################################################

    ############
    # Catplot
    ############
    def add_excel_catplot(self):
        #files = get_name_out_of_path(glob.glob(self.ui.path_for_plot.text() + '//' +'*.xlsx'))
        files = glob.glob(self.ui.path_for_catplot.text() + '//' + '*.xlsx')
        files = get_name_out_of_path(files)
        self.ui.comboBox_excel_catplot.clear()  #удалить все элементы из combobox
        self.ui.comboBox_excel_catplot.addItems(files)

    def catplot_add_sheets(self):
        path_file = self.ui.path_for_catplot.text() + '//' + self.ui.comboBox_excel_catplot.currentText()
        sheets = pd.ExcelFile(path_file).sheet_names
        self.ui.comboBox_excel_sheet_catplot.clear()  #удалить все элементы из combobox
        self.ui.comboBox_excel_sheet_catplot.addItems(sheets)

    def catplot_add_x_y_hue(self):
        path_file = self.ui.path_for_catplot.text() + '//' + self.ui.comboBox_excel_catplot.currentText()
        df = pd.read_excel(path_file, sheet_name=self.ui.comboBox_excel_sheet_catplot.currentText())
        self.ui.comboBox_catplot_x.clear()  #удалить все элементы из combobox
        self.ui.comboBox_catplot_y.clear()  # удалить все элементы из combobox
        self.ui.comboBox_catplot_hue.clear()  # удалить все элементы из combobox

        self.ui.comboBox_catplot_x.addItems(df.columns)
        self.ui.comboBox_catplot_y.addItems(df.columns)
        self.ui.comboBox_catplot_hue.addItems(df.columns.insert(0, '--без подгруппы'))

    ############
    # Графики
    ############
    def add_excel_files_to_combobox(self):
        #files = get_name_out_of_path(glob.glob(self.ui.path_for_plot.text() + '//' +'*.xlsx'))
        files = glob.glob(self.ui.path_for_plot.text() + '//' + '*.xlsx')
        files = get_name_out_of_path(files)
        self.ui.comboBox.clear()  #удалить все элементы из combobox
        self.ui.comboBox.addItems(files)
    def add_sheets_to_combobox(self):
        path_file = self.ui.path_for_plot.text() + '//' + self.ui.comboBox.currentText()
        sheets = pd.ExcelFile(path_file).sheet_names
        #прочитаем файл
        df = pd.read_excel(path_file, sheet_name=sheets[0])
        self.ui.comboBox_2.clear()  #удалить все элементы из combobox
        self.ui.comboBox_2.addItems(df.columns)

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
        sheets = pd.ExcelFile(path_file).sheet_names
        self.ui.comboBox_pivot_table_excel_sheet.clear()  #удалить все элементы из combobox
        self.ui.comboBox_pivot_table_excel_sheet.addItems(sheets)

    def add_columns_to_combobox_pivot(self):
        # прочитаем файл
        path_file = self.ui.path_for_pivot_table.text() + '//' + self.ui.comboBox_pivot_table.currentText()
        df = pd.read_excel(path_file, sheet_name=self.ui.comboBox_pivot_table_excel_sheet.currentText())
        self.ui.comboBox_pivot_hue.clear()  # удалить все элементы из combobox
        self.ui.comboBox_pivot_hue.addItems(df.columns)

    ############
    # Биола -- одновременно добавляем файлы txt и pdf
    ############
    def add_biola_file(self):
        files = glob.glob(self.ui.path_for_biola.text() + '//' + '*.txt')
        files = get_name_out_of_path(files)
        self.ui.comboBox_biola.clear()  #удалить все элементы из combobox
        self.ui.comboBox_biola.addItems(files)

        files2 = glob.glob(self.ui.path_for_biola.text() + '//' + '*.pdf')
        files2 = get_name_out_of_path(files2)
        self.ui.comboBox_biola_concentration.clear()  # удалить все элементы из combobox
        self.ui.comboBox_biola_concentration.addItems(files2)



#функция, чтобы разделить путь до файла на название файла без расширений
def get_name_out_of_path(files):
    out=[0]*(len(files))
    for i in range(len(files)):
        out[i]=files[i].split('\\')[-1]
    return out

# важно обозначить для того, чтобы лого обозначалось правильно
basedir = os.path.dirname(__file__)
###########################################
# запуск приложения
###########################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'LOGO.ico')))
    window = Main_window()
    window.show()
    sys.exit(app.exec())