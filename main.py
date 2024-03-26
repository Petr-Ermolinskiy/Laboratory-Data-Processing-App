#this is the main file

###############
##############
##############

import sys
############################
# библиотеки для создания приложения
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot
############################
#обработка RheoScan
from __RheoScan__ import *
from __RheoScan_sort__ import *
from __Profile__ import *
from __Figs__ import *
from __Pivot_table_and_corr__ import *
from __Catplot__ import *
from __Biola__ import *
from __Biola_concentration__ import *
from __LT__ import *
from additional_func import get_name_out_of_path
# основное окно приложения
from ui_main import Ui_MainWindow
#дополнительные библиотеки
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
        '''
        my_icon = QIcon()
        my_icon.addFile('LOGO.png')
        self.setWindowIcon(my_icon)
        '''
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

        #для нахождения файла Biola
        self.ui.path_for_biola.textChanged.connect(self.add_biola_file)

        #catplot
        self.ui.path_for_catplot.textChanged.connect(self.add_excel_catplot)
        self.ui.comboBox_excel_catplot.currentTextChanged.connect(self.catplot_add_sheets)
        self.ui.comboBox_excel_sheet_catplot.currentTextChanged.connect(self.catplot_add_x_y_hue)
    ##############################
    #изменим стиль
    ##############################
    @Slot(int)
    def on_comboBox_style_sheet_currentIndexChanged(self, index):
        #меняем стили, как перчатки
        if index == 1:
            with open("style_dark.qss", "r") as f:
                _style = f.read()
            self.setStyleSheet(_style)
        elif index == 2:
            with open("style_mac.qss", "r") as f:
                _style = f.read()
            self.setStyleSheet(_style)
        elif index == 3:
            with open("style_aqua.qss", "r") as f:
                _style = f.read()
            self.setStyleSheet(_style)
        else:
            self.setStyleSheet('')
    ##############################
    #функции при нажатии на кнопки
    ##############################
    #RheoScan
    def RheoScan(self):
        level_(self.ui.spinBox_level.value(),[[self.ui.tua_1_agg.text(), self.ui.tau_2_agg.text(), self.ui.r2_def.text(), self.ui.spinBox_n_max_deform.value()], self.ui.main_path.text(), self.ui.check_agg.isChecked(), self.ui.check_stress.isChecked(), self.ui.check_deform.isChecked(), self.ui.check_save_exel.isChecked(), self.ui.check_save_csv.isChecked(), self.ui.separator_for_data.text(), self.ui.check_stat_for_column.isChecked(), self.ui.check_figs_for_agg.isChecked(), self.ui.check_approx_agg.isChecked(), self.ui.check_approx_deform.isChecked(), self.ui.check_for_deform.isChecked(), self.ui.vibros_delete.isChecked(), self.ui.iqr_vibros.value()])
    #sort data
    def RheoScan_sort_data(self):
        sort_RheoScan_data(self.ui.main_path.text(),self.ui.spinBox_level.value())
    #Микрореологический профиль
    def Profile(self):
        lines_or_no_lines = [self.ui.check_profile_pat_line.isChecked(),self.ui.check_profile_pat_sd.isChecked(),self.ui.check_profile_norm_line.isChecked(),self.ui.check_profile_norm_sd.isChecked()]
        prifile_plot([self.ui.patient_prof.text(),self.ui.norm_prof.text(),self.ui.color_for_patient.text(),self.ui.color_for_norm.text()], self.ui.patient_data.text(), self.ui.norm_data.text(), self.ui.path_for_profile.text(), lines_or_no_lines)
    #Рисунки
    def Figs_and_stuff(self):
        #дополнительные настройки
        plot_feature_data__ = self.ui.comboBox_color_pal_box.currentText(), self.ui.comboBox_color_pal_points.currentText(), self.ui.color_box.text(), self.ui.color_points.text(), self.ui.comboBox_sd_or_minmax.currentText(), self.ui.bottom_lim.text(), self.ui.comboBox_color_pal_corr.currentText(), self.ui.del_hue.text(), self.ui.corr_mat_figsize.text(), self.ui.font_for_in.text(), self.ui.font_for_out.text(), self.ui.name_of_corr_matrix.text(), self.ui.comboBox_stat_test.currentText(), self.ui.comboBox_alter_hep.currentText(), self.ui.comboBox_spin_x_.currentText(), self.ui.check_sort_or_not.isChecked(), self.ui.check_stat_znachimost.isChecked(), self.ui.spinBox_x_label.value(), self.ui.spinBox_y_label.value(), self.ui.spinBox_x_val.value(), self.ui.spinBox_y_vals.value(), self.ui.comboBox_fonts.currentText(), self.ui.spinBox_mean_val_size.value(), self.ui.check_N_.isChecked(), self.ui.check_background.isChecked(), self.ui.check_change_corr_fig_down_limit.isChecked(), self.ui.doubleSpinBox_corr_figs.value(), self.ui.spinBox_points_corrFIGS.value(), self.ui.doubleSpinBox_corr_figs_fontscale.value(), self.ui.check_sort_or_not_corr_figs.isChecked(), self.ui.check_setka.isChecked(), self.ui.order_box_plot.text(), self.ui.STAT_znachimost_order_box_plot.text()
        #основная функция - comboBox и comboBox2 -- это для excel файла
        figs_plot(plot_feature_data__, self.ui.path_for_plot.text(), self.ui.comboBox.currentText(), self.ui.comboBox_2.currentText(),
                  self.ui.check_box_plot.isChecked(), self.ui.check_corr_matrix.isChecked(), self.ui.check_corr_figs.isChecked())
    #сводные таблицы
    def pivot_table(self):
        do_for_each_sheet(self.ui.path_for_pivot_table.text(), self.ui.comboBox_pivot_table.currentText(), self.ui.comboBox_pivot_hue.currentText(), self.ui.spinBox_pivot_table.value(), self.ui.comboBox_sd_or_se_pivot.currentText())

    def corr_table(self):
        corr_for_each_sheeeeeeet(self.ui.path_for_pivot_table.text(), self.ui.comboBox_pivot_table.currentText(), self.ui.comboBox_pivot_hue.currentText(), self.ui.comboBox_correlation_person_or_not.currentText(), self.ui.check_color_for_corr_pivot.isChecked(), self.ui.comboBox_correlation_color_map.currentText())

    #Biola
    def biola_do(self):
        plot_fiture = self.ui.doubleSpinBox_Biola.value(), self.ui.comboBox_Biola_SD_or.currentText(), self.ui.comboBox_Biola_language.currentText(), self.ui.check_setka_biola.isChecked()
        biola_result(plot_fiture, self.ui.path_for_biola.text(), self.ui.comboBox_biola.currentText(), self.ui.spinBox_biola_born.value(), self.ui.spinBox_biola_fluc.value(), self.ui.spinBox_biola_born_odd.value(), self.ui.spinBox_biola_fluc_odd.value())

    def biola_concentration(self):
        conentration_to_excel(self.ui.path_for_biola.text(), self.ui.comboBox_biola_concentration.currentText())

    #Лазерный пинцет
    def LT(self):
        laser_tweezers(self.ui.path_for_LT.text(), self.ui.sep_for_LT.text(), self.ui.a_dop.value(), self.ui.b_dop.value(),  self.ui.dateEdit_2.text(), self.ui.a_main.value(), self.ui.b_main.value(),  self.ui.dateEdit.text(), self.ui.sep_for_LT_values.text(), self.ui.position.value())

    #catplot

    def cat_plot(self):
        plot_catplot(self.ui.path_for_catplot.text(), self.ui.comboBox_excel_catplot.currentText(), self.ui.comboBox_excel_sheet_catplot.currentText(), self.ui.comboBox_catplot_x.currentText(), self.ui.comboBox_catplot_y.currentText(), self.ui.comboBox_catplot_hue.currentText(), self.ui.comboBox_color_catplot.currentText(), self.ui.comboBox_catplot_SD_or_not.currentText(), self.ui.comboBox_template_catplot.currentText(), self.ui.comboBox_catplot_form_x.currentText(), self.ui.comboBox_catplot_form_y.currentText(), self.ui.comboBox_catplot_form_hue.currentText(), self.ui.comboBox_stat_test_catplot.currentText(), self.ui.check_stat_znachimost_catplot.isChecked(), self.ui.doubleSpinBox_catplot.value(), self.ui.comboBox_catplot_mult_stat.currentText(), self.ui.comboBox_catplot_stat_formatt.currentText())
    ###
    #добавление списка файлов в папке в comboBox
    ###
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



######################################
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

    def add_excel_files_to_combobox_pivot(self):
        files = glob.glob(self.ui.path_for_pivot_table.text() + '//' + '*.xlsx')
        files = get_name_out_of_path(files)
        self.ui.comboBox_pivot_table.clear()  # удалить все элементы из combobox
        self.ui.comboBox_pivot_table.addItems(files)

    def add_sheets_to_combobox_pivot(self):
        path_file = self.ui.path_for_pivot_table.text() + '//' + self.ui.comboBox_pivot_table.currentText()
        sheets = pd.ExcelFile(path_file).sheet_names
        # прочитаем файл
        df = pd.read_excel(path_file, sheet_name=sheets[0])
        self.ui.comboBox_pivot_hue.clear()  # удалить все элементы из combobox
        self.ui.comboBox_pivot_hue.addItems(df.columns)


    def add_biola_file(self):
        files = glob.glob(self.ui.path_for_biola.text() + '//' + '*.txt')
        files = get_name_out_of_path(files)
        self.ui.comboBox_biola.clear()  #удалить все элементы из combobox
        self.ui.comboBox_biola.addItems(files)

        files2 = glob.glob(self.ui.path_for_biola.text() + '//' + '*.pdf')
        files2 = get_name_out_of_path(files2)
        self.ui.comboBox_biola_concentration.clear()  # удалить все элементы из combobox
        self.ui.comboBox_biola_concentration.addItems(files2)


basedir = os.path.dirname(__file__)
#стандарт
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'LOGO.ico')))
    window = Main_window()
    window.show()
    sys.exit(app.exec())