# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDateEdit, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(728, 739)
        icon = QIcon()
        icon.addFile(u"LOGO.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(128, 160, 165);")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.comboBox_style_sheet = QComboBox(self.centralwidget)
        self.comboBox_style_sheet.addItem("")
        self.comboBox_style_sheet.addItem("")
        self.comboBox_style_sheet.setObjectName(u"comboBox_style_sheet")
        self.comboBox_style_sheet.setFont(font)
        self.comboBox_style_sheet.setStyleSheet(u"color: rgb(128, 160, 165);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.comboBox_style_sheet, 1, 1, 1, 1)

        self.Lab_stuff = QTabWidget(self.centralwidget)
        self.Lab_stuff.setObjectName(u"Lab_stuff")
        palette = QPalette()
        brush = QBrush(QColor(249, 249, 249, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.Lab_stuff.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.Lab_stuff.setFont(font1)
        self.Lab_stuff.setStyleSheet(u"/*background-color: rgb(249, 249, 249);")
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.gridLayout_5 = QGridLayout(self.tabWidgetPage1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_save_exel_csv = QPushButton(self.tabWidgetPage1)
        self.btn_save_exel_csv.setObjectName(u"btn_save_exel_csv")
        palette1 = QPalette()
        brush1 = QBrush(QColor(128, 160, 165, 50))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.btn_save_exel_csv.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.btn_save_exel_csv.setFont(font2)
        self.btn_save_exel_csv.setAutoFillBackground(False)
        self.btn_save_exel_csv.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")
        self.btn_save_exel_csv.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_save_exel_csv, 16, 0, 1, 1)

        self.line_14 = QFrame(self.tabWidgetPage1)
        self.line_14.setObjectName(u"line_14")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.line_14.setFont(font3)
        self.line_14.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_14.setFrameShadow(QFrame.Plain)
        self.line_14.setLineWidth(3)
        self.line_14.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_14, 1, 0, 1, 1)

        self.line_3 = QFrame(self.tabWidgetPage1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFont(font3)
        self.line_3.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_3, 8, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(13, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_path = QLabel(self.tabWidgetPage1)
        self.lb_path.setObjectName(u"lb_path")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        self.lb_path.setFont(font4)

        self.horizontalLayout_7.addWidget(self.lb_path)

        self.main_path = QLineEdit(self.tabWidgetPage1)
        self.main_path.setObjectName(u"main_path")
        font5 = QFont()
        font5.setPointSize(11)
        self.main_path.setFont(font5)

        self.horizontalLayout_7.addWidget(self.main_path)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.comboBox_RheoScan_path_save = QComboBox(self.tabWidgetPage1)
        self.comboBox_RheoScan_path_save.addItem("")
        self.comboBox_RheoScan_path_save.addItem("")
        self.comboBox_RheoScan_path_save.setObjectName(u"comboBox_RheoScan_path_save")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_RheoScan_path_save.sizePolicy().hasHeightForWidth())
        self.comboBox_RheoScan_path_save.setSizePolicy(sizePolicy)
        self.comboBox_RheoScan_path_save.setFont(font5)

        self.horizontalLayout_71.addWidget(self.comboBox_RheoScan_path_save)

        self.check_approx_deform_raw_data = QCheckBox(self.tabWidgetPage1)
        self.check_approx_deform_raw_data.setObjectName(u"check_approx_deform_raw_data")
        self.check_approx_deform_raw_data.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.check_approx_deform_raw_data.sizePolicy().hasHeightForWidth())
        self.check_approx_deform_raw_data.setSizePolicy(sizePolicy1)
        self.check_approx_deform_raw_data.setFont(font4)

        self.horizontalLayout_71.addWidget(self.check_approx_deform_raw_data, 0, Qt.AlignHCenter)


        self.gridLayout_3.addLayout(self.horizontalLayout_71, 14, 0, 1, 1)

        self.line = QFrame(self.tabWidgetPage1)
        self.line.setObjectName(u"line")
        self.line.setFont(font3)
        self.line.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line, 11, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.tabWidgetPage1)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setMaximumSize(QSize(16777215, 61))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        font6.setStrikeOut(False)
        font6.setHintingPreference(QFont.PreferNoHinting)
        self.label_20.setFont(font6)
        self.label_20.setTextFormat(Qt.RichText)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setMargin(0)
        self.label_20.setIndent(1)

        self.horizontalLayout_2.addWidget(self.label_20)

        self.tua_1_agg = QSpinBox(self.widget)
        self.tua_1_agg.setObjectName(u"tua_1_agg")
        self.tua_1_agg.setEnabled(False)
        sizePolicy.setHeightForWidth(self.tua_1_agg.sizePolicy().hasHeightForWidth())
        self.tua_1_agg.setSizePolicy(sizePolicy)
        self.tua_1_agg.setFont(font5)
        self.tua_1_agg.setMinimum(1)
        self.tua_1_agg.setMaximum(200)
        self.tua_1_agg.setValue(20)

        self.horizontalLayout_2.addWidget(self.tua_1_agg)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setMaximumSize(QSize(16777215, 61))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(12)
        self.label_21.setFont(font7)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_21.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_21)

        self.tua_2_agg = QSpinBox(self.widget)
        self.tua_2_agg.setObjectName(u"tua_2_agg")
        self.tua_2_agg.setEnabled(False)
        sizePolicy.setHeightForWidth(self.tua_2_agg.sizePolicy().hasHeightForWidth())
        self.tua_2_agg.setSizePolicy(sizePolicy)
        self.tua_2_agg.setFont(font5)
        self.tua_2_agg.setMinimum(1)
        self.tua_2_agg.setMaximum(10000)
        self.tua_2_agg.setValue(200)

        self.horizontalLayout_3.addWidget(self.tua_2_agg)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addWidget(self.widget)

        self.widget1 = QWidget(self.tabWidgetPage1)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.label_23 = QLabel(self.widget1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy4)
        self.label_23.setFont(font5)
        self.label_23.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_23)

        self.r2_def = QDoubleSpinBox(self.widget1)
        self.r2_def.setObjectName(u"r2_def")
        self.r2_def.setEnabled(False)
        sizePolicy.setHeightForWidth(self.r2_def.sizePolicy().hasHeightForWidth())
        self.r2_def.setSizePolicy(sizePolicy)
        self.r2_def.setFont(font5)
        self.r2_def.setDecimals(3)
        self.r2_def.setMinimum(0.600000000000000)
        self.r2_def.setMaximum(0.999000000000000)
        self.r2_def.setSingleStep(0.001000000000000)
        self.r2_def.setValue(0.950000000000000)

        self.horizontalLayout.addWidget(self.r2_def, 0, Qt.AlignRight)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.label_18 = QLabel(self.widget1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setFont(font5)
        self.label_18.setWordWrap(True)

        self.horizontalLayout_118.addWidget(self.label_18)

        self.spinBox_n_max_deform = QSpinBox(self.widget1)
        self.spinBox_n_max_deform.setObjectName(u"spinBox_n_max_deform")
        self.spinBox_n_max_deform.setEnabled(False)
        sizePolicy.setHeightForWidth(self.spinBox_n_max_deform.sizePolicy().hasHeightForWidth())
        self.spinBox_n_max_deform.setSizePolicy(sizePolicy)
        self.spinBox_n_max_deform.setFont(font5)
        self.spinBox_n_max_deform.setMinimum(3)
        self.spinBox_n_max_deform.setMaximum(13)
        self.spinBox_n_max_deform.setValue(10)

        self.horizontalLayout_118.addWidget(self.spinBox_n_max_deform)


        self.verticalLayout_3.addLayout(self.horizontalLayout_118)


        self.horizontalLayout_4.addWidget(self.widget1)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 7, 0, 1, 1)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.dfd = QFrame(self.tabWidgetPage1)
        self.dfd.setObjectName(u"dfd")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.dfd.sizePolicy().hasHeightForWidth())
        self.dfd.setSizePolicy(sizePolicy5)
        self.dfd.setStyleSheet(u"QFrame#dfd{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.dfd)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.check_approx_agg = QCheckBox(self.dfd)
        self.check_approx_agg.setObjectName(u"check_approx_agg")
        self.check_approx_agg.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.check_approx_agg.sizePolicy().hasHeightForWidth())
        self.check_approx_agg.setSizePolicy(sizePolicy6)
        self.check_approx_agg.setFont(font4)
        self.check_approx_agg.setChecked(False)

        self.verticalLayout_5.addWidget(self.check_approx_agg)

        self.check_figs_for_agg = QCheckBox(self.dfd)
        self.check_figs_for_agg.setObjectName(u"check_figs_for_agg")
        self.check_figs_for_agg.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.check_figs_for_agg.sizePolicy().hasHeightForWidth())
        self.check_figs_for_agg.setSizePolicy(sizePolicy6)
        self.check_figs_for_agg.setFont(font4)

        self.verticalLayout_5.addWidget(self.check_figs_for_agg)


        self.horizontalLayout_117.addWidget(self.dfd)

        self.qwe = QFrame(self.tabWidgetPage1)
        self.qwe.setObjectName(u"qwe")
        sizePolicy1.setHeightForWidth(self.qwe.sizePolicy().hasHeightForWidth())
        self.qwe.setSizePolicy(sizePolicy1)
        self.qwe.setStyleSheet(u"QFrame#qwe{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.qwe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.check_approx_deform = QCheckBox(self.qwe)
        self.check_approx_deform.setObjectName(u"check_approx_deform")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.check_approx_deform.sizePolicy().hasHeightForWidth())
        self.check_approx_deform.setSizePolicy(sizePolicy7)
        self.check_approx_deform.setFont(font4)

        self.verticalLayout_2.addWidget(self.check_approx_deform)

        self.check_for_deform = QCheckBox(self.qwe)
        self.check_for_deform.setObjectName(u"check_for_deform")
        self.check_for_deform.setEnabled(False)
        self.check_for_deform.setFont(font4)

        self.verticalLayout_2.addWidget(self.check_for_deform)


        self.horizontalLayout_117.addWidget(self.qwe)


        self.gridLayout_3.addLayout(self.horizontalLayout_117, 5, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.check_stat_for_column = QCheckBox(self.tabWidgetPage1)
        self.check_stat_for_column.setObjectName(u"check_stat_for_column")
        self.check_stat_for_column.setFont(font4)

        self.horizontalLayout_27.addWidget(self.check_stat_for_column)

        self.vibros_delete = QCheckBox(self.tabWidgetPage1)
        self.vibros_delete.setObjectName(u"vibros_delete")
        self.vibros_delete.setFont(font4)
        self.vibros_delete.setChecked(False)

        self.horizontalLayout_27.addWidget(self.vibros_delete)

        self.iqr_vibros = QDoubleSpinBox(self.tabWidgetPage1)
        self.iqr_vibros.setObjectName(u"iqr_vibros")
        self.iqr_vibros.setEnabled(False)
        sizePolicy.setHeightForWidth(self.iqr_vibros.sizePolicy().hasHeightForWidth())
        self.iqr_vibros.setSizePolicy(sizePolicy)
        self.iqr_vibros.setFont(font5)
        self.iqr_vibros.setDecimals(1)
        self.iqr_vibros.setMinimum(0.500000000000000)
        self.iqr_vibros.setMaximum(5.000000000000000)
        self.iqr_vibros.setSingleStep(0.500000000000000)
        self.iqr_vibros.setValue(1.500000000000000)

        self.horizontalLayout_27.addWidget(self.iqr_vibros)

        self.label_11 = QLabel(self.tabWidgetPage1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(False)
        self.label_11.setFont(font5)

        self.horizontalLayout_27.addWidget(self.label_11)


        self.gridLayout_3.addLayout(self.horizontalLayout_27, 9, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_sort_data_RheoScan = QPushButton(self.tabWidgetPage1)
        self.btn_sort_data_RheoScan.setObjectName(u"btn_sort_data_RheoScan")
        sizePolicy.setHeightForWidth(self.btn_sort_data_RheoScan.sizePolicy().hasHeightForWidth())
        self.btn_sort_data_RheoScan.setSizePolicy(sizePolicy)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.btn_sort_data_RheoScan.setPalette(palette2)
        self.btn_sort_data_RheoScan.setFont(font2)
        self.btn_sort_data_RheoScan.setAutoFillBackground(False)
        self.btn_sort_data_RheoScan.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")
        self.btn_sort_data_RheoScan.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_sort_data_RheoScan)

        self.label = QLabel(self.tabWidgetPage1)
        self.label.setObjectName(u"label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy8)
        self.label.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label)

        self.spinBox_level = QSpinBox(self.tabWidgetPage1)
        self.spinBox_level.setObjectName(u"spinBox_level")
        sizePolicy.setHeightForWidth(self.spinBox_level.sizePolicy().hasHeightForWidth())
        self.spinBox_level.setSizePolicy(sizePolicy)
        self.spinBox_level.setFont(font4)
        self.spinBox_level.setMinimum(1)
        self.spinBox_level.setMaximum(5)
        self.spinBox_level.setValue(1)

        self.horizontalLayout_5.addWidget(self.spinBox_level)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.line_4 = QFrame(self.tabWidgetPage1)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFont(font3)
        self.line_4.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_4, 15, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.check_save_exel = QCheckBox(self.tabWidgetPage1)
        self.check_save_exel.setObjectName(u"check_save_exel")
        self.check_save_exel.setFont(font4)
        self.check_save_exel.setChecked(True)

        self.horizontalLayout_8.addWidget(self.check_save_exel)

        self.check_save_csv = QCheckBox(self.tabWidgetPage1)
        self.check_save_csv.setObjectName(u"check_save_csv")
        self.check_save_csv.setFont(font4)

        self.horizontalLayout_8.addWidget(self.check_save_csv)

        self.check_save_RheoScan_overall = QCheckBox(self.tabWidgetPage1)
        self.check_save_RheoScan_overall.setObjectName(u"check_save_RheoScan_overall")
        self.check_save_RheoScan_overall.setFont(font4)
        self.check_save_RheoScan_overall.setChecked(False)

        self.horizontalLayout_8.addWidget(self.check_save_RheoScan_overall)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 12, 0, 1, 1)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.hjgf = QFrame(self.tabWidgetPage1)
        self.hjgf.setObjectName(u"hjgf")
        sizePolicy1.setHeightForWidth(self.hjgf.sizePolicy().hasHeightForWidth())
        self.hjgf.setSizePolicy(sizePolicy1)
        self.hjgf.setStyleSheet(u"QFrame#hjgf{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_32 = QVBoxLayout(self.hjgf)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.lb_separator = QLabel(self.hjgf)
        self.lb_separator.setObjectName(u"lb_separator")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.lb_separator.sizePolicy().hasHeightForWidth())
        self.lb_separator.setSizePolicy(sizePolicy9)
        self.lb_separator.setFont(font4)

        self.horizontalLayout_65.addWidget(self.lb_separator, 0, Qt.AlignLeft)

        self.separator_for_data = QLineEdit(self.hjgf)
        self.separator_for_data.setObjectName(u"separator_for_data")
        sizePolicy.setHeightForWidth(self.separator_for_data.sizePolicy().hasHeightForWidth())
        self.separator_for_data.setSizePolicy(sizePolicy)
        self.separator_for_data.setFont(font5)
        self.separator_for_data.setToolTipDuration(4)
        self.separator_for_data.setAutoFillBackground(False)

        self.horizontalLayout_65.addWidget(self.separator_for_data)


        self.verticalLayout_32.addLayout(self.horizontalLayout_65)

        self.check_name_rheoscan = QCheckBox(self.hjgf)
        self.check_name_rheoscan.setObjectName(u"check_name_rheoscan")
        self.check_name_rheoscan.setEnabled(True)
        self.check_name_rheoscan.setFont(font4)
        self.check_name_rheoscan.setChecked(False)

        self.verticalLayout_32.addWidget(self.check_name_rheoscan, 0, Qt.AlignHCenter)

        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.label_19 = QLabel(self.hjgf)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy8)
        self.label_19.setFont(font4)

        self.horizontalLayout_116.addWidget(self.label_19)

        self.spinBox_check_name_rheoscan = QSpinBox(self.hjgf)
        self.spinBox_check_name_rheoscan.setObjectName(u"spinBox_check_name_rheoscan")
        self.spinBox_check_name_rheoscan.setEnabled(False)
        sizePolicy.setHeightForWidth(self.spinBox_check_name_rheoscan.sizePolicy().hasHeightForWidth())
        self.spinBox_check_name_rheoscan.setSizePolicy(sizePolicy)
        self.spinBox_check_name_rheoscan.setFont(font4)
        self.spinBox_check_name_rheoscan.setMinimum(1)
        self.spinBox_check_name_rheoscan.setMaximum(3)
        self.spinBox_check_name_rheoscan.setValue(1)

        self.horizontalLayout_116.addWidget(self.spinBox_check_name_rheoscan)


        self.verticalLayout_32.addLayout(self.horizontalLayout_116)


        self.horizontalLayout_119.addWidget(self.hjgf)

        self.vbn = QFrame(self.tabWidgetPage1)
        self.vbn.setObjectName(u"vbn")
        sizePolicy1.setHeightForWidth(self.vbn.sizePolicy().hasHeightForWidth())
        self.vbn.setSizePolicy(sizePolicy1)
        self.vbn.setAutoFillBackground(False)
        self.vbn.setStyleSheet(u"QFrame#vbn{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.vbn)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.check_agg = QCheckBox(self.vbn)
        self.check_agg.setObjectName(u"check_agg")
        self.check_agg.setFont(font4)
        self.check_agg.setChecked(True)

        self.verticalLayout_11.addWidget(self.check_agg)

        self.check_stress = QCheckBox(self.vbn)
        self.check_stress.setObjectName(u"check_stress")
        self.check_stress.setFont(font4)
        self.check_stress.setChecked(True)

        self.verticalLayout_11.addWidget(self.check_stress)

        self.check_deform = QCheckBox(self.vbn)
        self.check_deform.setObjectName(u"check_deform")
        self.check_deform.setFont(font4)
        self.check_deform.setChecked(True)

        self.verticalLayout_11.addWidget(self.check_deform)


        self.horizontalLayout_136.addLayout(self.verticalLayout_11)

        self.line_22 = QFrame(self.vbn)
        self.line_22.setObjectName(u"line_22")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.line_22.sizePolicy().hasHeightForWidth())
        self.line_22.setSizePolicy(sizePolicy10)
        self.line_22.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_22.setFrameShadow(QFrame.Plain)
        self.line_22.setLineWidth(4)
        self.line_22.setFrameShape(QFrame.VLine)

        self.horizontalLayout_136.addWidget(self.line_22)

        self.check_dop_CSS_parameter = QCheckBox(self.vbn)
        self.check_dop_CSS_parameter.setObjectName(u"check_dop_CSS_parameter")
        self.check_dop_CSS_parameter.setFont(font4)
        self.check_dop_CSS_parameter.setChecked(False)

        self.horizontalLayout_136.addWidget(self.check_dop_CSS_parameter)


        self.verticalLayout_4.addLayout(self.horizontalLayout_136)


        self.horizontalLayout_119.addWidget(self.vbn)


        self.gridLayout_3.addLayout(self.horizontalLayout_119, 4, 0, 1, 1)

        self.line_15 = QFrame(self.tabWidgetPage1)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFont(font3)
        self.line_15.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setLineWidth(3)
        self.line_15.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_15, 13, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.Lab_stuff.addTab(self.tabWidgetPage1, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_10 = QGridLayout(self.tab_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.lb_path_2 = QLabel(self.tab_5)
        self.lb_path_2.setObjectName(u"lb_path_2")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.lb_path_2.sizePolicy().hasHeightForWidth())
        self.lb_path_2.setSizePolicy(sizePolicy11)
        self.lb_path_2.setFont(font4)

        self.horizontalLayout_40.addWidget(self.lb_path_2)

        self.path_for_biola = QLineEdit(self.tab_5)
        self.path_for_biola.setObjectName(u"path_for_biola")
        self.path_for_biola.setFont(font5)

        self.horizontalLayout_40.addWidget(self.path_for_biola)


        self.gridLayout_10.addLayout(self.horizontalLayout_40, 0, 0, 1, 1)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.lb_path_3 = QLabel(self.tab_5)
        self.lb_path_3.setObjectName(u"lb_path_3")
        sizePolicy8.setHeightForWidth(self.lb_path_3.sizePolicy().hasHeightForWidth())
        self.lb_path_3.setSizePolicy(sizePolicy8)
        self.lb_path_3.setFont(font4)
        self.lb_path_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.lb_path_3)

        self.comboBox_biola = QComboBox(self.tab_5)
        self.comboBox_biola.setObjectName(u"comboBox_biola")
        sizePolicy11.setHeightForWidth(self.comboBox_biola.sizePolicy().hasHeightForWidth())
        self.comboBox_biola.setSizePolicy(sizePolicy11)
        self.comboBox_biola.setFont(font5)

        self.horizontalLayout_41.addWidget(self.comboBox_biola)


        self.horizontalLayout_73.addLayout(self.horizontalLayout_41)


        self.gridLayout_10.addLayout(self.horizontalLayout_73, 1, 0, 1, 1)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.lb_path_16 = QLabel(self.tab_5)
        self.lb_path_16.setObjectName(u"lb_path_16")
        sizePolicy8.setHeightForWidth(self.lb_path_16.sizePolicy().hasHeightForWidth())
        self.lb_path_16.setSizePolicy(sizePolicy8)
        self.lb_path_16.setFont(font4)
        self.lb_path_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_72.addWidget(self.lb_path_16)

        self.comboBox_biola_concentration = QComboBox(self.tab_5)
        self.comboBox_biola_concentration.setObjectName(u"comboBox_biola_concentration")
        sizePolicy11.setHeightForWidth(self.comboBox_biola_concentration.sizePolicy().hasHeightForWidth())
        self.comboBox_biola_concentration.setSizePolicy(sizePolicy11)
        self.comboBox_biola_concentration.setFont(font5)

        self.horizontalLayout_72.addWidget(self.comboBox_biola_concentration)


        self.gridLayout_10.addLayout(self.horizontalLayout_72, 2, 0, 1, 1)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.vvvv = QFrame(self.tab_5)
        self.vvvv.setObjectName(u"vvvv")
        sizePolicy11.setHeightForWidth(self.vvvv.sizePolicy().hasHeightForWidth())
        self.vvvv.setSizePolicy(sizePolicy11)
        self.vvvv.setStyleSheet(u"QFrame#vvvv{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.vvv = QHBoxLayout(self.vvvv)
        self.vvv.setObjectName(u"vvv")
        self.vvv.setContentsMargins(5, 5, 5, 5)
        self.label_15 = QLabel(self.vvvv)
        self.label_15.setObjectName(u"label_15")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy12)
        self.label_15.setFont(font5)

        self.vvv.addWidget(self.label_15)

        self.line_16 = QFrame(self.vvvv)
        self.line_16.setObjectName(u"line_16")
        sizePolicy10.setHeightForWidth(self.line_16.sizePolicy().hasHeightForWidth())
        self.line_16.setSizePolicy(sizePolicy10)
        self.line_16.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_16.setFrameShadow(QFrame.Plain)
        self.line_16.setLineWidth(4)
        self.line_16.setFrameShape(QFrame.VLine)

        self.vvv.addWidget(self.line_16)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_16 = QLabel(self.vvvv)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.label_16)

        self.spinBox_biola_born_odd = QSpinBox(self.vvvv)
        self.spinBox_biola_born_odd.setObjectName(u"spinBox_biola_born_odd")
        sizePolicy5.setHeightForWidth(self.spinBox_biola_born_odd.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_born_odd.setSizePolicy(sizePolicy5)
        self.spinBox_biola_born_odd.setFont(font5)
        self.spinBox_biola_born_odd.setMinimum(1)
        self.spinBox_biola_born_odd.setMaximum(201)
        self.spinBox_biola_born_odd.setSingleStep(2)
        self.spinBox_biola_born_odd.setValue(41)

        self.horizontalLayout_46.addWidget(self.spinBox_biola_born_odd)


        self.verticalLayout_23.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_17 = QLabel(self.vvvv)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setFont(font5)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.label_17)

        self.spinBox_biola_fluc_odd = QSpinBox(self.vvvv)
        self.spinBox_biola_fluc_odd.setObjectName(u"spinBox_biola_fluc_odd")
        sizePolicy5.setHeightForWidth(self.spinBox_biola_fluc_odd.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_fluc_odd.setSizePolicy(sizePolicy5)
        self.spinBox_biola_fluc_odd.setFont(font5)
        self.spinBox_biola_fluc_odd.setMinimum(1)
        self.spinBox_biola_fluc_odd.setMaximum(201)
        self.spinBox_biola_fluc_odd.setSingleStep(2)
        self.spinBox_biola_fluc_odd.setValue(41)

        self.horizontalLayout_47.addWidget(self.spinBox_biola_fluc_odd)


        self.verticalLayout_23.addLayout(self.horizontalLayout_47)


        self.vvv.addLayout(self.verticalLayout_23)


        self.verticalLayout_31.addWidget(self.vvvv)

        self.lll = QFrame(self.tab_5)
        self.lll.setObjectName(u"lll")
        sizePolicy11.setHeightForWidth(self.lll.sizePolicy().hasHeightForWidth())
        self.lll.setSizePolicy(sizePolicy11)
        self.lll.setStyleSheet(u"QFrame#lll{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.horizontalLayout_44 = QHBoxLayout(self.lll)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(self.lll)
        self.label_12.setObjectName(u"label_12")
        sizePolicy12.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy12)
        self.label_12.setFont(font5)

        self.horizontalLayout_44.addWidget(self.label_12)

        self.line_17 = QFrame(self.lll)
        self.line_17.setObjectName(u"line_17")
        sizePolicy10.setHeightForWidth(self.line_17.sizePolicy().hasHeightForWidth())
        self.line_17.setSizePolicy(sizePolicy10)
        self.line_17.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_17.setFrameShadow(QFrame.Plain)
        self.line_17.setLineWidth(4)
        self.line_17.setFrameShape(QFrame.VLine)

        self.horizontalLayout_44.addWidget(self.line_17)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_13 = QLabel(self.lll)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setFont(font5)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.label_13)

        self.spinBox_biola_born = QSpinBox(self.lll)
        self.spinBox_biola_born.setObjectName(u"spinBox_biola_born")
        sizePolicy13 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.spinBox_biola_born.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_born.setSizePolicy(sizePolicy13)
        self.spinBox_biola_born.setFont(font5)
        self.spinBox_biola_born.setMinimum(1)
        self.spinBox_biola_born.setMaximum(201)
        self.spinBox_biola_born.setSingleStep(2)
        self.spinBox_biola_born.setValue(71)

        self.horizontalLayout_42.addWidget(self.spinBox_biola_born)


        self.verticalLayout_22.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_14 = QLabel(self.lll)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setFont(font5)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_14)

        self.spinBox_biola_fluc = QSpinBox(self.lll)
        self.spinBox_biola_fluc.setObjectName(u"spinBox_biola_fluc")
        sizePolicy5.setHeightForWidth(self.spinBox_biola_fluc.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_fluc.setSizePolicy(sizePolicy5)
        self.spinBox_biola_fluc.setFont(font5)
        self.spinBox_biola_fluc.setMinimum(1)
        self.spinBox_biola_fluc.setMaximum(201)
        self.spinBox_biola_fluc.setSingleStep(2)
        self.spinBox_biola_fluc.setValue(61)

        self.horizontalLayout_43.addWidget(self.spinBox_biola_fluc)


        self.verticalLayout_22.addLayout(self.horizontalLayout_43)


        self.horizontalLayout_44.addLayout(self.verticalLayout_22)


        self.verticalLayout_31.addWidget(self.lll)

        self.check_biola_plot_figs = QCheckBox(self.tab_5)
        self.check_biola_plot_figs.setObjectName(u"check_biola_plot_figs")
        self.check_biola_plot_figs.setEnabled(True)
        self.check_biola_plot_figs.setFont(font4)
        self.check_biola_plot_figs.setChecked(True)
        self.check_biola_plot_figs.setTristate(False)

        self.verticalLayout_31.addWidget(self.check_biola_plot_figs, 0, Qt.AlignHCenter)

        self.plp = QFrame(self.tab_5)
        self.plp.setObjectName(u"plp")
        self.plp.setEnabled(True)
        sizePolicy11.setHeightForWidth(self.plp.sizePolicy().hasHeightForWidth())
        self.plp.setSizePolicy(sizePolicy11)
        self.plp.setStyleSheet(u"QFrame#plp{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.plp)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(6, 6, 6, 6)
        self.lb_color_pal_box_13 = QLabel(self.plp)
        self.lb_color_pal_box_13.setObjectName(u"lb_color_pal_box_13")
        sizePolicy5.setHeightForWidth(self.lb_color_pal_box_13.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_13.setSizePolicy(sizePolicy5)
        font8 = QFont()
        font8.setPointSize(11)
        font8.setUnderline(True)
        self.lb_color_pal_box_13.setFont(font8)
        self.lb_color_pal_box_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.lb_color_pal_box_13)

        self.line_18 = QFrame(self.plp)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFont(font3)
        self.line_18.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_18.setFrameShadow(QFrame.Plain)
        self.line_18.setLineWidth(4)
        self.line_18.setFrameShape(QFrame.HLine)

        self.verticalLayout_30.addWidget(self.line_18)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.lb_color_pal_box_9 = QLabel(self.plp)
        self.lb_color_pal_box_9.setObjectName(u"lb_color_pal_box_9")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_9.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_9.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_9.setFont(font5)

        self.horizontalLayout_61.addWidget(self.lb_color_pal_box_9)

        self.doubleSpinBox_Biola = QDoubleSpinBox(self.plp)
        self.doubleSpinBox_Biola.setObjectName(u"doubleSpinBox_Biola")
        self.doubleSpinBox_Biola.setFont(font5)
        self.doubleSpinBox_Biola.setDecimals(1)
        self.doubleSpinBox_Biola.setMinimum(0.100000000000000)
        self.doubleSpinBox_Biola.setSingleStep(0.100000000000000)
        self.doubleSpinBox_Biola.setValue(1.000000000000000)

        self.horizontalLayout_61.addWidget(self.doubleSpinBox_Biola)


        self.verticalLayout_29.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.lb_color_pal_box_10 = QLabel(self.plp)
        self.lb_color_pal_box_10.setObjectName(u"lb_color_pal_box_10")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_10.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_10.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_10.setFont(font5)

        self.horizontalLayout_62.addWidget(self.lb_color_pal_box_10)

        self.comboBox_Biola_SD_or = QComboBox(self.plp)
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.setObjectName(u"comboBox_Biola_SD_or")
        sizePolicy14 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.comboBox_Biola_SD_or.sizePolicy().hasHeightForWidth())
        self.comboBox_Biola_SD_or.setSizePolicy(sizePolicy14)
        self.comboBox_Biola_SD_or.setFont(font5)

        self.horizontalLayout_62.addWidget(self.comboBox_Biola_SD_or)


        self.verticalLayout_29.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.check_setka_biola = QCheckBox(self.plp)
        self.check_setka_biola.setObjectName(u"check_setka_biola")
        self.check_setka_biola.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.check_setka_biola.sizePolicy().hasHeightForWidth())
        self.check_setka_biola.setSizePolicy(sizePolicy9)
        self.check_setka_biola.setFont(font5)
        self.check_setka_biola.setChecked(True)

        self.horizontalLayout_63.addWidget(self.check_setka_biola)

        self.lb_color_pal_box_11 = QLabel(self.plp)
        self.lb_color_pal_box_11.setObjectName(u"lb_color_pal_box_11")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_11.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_11.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_11.setFont(font5)

        self.horizontalLayout_63.addWidget(self.lb_color_pal_box_11, 0, Qt.AlignRight)

        self.comboBox_Biola_language = QComboBox(self.plp)
        self.comboBox_Biola_language.addItem("")
        self.comboBox_Biola_language.addItem("")
        self.comboBox_Biola_language.setObjectName(u"comboBox_Biola_language")
        sizePolicy14.setHeightForWidth(self.comboBox_Biola_language.sizePolicy().hasHeightForWidth())
        self.comboBox_Biola_language.setSizePolicy(sizePolicy14)
        self.comboBox_Biola_language.setFont(font5)

        self.horizontalLayout_63.addWidget(self.comboBox_Biola_language)


        self.verticalLayout_29.addLayout(self.horizontalLayout_63)


        self.verticalLayout_30.addLayout(self.verticalLayout_29)


        self.verticalLayout_31.addWidget(self.plp)


        self.gridLayout_10.addLayout(self.verticalLayout_31, 3, 0, 1, 1)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.btn_biola = QPushButton(self.tab_5)
        self.btn_biola.setObjectName(u"btn_biola")
        self.btn_biola.setFont(font5)
        self.btn_biola.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.horizontalLayout_74.addWidget(self.btn_biola)

        self.btn_biola_concentration = QPushButton(self.tab_5)
        self.btn_biola_concentration.setObjectName(u"btn_biola_concentration")
        self.btn_biola_concentration.setFont(font5)
        self.btn_biola_concentration.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.horizontalLayout_74.addWidget(self.btn_biola_concentration)


        self.gridLayout_10.addLayout(self.horizontalLayout_74, 4, 0, 1, 1)

        self.Lab_stuff.addTab(self.tab_5, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.formLayout = QFormLayout(self.tab_7)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.lb_stattest_13 = QLabel(self.tab_7)
        self.lb_stattest_13.setObjectName(u"lb_stattest_13")
        self.lb_stattest_13.setEnabled(True)
        self.lb_stattest_13.setFont(font5)

        self.horizontalLayout_131.addWidget(self.lb_stattest_13)

        self.comboBox_LT_calibration = QComboBox(self.tab_7)
        self.comboBox_LT_calibration.addItem("")
        self.comboBox_LT_calibration.addItem("")
        self.comboBox_LT_calibration.setObjectName(u"comboBox_LT_calibration")
        self.comboBox_LT_calibration.setEnabled(True)
        self.comboBox_LT_calibration.setFont(font5)

        self.horizontalLayout_131.addWidget(self.comboBox_LT_calibration)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout_131)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.asd = QFrame(self.tab_7)
        self.asd.setObjectName(u"asd")
        sizePolicy15 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.asd.sizePolicy().hasHeightForWidth())
        self.asd.setSizePolicy(sizePolicy15)
        self.asd.setStyleSheet(u"QFrame#asd{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_26 = QVBoxLayout(self.asd)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.lb_path_5 = QLabel(self.asd)
        self.lb_path_5.setObjectName(u"lb_path_5")
        sizePolicy16 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.lb_path_5.sizePolicy().hasHeightForWidth())
        self.lb_path_5.setSizePolicy(sizePolicy16)
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(11)
        font9.setUnderline(True)
        self.lb_path_5.setFont(font9)
        self.lb_path_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.lb_path_5)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.lb_path_17 = QLabel(self.asd)
        self.lb_path_17.setObjectName(u"lb_path_17")
        sizePolicy16.setHeightForWidth(self.lb_path_17.sizePolicy().hasHeightForWidth())
        self.lb_path_17.setSizePolicy(sizePolicy16)
        self.lb_path_17.setFont(font4)

        self.horizontalLayout_48.addWidget(self.lb_path_17)

        self.lb_path_7 = QLabel(self.asd)
        self.lb_path_7.setObjectName(u"lb_path_7")
        sizePolicy16.setHeightForWidth(self.lb_path_7.sizePolicy().hasHeightForWidth())
        self.lb_path_7.setSizePolicy(sizePolicy16)
        self.lb_path_7.setFont(font4)

        self.horizontalLayout_48.addWidget(self.lb_path_7)

        self.a_main = QDoubleSpinBox(self.asd)
        self.a_main.setObjectName(u"a_main")
        self.a_main.setFont(font5)
        self.a_main.setDecimals(5)
        self.a_main.setMaximum(50.000000000000000)
        self.a_main.setValue(0.220000000000000)

        self.horizontalLayout_48.addWidget(self.a_main)

        self.lb_path_18 = QLabel(self.asd)
        self.lb_path_18.setObjectName(u"lb_path_18")
        sizePolicy16.setHeightForWidth(self.lb_path_18.sizePolicy().hasHeightForWidth())
        self.lb_path_18.setSizePolicy(sizePolicy16)
        self.lb_path_18.setFont(font4)

        self.horizontalLayout_48.addWidget(self.lb_path_18)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.lb_path_8 = QLabel(self.asd)
        self.lb_path_8.setObjectName(u"lb_path_8")
        sizePolicy16.setHeightForWidth(self.lb_path_8.sizePolicy().hasHeightForWidth())
        self.lb_path_8.setSizePolicy(sizePolicy16)
        self.lb_path_8.setFont(font4)

        self.horizontalLayout_49.addWidget(self.lb_path_8)

        self.b_main = QDoubleSpinBox(self.asd)
        self.b_main.setObjectName(u"b_main")
        self.b_main.setFont(font5)
        self.b_main.setDecimals(5)
        self.b_main.setMinimum(-200.000000000000000)
        self.b_main.setMaximum(200.000000000000000)
        self.b_main.setValue(-0.800000000000000)

        self.horizontalLayout_49.addWidget(self.b_main)


        self.horizontalLayout_48.addLayout(self.horizontalLayout_49)


        self.verticalLayout_25.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.lb_path_12 = QLabel(self.asd)
        self.lb_path_12.setObjectName(u"lb_path_12")
        sizePolicy16.setHeightForWidth(self.lb_path_12.sizePolicy().hasHeightForWidth())
        self.lb_path_12.setSizePolicy(sizePolicy16)
        self.lb_path_12.setFont(font4)

        self.horizontalLayout_50.addWidget(self.lb_path_12)

        self.dateEdit = QDateEdit(self.asd)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font5)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_50.addWidget(self.dateEdit)


        self.verticalLayout_25.addLayout(self.horizontalLayout_50)


        self.verticalLayout_26.addLayout(self.verticalLayout_25)


        self.verticalLayout_50.addWidget(self.asd)

        self.hhhhh = QFrame(self.tab_7)
        self.hhhhh.setObjectName(u"hhhhh")
        sizePolicy15.setHeightForWidth(self.hhhhh.sizePolicy().hasHeightForWidth())
        self.hhhhh.setSizePolicy(sizePolicy15)
        self.hhhhh.setStyleSheet(u"QFrame#hhhhh{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.hhhhh)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.lb_path_6 = QLabel(self.hhhhh)
        self.lb_path_6.setObjectName(u"lb_path_6")
        sizePolicy17 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.lb_path_6.sizePolicy().hasHeightForWidth())
        self.lb_path_6.setSizePolicy(sizePolicy17)
        self.lb_path_6.setFont(font9)
        self.lb_path_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.lb_path_6)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.lb_path_19 = QLabel(self.hhhhh)
        self.lb_path_19.setObjectName(u"lb_path_19")
        sizePolicy16.setHeightForWidth(self.lb_path_19.sizePolicy().hasHeightForWidth())
        self.lb_path_19.setSizePolicy(sizePolicy16)
        self.lb_path_19.setFont(font4)

        self.horizontalLayout_115.addWidget(self.lb_path_19)

        self.lb_path_9 = QLabel(self.hhhhh)
        self.lb_path_9.setObjectName(u"lb_path_9")
        sizePolicy16.setHeightForWidth(self.lb_path_9.sizePolicy().hasHeightForWidth())
        self.lb_path_9.setSizePolicy(sizePolicy16)
        self.lb_path_9.setFont(font4)

        self.horizontalLayout_115.addWidget(self.lb_path_9)

        self.a_dop = QDoubleSpinBox(self.hhhhh)
        self.a_dop.setObjectName(u"a_dop")
        self.a_dop.setFont(font5)
        self.a_dop.setDecimals(5)
        self.a_dop.setMaximum(50.000000000000000)
        self.a_dop.setValue(1.410000000000000)

        self.horizontalLayout_115.addWidget(self.a_dop)

        self.lb_path_20 = QLabel(self.hhhhh)
        self.lb_path_20.setObjectName(u"lb_path_20")
        sizePolicy16.setHeightForWidth(self.lb_path_20.sizePolicy().hasHeightForWidth())
        self.lb_path_20.setSizePolicy(sizePolicy16)
        self.lb_path_20.setFont(font4)

        self.horizontalLayout_115.addWidget(self.lb_path_20)

        self.lb_path_21 = QLabel(self.hhhhh)
        self.lb_path_21.setObjectName(u"lb_path_21")
        sizePolicy16.setHeightForWidth(self.lb_path_21.sizePolicy().hasHeightForWidth())
        self.lb_path_21.setSizePolicy(sizePolicy16)
        self.lb_path_21.setFont(font4)

        self.horizontalLayout_115.addWidget(self.lb_path_21)

        self.b_dop = QDoubleSpinBox(self.hhhhh)
        self.b_dop.setObjectName(u"b_dop")
        self.b_dop.setFont(font5)
        self.b_dop.setDecimals(5)
        self.b_dop.setMinimum(-200.000000000000000)
        self.b_dop.setMaximum(200.000000000000000)
        self.b_dop.setValue(-29.500000000000000)

        self.horizontalLayout_115.addWidget(self.b_dop)


        self.verticalLayout_46.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.lb_path_11 = QLabel(self.hhhhh)
        self.lb_path_11.setObjectName(u"lb_path_11")
        sizePolicy16.setHeightForWidth(self.lb_path_11.sizePolicy().hasHeightForWidth())
        self.lb_path_11.setSizePolicy(sizePolicy16)
        self.lb_path_11.setFont(font4)

        self.horizontalLayout_53.addWidget(self.lb_path_11)

        self.dateEdit_2 = QDateEdit(self.hhhhh)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setFont(font5)
        self.dateEdit_2.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_53.addWidget(self.dateEdit_2)


        self.verticalLayout_46.addLayout(self.horizontalLayout_53)


        self.verticalLayout_27.addLayout(self.verticalLayout_46)


        self.verticalLayout_50.addWidget(self.hhhhh)

        self.hhhhh_exp = QFrame(self.tab_7)
        self.hhhhh_exp.setObjectName(u"hhhhh_exp")
        self.hhhhh_exp.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.hhhhh_exp.sizePolicy().hasHeightForWidth())
        self.hhhhh_exp.setSizePolicy(sizePolicy10)
        self.hhhhh_exp.setStyleSheet(u"QFrame#hhhhh_exp{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_47 = QVBoxLayout(self.hhhhh_exp)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(5, 5, 5, 5)
        self.lb_path_10 = QLabel(self.hhhhh_exp)
        self.lb_path_10.setObjectName(u"lb_path_10")
        sizePolicy17.setHeightForWidth(self.lb_path_10.sizePolicy().hasHeightForWidth())
        self.lb_path_10.setSizePolicy(sizePolicy17)
        self.lb_path_10.setFont(font9)
        self.lb_path_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.lb_path_10)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.lb_path_22 = QLabel(self.hhhhh_exp)
        self.lb_path_22.setObjectName(u"lb_path_22")
        sizePolicy16.setHeightForWidth(self.lb_path_22.sizePolicy().hasHeightForWidth())
        self.lb_path_22.setSizePolicy(sizePolicy16)
        self.lb_path_22.setFont(font4)

        self.horizontalLayout_51.addWidget(self.lb_path_22)

        self.lb_path_23 = QLabel(self.hhhhh_exp)
        self.lb_path_23.setObjectName(u"lb_path_23")
        sizePolicy16.setHeightForWidth(self.lb_path_23.sizePolicy().hasHeightForWidth())
        self.lb_path_23.setSizePolicy(sizePolicy16)
        self.lb_path_23.setFont(font4)

        self.horizontalLayout_51.addWidget(self.lb_path_23, 0, Qt.AlignHCenter)

        self.dop_cal_k = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_k.setObjectName(u"dop_cal_k")
        self.dop_cal_k.setFont(font5)
        self.dop_cal_k.setDecimals(5)
        self.dop_cal_k.setMinimum(-50.000000000000000)
        self.dop_cal_k.setMaximum(50.000000000000000)
        self.dop_cal_k.setValue(0.500000000000000)

        self.horizontalLayout_51.addWidget(self.dop_cal_k)

        self.lb_path_27 = QLabel(self.hhhhh_exp)
        self.lb_path_27.setObjectName(u"lb_path_27")
        sizePolicy16.setHeightForWidth(self.lb_path_27.sizePolicy().hasHeightForWidth())
        self.lb_path_27.setSizePolicy(sizePolicy16)
        self.lb_path_27.setFont(font4)

        self.horizontalLayout_51.addWidget(self.lb_path_27, 0, Qt.AlignHCenter)

        self.dop_cal_y0 = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_y0.setObjectName(u"dop_cal_y0")
        self.dop_cal_y0.setFont(font5)
        self.dop_cal_y0.setDecimals(5)
        self.dop_cal_y0.setMinimum(-50.000000000000000)
        self.dop_cal_y0.setMaximum(50.000000000000000)
        self.dop_cal_y0.setValue(-1.000000000000000)

        self.horizontalLayout_51.addWidget(self.dop_cal_y0)

        self.lb_path_28 = QLabel(self.hhhhh_exp)
        self.lb_path_28.setObjectName(u"lb_path_28")
        sizePolicy16.setHeightForWidth(self.lb_path_28.sizePolicy().hasHeightForWidth())
        self.lb_path_28.setSizePolicy(sizePolicy16)
        self.lb_path_28.setFont(font4)

        self.horizontalLayout_51.addWidget(self.lb_path_28, 0, Qt.AlignHCenter)

        self.dop_cal_A = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_A.setObjectName(u"dop_cal_A")
        self.dop_cal_A.setFont(font5)
        self.dop_cal_A.setDecimals(5)
        self.dop_cal_A.setMinimum(-50.000000000000000)
        self.dop_cal_A.setMaximum(50.000000000000000)
        self.dop_cal_A.setValue(1.000000000000000)

        self.horizontalLayout_51.addWidget(self.dop_cal_A)


        self.verticalLayout_49.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.lb_path_29 = QLabel(self.hhhhh_exp)
        self.lb_path_29.setObjectName(u"lb_path_29")
        sizePolicy16.setHeightForWidth(self.lb_path_29.sizePolicy().hasHeightForWidth())
        self.lb_path_29.setSizePolicy(sizePolicy16)
        self.lb_path_29.setFont(font4)

        self.horizontalLayout_52.addWidget(self.lb_path_29)

        self.lb_path_30 = QLabel(self.hhhhh_exp)
        self.lb_path_30.setObjectName(u"lb_path_30")
        sizePolicy16.setHeightForWidth(self.lb_path_30.sizePolicy().hasHeightForWidth())
        self.lb_path_30.setSizePolicy(sizePolicy16)
        self.lb_path_30.setFont(font4)

        self.horizontalLayout_52.addWidget(self.lb_path_30, 0, Qt.AlignHCenter)

        self.dop_cal_R0 = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_R0.setObjectName(u"dop_cal_R0")
        self.dop_cal_R0.setFont(font5)
        self.dop_cal_R0.setDecimals(5)
        self.dop_cal_R0.setMinimum(-50.000000000000000)
        self.dop_cal_R0.setMaximum(50.000000000000000)
        self.dop_cal_R0.setValue(0.100000000000000)

        self.horizontalLayout_52.addWidget(self.dop_cal_R0)

        self.lb_path_31 = QLabel(self.hhhhh_exp)
        self.lb_path_31.setObjectName(u"lb_path_31")
        sizePolicy16.setHeightForWidth(self.lb_path_31.sizePolicy().hasHeightForWidth())
        self.lb_path_31.setSizePolicy(sizePolicy16)
        self.lb_path_31.setFont(font4)

        self.horizontalLayout_52.addWidget(self.lb_path_31, 0, Qt.AlignHCenter)

        self.dop_cal_b = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_b.setObjectName(u"dop_cal_b")
        self.dop_cal_b.setFont(font5)
        self.dop_cal_b.setDecimals(5)
        self.dop_cal_b.setMinimum(-1000.000000000000000)
        self.dop_cal_b.setMaximum(1000.000000000000000)
        self.dop_cal_b.setValue(-1.000000000000000)

        self.horizontalLayout_52.addWidget(self.dop_cal_b)


        self.verticalLayout_49.addLayout(self.horizontalLayout_52)


        self.verticalLayout_47.addLayout(self.verticalLayout_49)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.lb_path_26 = QLabel(self.hhhhh_exp)
        self.lb_path_26.setObjectName(u"lb_path_26")
        sizePolicy16.setHeightForWidth(self.lb_path_26.sizePolicy().hasHeightForWidth())
        self.lb_path_26.setSizePolicy(sizePolicy16)
        self.lb_path_26.setFont(font4)

        self.horizontalLayout_54.addWidget(self.lb_path_26)

        self.dateEdit_3 = QDateEdit(self.hhhhh_exp)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setFont(font5)
        self.dateEdit_3.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_54.addWidget(self.dateEdit_3)


        self.verticalLayout_48.addLayout(self.horizontalLayout_54)


        self.verticalLayout_47.addLayout(self.verticalLayout_48)


        self.verticalLayout_50.addWidget(self.hhhhh_exp)


        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.verticalLayout_50)

        self.btn_LT = QPushButton(self.tab_7)
        self.btn_LT.setObjectName(u"btn_LT")
        self.btn_LT.setFont(font5)
        self.btn_LT.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.btn_LT)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.lb_path_4 = QLabel(self.tab_7)
        self.lb_path_4.setObjectName(u"lb_path_4")
        sizePolicy11.setHeightForWidth(self.lb_path_4.sizePolicy().hasHeightForWidth())
        self.lb_path_4.setSizePolicy(sizePolicy11)
        self.lb_path_4.setFont(font4)

        self.horizontalLayout_45.addWidget(self.lb_path_4)

        self.path_for_LT = QLineEdit(self.tab_7)
        self.path_for_LT.setObjectName(u"path_for_LT")
        self.path_for_LT.setFont(font5)

        self.horizontalLayout_45.addWidget(self.path_for_LT)


        self.verticalLayout_24.addLayout(self.horizontalLayout_45)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.lb_path_13 = QLabel(self.tab_7)
        self.lb_path_13.setObjectName(u"lb_path_13")
        sizePolicy11.setHeightForWidth(self.lb_path_13.sizePolicy().hasHeightForWidth())
        self.lb_path_13.setSizePolicy(sizePolicy11)
        self.lb_path_13.setFont(font4)

        self.horizontalLayout_55.addWidget(self.lb_path_13)

        self.sep_for_LT = QLineEdit(self.tab_7)
        self.sep_for_LT.setObjectName(u"sep_for_LT")
        sizePolicy13.setHeightForWidth(self.sep_for_LT.sizePolicy().hasHeightForWidth())
        self.sep_for_LT.setSizePolicy(sizePolicy13)
        self.sep_for_LT.setFont(font5)

        self.horizontalLayout_55.addWidget(self.sep_for_LT)

        self.horizontalSpacer_3 = QSpacerItem(60, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_58.addLayout(self.horizontalLayout_55)


        self.verticalLayout_38.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.lb_path_15 = QLabel(self.tab_7)
        self.lb_path_15.setObjectName(u"lb_path_15")
        sizePolicy11.setHeightForWidth(self.lb_path_15.sizePolicy().hasHeightForWidth())
        self.lb_path_15.setSizePolicy(sizePolicy11)
        self.lb_path_15.setFont(font4)

        self.horizontalLayout_57.addWidget(self.lb_path_15)

        self.position = QSpinBox(self.tab_7)
        self.position.setObjectName(u"position")
        self.position.setEnabled(True)
        self.position.setFont(font5)
        self.position.setMinimum(1)
        self.position.setMaximum(5)
        self.position.setValue(1)

        self.horizontalLayout_57.addWidget(self.position)

        self.horizontalSpacer_4 = QSpacerItem(60, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_4)


        self.verticalLayout_38.addLayout(self.horizontalLayout_57)


        self.verticalLayout_24.addLayout(self.verticalLayout_38)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.line_6 = QFrame(self.tab_7)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFont(font3)
        self.line_6.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_28.addWidget(self.line_6)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.lb_path_14 = QLabel(self.tab_7)
        self.lb_path_14.setObjectName(u"lb_path_14")
        sizePolicy11.setHeightForWidth(self.lb_path_14.sizePolicy().hasHeightForWidth())
        self.lb_path_14.setSizePolicy(sizePolicy11)
        self.lb_path_14.setFont(font4)

        self.horizontalLayout_56.addWidget(self.lb_path_14)

        self.sep_for_LT_values = QLineEdit(self.tab_7)
        self.sep_for_LT_values.setObjectName(u"sep_for_LT_values")
        sizePolicy13.setHeightForWidth(self.sep_for_LT_values.sizePolicy().hasHeightForWidth())
        self.sep_for_LT_values.setSizePolicy(sizePolicy13)
        self.sep_for_LT_values.setFont(font5)

        self.horizontalLayout_56.addWidget(self.sep_for_LT_values)

        self.horizontalSpacer_2 = QSpacerItem(60, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_56)

        self.line_5 = QFrame(self.tab_7)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFont(font3)
        self.line_5.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_28.addWidget(self.line_5)


        self.verticalLayout_24.addLayout(self.verticalLayout_28)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.verticalLayout_24)

        self.Lab_stuff.addTab(self.tab_7, "")
        self.tabWidgetPage4 = QWidget()
        self.tabWidgetPage4.setObjectName(u"tabWidgetPage4")
        self.horizontalLayout_64 = QHBoxLayout(self.tabWidgetPage4)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.tabWidget_2 = QTabWidget(self.tabWidgetPage4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setFont(font5)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lb_path_for_plot = QLabel(self.tab)
        self.lb_path_for_plot.setObjectName(u"lb_path_for_plot")
        self.lb_path_for_plot.setFont(font5)

        self.horizontalLayout_13.addWidget(self.lb_path_for_plot)

        self.path_for_plot = QLineEdit(self.tab)
        self.path_for_plot.setObjectName(u"path_for_plot")
        self.path_for_plot.setFont(font5)

        self.horizontalLayout_13.addWidget(self.path_for_plot)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_exel_name = QLabel(self.tab)
        self.lb_exel_name.setObjectName(u"lb_exel_name")
        self.lb_exel_name.setFont(font5)

        self.horizontalLayout_14.addWidget(self.lb_exel_name)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_14.addWidget(self.comboBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.check_box_figs_all_sheets = QCheckBox(self.tab)
        self.check_box_figs_all_sheets.setObjectName(u"check_box_figs_all_sheets")
        self.check_box_figs_all_sheets.setFont(font5)
        self.check_box_figs_all_sheets.setChecked(True)

        self.horizontalLayout_138.addWidget(self.check_box_figs_all_sheets)

        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.lb_exel_name_8 = QLabel(self.tab)
        self.lb_exel_name_8.setObjectName(u"lb_exel_name_8")
        self.lb_exel_name_8.setEnabled(False)
        self.lb_exel_name_8.setFont(font5)

        self.horizontalLayout_137.addWidget(self.lb_exel_name_8)

        self.comboBox_figs_sheets = QComboBox(self.tab)
        self.comboBox_figs_sheets.setObjectName(u"comboBox_figs_sheets")
        self.comboBox_figs_sheets.setEnabled(False)

        self.horizontalLayout_137.addWidget(self.comboBox_figs_sheets)


        self.horizontalLayout_138.addLayout(self.horizontalLayout_137)


        self.verticalLayout_12.addLayout(self.horizontalLayout_138)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lb_hue_name = QLabel(self.tab)
        self.lb_hue_name.setObjectName(u"lb_hue_name")
        self.lb_hue_name.setFont(font5)

        self.horizontalLayout_15.addWidget(self.lb_hue_name)

        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_15.addWidget(self.comboBox_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.nmn = QFrame(self.tab)
        self.nmn.setObjectName(u"nmn")
        sizePolicy9.setHeightForWidth(self.nmn.sizePolicy().hasHeightForWidth())
        self.nmn.setSizePolicy(sizePolicy9)
        self.nmn.setStyleSheet(u"QFrame#nmn{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.nmn)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.check_box_plot = QCheckBox(self.nmn)
        self.check_box_plot.setObjectName(u"check_box_plot")
        self.check_box_plot.setFont(font5)
        self.check_box_plot.setChecked(True)

        self.verticalLayout_13.addWidget(self.check_box_plot)

        self.check_corr_matrix = QCheckBox(self.nmn)
        self.check_corr_matrix.setObjectName(u"check_corr_matrix")
        self.check_corr_matrix.setFont(font5)

        self.verticalLayout_13.addWidget(self.check_corr_matrix)

        self.check_corr_figs = QCheckBox(self.nmn)
        self.check_corr_figs.setObjectName(u"check_corr_figs")
        self.check_corr_figs.setFont(font5)

        self.verticalLayout_13.addWidget(self.check_corr_figs)


        self.verticalLayout_14.addWidget(self.nmn)


        self.verticalLayout_17.addLayout(self.verticalLayout_14)

        self.tabWidget = QTabWidget(self.tab)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy18 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy18)
        self.tabWidget.setFont(font5)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_12 = QGridLayout(self.tab_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(10)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 0, -1, -1)
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.verticalLayout_16 = QVBoxLayout(self.frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lb_color_pal_box = QLabel(self.frame)
        self.lb_color_pal_box.setObjectName(u"lb_color_pal_box")
        sizePolicy9.setHeightForWidth(self.lb_color_pal_box.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box.setSizePolicy(sizePolicy9)
        self.lb_color_pal_box.setFont(font5)

        self.horizontalLayout_19.addWidget(self.lb_color_pal_box)

        self.comboBox_color_pal_box = QComboBox(self.frame)
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.addItem("")
        self.comboBox_color_pal_box.setObjectName(u"comboBox_color_pal_box")
        sizePolicy.setHeightForWidth(self.comboBox_color_pal_box.sizePolicy().hasHeightForWidth())
        self.comboBox_color_pal_box.setSizePolicy(sizePolicy)
        self.comboBox_color_pal_box.setFont(font5)

        self.horizontalLayout_19.addWidget(self.comboBox_color_pal_box)


        self.verticalLayout_16.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lb_color_pal_points = QLabel(self.frame)
        self.lb_color_pal_points.setObjectName(u"lb_color_pal_points")
        sizePolicy9.setHeightForWidth(self.lb_color_pal_points.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_points.setSizePolicy(sizePolicy9)
        self.lb_color_pal_points.setFont(font5)

        self.horizontalLayout_24.addWidget(self.lb_color_pal_points)

        self.comboBox_color_pal_points = QComboBox(self.frame)
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.addItem("")
        self.comboBox_color_pal_points.setObjectName(u"comboBox_color_pal_points")
        sizePolicy.setHeightForWidth(self.comboBox_color_pal_points.sizePolicy().hasHeightForWidth())
        self.comboBox_color_pal_points.setSizePolicy(sizePolicy)
        self.comboBox_color_pal_points.setFont(font5)

        self.horizontalLayout_24.addWidget(self.comboBox_color_pal_points)


        self.verticalLayout_16.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lb_color_for_box = QLabel(self.frame)
        self.lb_color_for_box.setObjectName(u"lb_color_for_box")
        sizePolicy9.setHeightForWidth(self.lb_color_for_box.sizePolicy().hasHeightForWidth())
        self.lb_color_for_box.setSizePolicy(sizePolicy9)
        self.lb_color_for_box.setFont(font5)

        self.horizontalLayout_20.addWidget(self.lb_color_for_box)

        self.color_box = QLineEdit(self.frame)
        self.color_box.setObjectName(u"color_box")
        sizePolicy.setHeightForWidth(self.color_box.sizePolicy().hasHeightForWidth())
        self.color_box.setSizePolicy(sizePolicy)
        self.color_box.setFont(font5)

        self.horizontalLayout_20.addWidget(self.color_box)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lb_color_forpoints = QLabel(self.frame)
        self.lb_color_forpoints.setObjectName(u"lb_color_forpoints")
        sizePolicy9.setHeightForWidth(self.lb_color_forpoints.sizePolicy().hasHeightForWidth())
        self.lb_color_forpoints.setSizePolicy(sizePolicy9)
        self.lb_color_forpoints.setFont(font5)

        self.horizontalLayout_25.addWidget(self.lb_color_forpoints)

        self.color_points = QLineEdit(self.frame)
        self.color_points.setObjectName(u"color_points")
        sizePolicy.setHeightForWidth(self.color_points.sizePolicy().hasHeightForWidth())
        self.color_points.setSizePolicy(sizePolicy)
        self.color_points.setFont(font5)

        self.horizontalLayout_25.addWidget(self.color_points)


        self.verticalLayout_16.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.lb_color_pal_box_19 = QLabel(self.frame)
        self.lb_color_pal_box_19.setObjectName(u"lb_color_pal_box_19")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_19.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_19.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_19.setFont(font5)

        self.horizontalLayout_122.addWidget(self.lb_color_pal_box_19)

        self.spinBox_point_size = QSpinBox(self.frame)
        self.spinBox_point_size.setObjectName(u"spinBox_point_size")
        sizePolicy.setHeightForWidth(self.spinBox_point_size.sizePolicy().hasHeightForWidth())
        self.spinBox_point_size.setSizePolicy(sizePolicy)
        self.spinBox_point_size.setFont(font5)
        self.spinBox_point_size.setMinimum(0)
        self.spinBox_point_size.setMaximum(20)
        self.spinBox_point_size.setValue(4)

        self.horizontalLayout_122.addWidget(self.spinBox_point_size)


        self.verticalLayout_16.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.lb_color_pal_box_7 = QLabel(self.frame)
        self.lb_color_pal_box_7.setObjectName(u"lb_color_pal_box_7")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_7.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_7.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_7.setFont(font5)

        self.horizontalLayout_59.addWidget(self.lb_color_pal_box_7)

        self.spinBox_mean_val_size = QSpinBox(self.frame)
        self.spinBox_mean_val_size.setObjectName(u"spinBox_mean_val_size")
        sizePolicy.setHeightForWidth(self.spinBox_mean_val_size.sizePolicy().hasHeightForWidth())
        self.spinBox_mean_val_size.setSizePolicy(sizePolicy)
        self.spinBox_mean_val_size.setFont(font5)
        self.spinBox_mean_val_size.setMinimum(2)
        self.spinBox_mean_val_size.setMaximum(20)
        self.spinBox_mean_val_size.setValue(4)

        self.horizontalLayout_59.addWidget(self.spinBox_mean_val_size)


        self.verticalLayout_16.addLayout(self.horizontalLayout_59)


        self.horizontalLayout_38.addWidget(self.frame)

        self.frame1 = QFrame(self.tab_3)
        self.frame1.setObjectName(u"frame1")
        sizePolicy9.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy9)
        self.verticalLayout_20 = QVBoxLayout(self.frame1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.lb_color_pal_box_6 = QLabel(self.frame1)
        self.lb_color_pal_box_6.setObjectName(u"lb_color_pal_box_6")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_6.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_6.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_6.setFont(font5)

        self.horizontalLayout_39.addWidget(self.lb_color_pal_box_6)

        self.comboBox_fonts = QComboBox(self.frame1)
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.setObjectName(u"comboBox_fonts")
        self.comboBox_fonts.setFont(font5)

        self.horizontalLayout_39.addWidget(self.comboBox_fonts)


        self.verticalLayout_20.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.lb_color_pal_box_2 = QLabel(self.frame1)
        self.lb_color_pal_box_2.setObjectName(u"lb_color_pal_box_2")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_2.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_2.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_2.setFont(font5)

        self.horizontalLayout_34.addWidget(self.lb_color_pal_box_2)

        self.spinBox_x_label = QSpinBox(self.frame1)
        self.spinBox_x_label.setObjectName(u"spinBox_x_label")
        sizePolicy.setHeightForWidth(self.spinBox_x_label.sizePolicy().hasHeightForWidth())
        self.spinBox_x_label.setSizePolicy(sizePolicy)
        self.spinBox_x_label.setFont(font5)
        self.spinBox_x_label.setMinimum(2)
        self.spinBox_x_label.setMaximum(100)
        self.spinBox_x_label.setValue(14)

        self.horizontalLayout_34.addWidget(self.spinBox_x_label)


        self.verticalLayout_20.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.lb_color_pal_box_3 = QLabel(self.frame1)
        self.lb_color_pal_box_3.setObjectName(u"lb_color_pal_box_3")
        self.lb_color_pal_box_3.setFont(font5)

        self.horizontalLayout_35.addWidget(self.lb_color_pal_box_3)

        self.spinBox_y_label = QSpinBox(self.frame1)
        self.spinBox_y_label.setObjectName(u"spinBox_y_label")
        sizePolicy.setHeightForWidth(self.spinBox_y_label.sizePolicy().hasHeightForWidth())
        self.spinBox_y_label.setSizePolicy(sizePolicy)
        self.spinBox_y_label.setFont(font5)
        self.spinBox_y_label.setMinimum(2)
        self.spinBox_y_label.setMaximum(100)
        self.spinBox_y_label.setValue(14)

        self.horizontalLayout_35.addWidget(self.spinBox_y_label)


        self.verticalLayout_20.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.lb_color_pal_box_5 = QLabel(self.frame1)
        self.lb_color_pal_box_5.setObjectName(u"lb_color_pal_box_5")
        self.lb_color_pal_box_5.setFont(font5)

        self.horizontalLayout_36.addWidget(self.lb_color_pal_box_5)

        self.spinBox_x_val = QSpinBox(self.frame1)
        self.spinBox_x_val.setObjectName(u"spinBox_x_val")
        sizePolicy.setHeightForWidth(self.spinBox_x_val.sizePolicy().hasHeightForWidth())
        self.spinBox_x_val.setSizePolicy(sizePolicy)
        self.spinBox_x_val.setFont(font5)
        self.spinBox_x_val.setMinimum(2)
        self.spinBox_x_val.setMaximum(100)
        self.spinBox_x_val.setValue(14)

        self.horizontalLayout_36.addWidget(self.spinBox_x_val)


        self.verticalLayout_20.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.lb_color_pal_box_4 = QLabel(self.frame1)
        self.lb_color_pal_box_4.setObjectName(u"lb_color_pal_box_4")
        self.lb_color_pal_box_4.setFont(font5)

        self.horizontalLayout_37.addWidget(self.lb_color_pal_box_4)

        self.spinBox_y_vals = QSpinBox(self.frame1)
        self.spinBox_y_vals.setObjectName(u"spinBox_y_vals")
        sizePolicy.setHeightForWidth(self.spinBox_y_vals.sizePolicy().hasHeightForWidth())
        self.spinBox_y_vals.setSizePolicy(sizePolicy)
        self.spinBox_y_vals.setFont(font5)
        self.spinBox_y_vals.setMinimum(2)
        self.spinBox_y_vals.setMaximum(100)
        self.spinBox_y_vals.setValue(14)

        self.horizontalLayout_37.addWidget(self.spinBox_y_vals)


        self.verticalLayout_20.addLayout(self.horizontalLayout_37)


        self.horizontalLayout_38.addWidget(self.frame1)


        self.gridLayout_12.addLayout(self.horizontalLayout_38, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lb_stattest = QLabel(self.tab_4)
        self.lb_stattest.setObjectName(u"lb_stattest")
        self.lb_stattest.setEnabled(True)
        self.lb_stattest.setFont(font5)

        self.horizontalLayout_23.addWidget(self.lb_stattest)

        self.comboBox_stat_test = QComboBox(self.tab_4)
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.addItem("")
        self.comboBox_stat_test.setObjectName(u"comboBox_stat_test")
        self.comboBox_stat_test.setEnabled(True)
        self.comboBox_stat_test.setFont(font5)

        self.horizontalLayout_23.addWidget(self.comboBox_stat_test)


        self.gridLayout_6.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb__altern_heposisis = QLabel(self.tab_4)
        self.lb__altern_heposisis.setObjectName(u"lb__altern_heposisis")
        self.lb__altern_heposisis.setEnabled(True)
        self.lb__altern_heposisis.setFont(font5)

        self.horizontalLayout_18.addWidget(self.lb__altern_heposisis)

        self.comboBox_alter_hep = QComboBox(self.tab_4)
        self.comboBox_alter_hep.addItem("")
        self.comboBox_alter_hep.addItem("")
        self.comboBox_alter_hep.addItem("")
        self.comboBox_alter_hep.setObjectName(u"comboBox_alter_hep")
        self.comboBox_alter_hep.setEnabled(True)
        self.comboBox_alter_hep.setFont(font5)

        self.horizontalLayout_18.addWidget(self.comboBox_alter_hep)


        self.gridLayout_6.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lb_stattest_2 = QLabel(self.tab_4)
        self.lb_stattest_2.setObjectName(u"lb_stattest_2")
        self.lb_stattest_2.setFont(font5)

        self.horizontalLayout_21.addWidget(self.lb_stattest_2)

        self.check_stat_znachimost = QCheckBox(self.tab_4)
        self.check_stat_znachimost.setObjectName(u"check_stat_znachimost")
        self.check_stat_znachimost.setEnabled(True)
        self.check_stat_znachimost.setFont(font5)
        self.check_stat_znachimost.setChecked(True)

        self.horizontalLayout_21.addWidget(self.check_stat_znachimost)


        self.gridLayout_6.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.lb_del_hue_7 = QLabel(self.tab_4)
        self.lb_del_hue_7.setObjectName(u"lb_del_hue_7")
        self.lb_del_hue_7.setFont(font5)
        self.lb_del_hue_7.setWordWrap(True)

        self.horizontalLayout_82.addWidget(self.lb_del_hue_7)

        self.STAT_znachimost_order_box_plot = QLineEdit(self.tab_4)
        self.STAT_znachimost_order_box_plot.setObjectName(u"STAT_znachimost_order_box_plot")
        self.STAT_znachimost_order_box_plot.setFont(font5)

        self.horizontalLayout_82.addWidget(self.STAT_znachimost_order_box_plot)


        self.gridLayout_6.addLayout(self.horizontalLayout_82, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_7 = QGridLayout(self.tab_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.check_sort_or_not = QCheckBox(self.tab_9)
        self.check_sort_or_not.setObjectName(u"check_sort_or_not")
        sizePolicy4.setHeightForWidth(self.check_sort_or_not.sizePolicy().hasHeightForWidth())
        self.check_sort_or_not.setSizePolicy(sizePolicy4)
        self.check_sort_or_not.setFont(font5)
        self.check_sort_or_not.setChecked(False)

        self.verticalLayout_18.addWidget(self.check_sort_or_not)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.lb_del_hue_6 = QLabel(self.tab_9)
        self.lb_del_hue_6.setObjectName(u"lb_del_hue_6")
        self.lb_del_hue_6.setFont(font5)

        self.horizontalLayout_81.addWidget(self.lb_del_hue_6)

        self.order_box_plot = QLineEdit(self.tab_9)
        self.order_box_plot.setObjectName(u"order_box_plot")
        self.order_box_plot.setFont(font5)

        self.horizontalLayout_81.addWidget(self.order_box_plot)


        self.verticalLayout_18.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.lb_stattest_3 = QLabel(self.tab_9)
        self.lb_stattest_3.setObjectName(u"lb_stattest_3")
        self.lb_stattest_3.setFont(font5)

        self.horizontalLayout_60.addWidget(self.lb_stattest_3)

        self.check_N_ = QCheckBox(self.tab_9)
        self.check_N_.setObjectName(u"check_N_")
        self.check_N_.setEnabled(True)
        sizePolicy19 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy19.setHorizontalStretch(0)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.check_N_.sizePolicy().hasHeightForWidth())
        self.check_N_.setSizePolicy(sizePolicy19)
        self.check_N_.setChecked(True)

        self.horizontalLayout_60.addWidget(self.check_N_)


        self.verticalLayout_18.addLayout(self.horizontalLayout_60)

        self.line_7 = QFrame(self.tab_9)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFont(font3)
        self.line_7.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout_18.addWidget(self.line_7)


        self.gridLayout_7.addLayout(self.verticalLayout_18, 0, 0, 1, 1)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_9 = QLabel(self.tab_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.horizontalLayout_22.addWidget(self.label_9)

        self.comboBox_spin_x_ = QComboBox(self.tab_9)
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.addItem("")
        self.comboBox_spin_x_.setObjectName(u"comboBox_spin_x_")
        sizePolicy5.setHeightForWidth(self.comboBox_spin_x_.sizePolicy().hasHeightForWidth())
        self.comboBox_spin_x_.setSizePolicy(sizePolicy5)
        self.comboBox_spin_x_.setFont(font5)

        self.horizontalLayout_22.addWidget(self.comboBox_spin_x_)


        self.horizontalLayout_83.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.lb_stattest_4 = QLabel(self.tab_9)
        self.lb_stattest_4.setObjectName(u"lb_stattest_4")
        sizePolicy4.setHeightForWidth(self.lb_stattest_4.sizePolicy().hasHeightForWidth())
        self.lb_stattest_4.setSizePolicy(sizePolicy4)
        self.lb_stattest_4.setFont(font5)

        self.horizontalLayout_66.addWidget(self.lb_stattest_4)

        self.check_background = QCheckBox(self.tab_9)
        self.check_background.setObjectName(u"check_background")
        self.check_background.setEnabled(True)
        sizePolicy19.setHeightForWidth(self.check_background.sizePolicy().hasHeightForWidth())
        self.check_background.setSizePolicy(sizePolicy19)
        self.check_background.setChecked(False)

        self.horizontalLayout_66.addWidget(self.check_background)


        self.horizontalLayout_83.addLayout(self.horizontalLayout_66)


        self.gridLayout_7.addLayout(self.horizontalLayout_83, 1, 0, 1, 1)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lb_sd_or_minmax = QLabel(self.tab_9)
        self.lb_sd_or_minmax.setObjectName(u"lb_sd_or_minmax")
        self.lb_sd_or_minmax.setFont(font5)

        self.horizontalLayout_17.addWidget(self.lb_sd_or_minmax)

        self.comboBox_sd_or_minmax = QComboBox(self.tab_9)
        self.comboBox_sd_or_minmax.addItem("")
        self.comboBox_sd_or_minmax.addItem("")
        self.comboBox_sd_or_minmax.setObjectName(u"comboBox_sd_or_minmax")
        sizePolicy5.setHeightForWidth(self.comboBox_sd_or_minmax.sizePolicy().hasHeightForWidth())
        self.comboBox_sd_or_minmax.setSizePolicy(sizePolicy5)
        self.comboBox_sd_or_minmax.setFont(font5)

        self.horizontalLayout_17.addWidget(self.comboBox_sd_or_minmax)


        self.horizontalLayout_84.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lb_bottom_lim = QLabel(self.tab_9)
        self.lb_bottom_lim.setObjectName(u"lb_bottom_lim")
        sizePolicy11.setHeightForWidth(self.lb_bottom_lim.sizePolicy().hasHeightForWidth())
        self.lb_bottom_lim.setSizePolicy(sizePolicy11)
        self.lb_bottom_lim.setFont(font5)

        self.horizontalLayout_16.addWidget(self.lb_bottom_lim)

        self.bottom_lim = QLineEdit(self.tab_9)
        self.bottom_lim.setObjectName(u"bottom_lim")
        self.bottom_lim.setFont(font5)

        self.horizontalLayout_16.addWidget(self.bottom_lim)


        self.horizontalLayout_84.addLayout(self.horizontalLayout_16)


        self.gridLayout_7.addLayout(self.horizontalLayout_84, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_9, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lb_corr_color_pallete_3 = QLabel(self.tab_2)
        self.lb_corr_color_pallete_3.setObjectName(u"lb_corr_color_pallete_3")
        self.lb_corr_color_pallete_3.setFont(font5)

        self.horizontalLayout_32.addWidget(self.lb_corr_color_pallete_3)

        self.comboBox_color_pal_corr = QComboBox(self.tab_2)
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.addItem("")
        self.comboBox_color_pal_corr.setObjectName(u"comboBox_color_pal_corr")
        self.comboBox_color_pal_corr.setFont(font5)

        self.horizontalLayout_32.addWidget(self.comboBox_color_pal_corr)


        self.verticalLayout_33.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.lb_del_hue_4 = QLabel(self.tab_2)
        self.lb_del_hue_4.setObjectName(u"lb_del_hue_4")
        self.lb_del_hue_4.setFont(font5)

        self.horizontalLayout_67.addWidget(self.lb_del_hue_4)

        self.check_change_corr_fig_down_limit = QCheckBox(self.tab_2)
        self.check_change_corr_fig_down_limit.setObjectName(u"check_change_corr_fig_down_limit")
        self.check_change_corr_fig_down_limit.setEnabled(True)
        self.check_change_corr_fig_down_limit.setFont(font5)
        self.check_change_corr_fig_down_limit.setChecked(False)

        self.horizontalLayout_67.addWidget(self.check_change_corr_fig_down_limit)

        self.doubleSpinBox_corr_figs = QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_corr_figs.setObjectName(u"doubleSpinBox_corr_figs")
        self.doubleSpinBox_corr_figs.setEnabled(False)
        self.doubleSpinBox_corr_figs.setFont(font5)
        self.doubleSpinBox_corr_figs.setMinimum(-100000.000000000000000)
        self.doubleSpinBox_corr_figs.setMaximum(1000000.000000000000000)

        self.horizontalLayout_67.addWidget(self.doubleSpinBox_corr_figs)


        self.verticalLayout_33.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.lb_del_hue_3 = QLabel(self.tab_2)
        self.lb_del_hue_3.setObjectName(u"lb_del_hue_3")
        self.lb_del_hue_3.setFont(font5)

        self.horizontalLayout_33.addWidget(self.lb_del_hue_3)

        self.del_hue = QLineEdit(self.tab_2)
        self.del_hue.setObjectName(u"del_hue")
        self.del_hue.setFont(font5)

        self.horizontalLayout_33.addWidget(self.del_hue)


        self.verticalLayout_33.addLayout(self.horizontalLayout_33)


        self.horizontalLayout_70.addLayout(self.verticalLayout_33)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.lb_del_hue_5 = QLabel(self.tab_2)
        self.lb_del_hue_5.setObjectName(u"lb_del_hue_5")
        self.lb_del_hue_5.setFont(font5)

        self.horizontalLayout_68.addWidget(self.lb_del_hue_5)

        self.spinBox_points_corrFIGS = QSpinBox(self.tab_2)
        self.spinBox_points_corrFIGS.setObjectName(u"spinBox_points_corrFIGS")
        sizePolicy.setHeightForWidth(self.spinBox_points_corrFIGS.sizePolicy().hasHeightForWidth())
        self.spinBox_points_corrFIGS.setSizePolicy(sizePolicy)
        self.spinBox_points_corrFIGS.setFont(font5)
        self.spinBox_points_corrFIGS.setMinimum(1)
        self.spinBox_points_corrFIGS.setMaximum(150)
        self.spinBox_points_corrFIGS.setValue(8)

        self.horizontalLayout_68.addWidget(self.spinBox_points_corrFIGS)


        self.verticalLayout_21.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.lb_color_pal_box_12 = QLabel(self.tab_2)
        self.lb_color_pal_box_12.setObjectName(u"lb_color_pal_box_12")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_12.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_12.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_12.setFont(font5)

        self.horizontalLayout_69.addWidget(self.lb_color_pal_box_12)

        self.doubleSpinBox_corr_figs_fontscale = QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_corr_figs_fontscale.setObjectName(u"doubleSpinBox_corr_figs_fontscale")
        self.doubleSpinBox_corr_figs_fontscale.setFont(font5)
        self.doubleSpinBox_corr_figs_fontscale.setDecimals(1)
        self.doubleSpinBox_corr_figs_fontscale.setMinimum(0.100000000000000)
        self.doubleSpinBox_corr_figs_fontscale.setMaximum(25.000000000000000)
        self.doubleSpinBox_corr_figs_fontscale.setSingleStep(0.100000000000000)
        self.doubleSpinBox_corr_figs_fontscale.setValue(1.000000000000000)

        self.horizontalLayout_69.addWidget(self.doubleSpinBox_corr_figs_fontscale)


        self.verticalLayout_21.addLayout(self.horizontalLayout_69)

        self.check_sort_or_not_corr_figs = QCheckBox(self.tab_2)
        self.check_sort_or_not_corr_figs.setObjectName(u"check_sort_or_not_corr_figs")
        self.check_sort_or_not_corr_figs.setFont(font5)
        self.check_sort_or_not_corr_figs.setChecked(False)

        self.verticalLayout_21.addWidget(self.check_sort_or_not_corr_figs)

        self.check_setka = QCheckBox(self.tab_2)
        self.check_setka.setObjectName(u"check_setka")
        self.check_setka.setFont(font5)
        self.check_setka.setChecked(False)

        self.verticalLayout_21.addWidget(self.check_setka)


        self.horizontalLayout_70.addLayout(self.verticalLayout_21)


        self.gridLayout_8.addLayout(self.horizontalLayout_70, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.formLayout_2 = QFormLayout(self.tab_6)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.frame2 = QFrame(self.tab_6)
        self.frame2.setObjectName(u"frame2")
        sizePolicy9.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy9)
        self.frame2.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_19 = QVBoxLayout(self.frame2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setSpacing(10)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.lb_sd_or_minmax_6 = QLabel(self.frame2)
        self.lb_sd_or_minmax_6.setObjectName(u"lb_sd_or_minmax_6")
        sizePolicy.setHeightForWidth(self.lb_sd_or_minmax_6.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_6.setSizePolicy(sizePolicy)
        self.lb_sd_or_minmax_6.setFont(font5)

        self.horizontalLayout_123.addWidget(self.lb_sd_or_minmax_6)

        self.comboBox_correlation_figs_matrix = QComboBox(self.frame2)
        self.comboBox_correlation_figs_matrix.addItem("")
        self.comboBox_correlation_figs_matrix.addItem("")
        self.comboBox_correlation_figs_matrix.addItem("")
        self.comboBox_correlation_figs_matrix.setObjectName(u"comboBox_correlation_figs_matrix")
        sizePolicy5.setHeightForWidth(self.comboBox_correlation_figs_matrix.sizePolicy().hasHeightForWidth())
        self.comboBox_correlation_figs_matrix.setSizePolicy(sizePolicy5)
        self.comboBox_correlation_figs_matrix.setFont(font5)

        self.horizontalLayout_123.addWidget(self.comboBox_correlation_figs_matrix)


        self.verticalLayout_19.addLayout(self.horizontalLayout_123)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setSpacing(10)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.lb_sd_or_minmax_7 = QLabel(self.frame2)
        self.lb_sd_or_minmax_7.setObjectName(u"lb_sd_or_minmax_7")
        sizePolicy.setHeightForWidth(self.lb_sd_or_minmax_7.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_7.setSizePolicy(sizePolicy)
        self.lb_sd_or_minmax_7.setFont(font5)

        self.horizontalLayout_124.addWidget(self.lb_sd_or_minmax_7)

        self.comboBox_correlation_color_map_for_figs = QComboBox(self.frame2)
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.addItem("")
        self.comboBox_correlation_color_map_for_figs.setObjectName(u"comboBox_correlation_color_map_for_figs")
        sizePolicy5.setHeightForWidth(self.comboBox_correlation_color_map_for_figs.sizePolicy().hasHeightForWidth())
        self.comboBox_correlation_color_map_for_figs.setSizePolicy(sizePolicy5)
        self.comboBox_correlation_color_map_for_figs.setFont(font5)

        self.horizontalLayout_124.addWidget(self.comboBox_correlation_color_map_for_figs)


        self.verticalLayout_19.addLayout(self.horizontalLayout_124)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lb_size_corr_matrix = QLabel(self.frame2)
        self.lb_size_corr_matrix.setObjectName(u"lb_size_corr_matrix")
        self.lb_size_corr_matrix.setFont(font5)
        self.lb_size_corr_matrix.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.lb_size_corr_matrix)

        self.corr_mat_figsize = QDoubleSpinBox(self.frame2)
        self.corr_mat_figsize.setObjectName(u"corr_mat_figsize")
        self.corr_mat_figsize.setFont(font5)
        self.corr_mat_figsize.setDecimals(0)
        self.corr_mat_figsize.setMinimum(1.000000000000000)
        self.corr_mat_figsize.setMaximum(100.000000000000000)
        self.corr_mat_figsize.setSingleStep(1.000000000000000)
        self.corr_mat_figsize.setValue(20.000000000000000)

        self.horizontalLayout_28.addWidget(self.corr_mat_figsize)


        self.verticalLayout_19.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lb_font_in = QLabel(self.frame2)
        self.lb_font_in.setObjectName(u"lb_font_in")
        self.lb_font_in.setFont(font5)
        self.lb_font_in.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.lb_font_in)

        self.font_for_in = QDoubleSpinBox(self.frame2)
        self.font_for_in.setObjectName(u"font_for_in")
        self.font_for_in.setFont(font5)
        self.font_for_in.setDecimals(1)
        self.font_for_in.setMinimum(0.100000000000000)
        self.font_for_in.setSingleStep(0.100000000000000)
        self.font_for_in.setValue(1.300000000000000)

        self.horizontalLayout_29.addWidget(self.font_for_in)


        self.verticalLayout_19.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lb_font_out = QLabel(self.frame2)
        self.lb_font_out.setObjectName(u"lb_font_out")
        self.lb_font_out.setFont(font5)
        self.lb_font_out.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.lb_font_out)

        self.font_for_out = QDoubleSpinBox(self.frame2)
        self.font_for_out.setObjectName(u"font_for_out")
        self.font_for_out.setFont(font5)
        self.font_for_out.setDecimals(0)
        self.font_for_out.setMinimum(1.000000000000000)
        self.font_for_out.setMaximum(100.000000000000000)
        self.font_for_out.setSingleStep(1.000000000000000)
        self.font_for_out.setValue(26.000000000000000)

        self.horizontalLayout_30.addWidget(self.font_for_out)


        self.verticalLayout_19.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lb_name_of_title = QLabel(self.frame2)
        self.lb_name_of_title.setObjectName(u"lb_name_of_title")
        self.lb_name_of_title.setFont(font5)
        self.lb_name_of_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.lb_name_of_title)

        self.name_of_corr_matrix = QLineEdit(self.frame2)
        self.name_of_corr_matrix.setObjectName(u"name_of_corr_matrix")
        sizePolicy.setHeightForWidth(self.name_of_corr_matrix.sizePolicy().hasHeightForWidth())
        self.name_of_corr_matrix.setSizePolicy(sizePolicy)
        self.name_of_corr_matrix.setFont(font5)

        self.horizontalLayout_31.addWidget(self.name_of_corr_matrix)


        self.verticalLayout_19.addLayout(self.horizontalLayout_31)


        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.frame2)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_17.addWidget(self.tabWidget)


        self.gridLayout_4.addLayout(self.verticalLayout_17, 0, 0, 1, 1)

        self.btn_plot_and_save_figs = QPushButton(self.tab)
        self.btn_plot_and_save_figs.setObjectName(u"btn_plot_and_save_figs")
        self.btn_plot_and_save_figs.setFont(font5)
        self.btn_plot_and_save_figs.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.gridLayout_4.addWidget(self.btn_plot_and_save_figs, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab, "")
        self.widget2 = QWidget()
        self.widget2.setObjectName(u"widget2")
        self.gridLayout_11 = QGridLayout(self.widget2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame3 = QFrame(self.widget2)
        self.frame3.setObjectName(u"frame3")
        sizePolicy11.setHeightForWidth(self.frame3.sizePolicy().hasHeightForWidth())
        self.frame3.setSizePolicy(sizePolicy11)
        self.verticalLayout_10 = QVBoxLayout(self.frame3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_path_for_profile = QLabel(self.frame3)
        self.lb_path_for_profile.setObjectName(u"lb_path_for_profile")
        sizePolicy11.setHeightForWidth(self.lb_path_for_profile.sizePolicy().hasHeightForWidth())
        self.lb_path_for_profile.setSizePolicy(sizePolicy11)
        self.lb_path_for_profile.setFont(font5)

        self.horizontalLayout_10.addWidget(self.lb_path_for_profile)

        self.path_for_profile = QLineEdit(self.frame3)
        self.path_for_profile.setObjectName(u"path_for_profile")
        self.path_for_profile.setFont(font5)

        self.horizontalLayout_10.addWidget(self.path_for_profile)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_patient_data = QLabel(self.frame3)
        self.lb_patient_data.setObjectName(u"lb_patient_data")
        sizePolicy11.setHeightForWidth(self.lb_patient_data.sizePolicy().hasHeightForWidth())
        self.lb_patient_data.setSizePolicy(sizePolicy11)
        self.lb_patient_data.setFont(font5)

        self.horizontalLayout_11.addWidget(self.lb_patient_data)

        self.patient_data = QLineEdit(self.frame3)
        self.patient_data.setObjectName(u"patient_data")
        self.patient_data.setFont(font5)

        self.horizontalLayout_11.addWidget(self.patient_data)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_norm_data = QLabel(self.frame3)
        self.lb_norm_data.setObjectName(u"lb_norm_data")
        sizePolicy11.setHeightForWidth(self.lb_norm_data.sizePolicy().hasHeightForWidth())
        self.lb_norm_data.setSizePolicy(sizePolicy11)
        self.lb_norm_data.setFont(font5)

        self.horizontalLayout_12.addWidget(self.lb_norm_data)

        self.norm_data = QLineEdit(self.frame3)
        self.norm_data.setObjectName(u"norm_data")
        self.norm_data.setFont(font5)

        self.horizontalLayout_12.addWidget(self.norm_data)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.line_19 = QFrame(self.frame3)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFont(font3)
        self.line_19.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_19.setFrameShadow(QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QFrame.HLine)

        self.verticalLayout_10.addWidget(self.line_19)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.lb_norm_data_2 = QLabel(self.frame3)
        self.lb_norm_data_2.setObjectName(u"lb_norm_data_2")
        sizePolicy11.setHeightForWidth(self.lb_norm_data_2.sizePolicy().hasHeightForWidth())
        self.lb_norm_data_2.setSizePolicy(sizePolicy11)
        self.lb_norm_data_2.setFont(font5)

        self.horizontalLayout_132.addWidget(self.lb_norm_data_2)

        self.profile_title_rad = QLineEdit(self.frame3)
        self.profile_title_rad.setObjectName(u"profile_title_rad")
        self.profile_title_rad.setFont(font5)

        self.horizontalLayout_132.addWidget(self.profile_title_rad)


        self.verticalLayout_10.addLayout(self.horizontalLayout_132)

        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.lb_norm_data_3 = QLabel(self.frame3)
        self.lb_norm_data_3.setObjectName(u"lb_norm_data_3")
        sizePolicy11.setHeightForWidth(self.lb_norm_data_3.sizePolicy().hasHeightForWidth())
        self.lb_norm_data_3.setSizePolicy(sizePolicy11)
        self.lb_norm_data_3.setFont(font5)

        self.horizontalLayout_133.addWidget(self.lb_norm_data_3)

        self.profile_title_lin = QLineEdit(self.frame3)
        self.profile_title_lin.setObjectName(u"profile_title_lin")
        self.profile_title_lin.setFont(font5)

        self.horizontalLayout_133.addWidget(self.profile_title_lin)

        self.check_profile_legend = QCheckBox(self.frame3)
        self.check_profile_legend.setObjectName(u"check_profile_legend")
        self.check_profile_legend.setEnabled(True)
        self.check_profile_legend.setFont(font5)
        self.check_profile_legend.setChecked(True)

        self.horizontalLayout_133.addWidget(self.check_profile_legend)


        self.verticalLayout_10.addLayout(self.horizontalLayout_133)

        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.lb__altern_heposisis_3 = QLabel(self.frame3)
        self.lb__altern_heposisis_3.setObjectName(u"lb__altern_heposisis_3")
        self.lb__altern_heposisis_3.setEnabled(True)
        self.lb__altern_heposisis_3.setFont(font5)

        self.horizontalLayout_134.addWidget(self.lb__altern_heposisis_3)

        self.comboBox_profile_lin_spin = QComboBox(self.frame3)
        self.comboBox_profile_lin_spin.addItem("")
        self.comboBox_profile_lin_spin.addItem("")
        self.comboBox_profile_lin_spin.setObjectName(u"comboBox_profile_lin_spin")
        self.comboBox_profile_lin_spin.setEnabled(True)
        self.comboBox_profile_lin_spin.setFont(font5)

        self.horizontalLayout_134.addWidget(self.comboBox_profile_lin_spin)

        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.lb_color_pal_box_20 = QLabel(self.frame3)
        self.lb_color_pal_box_20.setObjectName(u"lb_color_pal_box_20")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_20.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_20.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_20.setFont(font5)

        self.horizontalLayout_135.addWidget(self.lb_color_pal_box_20)

        self.doubleSpinBoX_profile = QDoubleSpinBox(self.frame3)
        self.doubleSpinBoX_profile.setObjectName(u"doubleSpinBoX_profile")
        self.doubleSpinBoX_profile.setFont(font5)
        self.doubleSpinBoX_profile.setDecimals(1)
        self.doubleSpinBoX_profile.setMinimum(0.100000000000000)
        self.doubleSpinBoX_profile.setSingleStep(0.100000000000000)
        self.doubleSpinBoX_profile.setValue(1.000000000000000)

        self.horizontalLayout_135.addWidget(self.doubleSpinBoX_profile)


        self.horizontalLayout_134.addLayout(self.horizontalLayout_135)


        self.verticalLayout_10.addLayout(self.horizontalLayout_134)


        self.gridLayout_11.addWidget(self.frame3, 0, 0, 1, 1)

        self.tyt = QFrame(self.widget2)
        self.tyt.setObjectName(u"tyt")
        sizePolicy11.setHeightForWidth(self.tyt.sizePolicy().hasHeightForWidth())
        self.tyt.setSizePolicy(sizePolicy11)
        self.tyt.setFont(font5)
        self.tyt.setStyleSheet(u"QFrame#tyt{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.tyt)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.tyt)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_4 = QLabel(self.tyt)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)

        self.verticalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.patient_prof = QLineEdit(self.tyt)
        self.patient_prof.setObjectName(u"patient_prof")
        self.patient_prof.setFont(font5)

        self.verticalLayout_7.addWidget(self.patient_prof)

        self.color_for_patient = QLineEdit(self.tyt)
        self.color_for_patient.setObjectName(u"color_for_patient")
        self.color_for_patient.setFont(font5)

        self.verticalLayout_7.addWidget(self.color_for_patient)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.check_profile_pat_line = QCheckBox(self.tyt)
        self.check_profile_pat_line.setObjectName(u"check_profile_pat_line")
        self.check_profile_pat_line.setEnabled(True)
        self.check_profile_pat_line.setFont(font5)
        self.check_profile_pat_line.setChecked(True)

        self.verticalLayout_34.addWidget(self.check_profile_pat_line)

        self.check_profile_pat_sd = QCheckBox(self.tyt)
        self.check_profile_pat_sd.setObjectName(u"check_profile_pat_sd")
        self.check_profile_pat_sd.setEnabled(True)
        self.check_profile_pat_sd.setFont(font5)
        self.check_profile_pat_sd.setChecked(True)

        self.verticalLayout_34.addWidget(self.check_profile_pat_sd)


        self.horizontalLayout_9.addLayout(self.verticalLayout_34)


        self.gridLayout_11.addWidget(self.tyt, 1, 0, 1, 1)

        self.opo = QFrame(self.widget2)
        self.opo.setObjectName(u"opo")
        sizePolicy11.setHeightForWidth(self.opo.sizePolicy().hasHeightForWidth())
        self.opo.setSizePolicy(sizePolicy11)
        self.opo.setStyleSheet(u"QFrame#opo{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.opo)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.opo)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_7 = QLabel(self.opo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.norm_prof = QLineEdit(self.opo)
        self.norm_prof.setObjectName(u"norm_prof")
        self.norm_prof.setFont(font5)

        self.verticalLayout_8.addWidget(self.norm_prof)

        self.color_for_norm = QLineEdit(self.opo)
        self.color_for_norm.setObjectName(u"color_for_norm")
        self.color_for_norm.setFont(font5)

        self.verticalLayout_8.addWidget(self.color_for_norm)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.check_profile_norm_line = QCheckBox(self.opo)
        self.check_profile_norm_line.setObjectName(u"check_profile_norm_line")
        self.check_profile_norm_line.setEnabled(True)
        self.check_profile_norm_line.setFont(font5)
        self.check_profile_norm_line.setChecked(False)

        self.verticalLayout_35.addWidget(self.check_profile_norm_line)

        self.check_profile_norm_sd = QCheckBox(self.opo)
        self.check_profile_norm_sd.setObjectName(u"check_profile_norm_sd")
        self.check_profile_norm_sd.setEnabled(True)
        self.check_profile_norm_sd.setFont(font5)
        self.check_profile_norm_sd.setChecked(True)

        self.verticalLayout_35.addWidget(self.check_profile_norm_sd)


        self.horizontalLayout_6.addLayout(self.verticalLayout_35)


        self.gridLayout_11.addWidget(self.opo, 2, 0, 1, 1)

        self.btn_plot_and_save_profile = QPushButton(self.widget2)
        self.btn_plot_and_save_profile.setObjectName(u"btn_plot_and_save_profile")
        self.btn_plot_and_save_profile.setFont(font5)
        self.btn_plot_and_save_profile.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.gridLayout_11.addWidget(self.btn_plot_and_save_profile, 3, 0, 1, 1)

        self.scrollArea = QScrollArea(self.widget2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 621, 207))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setBackground(QColor(255, 255, 255));
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(255, 255, 255));
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.verticalHeader().setMinimumSectionSize(15)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.lb_norm_data_4 = QLabel(self.scrollAreaWidgetContents)
        self.lb_norm_data_4.setObjectName(u"lb_norm_data_4")
        sizePolicy11.setHeightForWidth(self.lb_norm_data_4.sizePolicy().hasHeightForWidth())
        self.lb_norm_data_4.setSizePolicy(sizePolicy11)
        self.lb_norm_data_4.setFont(font5)

        self.gridLayout_2.addWidget(self.lb_norm_data_4, 0, 0, 1, 1, Qt.AlignHCenter)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 4, 0, 1, 1)

        self.tabWidget_2.addTab(self.widget2, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_13 = QGridLayout(self.tab_8)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.lb_path_for_plot_2 = QLabel(self.tab_8)
        self.lb_path_for_plot_2.setObjectName(u"lb_path_for_plot_2")
        self.lb_path_for_plot_2.setFont(font5)

        self.horizontalLayout_75.addWidget(self.lb_path_for_plot_2)

        self.path_for_pivot_table = QLineEdit(self.tab_8)
        self.path_for_pivot_table.setObjectName(u"path_for_pivot_table")
        self.path_for_pivot_table.setFont(font5)

        self.horizontalLayout_75.addWidget(self.path_for_pivot_table)


        self.verticalLayout_36.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.lb_exel_name_2 = QLabel(self.tab_8)
        self.lb_exel_name_2.setObjectName(u"lb_exel_name_2")
        self.lb_exel_name_2.setFont(font5)

        self.horizontalLayout_76.addWidget(self.lb_exel_name_2)

        self.comboBox_pivot_table = QComboBox(self.tab_8)
        self.comboBox_pivot_table.setObjectName(u"comboBox_pivot_table")

        self.horizontalLayout_76.addWidget(self.comboBox_pivot_table)


        self.verticalLayout_36.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.lb_exel_name_7 = QLabel(self.tab_8)
        self.lb_exel_name_7.setObjectName(u"lb_exel_name_7")
        self.lb_exel_name_7.setFont(font5)

        self.horizontalLayout_120.addWidget(self.lb_exel_name_7)

        self.comboBox_pivot_table_excel_sheet = QComboBox(self.tab_8)
        self.comboBox_pivot_table_excel_sheet.setObjectName(u"comboBox_pivot_table_excel_sheet")

        self.horizontalLayout_120.addWidget(self.comboBox_pivot_table_excel_sheet)


        self.verticalLayout_36.addLayout(self.horizontalLayout_120)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.lb_hue_name_2 = QLabel(self.tab_8)
        self.lb_hue_name_2.setObjectName(u"lb_hue_name_2")
        self.lb_hue_name_2.setFont(font5)

        self.horizontalLayout_77.addWidget(self.lb_hue_name_2)

        self.comboBox_pivot_hue = QComboBox(self.tab_8)
        self.comboBox_pivot_hue.setObjectName(u"comboBox_pivot_hue")

        self.horizontalLayout_77.addWidget(self.comboBox_pivot_hue)


        self.verticalLayout_36.addLayout(self.horizontalLayout_77)


        self.verticalLayout_37.addLayout(self.verticalLayout_36)


        self.verticalLayout_43.addLayout(self.verticalLayout_37)

        self.line_2 = QFrame(self.tab_8)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font3)
        self.line_2.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(10)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_43.addWidget(self.line_2)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_43.addItem(self.verticalSpacer_6)

        self.yyy = QFrame(self.tab_8)
        self.yyy.setObjectName(u"yyy")
        self.yyy.setStyleSheet(u"QFrame#yyy{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_40 = QVBoxLayout(self.yyy)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(8, 8, 8, 8)
        self.lb_color_pal_box_17 = QLabel(self.yyy)
        self.lb_color_pal_box_17.setObjectName(u"lb_color_pal_box_17")
        sizePolicy18.setHeightForWidth(self.lb_color_pal_box_17.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_17.setSizePolicy(sizePolicy18)
        font10 = QFont()
        font10.setPointSize(11)
        font10.setBold(False)
        font10.setUnderline(True)
        self.lb_color_pal_box_17.setFont(font10)

        self.verticalLayout_40.addWidget(self.lb_color_pal_box_17, 0, Qt.AlignHCenter)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.lb_color_pal_box_8 = QLabel(self.yyy)
        self.lb_color_pal_box_8.setObjectName(u"lb_color_pal_box_8")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_8.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_8.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_8.setFont(font5)

        self.horizontalLayout_79.addWidget(self.lb_color_pal_box_8)

        self.spinBox_pivot_table = QSpinBox(self.yyy)
        self.spinBox_pivot_table.setObjectName(u"spinBox_pivot_table")
        sizePolicy.setHeightForWidth(self.spinBox_pivot_table.sizePolicy().hasHeightForWidth())
        self.spinBox_pivot_table.setSizePolicy(sizePolicy)
        self.spinBox_pivot_table.setFont(font5)
        self.spinBox_pivot_table.setMinimum(0)
        self.spinBox_pivot_table.setMaximum(10)
        self.spinBox_pivot_table.setValue(1)

        self.horizontalLayout_79.addWidget(self.spinBox_pivot_table)


        self.horizontalLayout_80.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.lb_sd_or_minmax_2 = QLabel(self.yyy)
        self.lb_sd_or_minmax_2.setObjectName(u"lb_sd_or_minmax_2")
        self.lb_sd_or_minmax_2.setFont(font5)

        self.horizontalLayout_78.addWidget(self.lb_sd_or_minmax_2)

        self.comboBox_sd_or_se_pivot = QComboBox(self.yyy)
        self.comboBox_sd_or_se_pivot.addItem("")
        self.comboBox_sd_or_se_pivot.addItem("")
        self.comboBox_sd_or_se_pivot.setObjectName(u"comboBox_sd_or_se_pivot")
        sizePolicy5.setHeightForWidth(self.comboBox_sd_or_se_pivot.sizePolicy().hasHeightForWidth())
        self.comboBox_sd_or_se_pivot.setSizePolicy(sizePolicy5)
        self.comboBox_sd_or_se_pivot.setFont(font5)

        self.horizontalLayout_78.addWidget(self.comboBox_sd_or_se_pivot)


        self.horizontalLayout_80.addLayout(self.horizontalLayout_78)


        self.verticalLayout_40.addLayout(self.horizontalLayout_80)

        self.btn_plot_and_save_pivot_table = QPushButton(self.yyy)
        self.btn_plot_and_save_pivot_table.setObjectName(u"btn_plot_and_save_pivot_table")
        self.btn_plot_and_save_pivot_table.setFont(font5)
        self.btn_plot_and_save_pivot_table.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.verticalLayout_40.addWidget(self.btn_plot_and_save_pivot_table)


        self.verticalLayout_43.addWidget(self.yyy)

        self.verticalSpacer_5 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_43.addItem(self.verticalSpacer_5)

        self.ppp = QFrame(self.tab_8)
        self.ppp.setObjectName(u"ppp")
        self.ppp.setStyleSheet(u"QFrame#ppp{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_42 = QVBoxLayout(self.ppp)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(8, 8, 8, 8)
        self.lb_color_pal_box_18 = QLabel(self.ppp)
        self.lb_color_pal_box_18.setObjectName(u"lb_color_pal_box_18")
        sizePolicy18.setHeightForWidth(self.lb_color_pal_box_18.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_18.setSizePolicy(sizePolicy18)
        self.lb_color_pal_box_18.setFont(font10)

        self.verticalLayout_42.addWidget(self.lb_color_pal_box_18, 0, Qt.AlignHCenter)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setSpacing(10)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.lb_sd_or_minmax_3 = QLabel(self.ppp)
        self.lb_sd_or_minmax_3.setObjectName(u"lb_sd_or_minmax_3")
        sizePolicy.setHeightForWidth(self.lb_sd_or_minmax_3.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_3.setSizePolicy(sizePolicy)
        self.lb_sd_or_minmax_3.setFont(font5)

        self.horizontalLayout_85.addWidget(self.lb_sd_or_minmax_3)

        self.comboBox_correlation_person_or_not = QComboBox(self.ppp)
        self.comboBox_correlation_person_or_not.addItem("")
        self.comboBox_correlation_person_or_not.addItem("")
        self.comboBox_correlation_person_or_not.addItem("")
        self.comboBox_correlation_person_or_not.setObjectName(u"comboBox_correlation_person_or_not")
        sizePolicy5.setHeightForWidth(self.comboBox_correlation_person_or_not.sizePolicy().hasHeightForWidth())
        self.comboBox_correlation_person_or_not.setSizePolicy(sizePolicy5)
        self.comboBox_correlation_person_or_not.setFont(font5)

        self.horizontalLayout_85.addWidget(self.comboBox_correlation_person_or_not)


        self.verticalLayout_41.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lb_sd_or_minmax_4 = QLabel(self.ppp)
        self.lb_sd_or_minmax_4.setObjectName(u"lb_sd_or_minmax_4")
        sizePolicy.setHeightForWidth(self.lb_sd_or_minmax_4.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_4.setSizePolicy(sizePolicy)
        self.lb_sd_or_minmax_4.setFont(font5)

        self.horizontalLayout_26.addWidget(self.lb_sd_or_minmax_4)

        self.check_color_for_corr_pivot = QCheckBox(self.ppp)
        self.check_color_for_corr_pivot.setObjectName(u"check_color_for_corr_pivot")
        self.check_color_for_corr_pivot.setEnabled(True)
        self.check_color_for_corr_pivot.setFont(font5)
        self.check_color_for_corr_pivot.setChecked(True)

        self.horizontalLayout_26.addWidget(self.check_color_for_corr_pivot)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(10)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.lb_sd_or_minmax_5 = QLabel(self.ppp)
        self.lb_sd_or_minmax_5.setObjectName(u"lb_sd_or_minmax_5")
        sizePolicy.setHeightForWidth(self.lb_sd_or_minmax_5.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_5.setSizePolicy(sizePolicy)
        self.lb_sd_or_minmax_5.setFont(font5)

        self.horizontalLayout_86.addWidget(self.lb_sd_or_minmax_5)

        self.comboBox_correlation_color_map = QComboBox(self.ppp)
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.addItem("")
        self.comboBox_correlation_color_map.setObjectName(u"comboBox_correlation_color_map")
        sizePolicy5.setHeightForWidth(self.comboBox_correlation_color_map.sizePolicy().hasHeightForWidth())
        self.comboBox_correlation_color_map.setSizePolicy(sizePolicy5)
        self.comboBox_correlation_color_map.setFont(font5)

        self.horizontalLayout_86.addWidget(self.comboBox_correlation_color_map)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_86)


        self.verticalLayout_41.addLayout(self.horizontalLayout_121)


        self.verticalLayout_42.addLayout(self.verticalLayout_41)

        self.btn_plot_and_save_corr_table = QPushButton(self.ppp)
        self.btn_plot_and_save_corr_table.setObjectName(u"btn_plot_and_save_corr_table")
        self.btn_plot_and_save_corr_table.setFont(font5)
        self.btn_plot_and_save_corr_table.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.verticalLayout_42.addWidget(self.btn_plot_and_save_corr_table)


        self.verticalLayout_43.addWidget(self.ppp)

        self.verticalSpacer_7 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_43.addItem(self.verticalSpacer_7)

        self.ppp_2 = QFrame(self.tab_8)
        self.ppp_2.setObjectName(u"ppp_2")
        self.ppp_2.setStyleSheet(u"QFrame#ppp_2{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_53 = QVBoxLayout(self.ppp_2)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(8, 8, 8, 8)
        self.lb_color_pal_box_22 = QLabel(self.ppp_2)
        self.lb_color_pal_box_22.setObjectName(u"lb_color_pal_box_22")
        sizePolicy18.setHeightForWidth(self.lb_color_pal_box_22.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_22.setSizePolicy(sizePolicy18)
        self.lb_color_pal_box_22.setFont(font10)

        self.verticalLayout_53.addWidget(self.lb_color_pal_box_22, 0, Qt.AlignHCenter)

        self.horizontalLayout_143 = QHBoxLayout()
        self.horizontalLayout_143.setSpacing(10)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.lb_sd_or_minmax_11 = QLabel(self.ppp_2)
        self.lb_sd_or_minmax_11.setObjectName(u"lb_sd_or_minmax_11")
        sizePolicy.setHeightForWidth(self.lb_sd_or_minmax_11.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_11.setSizePolicy(sizePolicy)
        self.lb_sd_or_minmax_11.setFont(font5)

        self.horizontalLayout_143.addWidget(self.lb_sd_or_minmax_11)

        self.comboBox_index_data_or_raw = QComboBox(self.ppp_2)
        self.comboBox_index_data_or_raw.addItem("")
        self.comboBox_index_data_or_raw.addItem("")
        self.comboBox_index_data_or_raw.setObjectName(u"comboBox_index_data_or_raw")
        sizePolicy5.setHeightForWidth(self.comboBox_index_data_or_raw.sizePolicy().hasHeightForWidth())
        self.comboBox_index_data_or_raw.setSizePolicy(sizePolicy5)
        self.comboBox_index_data_or_raw.setFont(font5)

        self.horizontalLayout_143.addWidget(self.comboBox_index_data_or_raw)


        self.verticalLayout_53.addLayout(self.horizontalLayout_143)

        self.btn_save_pivot_or_melt = QPushButton(self.ppp_2)
        self.btn_save_pivot_or_melt.setObjectName(u"btn_save_pivot_or_melt")
        self.btn_save_pivot_or_melt.setFont(font5)
        self.btn_save_pivot_or_melt.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.verticalLayout_53.addWidget(self.btn_save_pivot_or_melt)


        self.verticalLayout_43.addWidget(self.ppp_2)


        self.gridLayout_13.addLayout(self.verticalLayout_43, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.formLayout_5 = QFormLayout(self.tab_10)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_5.setItem(8, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.lb_path_for_plot_3 = QLabel(self.tab_10)
        self.lb_path_for_plot_3.setObjectName(u"lb_path_for_plot_3")
        self.lb_path_for_plot_3.setFont(font5)

        self.horizontalLayout_87.addWidget(self.lb_path_for_plot_3)

        self.path_for_catplot = QLineEdit(self.tab_10)
        self.path_for_catplot.setObjectName(u"path_for_catplot")
        self.path_for_catplot.setFont(font5)

        self.horizontalLayout_87.addWidget(self.path_for_catplot)


        self.formLayout_5.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_87)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.lb_exel_name_3 = QLabel(self.tab_10)
        self.lb_exel_name_3.setObjectName(u"lb_exel_name_3")
        self.lb_exel_name_3.setFont(font5)

        self.horizontalLayout_88.addWidget(self.lb_exel_name_3)

        self.comboBox_excel_catplot = QComboBox(self.tab_10)
        self.comboBox_excel_catplot.setObjectName(u"comboBox_excel_catplot")

        self.horizontalLayout_88.addWidget(self.comboBox_excel_catplot)


        self.formLayout_5.setLayout(1, QFormLayout.SpanningRole, self.horizontalLayout_88)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.lb_exel_name_4 = QLabel(self.tab_10)
        self.lb_exel_name_4.setObjectName(u"lb_exel_name_4")
        self.lb_exel_name_4.setFont(font5)

        self.horizontalLayout_99.addWidget(self.lb_exel_name_4)

        self.comboBox_excel_sheet_catplot = QComboBox(self.tab_10)
        self.comboBox_excel_sheet_catplot.setObjectName(u"comboBox_excel_sheet_catplot")

        self.horizontalLayout_99.addWidget(self.comboBox_excel_sheet_catplot)


        self.formLayout_5.setLayout(2, QFormLayout.SpanningRole, self.horizontalLayout_99)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.line_9 = QFrame(self.tab_10)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFont(font3)
        self.line_9.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QFrame.HLine)

        self.verticalLayout_15.addWidget(self.line_9)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.lb_hue_name_3 = QLabel(self.tab_10)
        self.lb_hue_name_3.setObjectName(u"lb_hue_name_3")
        self.lb_hue_name_3.setFont(font5)

        self.horizontalLayout_89.addWidget(self.lb_hue_name_3)

        self.comboBox_catplot_x = QComboBox(self.tab_10)
        self.comboBox_catplot_x.setObjectName(u"comboBox_catplot_x")

        self.horizontalLayout_89.addWidget(self.comboBox_catplot_x)


        self.horizontalLayout_100.addLayout(self.horizontalLayout_89)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.lb_hue_name_7 = QLabel(self.tab_10)
        self.lb_hue_name_7.setObjectName(u"lb_hue_name_7")
        self.lb_hue_name_7.setFont(font5)

        self.horizontalLayout_96.addWidget(self.lb_hue_name_7)

        self.comboBox_catplot_form_x = QComboBox(self.tab_10)
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.setObjectName(u"comboBox_catplot_form_x")

        self.horizontalLayout_96.addWidget(self.comboBox_catplot_form_x)


        self.horizontalLayout_100.addLayout(self.horizontalLayout_96)


        self.verticalLayout_15.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.lb_hue_name_4 = QLabel(self.tab_10)
        self.lb_hue_name_4.setObjectName(u"lb_hue_name_4")
        self.lb_hue_name_4.setFont(font5)

        self.horizontalLayout_90.addWidget(self.lb_hue_name_4)

        self.comboBox_catplot_y = QComboBox(self.tab_10)
        self.comboBox_catplot_y.setObjectName(u"comboBox_catplot_y")

        self.horizontalLayout_90.addWidget(self.comboBox_catplot_y)


        self.horizontalLayout_101.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.lb_hue_name_6 = QLabel(self.tab_10)
        self.lb_hue_name_6.setObjectName(u"lb_hue_name_6")
        self.lb_hue_name_6.setFont(font5)

        self.horizontalLayout_95.addWidget(self.lb_hue_name_6)

        self.comboBox_catplot_form_y = QComboBox(self.tab_10)
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.setObjectName(u"comboBox_catplot_form_y")

        self.horizontalLayout_95.addWidget(self.comboBox_catplot_form_y)


        self.horizontalLayout_101.addLayout(self.horizontalLayout_95)


        self.verticalLayout_15.addLayout(self.horizontalLayout_101)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.lb_hue_name_5 = QLabel(self.tab_10)
        self.lb_hue_name_5.setObjectName(u"lb_hue_name_5")
        self.lb_hue_name_5.setFont(font5)

        self.horizontalLayout_91.addWidget(self.lb_hue_name_5)

        self.comboBox_catplot_hue = QComboBox(self.tab_10)
        self.comboBox_catplot_hue.setObjectName(u"comboBox_catplot_hue")

        self.horizontalLayout_91.addWidget(self.comboBox_catplot_hue)


        self.horizontalLayout_102.addLayout(self.horizontalLayout_91)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.lb_hue_name_8 = QLabel(self.tab_10)
        self.lb_hue_name_8.setObjectName(u"lb_hue_name_8")
        self.lb_hue_name_8.setFont(font5)

        self.horizontalLayout_97.addWidget(self.lb_hue_name_8)

        self.comboBox_catplot_form_hue = QComboBox(self.tab_10)
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.setObjectName(u"comboBox_catplot_form_hue")

        self.horizontalLayout_97.addWidget(self.comboBox_catplot_form_hue)


        self.horizontalLayout_102.addLayout(self.horizontalLayout_97)


        self.verticalLayout_15.addLayout(self.horizontalLayout_102)

        self.line_8 = QFrame(self.tab_10)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFont(font3)
        self.line_8.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QFrame.HLine)

        self.verticalLayout_15.addWidget(self.line_8)


        self.formLayout_5.setLayout(3, QFormLayout.SpanningRole, self.verticalLayout_15)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.lb_color_pal_box_14 = QLabel(self.tab_10)
        self.lb_color_pal_box_14.setObjectName(u"lb_color_pal_box_14")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_14.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_14.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_14.setFont(font5)

        self.horizontalLayout_93.addWidget(self.lb_color_pal_box_14)

        self.doubleSpinBox_catplot = QDoubleSpinBox(self.tab_10)
        self.doubleSpinBox_catplot.setObjectName(u"doubleSpinBox_catplot")
        self.doubleSpinBox_catplot.setFont(font5)
        self.doubleSpinBox_catplot.setDecimals(1)
        self.doubleSpinBox_catplot.setMinimum(0.100000000000000)
        self.doubleSpinBox_catplot.setSingleStep(0.100000000000000)
        self.doubleSpinBox_catplot.setValue(1.000000000000000)

        self.horizontalLayout_93.addWidget(self.doubleSpinBox_catplot)


        self.horizontalLayout_106.addLayout(self.horizontalLayout_93)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.lb_color_pal_box_16 = QLabel(self.tab_10)
        self.lb_color_pal_box_16.setObjectName(u"lb_color_pal_box_16")
        sizePolicy9.setHeightForWidth(self.lb_color_pal_box_16.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_16.setSizePolicy(sizePolicy9)
        self.lb_color_pal_box_16.setFont(font5)

        self.horizontalLayout_105.addWidget(self.lb_color_pal_box_16)

        self.comboBox_color_catplot = QComboBox(self.tab_10)
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.addItem("")
        self.comboBox_color_catplot.setObjectName(u"comboBox_color_catplot")
        sizePolicy.setHeightForWidth(self.comboBox_color_catplot.sizePolicy().hasHeightForWidth())
        self.comboBox_color_catplot.setSizePolicy(sizePolicy)
        self.comboBox_color_catplot.setFont(font5)

        self.horizontalLayout_105.addWidget(self.comboBox_color_catplot)


        self.horizontalLayout_106.addLayout(self.horizontalLayout_105)


        self.formLayout_5.setLayout(4, QFormLayout.SpanningRole, self.horizontalLayout_106)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.line_11 = QFrame(self.tab_10)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFont(font3)
        self.line_11.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QFrame.HLine)

        self.verticalLayout_39.addWidget(self.line_11)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.lb_stattest_6 = QLabel(self.tab_10)
        self.lb_stattest_6.setObjectName(u"lb_stattest_6")
        self.lb_stattest_6.setFont(font5)

        self.horizontalLayout_94.addWidget(self.lb_stattest_6)

        self.check_stat_znachimost_catplot = QCheckBox(self.tab_10)
        self.check_stat_znachimost_catplot.setObjectName(u"check_stat_znachimost_catplot")
        self.check_stat_znachimost_catplot.setEnabled(True)
        self.check_stat_znachimost_catplot.setFont(font5)
        self.check_stat_znachimost_catplot.setChecked(True)

        self.horizontalLayout_94.addWidget(self.check_stat_znachimost_catplot)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.lb_stattest_5 = QLabel(self.tab_10)
        self.lb_stattest_5.setObjectName(u"lb_stattest_5")
        self.lb_stattest_5.setEnabled(True)
        self.lb_stattest_5.setFont(font5)

        self.horizontalLayout_92.addWidget(self.lb_stattest_5)

        self.comboBox_stat_test_catplot = QComboBox(self.tab_10)
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.addItem("")
        self.comboBox_stat_test_catplot.setObjectName(u"comboBox_stat_test_catplot")
        self.comboBox_stat_test_catplot.setEnabled(True)
        self.comboBox_stat_test_catplot.setFont(font5)

        self.horizontalLayout_92.addWidget(self.comboBox_stat_test_catplot)


        self.horizontalLayout_94.addLayout(self.horizontalLayout_92)


        self.verticalLayout_39.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.lb_stattest_9 = QLabel(self.tab_10)
        self.lb_stattest_9.setObjectName(u"lb_stattest_9")
        self.lb_stattest_9.setEnabled(True)
        self.lb_stattest_9.setFont(font5)

        self.horizontalLayout_108.addWidget(self.lb_stattest_9)

        self.comboBox_catplot_stat_formatt = QComboBox(self.tab_10)
        self.comboBox_catplot_stat_formatt.addItem("")
        self.comboBox_catplot_stat_formatt.addItem("")
        self.comboBox_catplot_stat_formatt.addItem("")
        self.comboBox_catplot_stat_formatt.setObjectName(u"comboBox_catplot_stat_formatt")
        self.comboBox_catplot_stat_formatt.setEnabled(True)
        self.comboBox_catplot_stat_formatt.setFont(font5)

        self.horizontalLayout_108.addWidget(self.comboBox_catplot_stat_formatt)


        self.verticalLayout_39.addLayout(self.horizontalLayout_108)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.lb_stattest_10 = QLabel(self.tab_10)
        self.lb_stattest_10.setObjectName(u"lb_stattest_10")
        self.lb_stattest_10.setEnabled(True)
        self.lb_stattest_10.setFont(font5)

        self.horizontalLayout_109.addWidget(self.lb_stattest_10)

        self.comboBox_catplot_mult_stat = QComboBox(self.tab_10)
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.setObjectName(u"comboBox_catplot_mult_stat")
        self.comboBox_catplot_mult_stat.setEnabled(True)
        self.comboBox_catplot_mult_stat.setFont(font5)

        self.horizontalLayout_109.addWidget(self.comboBox_catplot_mult_stat)


        self.verticalLayout_39.addLayout(self.horizontalLayout_109)

        self.line_10 = QFrame(self.tab_10)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFont(font3)
        self.line_10.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QFrame.HLine)

        self.verticalLayout_39.addWidget(self.line_10)


        self.formLayout_5.setLayout(5, QFormLayout.SpanningRole, self.verticalLayout_39)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.lb_stattest_7 = QLabel(self.tab_10)
        self.lb_stattest_7.setObjectName(u"lb_stattest_7")
        self.lb_stattest_7.setEnabled(True)
        self.lb_stattest_7.setFont(font5)

        self.horizontalLayout_98.addWidget(self.lb_stattest_7)

        self.comboBox_template_catplot = QComboBox(self.tab_10)
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.setObjectName(u"comboBox_template_catplot")
        self.comboBox_template_catplot.setEnabled(True)
        self.comboBox_template_catplot.setFont(font5)

        self.horizontalLayout_98.addWidget(self.comboBox_template_catplot)


        self.horizontalLayout_104.addLayout(self.horizontalLayout_98)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.lb_color_pal_box_15 = QLabel(self.tab_10)
        self.lb_color_pal_box_15.setObjectName(u"lb_color_pal_box_15")
        sizePolicy1.setHeightForWidth(self.lb_color_pal_box_15.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_15.setSizePolicy(sizePolicy1)
        self.lb_color_pal_box_15.setFont(font5)

        self.horizontalLayout_103.addWidget(self.lb_color_pal_box_15)

        self.comboBox_catplot_SD_or_not = QComboBox(self.tab_10)
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.setObjectName(u"comboBox_catplot_SD_or_not")
        sizePolicy14.setHeightForWidth(self.comboBox_catplot_SD_or_not.sizePolicy().hasHeightForWidth())
        self.comboBox_catplot_SD_or_not.setSizePolicy(sizePolicy14)
        self.comboBox_catplot_SD_or_not.setFont(font5)

        self.horizontalLayout_103.addWidget(self.comboBox_catplot_SD_or_not)


        self.horizontalLayout_104.addLayout(self.horizontalLayout_103)


        self.formLayout_5.setLayout(6, QFormLayout.SpanningRole, self.horizontalLayout_104)

        self.btn_plot_and_save_catplot = QPushButton(self.tab_10)
        self.btn_plot_and_save_catplot.setObjectName(u"btn_plot_and_save_catplot")
        self.btn_plot_and_save_catplot.setFont(font5)
        self.btn_plot_and_save_catplot.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.formLayout_5.setWidget(7, QFormLayout.SpanningRole, self.btn_plot_and_save_catplot)

        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_9 = QGridLayout(self.tab_12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.lb_path_for_plot_7 = QLabel(self.tab_12)
        self.lb_path_for_plot_7.setObjectName(u"lb_path_for_plot_7")
        self.lb_path_for_plot_7.setFont(font10)

        self.verticalLayout_44.addWidget(self.lb_path_for_plot_7, 0, Qt.AlignHCenter)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.lb_path_for_plot_5 = QLabel(self.tab_12)
        self.lb_path_for_plot_5.setObjectName(u"lb_path_for_plot_5")
        self.lb_path_for_plot_5.setFont(font5)

        self.horizontalLayout_128.addWidget(self.lb_path_for_plot_5)

        self.path_for_RheoScan_describe = QLineEdit(self.tab_12)
        self.path_for_RheoScan_describe.setObjectName(u"path_for_RheoScan_describe")
        self.path_for_RheoScan_describe.setFont(font5)

        self.horizontalLayout_128.addWidget(self.path_for_RheoScan_describe)


        self.verticalLayout_44.addLayout(self.horizontalLayout_128)

        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.lb_stattest_12 = QLabel(self.tab_12)
        self.lb_stattest_12.setObjectName(u"lb_stattest_12")
        self.lb_stattest_12.setEnabled(True)
        self.lb_stattest_12.setFont(font5)

        self.horizontalLayout_129.addWidget(self.lb_stattest_12)

        self.comboBox_RheoScan_describe = QComboBox(self.tab_12)
        self.comboBox_RheoScan_describe.addItem("")
        self.comboBox_RheoScan_describe.addItem("")
        self.comboBox_RheoScan_describe.setObjectName(u"comboBox_RheoScan_describe")
        self.comboBox_RheoScan_describe.setEnabled(True)
        self.comboBox_RheoScan_describe.setFont(font5)

        self.horizontalLayout_129.addWidget(self.comboBox_RheoScan_describe)


        self.verticalLayout_44.addLayout(self.horizontalLayout_129)

        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.lb_path_for_plot_6 = QLabel(self.tab_12)
        self.lb_path_for_plot_6.setObjectName(u"lb_path_for_plot_6")
        self.lb_path_for_plot_6.setFont(font5)

        self.horizontalLayout_130.addWidget(self.lb_path_for_plot_6)

        self.RheoScan_describe_mask_sheets = QLineEdit(self.tab_12)
        self.RheoScan_describe_mask_sheets.setObjectName(u"RheoScan_describe_mask_sheets")
        self.RheoScan_describe_mask_sheets.setFont(font5)

        self.horizontalLayout_130.addWidget(self.RheoScan_describe_mask_sheets)


        self.verticalLayout_44.addLayout(self.horizontalLayout_130)

        self.btn_RheoScan_describe_file_or_files = QPushButton(self.tab_12)
        self.btn_RheoScan_describe_file_or_files.setObjectName(u"btn_RheoScan_describe_file_or_files")
        self.btn_RheoScan_describe_file_or_files.setFont(font5)
        self.btn_RheoScan_describe_file_or_files.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.verticalLayout_44.addWidget(self.btn_RheoScan_describe_file_or_files)


        self.gridLayout_9.addLayout(self.verticalLayout_44, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.lb_path_for_plot_8 = QLabel(self.tab_12)
        self.lb_path_for_plot_8.setObjectName(u"lb_path_for_plot_8")
        self.lb_path_for_plot_8.setFont(font10)

        self.verticalLayout_45.addWidget(self.lb_path_for_plot_8, 0, Qt.AlignHCenter)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.lb_path_for_plot_4 = QLabel(self.tab_12)
        self.lb_path_for_plot_4.setObjectName(u"lb_path_for_plot_4")
        self.lb_path_for_plot_4.setFont(font5)

        self.horizontalLayout_107.addWidget(self.lb_path_for_plot_4)

        self.path_for_dop_stat = QLineEdit(self.tab_12)
        self.path_for_dop_stat.setObjectName(u"path_for_dop_stat")
        self.path_for_dop_stat.setFont(font5)

        self.horizontalLayout_107.addWidget(self.path_for_dop_stat)


        self.verticalLayout_45.addLayout(self.horizontalLayout_107)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.lb_exel_name_5 = QLabel(self.tab_12)
        self.lb_exel_name_5.setObjectName(u"lb_exel_name_5")
        self.lb_exel_name_5.setFont(font5)

        self.horizontalLayout_110.addWidget(self.lb_exel_name_5)

        self.comboBox_excel_dop_stat = QComboBox(self.tab_12)
        self.comboBox_excel_dop_stat.setObjectName(u"comboBox_excel_dop_stat")

        self.horizontalLayout_110.addWidget(self.comboBox_excel_dop_stat)


        self.verticalLayout_45.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.lb_exel_name_6 = QLabel(self.tab_12)
        self.lb_exel_name_6.setObjectName(u"lb_exel_name_6")
        self.lb_exel_name_6.setFont(font5)

        self.horizontalLayout_112.addWidget(self.lb_exel_name_6)

        self.comboBox_excel_sheet_dop_stat = QComboBox(self.tab_12)
        self.comboBox_excel_sheet_dop_stat.setObjectName(u"comboBox_excel_sheet_dop_stat")

        self.horizontalLayout_112.addWidget(self.comboBox_excel_sheet_dop_stat)


        self.verticalLayout_45.addLayout(self.horizontalLayout_112)

        self.line_12 = QFrame(self.tab_12)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFont(font3)
        self.line_12.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QFrame.HLine)

        self.verticalLayout_45.addWidget(self.line_12)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.lb_hue_name_9 = QLabel(self.tab_12)
        self.lb_hue_name_9.setObjectName(u"lb_hue_name_9")
        self.lb_hue_name_9.setFont(font5)

        self.horizontalLayout_111.addWidget(self.lb_hue_name_9)

        self.comboBox_dop_stat_x = QComboBox(self.tab_12)
        self.comboBox_dop_stat_x.setObjectName(u"comboBox_dop_stat_x")

        self.horizontalLayout_111.addWidget(self.comboBox_dop_stat_x)


        self.verticalLayout_45.addLayout(self.horizontalLayout_111)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.lb_hue_name_10 = QLabel(self.tab_12)
        self.lb_hue_name_10.setObjectName(u"lb_hue_name_10")
        self.lb_hue_name_10.setFont(font5)

        self.horizontalLayout_114.addWidget(self.lb_hue_name_10)

        self.comboBox_dop_stat_y = QComboBox(self.tab_12)
        self.comboBox_dop_stat_y.setObjectName(u"comboBox_dop_stat_y")

        self.horizontalLayout_114.addWidget(self.comboBox_dop_stat_y)


        self.verticalLayout_45.addLayout(self.horizontalLayout_114)

        self.line_13 = QFrame(self.tab_12)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFont(font3)
        self.line_13.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QFrame.HLine)

        self.verticalLayout_45.addWidget(self.line_13)

        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.lb_stattest_8 = QLabel(self.tab_12)
        self.lb_stattest_8.setObjectName(u"lb_stattest_8")
        self.lb_stattest_8.setEnabled(True)
        self.lb_stattest_8.setFont(font5)

        self.horizontalLayout_113.addWidget(self.lb_stattest_8)

        self.comboBox_stat_test_dop_stat = QComboBox(self.tab_12)
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.addItem("")
        self.comboBox_stat_test_dop_stat.setObjectName(u"comboBox_stat_test_dop_stat")
        self.comboBox_stat_test_dop_stat.setEnabled(True)
        self.comboBox_stat_test_dop_stat.setFont(font5)

        self.horizontalLayout_113.addWidget(self.comboBox_stat_test_dop_stat)


        self.horizontalLayout_127.addLayout(self.horizontalLayout_113)


        self.verticalLayout_45.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.lb__altern_heposisis_2 = QLabel(self.tab_12)
        self.lb__altern_heposisis_2.setObjectName(u"lb__altern_heposisis_2")
        self.lb__altern_heposisis_2.setEnabled(True)
        self.lb__altern_heposisis_2.setFont(font5)

        self.horizontalLayout_126.addWidget(self.lb__altern_heposisis_2)

        self.comboBox_alter_hep_dop_stat = QComboBox(self.tab_12)
        self.comboBox_alter_hep_dop_stat.addItem("")
        self.comboBox_alter_hep_dop_stat.addItem("")
        self.comboBox_alter_hep_dop_stat.addItem("")
        self.comboBox_alter_hep_dop_stat.setObjectName(u"comboBox_alter_hep_dop_stat")
        self.comboBox_alter_hep_dop_stat.setEnabled(True)
        self.comboBox_alter_hep_dop_stat.setFont(font5)

        self.horizontalLayout_126.addWidget(self.comboBox_alter_hep_dop_stat)


        self.verticalLayout_45.addLayout(self.horizontalLayout_126)

        self.line_20 = QFrame(self.tab_12)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFont(font3)
        self.line_20.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_20.setFrameShadow(QFrame.Plain)
        self.line_20.setLineWidth(3)
        self.line_20.setFrameShape(QFrame.HLine)

        self.verticalLayout_45.addWidget(self.line_20)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.lb_hue_name_11 = QLabel(self.tab_12)
        self.lb_hue_name_11.setObjectName(u"lb_hue_name_11")
        self.lb_hue_name_11.setFont(font5)

        self.horizontalLayout_125.addWidget(self.lb_hue_name_11)

        self.p_value_dop_stat = QLineEdit(self.tab_12)
        self.p_value_dop_stat.setObjectName(u"p_value_dop_stat")
        self.p_value_dop_stat.setFont(font5)

        self.horizontalLayout_125.addWidget(self.p_value_dop_stat)


        self.verticalLayout_45.addLayout(self.horizontalLayout_125)

        self.btn_dop_stat_calc = QPushButton(self.tab_12)
        self.btn_dop_stat_calc.setObjectName(u"btn_dop_stat_calc")
        self.btn_dop_stat_calc.setFont(font5)
        self.btn_dop_stat_calc.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.verticalLayout_45.addWidget(self.btn_dop_stat_calc)


        self.gridLayout_9.addLayout(self.verticalLayout_45, 2, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_12, "")

        self.horizontalLayout_64.addWidget(self.tabWidget_2)

        self.Lab_stuff.addTab(self.tabWidgetPage4, "")

        self.gridLayout.addWidget(self.Lab_stuff, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.comboBox_style_sheet, self.Lab_stuff)
        QWidget.setTabOrder(self.Lab_stuff, self.btn_save_exel_csv)
        QWidget.setTabOrder(self.btn_save_exel_csv, self.main_path)
        QWidget.setTabOrder(self.main_path, self.check_approx_agg)
        QWidget.setTabOrder(self.check_approx_agg, self.check_figs_for_agg)
        QWidget.setTabOrder(self.check_figs_for_agg, self.check_approx_deform)
        QWidget.setTabOrder(self.check_approx_deform, self.check_for_deform)
        QWidget.setTabOrder(self.check_for_deform, self.check_stat_for_column)
        QWidget.setTabOrder(self.check_stat_for_column, self.vibros_delete)
        QWidget.setTabOrder(self.vibros_delete, self.iqr_vibros)
        QWidget.setTabOrder(self.iqr_vibros, self.btn_sort_data_RheoScan)
        QWidget.setTabOrder(self.btn_sort_data_RheoScan, self.spinBox_level)
        QWidget.setTabOrder(self.spinBox_level, self.check_save_exel)
        QWidget.setTabOrder(self.check_save_exel, self.check_save_csv)
        QWidget.setTabOrder(self.check_save_csv, self.check_save_RheoScan_overall)
        QWidget.setTabOrder(self.check_save_RheoScan_overall, self.tua_1_agg)
        QWidget.setTabOrder(self.tua_1_agg, self.tua_2_agg)
        QWidget.setTabOrder(self.tua_2_agg, self.r2_def)
        QWidget.setTabOrder(self.r2_def, self.spinBox_n_max_deform)
        QWidget.setTabOrder(self.spinBox_n_max_deform, self.separator_for_data)
        QWidget.setTabOrder(self.separator_for_data, self.check_name_rheoscan)
        QWidget.setTabOrder(self.check_name_rheoscan, self.spinBox_check_name_rheoscan)
        QWidget.setTabOrder(self.spinBox_check_name_rheoscan, self.path_for_biola)
        QWidget.setTabOrder(self.path_for_biola, self.comboBox_biola)
        QWidget.setTabOrder(self.comboBox_biola, self.comboBox_biola_concentration)
        QWidget.setTabOrder(self.comboBox_biola_concentration, self.spinBox_biola_born_odd)
        QWidget.setTabOrder(self.spinBox_biola_born_odd, self.spinBox_biola_fluc_odd)
        QWidget.setTabOrder(self.spinBox_biola_fluc_odd, self.spinBox_biola_born)
        QWidget.setTabOrder(self.spinBox_biola_born, self.spinBox_biola_fluc)
        QWidget.setTabOrder(self.spinBox_biola_fluc, self.check_biola_plot_figs)
        QWidget.setTabOrder(self.check_biola_plot_figs, self.doubleSpinBox_Biola)
        QWidget.setTabOrder(self.doubleSpinBox_Biola, self.comboBox_Biola_SD_or)
        QWidget.setTabOrder(self.comboBox_Biola_SD_or, self.check_setka_biola)
        QWidget.setTabOrder(self.check_setka_biola, self.comboBox_Biola_language)
        QWidget.setTabOrder(self.comboBox_Biola_language, self.btn_biola)
        QWidget.setTabOrder(self.btn_biola, self.btn_biola_concentration)
        QWidget.setTabOrder(self.btn_biola_concentration, self.path_for_LT)
        QWidget.setTabOrder(self.path_for_LT, self.sep_for_LT)
        QWidget.setTabOrder(self.sep_for_LT, self.position)
        QWidget.setTabOrder(self.position, self.sep_for_LT_values)
        QWidget.setTabOrder(self.sep_for_LT_values, self.a_main)
        QWidget.setTabOrder(self.a_main, self.b_main)
        QWidget.setTabOrder(self.b_main, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.dateEdit_2)
        QWidget.setTabOrder(self.dateEdit_2, self.btn_LT)
        QWidget.setTabOrder(self.btn_LT, self.path_for_plot)
        QWidget.setTabOrder(self.path_for_plot, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.check_box_plot)
        QWidget.setTabOrder(self.check_box_plot, self.check_corr_matrix)
        QWidget.setTabOrder(self.check_corr_matrix, self.check_corr_figs)
        QWidget.setTabOrder(self.check_corr_figs, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.comboBox_color_pal_box)
        QWidget.setTabOrder(self.comboBox_color_pal_box, self.comboBox_color_pal_points)
        QWidget.setTabOrder(self.comboBox_color_pal_points, self.color_box)
        QWidget.setTabOrder(self.color_box, self.color_points)
        QWidget.setTabOrder(self.color_points, self.spinBox_mean_val_size)
        QWidget.setTabOrder(self.spinBox_mean_val_size, self.comboBox_fonts)
        QWidget.setTabOrder(self.comboBox_fonts, self.spinBox_x_label)
        QWidget.setTabOrder(self.spinBox_x_label, self.spinBox_y_label)
        QWidget.setTabOrder(self.spinBox_y_label, self.spinBox_x_val)
        QWidget.setTabOrder(self.spinBox_x_val, self.spinBox_y_vals)
        QWidget.setTabOrder(self.spinBox_y_vals, self.comboBox_stat_test)
        QWidget.setTabOrder(self.comboBox_stat_test, self.comboBox_alter_hep)
        QWidget.setTabOrder(self.comboBox_alter_hep, self.check_stat_znachimost)
        QWidget.setTabOrder(self.check_stat_znachimost, self.STAT_znachimost_order_box_plot)
        QWidget.setTabOrder(self.STAT_znachimost_order_box_plot, self.check_sort_or_not)
        QWidget.setTabOrder(self.check_sort_or_not, self.order_box_plot)
        QWidget.setTabOrder(self.order_box_plot, self.check_N_)
        QWidget.setTabOrder(self.check_N_, self.comboBox_spin_x_)
        QWidget.setTabOrder(self.comboBox_spin_x_, self.check_background)
        QWidget.setTabOrder(self.check_background, self.comboBox_sd_or_minmax)
        QWidget.setTabOrder(self.comboBox_sd_or_minmax, self.bottom_lim)
        QWidget.setTabOrder(self.bottom_lim, self.comboBox_color_pal_corr)
        QWidget.setTabOrder(self.comboBox_color_pal_corr, self.check_change_corr_fig_down_limit)
        QWidget.setTabOrder(self.check_change_corr_fig_down_limit, self.doubleSpinBox_corr_figs)
        QWidget.setTabOrder(self.doubleSpinBox_corr_figs, self.del_hue)
        QWidget.setTabOrder(self.del_hue, self.spinBox_points_corrFIGS)
        QWidget.setTabOrder(self.spinBox_points_corrFIGS, self.doubleSpinBox_corr_figs_fontscale)
        QWidget.setTabOrder(self.doubleSpinBox_corr_figs_fontscale, self.check_sort_or_not_corr_figs)
        QWidget.setTabOrder(self.check_sort_or_not_corr_figs, self.check_setka)
        QWidget.setTabOrder(self.check_setka, self.name_of_corr_matrix)
        QWidget.setTabOrder(self.name_of_corr_matrix, self.btn_plot_and_save_figs)
        QWidget.setTabOrder(self.btn_plot_and_save_figs, self.path_for_profile)
        QWidget.setTabOrder(self.path_for_profile, self.patient_data)
        QWidget.setTabOrder(self.patient_data, self.norm_data)
        QWidget.setTabOrder(self.norm_data, self.patient_prof)
        QWidget.setTabOrder(self.patient_prof, self.color_for_patient)
        QWidget.setTabOrder(self.color_for_patient, self.check_profile_pat_line)
        QWidget.setTabOrder(self.check_profile_pat_line, self.check_profile_pat_sd)
        QWidget.setTabOrder(self.check_profile_pat_sd, self.norm_prof)
        QWidget.setTabOrder(self.norm_prof, self.color_for_norm)
        QWidget.setTabOrder(self.color_for_norm, self.check_profile_norm_line)
        QWidget.setTabOrder(self.check_profile_norm_line, self.check_profile_norm_sd)
        QWidget.setTabOrder(self.check_profile_norm_sd, self.btn_plot_and_save_profile)
        QWidget.setTabOrder(self.btn_plot_and_save_profile, self.path_for_pivot_table)
        QWidget.setTabOrder(self.path_for_pivot_table, self.comboBox_pivot_table)
        QWidget.setTabOrder(self.comboBox_pivot_table, self.comboBox_pivot_hue)
        QWidget.setTabOrder(self.comboBox_pivot_hue, self.spinBox_pivot_table)
        QWidget.setTabOrder(self.spinBox_pivot_table, self.comboBox_sd_or_se_pivot)
        QWidget.setTabOrder(self.comboBox_sd_or_se_pivot, self.comboBox_correlation_person_or_not)
        QWidget.setTabOrder(self.comboBox_correlation_person_or_not, self.check_color_for_corr_pivot)
        QWidget.setTabOrder(self.check_color_for_corr_pivot, self.comboBox_correlation_color_map)
        QWidget.setTabOrder(self.comboBox_correlation_color_map, self.path_for_catplot)
        QWidget.setTabOrder(self.path_for_catplot, self.comboBox_excel_catplot)
        QWidget.setTabOrder(self.comboBox_excel_catplot, self.comboBox_excel_sheet_catplot)
        QWidget.setTabOrder(self.comboBox_excel_sheet_catplot, self.comboBox_catplot_x)
        QWidget.setTabOrder(self.comboBox_catplot_x, self.comboBox_catplot_form_x)
        QWidget.setTabOrder(self.comboBox_catplot_form_x, self.comboBox_catplot_y)
        QWidget.setTabOrder(self.comboBox_catplot_y, self.comboBox_catplot_form_y)
        QWidget.setTabOrder(self.comboBox_catplot_form_y, self.comboBox_catplot_hue)
        QWidget.setTabOrder(self.comboBox_catplot_hue, self.comboBox_catplot_form_hue)
        QWidget.setTabOrder(self.comboBox_catplot_form_hue, self.doubleSpinBox_catplot)
        QWidget.setTabOrder(self.doubleSpinBox_catplot, self.comboBox_color_catplot)
        QWidget.setTabOrder(self.comboBox_color_catplot, self.check_stat_znachimost_catplot)
        QWidget.setTabOrder(self.check_stat_znachimost_catplot, self.comboBox_stat_test_catplot)
        QWidget.setTabOrder(self.comboBox_stat_test_catplot, self.comboBox_catplot_stat_formatt)
        QWidget.setTabOrder(self.comboBox_catplot_stat_formatt, self.comboBox_catplot_mult_stat)
        QWidget.setTabOrder(self.comboBox_catplot_mult_stat, self.comboBox_template_catplot)
        QWidget.setTabOrder(self.comboBox_template_catplot, self.comboBox_catplot_SD_or_not)
        QWidget.setTabOrder(self.comboBox_catplot_SD_or_not, self.btn_plot_and_save_catplot)

        self.retranslateUi(MainWindow)
        self.check_stat_znachimost_catplot.toggled.connect(self.comboBox_stat_test_catplot.setEnabled)
        self.check_stat_znachimost_catplot.toggled.connect(self.comboBox_catplot_stat_formatt.setEnabled)
        self.check_stat_znachimost_catplot.toggled.connect(self.comboBox_catplot_mult_stat.setEnabled)
        self.check_biola_plot_figs.toggled.connect(self.plp.setEnabled)
        self.check_box_figs_all_sheets.toggled.connect(self.comboBox_figs_sheets.setDisabled)
        self.check_box_figs_all_sheets.toggled.connect(self.lb_exel_name_8.setDisabled)
        self.check_stat_znachimost.toggled.connect(self.comboBox_stat_test.setEnabled)
        self.check_stat_znachimost.toggled.connect(self.comboBox_alter_hep.setEnabled)
        self.check_stat_znachimost.toggled.connect(self.STAT_znachimost_order_box_plot.setEnabled)
        self.check_approx_agg.toggled.connect(self.check_figs_for_agg.setEnabled)
        self.check_approx_deform.toggled.connect(self.check_for_deform.setEnabled)
        self.check_approx_agg.toggled.connect(self.tua_1_agg.setEnabled)
        self.check_approx_agg.toggled.connect(self.tua_2_agg.setEnabled)
        self.check_approx_agg.toggled.connect(self.label_20.setEnabled)
        self.check_approx_agg.toggled.connect(self.label_21.setEnabled)
        self.check_approx_deform.toggled.connect(self.r2_def.setEnabled)
        self.check_approx_deform.toggled.connect(self.spinBox_n_max_deform.setEnabled)
        self.check_approx_deform.toggled.connect(self.label_23.setEnabled)
        self.check_approx_deform.toggled.connect(self.label_18.setEnabled)
        self.check_approx_deform.toggled.connect(self.check_approx_deform_raw_data.setEnabled)
        self.vibros_delete.toggled.connect(self.iqr_vibros.setEnabled)
        self.vibros_delete.toggled.connect(self.label_11.setEnabled)
        self.check_name_rheoscan.toggled.connect(self.label_19.setEnabled)
        self.check_name_rheoscan.toggled.connect(self.spinBox_check_name_rheoscan.setEnabled)

        self.Lab_stuff.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0440\u043c\u043e\u043b\u0438\u043d\u0441\u043a\u0438\u0439 \u041f\u0435\u0442\u0440 \u2014 \u0432\u0435\u0440\u0441\u0438\u044f 3.41", None))
        self.comboBox_style_sheet.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.comboBox_style_sheet.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))

        self.btn_save_exel_csv.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
#if QT_CONFIG(tooltip)
        self.lb_path.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u043e \u0434\u0430\u043d\u043d\u043e\u043c\u0443 \u043f\u0443\u0442\u0438 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c 3 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 (agg, stress, deform), \u0435\u0441\u043b\u0438 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a 1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c\u0438", None))
        self.main_path.setText("")
        self.comboBox_RheoScan_path_save.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel/cvs \u0444\u0430\u0439\u043b\u044b \u043f\u043e \u043f\u0430\u043f\u043a\u0430\u043c", None))
        self.comboBox_RheoScan_path_save.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel/cvs \u0444\u0430\u0439\u043b\u044b \u0432 \u043e\u0434\u043d\u043e\u043c \u043c\u0435\u0441\u0442\u0435", None))

        self.check_approx_deform_raw_data.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u044b\u0440\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e deform", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0439 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Max \u0432\u0440\u0435\u043c\u044f \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u043b\u0438\u043d\u0435\u0439\u043d\u044b\u0445 \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0432</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_21.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0439 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Max \u0432\u0440\u0435\u043c\u044f \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f 3D \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0432</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_23.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0442\u043e\u0447\u0435\u043a \u0442\u043e\u0447\u043d\u043e \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0434\u043b\u044f \u0430\u043f\u0440\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438. \u0415\u0441\u043b\u0438 R<span style=\" vertical-align:super;\">2</span> \u0431\u0443\u0434\u0435\u0442 \u043c\u0435\u043d\u044c\u0448\u0435, \u0447\u0435\u043c \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u043d\u044b\u0439, \u043d\u043e \u0442\u043e\u0447\u0435\u043a \u0443\u0436\u0435 \u043c\u0435\u043d\u044c\u0448\u0435, \u0442\u043e \u0434\u0430\u043b\u044c\u043d\u0435\u0439\u0448\u0435\u0433\u043e \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u0438\u044f \u043d\u0435 \u0431\u0443\u0434\u0435\u0442. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>R-\u043a\u0432\u0430\u0434\u0440\u0430\u0442 \u0434\u043b\u044f \u043e\u0442\u0441\u0435\u0447\u043a\u0438</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0442\u043e\u0447\u0435\u043a \u0442\u043e\u0447\u043d\u043e \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0434\u043b\u044f \u0430\u043f\u0440\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438. \u0415\u0441\u043b\u0438 R<span style=\" vertical-align:super;\">2</span> \u0431\u0443\u0434\u0435\u0442 \u043c\u0435\u043d\u044c\u0448\u0435, \u0447\u0435\u043c \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u043d\u044b\u0439, \u043d\u043e \u0442\u043e\u0447\u0435\u043a \u0443\u0436\u0435 \u043c\u0435\u043d\u044c\u0448\u0435, \u0442\u043e \u0434\u0430\u043b\u044c\u043d\u0435\u0439\u0448\u0435\u0433\u043e \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u0438\u044f \u043d\u0435 \u0431\u0443\u0434\u0435\u0442. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b-\u0432\u043e \u0442\u043e\u0447\u0435\u043a \u0434\u043b\u044f \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438</p></body></html>", None))
        self.check_approx_agg.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u0434\u043b\u044f agg", None))
        self.check_figs_for_agg.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.check_approx_deform.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u0434\u043b\u044f deform", None))
        self.check_for_deform.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.check_stat_for_column.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430\u043c", None))
#if QT_CONFIG(tooltip)
        self.vibros_delete.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u044b\u0431\u0440\u043e\u0441\u044b \u0443\u0431\u0438\u0440\u0430\u044e\u0442\u0441\u044f \u043f\u043e \u0438\u043d\u0442\u0435\u0440\u043a\u0430\u043d\u0442\u0438\u043b\u044c\u043d\u043e\u043c\u0443 \u0440\u0430\u0437\u043c\u0430\u0445\u0443 -- \u0441\u043c. \u0438\u043d\u0444\u0443 \u043f\u043e \u0442\u043e\u043c\u0443, \u0447\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u0432\u044b\u0431\u0440\u043e\u0441\u044b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vibros_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c \u0432\u044b\u0431\u0440\u043e\u0441\u044b", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0438\u043d\u0442\u0435\u0440\u043a\u0432\u0430\u0440\u0442\u0438\u043b\u044c\u043d\u044b\u0445 \u0440\u0430\u0437\u043c\u0430\u0445\u0430", None))
#if QT_CONFIG(tooltip)
        self.btn_sort_data_RheoScan.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">\u0415\u0441\u043b\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u0440\u043e\u0441\u0442\u043e \u043d\u0430\u0433\u0440\u043e\u043c\u043e\u0436\u0434\u0435\u043d\u044b \u0432 \u043e\u0434\u043d\u0443 \u043f\u0430\u043f\u043a\u0443, \u0442\u043e \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u044d\u0442\u0443 \u043a\u043d\u043e\u043f\u043a\u0443. \u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0442\u0443\u0442</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_sort_data_RheoScan.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0435\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u043f\u0430\u043f\u043a\u0430 \u0441 \u043f\u0430\u043f\u043a\u0430\u043c\u0438, \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0435\u0441\u0442\u044c 3 \u043f\u0430\u043f\u043a\u0438, \u0442\u043e \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c 2, \u0438 \u0442.\u0434.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a           ", None))
        self.check_save_exel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b", None))
        self.check_save_csv.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c csv \u0444\u0430\u0439\u043b(\u044b)", None))
        self.check_save_RheoScan_overall.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0432\u043e\u0434\u043d\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
#if QT_CONFIG(tooltip)
        self.lb_separator.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u042d\u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0438 \u0444\u0430\u0439\u043b\u043e\u0432. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u0444\u0430\u0439\u043b\u044b \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c: &quot;NAME-##-#&quot;, \u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c &quot;-&quot;.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_separator.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.separator_for_data.setText("")
        self.check_name_rheoscan.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u043d\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u043f\u0430\u043f\u043a\u0430 \u0441 \u043f\u0430\u043f\u043a\u0430\u043c\u0438, \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0435\u0441\u0442\u044c 3 \u043f\u0430\u043f\u043a\u0438, \u0442\u043e \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c 2, \u0438 \u0442.\u0434.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u0438\u043c\u0435\u043d\u0438", None))
        self.check_agg.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 agg", None))
        self.check_stress.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 stress", None))
        self.check_deform.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 deform", None))
        self.check_dop_CSS_parameter.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f. \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 CSS", None))
        self.Lab_stuff.setTabText(self.Lab_stuff.indexOf(self.tabWidgetPage1), QCoreApplication.translate("MainWindow", u" RheoScan", None))
        self.lb_path_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0444\u0430\u0439\u043b\u043e\u043c", None))
#if QT_CONFIG(tooltip)
        self.path_for_biola.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0444\u0430\u0439\u043b\u043e\u043c txt, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0431\u044b\u043b \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d \u0438\u0437 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0434\u043b\u044f \u0411\u0438\u043e\u043b\u044b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.path_for_biola.setText("")
        self.lb_path_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0433\u0440\u0430\u043c\u043c (txt)", None))
        self.lb_path_16.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u0438 \u0442\u0440\u043e\u043c\u0431\u043e\u0446\u0438\u0442\u043e\u0432 (pdf)", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u042d\u0442\u043e \u0444\u0438\u043b\u044c\u0442\u0440 \u0421\u0430\u0432\u0438\u0446\u043a\u043e\u0433\u043e-\u0433\u043e\u043b\u0435\u044f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u043a\u0440\u0438\u0432\u044b\u0445", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u0440\u043d", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043b\u0443\u043a\u0442\u0430\u0446\u0438\u0438", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("MainWindow", u"\u042d\u0442\u043e \u0444\u0438\u043b\u044c\u0442\u0440 \u0421\u0430\u0432\u0438\u0446\u043a\u043e\u0433\u043e-\u0433\u043e\u043b\u0435\u044f", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u044b\u0445", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u0440\u043d", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043b\u0443\u043a\u0442\u0430\u0446\u0438\u0438", None))
        self.check_biola_plot_figs.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0435\u0440\u0442\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.lb_color_pal_box_13.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432", None))
        self.lb_color_pal_box_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430", None))
#if QT_CONFIG(tooltip)
        self.lb_color_pal_box_10.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.lb_color_pal_box_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0438", None))
        self.comboBox_Biola_SD_or.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435", None))
        self.comboBox_Biola_SD_or.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0448\u0438\u0431\u043a\u0430", None))
        self.comboBox_Biola_SD_or.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b", None))
        self.comboBox_Biola_SD_or.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0446\u0435\u043d\u0442\u0438\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b", None))

#if QT_CONFIG(tooltip)
        self.check_setka_biola.setToolTip(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u0444\u043b\u0430\u0436\u043a\u0430 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0431\u0443\u0434\u0435\u0442 \u0442\u0430\u043a\u0438\u043c, \u043a\u0430\u043a\u043e\u0439 \u043e\u043d \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.check_setka_biola.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0442\u043a\u0430", None))
        self.lb_color_pal_box_11.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a  ", None))
        self.comboBox_Biola_language.setItemText(0, QCoreApplication.translate("MainWindow", u"Rus", None))
        self.comboBox_Biola_language.setItemText(1, QCoreApplication.translate("MainWindow", u"Eng", None))

        self.btn_biola.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435, \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0438\u0441\u0443\u043d\u043a\u0438 \u0438 excel \u0444\u0430\u0439\u043b", None))
        self.btn_biola_concentration.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430 pdf", None))
        self.Lab_stuff.setTabText(self.Lab_stuff.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u0411\u0438\u043e\u043b\u0430", None))
#if QT_CONFIG(tooltip)
        self.lb_stattest_13.setToolTip(QCoreApplication.translate("MainWindow", u"\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430 \u0434\u043b\u044f \u0434\u043e\u043f. \u043f\u0443\u0447\u043a\u0430", None))
        self.comboBox_LT_calibration.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0435\u0439\u043d\u0430\u044f", None))
        self.comboBox_LT_calibration.setItemText(1, QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u0430\u044f", None))

#if QT_CONFIG(tooltip)
        self.lb_path_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0441\u0435 \u0441\u0438\u043b\u044b \u043c\u0435\u0436\u0434\u0443 \u044d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u0430\u043c\u0438 \u0438 \u044d\u043d\u0434\u043e\u0442\u0435\u043b\u0438\u0435\u043c \u0447\u0435\u0440\u0435\u0437 \u044d\u0442\u043e \u043f\u0440\u043e\u0433\u043e\u043d\u044f\u044e\u0442\u0441\u044f. \u0421\u0438\u043b\u044b  \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u044e\u0442\u0441\u044f End...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0443\u0447\u043e\u043a", None))
#if QT_CONFIG(tooltip)
        self.lb_path_17.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = k*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_17.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = ", None))
#if QT_CONFIG(tooltip)
        self.lb_path_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_7.setText(QCoreApplication.translate("MainWindow", u"k", None))
#if QT_CONFIG(tooltip)
        self.lb_path_18.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_18.setText(QCoreApplication.translate("MainWindow", u"*\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u043d\u0430 \u0444\u043e\u0442\u043e\u0434\u0435\u0442\u0435\u043a\u0442\u043e\u0440\u0435", None))
#if QT_CONFIG(tooltip)
        self.lb_path_8.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_8.setText(QCoreApplication.translate("MainWindow", u" + b", None))
        self.lb_path_12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.lb_path_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0441\u0435 \u0441\u0438\u043b\u044b \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u0438 \u0434\u0435\u0437\u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u0447\u0435\u0440\u0435\u0437 \u044d\u0442\u043e \u043f\u0440\u043e\u0433\u043e\u043d\u044f\u044e\u0442\u0441\u044f. \u0421\u0438\u043b\u044b \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u044e\u0442\u0441\u044f FA..., FD...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0443\u0447\u043e\u043a", None))
#if QT_CONFIG(tooltip)
        self.lb_path_19.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = k*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_19.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = ", None))
#if QT_CONFIG(tooltip)
        self.lb_path_9.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_9.setText(QCoreApplication.translate("MainWindow", u"k", None))
#if QT_CONFIG(tooltip)
        self.lb_path_20.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_20.setText(QCoreApplication.translate("MainWindow", u"*\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u043d\u0430 \u0444\u043e\u0442\u043e\u0434\u0435\u0442\u0435\u043a\u0442\u043e\u0440\u0435", None))
#if QT_CONFIG(tooltip)
        self.lb_path_21.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_21.setText(QCoreApplication.translate("MainWindow", u" + b", None))
        self.lb_path_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.lb_path_10.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0441\u0435 \u0441\u0438\u043b\u044b \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u0438 \u0434\u0435\u0437\u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u0447\u0435\u0440\u0435\u0437 \u044d\u0442\u043e \u043f\u0440\u043e\u0433\u043e\u043d\u044f\u044e\u0442\u0441\u044f. \u0421\u0438\u043b\u044b \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u044e\u0442\u0441\u044f FA..., FD...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0443\u0447\u043e\u043a", None))
#if QT_CONFIG(tooltip)
        self.lb_path_22.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_path_22.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = ", None))
#if QT_CONFIG(tooltip)
        self.lb_path_23.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_23.setText(QCoreApplication.translate("MainWindow", u"k", None))
#if QT_CONFIG(tooltip)
        self.lb_path_27.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_27.setText(QCoreApplication.translate("MainWindow", u"*( y0", None))
#if QT_CONFIG(tooltip)
        self.lb_path_28.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_28.setText(QCoreApplication.translate("MainWindow", u"+ A", None))
#if QT_CONFIG(tooltip)
        self.lb_path_29.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_29.setText(QCoreApplication.translate("MainWindow", u"* EXP( \u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c * ", None))
#if QT_CONFIG(tooltip)
        self.lb_path_30.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_30.setText(QCoreApplication.translate("MainWindow", u"R0", None))
#if QT_CONFIG(tooltip)
        self.lb_path_31.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_31.setText(QCoreApplication.translate("MainWindow", u")) + b", None))
        self.lb_path_26.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438", None))
        self.btn_LT.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b", None))
#if QT_CONFIG(tooltip)
        self.lb_path_4.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0435\u0441\u0442\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 \u0441 \u0432\u0438\u0434\u0435\u043e avi", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c\u0438", None))
        self.path_for_LT.setText("")
#if QT_CONFIG(tooltip)
        self.lb_path_13.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u043b\u0438 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f '1-Name1-Name2', \u0442\u043e \u043c\u043e\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c '-'</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_13.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0438 \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a", None))
        self.sep_for_LT.setText("")
#if QT_CONFIG(tooltip)
        self.lb_path_15.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0432\u044b\u0431\u0440\u0430\u043d \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c '-' \u0434\u043b\u044f \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a '1-Name1-Name2', \u0442\u043e \u043f\u0440\u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0438 2 \u0431\u0443\u0434\u0435\u0442 Name1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_15.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u0438\u043d\u0442\u0435\u0440\u0438\u0441\u0443\u044e\u0449\u0435\u0435 \u0438\u043c\u044f", None))
#if QT_CONFIG(tooltip)
        self.lb_path_14.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0432\u0441\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0441\u0438\u043b \u0432 \u0432\u0438\u0434\u0435 &quot;FA-18.9.avi&quot;, \u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0435\u043c \u0431\u0443\u0434\u0435\u0442 &quot;-&quot;. \u0422\u0430\u043a \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0434\u043b\u044f \u0432\u0441\u0435\u0445. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_14.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u043c\u0435\u0436\u0434\u0443 \u0441\u0438\u043b\u043e\u0439 \u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u043c", None))
        self.sep_for_LT_values.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Lab_stuff.setTabText(self.Lab_stuff.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0437\u0435\u0440\u043d\u044b\u0439 \u043f\u0438\u043d\u0446\u0435\u0442", None))
#if QT_CONFIG(tooltip)
        self.lb_path_for_plot.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443", None))
        self.path_for_plot.setText("")
        self.lb_exel_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430", None))
        self.check_box_figs_all_sheets.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0432\u0441\u0435\u043c \u043b\u0438\u0441\u0442\u0430\u043c", None))
        self.lb_exel_name_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 \u0444\u0430\u0439\u043b\u0435", None))
#if QT_CONFIG(tooltip)
        self.lb_hue_name.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u0435\u043d\u043d\u043e \u043f\u043e\u0441\u043b\u0435 \u044d\u0442\u043e\u0433\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043e\u043b\u0436\u043d\u044b \u0438\u0434\u0442\u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f", None))
        self.check_box_plot.setText(QCoreApplication.translate("MainWindow", u"Box plot", None))
        self.check_corr_matrix.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u043c\u0430\u0442\u0440\u0438\u0446\u044b", None))
        self.check_corr_figs.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.lb_color_pal_box.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430 \u0434\u043b\u044f box", None))
        self.comboBox_color_pal_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Set1", None))
        self.comboBox_color_pal_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Set2", None))
        self.comboBox_color_pal_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Set3", None))
        self.comboBox_color_pal_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Paired", None))
        self.comboBox_color_pal_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Accent", None))
        self.comboBox_color_pal_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Pastel1", None))
        self.comboBox_color_pal_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Pastel2", None))
        self.comboBox_color_pal_box.setItemText(7, QCoreApplication.translate("MainWindow", u"Dark2", None))
        self.comboBox_color_pal_box.setItemText(8, QCoreApplication.translate("MainWindow", u"rocket", None))
        self.comboBox_color_pal_box.setItemText(9, QCoreApplication.translate("MainWindow", u"mako", None))
        self.comboBox_color_pal_box.setItemText(10, QCoreApplication.translate("MainWindow", u"flare", None))
        self.comboBox_color_pal_box.setItemText(11, QCoreApplication.translate("MainWindow", u"crest", None))
        self.comboBox_color_pal_box.setItemText(12, QCoreApplication.translate("MainWindow", u"viridis", None))
        self.comboBox_color_pal_box.setItemText(13, QCoreApplication.translate("MainWindow", u"plasma", None))
        self.comboBox_color_pal_box.setItemText(14, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.comboBox_color_pal_box.setItemText(15, QCoreApplication.translate("MainWindow", u"magma", None))
        self.comboBox_color_pal_box.setItemText(16, QCoreApplication.translate("MainWindow", u"cividis", None))
        self.comboBox_color_pal_box.setItemText(17, QCoreApplication.translate("MainWindow", u"Greys", None))
        self.comboBox_color_pal_box.setItemText(18, QCoreApplication.translate("MainWindow", u"Reds", None))
        self.comboBox_color_pal_box.setItemText(19, QCoreApplication.translate("MainWindow", u"Greens", None))
        self.comboBox_color_pal_box.setItemText(20, QCoreApplication.translate("MainWindow", u"Blues", None))
        self.comboBox_color_pal_box.setItemText(21, QCoreApplication.translate("MainWindow", u"Oranges", None))
        self.comboBox_color_pal_box.setItemText(22, QCoreApplication.translate("MainWindow", u"Purples", None))
        self.comboBox_color_pal_box.setItemText(23, QCoreApplication.translate("MainWindow", u"YlOrRd", None))
        self.comboBox_color_pal_box.setItemText(24, QCoreApplication.translate("MainWindow", u"tab10", None))
        self.comboBox_color_pal_box.setItemText(25, QCoreApplication.translate("MainWindow", u"deep", None))
        self.comboBox_color_pal_box.setItemText(26, QCoreApplication.translate("MainWindow", u"muted", None))
        self.comboBox_color_pal_box.setItemText(27, QCoreApplication.translate("MainWindow", u"pastel", None))
        self.comboBox_color_pal_box.setItemText(28, QCoreApplication.translate("MainWindow", u"bright", None))
        self.comboBox_color_pal_box.setItemText(29, QCoreApplication.translate("MainWindow", u"dark", None))
        self.comboBox_color_pal_box.setItemText(30, QCoreApplication.translate("MainWindow", u"colorblind", None))
        self.comboBox_color_pal_box.setItemText(31, QCoreApplication.translate("MainWindow", u"tab20", None))
        self.comboBox_color_pal_box.setItemText(32, QCoreApplication.translate("MainWindow", u"tab20b", None))
        self.comboBox_color_pal_box.setItemText(33, QCoreApplication.translate("MainWindow", u"tab20c", None))
        self.comboBox_color_pal_box.setItemText(34, QCoreApplication.translate("MainWindow", u"BuPu", None))
        self.comboBox_color_pal_box.setItemText(35, QCoreApplication.translate("MainWindow", u"BuPu_r", None))

        self.lb_color_pal_points.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430 \u0434\u043b\u044f \u0442\u043e\u0447\u0435\u043a", None))
        self.comboBox_color_pal_points.setItemText(0, QCoreApplication.translate("MainWindow", u"Set1", None))
        self.comboBox_color_pal_points.setItemText(1, QCoreApplication.translate("MainWindow", u"Set2", None))
        self.comboBox_color_pal_points.setItemText(2, QCoreApplication.translate("MainWindow", u"Set3", None))
        self.comboBox_color_pal_points.setItemText(3, QCoreApplication.translate("MainWindow", u"Paired", None))
        self.comboBox_color_pal_points.setItemText(4, QCoreApplication.translate("MainWindow", u"Accent", None))
        self.comboBox_color_pal_points.setItemText(5, QCoreApplication.translate("MainWindow", u"Pastel1", None))
        self.comboBox_color_pal_points.setItemText(6, QCoreApplication.translate("MainWindow", u"Pastel2", None))
        self.comboBox_color_pal_points.setItemText(7, QCoreApplication.translate("MainWindow", u"Dark2", None))
        self.comboBox_color_pal_points.setItemText(8, QCoreApplication.translate("MainWindow", u"rocket", None))
        self.comboBox_color_pal_points.setItemText(9, QCoreApplication.translate("MainWindow", u"mako", None))
        self.comboBox_color_pal_points.setItemText(10, QCoreApplication.translate("MainWindow", u"flare", None))
        self.comboBox_color_pal_points.setItemText(11, QCoreApplication.translate("MainWindow", u"crest", None))
        self.comboBox_color_pal_points.setItemText(12, QCoreApplication.translate("MainWindow", u"viridis", None))
        self.comboBox_color_pal_points.setItemText(13, QCoreApplication.translate("MainWindow", u"plasma", None))
        self.comboBox_color_pal_points.setItemText(14, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.comboBox_color_pal_points.setItemText(15, QCoreApplication.translate("MainWindow", u"magma", None))
        self.comboBox_color_pal_points.setItemText(16, QCoreApplication.translate("MainWindow", u"cividis", None))
        self.comboBox_color_pal_points.setItemText(17, QCoreApplication.translate("MainWindow", u"Greys", None))
        self.comboBox_color_pal_points.setItemText(18, QCoreApplication.translate("MainWindow", u"Reds", None))
        self.comboBox_color_pal_points.setItemText(19, QCoreApplication.translate("MainWindow", u"Greens", None))
        self.comboBox_color_pal_points.setItemText(20, QCoreApplication.translate("MainWindow", u"Blues", None))
        self.comboBox_color_pal_points.setItemText(21, QCoreApplication.translate("MainWindow", u"Oranges", None))
        self.comboBox_color_pal_points.setItemText(22, QCoreApplication.translate("MainWindow", u"Purples", None))
        self.comboBox_color_pal_points.setItemText(23, QCoreApplication.translate("MainWindow", u"YlOrRd", None))
        self.comboBox_color_pal_points.setItemText(24, QCoreApplication.translate("MainWindow", u"tab10", None))
        self.comboBox_color_pal_points.setItemText(25, QCoreApplication.translate("MainWindow", u"deep", None))
        self.comboBox_color_pal_points.setItemText(26, QCoreApplication.translate("MainWindow", u"muted", None))
        self.comboBox_color_pal_points.setItemText(27, QCoreApplication.translate("MainWindow", u"pastel", None))
        self.comboBox_color_pal_points.setItemText(28, QCoreApplication.translate("MainWindow", u"bright", None))
        self.comboBox_color_pal_points.setItemText(29, QCoreApplication.translate("MainWindow", u"dark", None))
        self.comboBox_color_pal_points.setItemText(30, QCoreApplication.translate("MainWindow", u"colorblind", None))
        self.comboBox_color_pal_points.setItemText(31, QCoreApplication.translate("MainWindow", u"tab20", None))
        self.comboBox_color_pal_points.setItemText(32, QCoreApplication.translate("MainWindow", u"tab20b", None))
        self.comboBox_color_pal_points.setItemText(33, QCoreApplication.translate("MainWindow", u"tab20c", None))
        self.comboBox_color_pal_points.setItemText(34, QCoreApplication.translate("MainWindow", u"BuPu", None))
        self.comboBox_color_pal_points.setItemText(35, QCoreApplication.translate("MainWindow", u"BuPu_r", None))

#if QT_CONFIG(tooltip)
        self.lb_color_for_box.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u043b\u0438 \u043f\u043e\u043b\u0435 \u043f\u0443\u0441\u0442\u043e\u0435, \u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u0446\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430. \u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0446\u0432\u0435\u0442 \u0431\u044b\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX: #......</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_color_for_box.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u044f box (HEX)", None))
#if QT_CONFIG(tooltip)
        self.lb_color_forpoints.setToolTip(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u043b\u0438 \u043f\u043e\u043b\u0435 \u043f\u0443\u0441\u0442\u043e\u0435, \u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u0446\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430. \u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0446\u0432\u0435\u0442 \u0431\u044b\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX: #......", None))
#endif // QT_CONFIG(tooltip)
        self.lb_color_forpoints.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u0442\u043e\u0447\u0435\u043a (HEX)", None))
        self.lb_color_pal_box_19.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435", None))
        self.lb_color_pal_box_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a \u0434\u043b\u044f \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.lb_color_pal_box_6.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0440\u0438\u0444\u0442", None))
        self.comboBox_fonts.setItemText(0, QCoreApplication.translate("MainWindow", u"DejaVu Sans", None))
        self.comboBox_fonts.setItemText(1, QCoreApplication.translate("MainWindow", u"Tahoma", None))
        self.comboBox_fonts.setItemText(2, QCoreApplication.translate("MainWindow", u"Verdana", None))
        self.comboBox_fonts.setItemText(3, QCoreApplication.translate("MainWindow", u"Arial", None))
        self.comboBox_fonts.setItemText(4, QCoreApplication.translate("MainWindow", u"Trebuchet MS", None))
        self.comboBox_fonts.setItemText(5, QCoreApplication.translate("MainWindow", u"Times New Roman", None))
        self.comboBox_fonts.setItemText(6, QCoreApplication.translate("MainWindow", u"Georgia", None))

        self.lb_color_pal_box_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 X", None))
        self.lb_color_pal_box_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 Y", None))
        self.lb_color_pal_box_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 X", None))
        self.lb_color_pal_box_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 Y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Box plot (1)", None))
#if QT_CONFIG(tooltip)
        self.lb_stattest.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u043c. \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044e \u043a <a href=\"https://docs.scipy.org/doc/scipy/reference/stats.html\"><span style=\" text-decoration: underline; color:#0000ff;\">scipy.stats</span></a></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442", None))
        self.comboBox_stat_test.setItemText(0, QCoreApplication.translate("MainWindow", u"U-\u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041c\u0430\u043d\u043d\u0430 \u2014 \u0423\u0438\u0442\u043d\u0438", None))
        self.comboBox_stat_test.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422-\u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0421\u0442\u044c\u044e\u0434\u0435\u043d\u0442\u0430", None))
        self.comboBox_stat_test.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f", None))
        self.comboBox_stat_test.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f (normal)", None))
        self.comboBox_stat_test.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0423\u0438\u043b\u043a\u043e\u043a\u0441\u043e\u043d\u0430", None))
        self.comboBox_stat_test.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041a\u0440\u0430\u0441\u043a\u0435\u043b\u0430 \u2014 \u0423\u043e\u043b\u043b\u0438\u0441\u0430", None))
        self.comboBox_stat_test.setItemText(6, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0430\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439", None))
        self.comboBox_stat_test.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0410\u043d\u0441\u0430\u0440\u0438-\u0411\u0440\u044d\u0434\u043b\u0438", None))
        self.comboBox_stat_test.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0424\u0438\u0448\u0435\u0440\u0430-\u041f\u0438\u0442\u043c\u0430\u043d\u0430", None))
        self.comboBox_stat_test.setItemText(9, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f", None))
        self.comboBox_stat_test.setItemText(10, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041c\u0430\u043d\u043d\u0430 \u2014 \u0423\u0438\u0442\u043d\u0438", None))
        self.comboBox_stat_test.setItemText(11, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0423\u0438\u043b\u043a\u043e\u043a\u0441\u043e\u043d\u0430", None))
        self.comboBox_stat_test.setItemText(12, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0424\u0440\u0438\u0434\u043c\u0430\u043d\u0430", None))

        self.lb__altern_heposisis.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u0433\u0438\u043f\u043e\u0442\u0435\u0437\u0430", None))
        self.comboBox_alter_hep.setItemText(0, QCoreApplication.translate("MainWindow", u"two-sided", None))
        self.comboBox_alter_hep.setItemText(1, QCoreApplication.translate("MainWindow", u"less", None))
        self.comboBox_alter_hep.setItemText(2, QCoreApplication.translate("MainWindow", u"greater", None))

        self.lb_stattest_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c?", None))
        self.check_stat_znachimost.setText("")
#if QT_CONFIG(tooltip)
        self.lb_del_hue_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u043b\u0438 \u043d\u0435 \u043d\u0443\u0436\u043d\u043e \u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u043c\u0435\u0436\u0434\u0443 \u0432\u0441\u0435\u043c\u0438 \u0433\u0440\u0443\u043f\u043f\u0430\u043c\u0438, \u0442\u043e \u043d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u044d\u0442\u043e. \u0412\u0432\u0435\u0441\u0442\u0438 \u043d\u0430\u0434\u043e \u0432 \u0441\u0442\u0440\u043e\u043a\u0443 \u043c\u0430\u0441\u0441\u0438\u0432 \u0438\u0437 \u0433\u0440\u0443\u043f\u043f. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u0442\u044c 4 \u0433\u0440\u0443\u043f\u043f\u044b \u0438 \u0445\u043e\u0447\u0435\u0442\u0441\u044f \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u0442\u0430\u0442.\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u0436\u0434\u0443 1 \u0438 2, \u0430"
                        " \u0442\u0430\u043a\u0436\u0435 3 \u0438 4. \u0422\u043e\u0433\u0434\u0430 \u043d\u0430\u0434\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0441 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u043c '(1,2) (3,4)'</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_del_hue_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442 \u0441\u0442\u0430\u0442.\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438 \u0442\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u0436\u0434\u0443 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c\u0438 \u0433\u0440\u0443\u043f\u043f\u0430\u043c\u0438", None))
#if QT_CONFIG(tooltip)
        self.STAT_znachimost_order_box_plot.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Box plot (2)", None))
#if QT_CONFIG(tooltip)
        self.check_sort_or_not.setToolTip(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u0444\u043b\u0430\u0436\u043a\u0430 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0431\u0443\u0434\u0435\u0442 \u0442\u0430\u043a\u0438\u043c, \u043a\u0430\u043a\u043e\u0439 \u043e\u043d \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.check_sort_or_not.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0433\u0440\u0443\u043f\u043f\u0435", None))
#if QT_CONFIG(tooltip)
        self.lb_del_hue_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u0440\u043e\u043f\u0438\u0441\u0430\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b, \u043d\u0430\u0447\u0438\u043d\u0430\u044f \u0441 \u043f\u0435\u0440\u0432\u043e\u0433\u043e. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, '1 2 4 3'</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_del_hue_6.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439", None))
#if QT_CONFIG(tooltip)
        self.order_box_plot.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lb_stattest_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432 \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u0435 -- \u043f\u043e\u0434\u043f\u0438\u0441\u044c \u0441\u043d\u0438\u0437\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043f\u0438\u0441\u0438 N \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0432 \u0433\u0440\u0443\u043f\u043f\u0430\u0445", None))
        self.check_N_.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0430\u0449\u0430\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u043d\u0430 \u0443\u0433\u043e\u043b", None))
        self.comboBox_spin_x_.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_spin_x_.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_spin_x_.setItemText(2, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_spin_x_.setItemText(3, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_spin_x_.setItemText(4, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_spin_x_.setItemText(5, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_spin_x_.setItemText(6, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_spin_x_.setItemText(7, QCoreApplication.translate("MainWindow", u"35", None))
        self.comboBox_spin_x_.setItemText(8, QCoreApplication.translate("MainWindow", u"40", None))
        self.comboBox_spin_x_.setItemText(9, QCoreApplication.translate("MainWindow", u"45", None))
        self.comboBox_spin_x_.setItemText(10, QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBox_spin_x_.setItemText(11, QCoreApplication.translate("MainWindow", u"55", None))
        self.comboBox_spin_x_.setItemText(12, QCoreApplication.translate("MainWindow", u"60", None))
        self.comboBox_spin_x_.setItemText(13, QCoreApplication.translate("MainWindow", u"65", None))
        self.comboBox_spin_x_.setItemText(14, QCoreApplication.translate("MainWindow", u"70", None))
        self.comboBox_spin_x_.setItemText(15, QCoreApplication.translate("MainWindow", u"75", None))
        self.comboBox_spin_x_.setItemText(16, QCoreApplication.translate("MainWindow", u"80", None))
        self.comboBox_spin_x_.setItemText(17, QCoreApplication.translate("MainWindow", u"85", None))
        self.comboBox_spin_x_.setItemText(18, QCoreApplication.translate("MainWindow", u"90", None))

#if QT_CONFIG(tooltip)
        self.lb_stattest_4.setToolTip(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432 \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u0435 -- \u043f\u043e\u0434\u043f\u0438\u0441\u044c \u0441\u043d\u0438\u0437\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u0444\u043e\u043d \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u043c", None))
        self.check_background.setText("")
        self.lb_sd_or_minmax.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439", None))
        self.comboBox_sd_or_minmax.setItemText(0, QCoreApplication.translate("MainWindow", u"SD", None))
        self.comboBox_sd_or_minmax.setItemText(1, QCoreApplication.translate("MainWindow", u"MIN-MAX", None))

        self.lb_bottom_lim.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0438\u0436\u043d\u044e\u044e \u0433\u0440\u0430\u043d\u0438\u0446\u0443", None))
#if QT_CONFIG(tooltip)
        self.bottom_lim.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0447\u0438\u0441\u043b\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Box plot (3)", None))
        self.lb_corr_color_pallete_3.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430", None))
        self.comboBox_color_pal_corr.setItemText(0, QCoreApplication.translate("MainWindow", u"Set1", None))
        self.comboBox_color_pal_corr.setItemText(1, QCoreApplication.translate("MainWindow", u"Set2", None))
        self.comboBox_color_pal_corr.setItemText(2, QCoreApplication.translate("MainWindow", u"Set3", None))
        self.comboBox_color_pal_corr.setItemText(3, QCoreApplication.translate("MainWindow", u"Paired", None))
        self.comboBox_color_pal_corr.setItemText(4, QCoreApplication.translate("MainWindow", u"Accent", None))
        self.comboBox_color_pal_corr.setItemText(5, QCoreApplication.translate("MainWindow", u"Pastel1", None))
        self.comboBox_color_pal_corr.setItemText(6, QCoreApplication.translate("MainWindow", u"Pastel2", None))
        self.comboBox_color_pal_corr.setItemText(7, QCoreApplication.translate("MainWindow", u"Dark2", None))
        self.comboBox_color_pal_corr.setItemText(8, QCoreApplication.translate("MainWindow", u"rocket", None))
        self.comboBox_color_pal_corr.setItemText(9, QCoreApplication.translate("MainWindow", u"mako", None))
        self.comboBox_color_pal_corr.setItemText(10, QCoreApplication.translate("MainWindow", u"flare", None))
        self.comboBox_color_pal_corr.setItemText(11, QCoreApplication.translate("MainWindow", u"crest", None))
        self.comboBox_color_pal_corr.setItemText(12, QCoreApplication.translate("MainWindow", u"viridis", None))
        self.comboBox_color_pal_corr.setItemText(13, QCoreApplication.translate("MainWindow", u"plasma", None))
        self.comboBox_color_pal_corr.setItemText(14, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.comboBox_color_pal_corr.setItemText(15, QCoreApplication.translate("MainWindow", u"magma", None))
        self.comboBox_color_pal_corr.setItemText(16, QCoreApplication.translate("MainWindow", u"cividis", None))
        self.comboBox_color_pal_corr.setItemText(17, QCoreApplication.translate("MainWindow", u"Greys", None))
        self.comboBox_color_pal_corr.setItemText(18, QCoreApplication.translate("MainWindow", u"Reds", None))
        self.comboBox_color_pal_corr.setItemText(19, QCoreApplication.translate("MainWindow", u"Greens", None))
        self.comboBox_color_pal_corr.setItemText(20, QCoreApplication.translate("MainWindow", u"Blues", None))
        self.comboBox_color_pal_corr.setItemText(21, QCoreApplication.translate("MainWindow", u"Oranges", None))
        self.comboBox_color_pal_corr.setItemText(22, QCoreApplication.translate("MainWindow", u"Purples", None))
        self.comboBox_color_pal_corr.setItemText(23, QCoreApplication.translate("MainWindow", u"YlOrRd", None))
        self.comboBox_color_pal_corr.setItemText(24, QCoreApplication.translate("MainWindow", u"tab10", None))
        self.comboBox_color_pal_corr.setItemText(25, QCoreApplication.translate("MainWindow", u"deep", None))
        self.comboBox_color_pal_corr.setItemText(26, QCoreApplication.translate("MainWindow", u"muted", None))
        self.comboBox_color_pal_corr.setItemText(27, QCoreApplication.translate("MainWindow", u"pastel", None))
        self.comboBox_color_pal_corr.setItemText(28, QCoreApplication.translate("MainWindow", u"bright", None))
        self.comboBox_color_pal_corr.setItemText(29, QCoreApplication.translate("MainWindow", u"dark", None))
        self.comboBox_color_pal_corr.setItemText(30, QCoreApplication.translate("MainWindow", u"colorblind", None))
        self.comboBox_color_pal_corr.setItemText(31, QCoreApplication.translate("MainWindow", u"tab20", None))
        self.comboBox_color_pal_corr.setItemText(32, QCoreApplication.translate("MainWindow", u"tab20b", None))
        self.comboBox_color_pal_corr.setItemText(33, QCoreApplication.translate("MainWindow", u"tab20c", None))

#if QT_CONFIG(tooltip)
        self.lb_del_hue_4.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u043a\u043e \u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440. \u041c\u043e\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439.", None))
#endif // QT_CONFIG(tooltip)
        self.lb_del_hue_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0438\u0436\u043d\u044e\u044e \u0433\u0440\u0430\u043d\u0438\u0446\u0443", None))
        self.check_change_corr_fig_down_limit.setText("")
#if QT_CONFIG(tooltip)
        self.lb_del_hue_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u043a\u043e \u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440. \u041c\u043e\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439.", None))
#endif // QT_CONFIG(tooltip)
        self.lb_del_hue_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0438\u0437 \u0433\u0440\u0443\u043f\u043f\u044b", None))
#if QT_CONFIG(tooltip)
        self.del_hue.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lb_del_hue_5.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u043a\u043e \u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440. \u041c\u043e\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439.", None))
#endif // QT_CONFIG(tooltip)
        self.lb_del_hue_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a", None))
        self.lb_color_pal_box_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430", None))
#if QT_CONFIG(tooltip)
        self.check_sort_or_not_corr_figs.setToolTip(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u0444\u043b\u0430\u0436\u043a\u0430 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0431\u0443\u0434\u0435\u0442 \u0442\u0430\u043a\u0438\u043c, \u043a\u0430\u043a\u043e\u0439 \u043e\u043d \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.check_sort_or_not_corr_figs.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0433\u0440\u0443\u043f\u043f\u0435", None))
#if QT_CONFIG(tooltip)
        self.check_setka.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.check_setka.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0442\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.lb_sd_or_minmax_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043f\u043e", None))
        self.comboBox_correlation_figs_matrix.setItemText(0, QCoreApplication.translate("MainWindow", u"pearson", None))
        self.comboBox_correlation_figs_matrix.setItemText(1, QCoreApplication.translate("MainWindow", u"kendall", None))
        self.comboBox_correlation_figs_matrix.setItemText(2, QCoreApplication.translate("MainWindow", u"spearman", None))

        self.lb_sd_or_minmax_7.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u0441\u0445\u0435\u043c\u0430", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(0, QCoreApplication.translate("MainWindow", u"coolwarm", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(1, QCoreApplication.translate("MainWindow", u"RdBu_r", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(2, QCoreApplication.translate("MainWindow", u"YlGn", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(3, QCoreApplication.translate("MainWindow", u"BuGn", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(4, QCoreApplication.translate("MainWindow", u"GnBu", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(5, QCoreApplication.translate("MainWindow", u"bwr", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(6, QCoreApplication.translate("MainWindow", u"seismic", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(7, QCoreApplication.translate("MainWindow", u"PiYG", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(8, QCoreApplication.translate("MainWindow", u"RdGy", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(9, QCoreApplication.translate("MainWindow", u"seismic", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(10, QCoreApplication.translate("MainWindow", u"hot", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(11, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.comboBox_correlation_color_map_for_figs.setItemText(12, QCoreApplication.translate("MainWindow", u"gist_heat", None))

        self.lb_size_corr_matrix.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0440\u0438\u0441\u0443\u043d\u043a\u0430", None))
        self.lb_font_in.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0444 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439", None))
        self.lb_font_out.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430", None))
#if QT_CONFIG(tooltip)
        self.lb_name_of_title.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_name_of_title.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u043c\u0430\u0442\u0440\u0438\u0446\u044b", None))
        self.btn_plot_and_save_figs.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.lb_path_for_profile.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.path_for_profile.setText("")
#if QT_CONFIG(tooltip)
        self.lb_patient_data.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0438\u0437 \u0442\u0430\u0431\u043b\u0438\u0446\u044b, \u0433\u0434\u0435 \u0435\u0441\u0442\u044c 3 \u0441\u0442\u043e\u043b\u0431\u0446\u0430: \u0438\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430, \u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_patient_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.patient_data.setText("")
#if QT_CONFIG(tooltip)
        self.lb_norm_data.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0438\u0437 \u0442\u0430\u0431\u043b\u0438\u0446\u044b, \u0433\u0434\u0435 \u0435\u0441\u0442\u044c 3 \u0441\u0442\u043e\u043b\u0431\u0446\u0430: \u0438\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430, \u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_norm_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043d\u043e\u0440\u043c\u044b", None))
        self.norm_data.setText("")
#if QT_CONFIG(tooltip)
        self.lb_norm_data_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0438\u0437 \u0442\u0430\u0431\u043b\u0438\u0446\u044b, \u0433\u0434\u0435 \u0435\u0441\u0442\u044c 3 \u0441\u0442\u043e\u043b\u0431\u0446\u0430: \u0438\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430, \u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_norm_data_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f", None))
        self.profile_title_rad.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043a\u0440\u043e\u0440\u0435\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430 ", None))
#if QT_CONFIG(tooltip)
        self.lb_norm_data_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0438\u0437 \u0442\u0430\u0431\u043b\u0438\u0446\u044b, \u0433\u0434\u0435 \u0435\u0441\u0442\u044c 3 \u0441\u0442\u043e\u043b\u0431\u0446\u0430: \u0438\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430, \u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_norm_data_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043e\u0441\u0438 \u0434\u043b\u044f \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f", None))
        self.profile_title_lin.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 \u043e\u0442 \u043d\u043e\u0440\u043c\u044b, %", None))
        self.check_profile_legend.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u0435\u043d\u0434\u0430", None))
        self.lb__altern_heposisis_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0430\u0449\u0430\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u0434\u043b\u044f \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f", None))
        self.comboBox_profile_lin_spin.setItemText(0, QCoreApplication.translate("MainWindow", u"90", None))
        self.comboBox_profile_lin_spin.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))

        self.lb_color_pal_box_20.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0446\u0432\u0435\u0442 \u0431\u044b\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX: #......</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430 (HEX)", None))
        self.patient_prof.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0446\u0438\u0435\u043d\u0442", None))
        self.color_for_patient.setText(QCoreApplication.translate("MainWindow", u"#DB4900", None))
        self.check_profile_pat_line.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0438\u044f \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435", None))
        self.check_profile_pat_sd.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u044b", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0446\u0432\u0435\u0442 \u0431\u044b\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX: #......</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u043e\u0440\u043c\u044b (HEX)", None))
        self.norm_prof.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.color_for_norm.setText(QCoreApplication.translate("MainWindow", u"#2A968D", None))
        self.check_profile_norm_line.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0438\u044f \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435", None))
        self.check_profile_norm_sd.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435", None))
        self.btn_plot_and_save_profile.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0440\u043e\u0444\u0438\u043b\u0438", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"1 \u0433\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2 \u0433\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3 \u0433\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043f\u0438\u0441\u044c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u0430", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0438\u043b\u044c \u043b\u0438\u043d\u0438\u0438", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u044f \u044d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u043e\u0432", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u043c\u043e\u0441\u0442\u044c \u044d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u043e\u0432", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u044f \u0442\u0440\u043e\u043c\u0431\u043e\u0446\u0438\u0442\u043e\u0432", None));
        ___qtablewidgetitem10 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"red", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"green", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"blue", None));
        ___qtablewidgetitem13 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"solid", None));
        ___qtablewidgetitem14 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"solid", None));
        ___qtablewidgetitem15 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"solid", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(whatsthis)
        self.tableWidget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0443\u0436\u043d\u043e \u043f\u0438\u0441\u0430\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u0442\u0438\u0440\u0435.</p><p>\u041f\u0440\u0438\u043c\u0435\u0440: 0-3</p><p>\u0426\u0432\u0435\u0442\u0430:  matplotlib.colors</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.lb_norm_data_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0443\u0436\u043d\u043e \u043f\u0438\u0441\u0430\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u0442\u0438\u0440\u0435.</p><p>\u041f\u0440\u0438\u043c\u0435\u0440: 0-3</p><p>\u0426\u0432\u0435\u0442\u0430: matplotlib.colors</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lb_norm_data_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0443\u0436\u043d\u043e \u043f\u0438\u0441\u0430\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u0442\u0438\u0440\u0435.</p><p>\u041f\u0440\u0438\u043c\u0435\u0440: 0-3</p><p>\u0426\u0432\u0435\u0442\u0430: matplotlib.colors</p><p>\u0421\u0442\u0438\u043b\u044c \u043b\u0438\u043d\u0438\u0438: \u0441\u043c. matplotlib </p><p><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#7a7e85;\">solid, dashed, dashdot, dotted</span><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lb_norm_data_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0434\u043b\u044f \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u043d\u044b\u0445 \u0433\u0440\u0443\u043f\u043f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0430 \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u043c \u0433\u0440\u0430\u0444\u0438\u043a\u0435", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.widget2), QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043a\u0440\u043e\u0440\u0435\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.lb_path_for_plot_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443", None))
        self.path_for_pivot_table.setText("")
        self.lb_exel_name_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430", None))
        self.lb_exel_name_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430", None))
#if QT_CONFIG(tooltip)
        self.lb_hue_name_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u0435\u043d\u043d\u043e \u043f\u043e\u0441\u043b\u0435 \u044d\u0442\u043e\u0433\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043e\u043b\u0436\u043d\u044b \u0438\u0434\u0442\u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f", None))
        self.lb_color_pal_box_17.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.lb_color_pal_box_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0433\u043b\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0434\u043e \u0437\u043d\u0430\u043a\u0430 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439", None))
        self.lb_sd_or_minmax_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439", None))
        self.comboBox_sd_or_se_pivot.setItemText(0, QCoreApplication.translate("MainWindow", u"SD", None))
        self.comboBox_sd_or_se_pivot.setItemText(1, QCoreApplication.translate("MainWindow", u"SE", None))

        self.btn_plot_and_save_pivot_table.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0432\u043e\u0434\u043d\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.lb_color_pal_box_18.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u0430", None))
        self.lb_sd_or_minmax_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043f\u043e", None))
        self.comboBox_correlation_person_or_not.setItemText(0, QCoreApplication.translate("MainWindow", u"pearson", None))
        self.comboBox_correlation_person_or_not.setItemText(1, QCoreApplication.translate("MainWindow", u"kendall", None))
        self.comboBox_correlation_person_or_not.setItemText(2, QCoreApplication.translate("MainWindow", u"spearman", None))

        self.lb_sd_or_minmax_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u044f\u0447\u0435\u0439\u043a\u0438 \u0446\u0432\u0435\u0442\u043e\u043c", None))
        self.check_color_for_corr_pivot.setText("")
        self.lb_sd_or_minmax_5.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u0441\u0445\u0435\u043c\u0430", None))
        self.comboBox_correlation_color_map.setItemText(0, QCoreApplication.translate("MainWindow", u"coolwarm", None))
        self.comboBox_correlation_color_map.setItemText(1, QCoreApplication.translate("MainWindow", u"RdBu_r", None))
        self.comboBox_correlation_color_map.setItemText(2, QCoreApplication.translate("MainWindow", u"YlGn", None))
        self.comboBox_correlation_color_map.setItemText(3, QCoreApplication.translate("MainWindow", u"BuGn", None))
        self.comboBox_correlation_color_map.setItemText(4, QCoreApplication.translate("MainWindow", u"GnBu", None))
        self.comboBox_correlation_color_map.setItemText(5, QCoreApplication.translate("MainWindow", u"bwr", None))
        self.comboBox_correlation_color_map.setItemText(6, QCoreApplication.translate("MainWindow", u"seismic", None))
        self.comboBox_correlation_color_map.setItemText(7, QCoreApplication.translate("MainWindow", u"PiYG", None))
        self.comboBox_correlation_color_map.setItemText(8, QCoreApplication.translate("MainWindow", u"RdGy", None))
        self.comboBox_correlation_color_map.setItemText(9, QCoreApplication.translate("MainWindow", u"seismic", None))
        self.comboBox_correlation_color_map.setItemText(10, QCoreApplication.translate("MainWindow", u"hot", None))
        self.comboBox_correlation_color_map.setItemText(11, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.comboBox_correlation_color_map.setItemText(12, QCoreApplication.translate("MainWindow", u"gist_heat", None))

        self.btn_plot_and_save_corr_table.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0443\u044e \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u043f\u043e \u0432\u0441\u0435\u043c \u0434\u0430\u043d\u043d\u044b\u043c", None))
        self.lb_color_pal_box_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u0438\u043d\u0434\u0435\u043a\u0441\u0438\u0440\u0443\u0435\u043c\u044b\u0435/\u043f\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430\u043c", None))
        self.lb_sd_or_minmax_11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.comboBox_index_data_or_raw.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0438\u0437 \u0438\u043d\u0434\u0435\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u0441\u044b\u0440\u044b\u0435", None))
        self.comboBox_index_data_or_raw.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0438\u0437 \u0441\u044b\u0440\u044b\u0445 \u0432 \u0438\u043d\u0434\u0435\u043a\u0441\u0438\u0440\u0443\u0435\u043c\u044b\u0435", None))

        self.btn_save_pivot_or_melt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430", None))
#if QT_CONFIG(tooltip)
        self.lb_path_for_plot_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443", None))
        self.path_for_catplot.setText("")
        self.lb_exel_name_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430", None))
        self.lb_exel_name_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 \u0444\u0430\u0439\u043b\u0435", None))
#if QT_CONFIG(tooltip)
        self.lb_hue_name_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430 \u043f\u043e \u043e\u0441\u0438 x", None))
#if QT_CONFIG(tooltip)
        self.lb_hue_name_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_7.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442", None))
        self.comboBox_catplot_form_x.setItemText(0, QCoreApplication.translate("MainWindow", u"str", None))
        self.comboBox_catplot_form_x.setItemText(1, QCoreApplication.translate("MainWindow", u"int", None))
        self.comboBox_catplot_form_x.setItemText(2, QCoreApplication.translate("MainWindow", u"float", None))
        self.comboBox_catplot_form_x.setItemText(3, QCoreApplication.translate("MainWindow", u"bool", None))
        self.comboBox_catplot_form_x.setItemText(4, QCoreApplication.translate("MainWindow", u"default", None))

#if QT_CONFIG(tooltip)
        self.lb_hue_name_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u043e \u043e\u0441\u0438 y", None))
#if QT_CONFIG(tooltip)
        self.lb_hue_name_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_6.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442", None))
        self.comboBox_catplot_form_y.setItemText(0, QCoreApplication.translate("MainWindow", u"float", None))
        self.comboBox_catplot_form_y.setItemText(1, QCoreApplication.translate("MainWindow", u"int", None))
        self.comboBox_catplot_form_y.setItemText(2, QCoreApplication.translate("MainWindow", u"str", None))
        self.comboBox_catplot_form_y.setItemText(3, QCoreApplication.translate("MainWindow", u"bool", None))
        self.comboBox_catplot_form_y.setItemText(4, QCoreApplication.translate("MainWindow", u"default", None))

#if QT_CONFIG(tooltip)
        self.lb_hue_name_5.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0433\u0440\u0443\u043f\u043f\u0430", None))
#if QT_CONFIG(tooltip)
        self.lb_hue_name_8.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_8.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442", None))
        self.comboBox_catplot_form_hue.setItemText(0, QCoreApplication.translate("MainWindow", u"str", None))
        self.comboBox_catplot_form_hue.setItemText(1, QCoreApplication.translate("MainWindow", u"int", None))
        self.comboBox_catplot_form_hue.setItemText(2, QCoreApplication.translate("MainWindow", u"float", None))
        self.comboBox_catplot_form_hue.setItemText(3, QCoreApplication.translate("MainWindow", u"bool", None))
        self.comboBox_catplot_form_hue.setItemText(4, QCoreApplication.translate("MainWindow", u"default", None))

        self.lb_color_pal_box_14.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.lb_color_pal_box_16.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430", None))
        self.comboBox_color_catplot.setItemText(0, QCoreApplication.translate("MainWindow", u"Pastel1", None))
        self.comboBox_color_catplot.setItemText(1, QCoreApplication.translate("MainWindow", u"Pastel2", None))
        self.comboBox_color_catplot.setItemText(2, QCoreApplication.translate("MainWindow", u"Set1", None))
        self.comboBox_color_catplot.setItemText(3, QCoreApplication.translate("MainWindow", u"Set2", None))
        self.comboBox_color_catplot.setItemText(4, QCoreApplication.translate("MainWindow", u"Set3", None))
        self.comboBox_color_catplot.setItemText(5, QCoreApplication.translate("MainWindow", u"Paired", None))
        self.comboBox_color_catplot.setItemText(6, QCoreApplication.translate("MainWindow", u"Accent", None))
        self.comboBox_color_catplot.setItemText(7, QCoreApplication.translate("MainWindow", u"Dark2", None))
        self.comboBox_color_catplot.setItemText(8, QCoreApplication.translate("MainWindow", u"rocket", None))
        self.comboBox_color_catplot.setItemText(9, QCoreApplication.translate("MainWindow", u"mako", None))
        self.comboBox_color_catplot.setItemText(10, QCoreApplication.translate("MainWindow", u"flare", None))
        self.comboBox_color_catplot.setItemText(11, QCoreApplication.translate("MainWindow", u"crest", None))
        self.comboBox_color_catplot.setItemText(12, QCoreApplication.translate("MainWindow", u"viridis", None))
        self.comboBox_color_catplot.setItemText(13, QCoreApplication.translate("MainWindow", u"plasma", None))
        self.comboBox_color_catplot.setItemText(14, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.comboBox_color_catplot.setItemText(15, QCoreApplication.translate("MainWindow", u"magma", None))
        self.comboBox_color_catplot.setItemText(16, QCoreApplication.translate("MainWindow", u"cividis", None))
        self.comboBox_color_catplot.setItemText(17, QCoreApplication.translate("MainWindow", u"Greys", None))
        self.comboBox_color_catplot.setItemText(18, QCoreApplication.translate("MainWindow", u"Reds", None))
        self.comboBox_color_catplot.setItemText(19, QCoreApplication.translate("MainWindow", u"Greens", None))
        self.comboBox_color_catplot.setItemText(20, QCoreApplication.translate("MainWindow", u"Blues", None))
        self.comboBox_color_catplot.setItemText(21, QCoreApplication.translate("MainWindow", u"Oranges", None))
        self.comboBox_color_catplot.setItemText(22, QCoreApplication.translate("MainWindow", u"Purples", None))
        self.comboBox_color_catplot.setItemText(23, QCoreApplication.translate("MainWindow", u"YlOrRd", None))
        self.comboBox_color_catplot.setItemText(24, QCoreApplication.translate("MainWindow", u"tab10", None))
        self.comboBox_color_catplot.setItemText(25, QCoreApplication.translate("MainWindow", u"deep", None))
        self.comboBox_color_catplot.setItemText(26, QCoreApplication.translate("MainWindow", u"muted", None))
        self.comboBox_color_catplot.setItemText(27, QCoreApplication.translate("MainWindow", u"pastel", None))
        self.comboBox_color_catplot.setItemText(28, QCoreApplication.translate("MainWindow", u"bright", None))
        self.comboBox_color_catplot.setItemText(29, QCoreApplication.translate("MainWindow", u"dark", None))
        self.comboBox_color_catplot.setItemText(30, QCoreApplication.translate("MainWindow", u"colorblind", None))
        self.comboBox_color_catplot.setItemText(31, QCoreApplication.translate("MainWindow", u"tab20", None))
        self.comboBox_color_catplot.setItemText(32, QCoreApplication.translate("MainWindow", u"tab20b", None))
        self.comboBox_color_catplot.setItemText(33, QCoreApplication.translate("MainWindow", u"tab20c", None))

#if QT_CONFIG(tooltip)
        self.lb_stattest_6.setToolTip(QCoreApplication.translate("MainWindow", u"\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c?", None))
        self.check_stat_znachimost_catplot.setText("")
#if QT_CONFIG(tooltip)
        self.lb_stattest_5.setToolTip(QCoreApplication.translate("MainWindow", u"\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442", None))
        self.comboBox_stat_test_catplot.setItemText(0, QCoreApplication.translate("MainWindow", u"Brunner-Munzel", None))
        self.comboBox_stat_test_catplot.setItemText(1, QCoreApplication.translate("MainWindow", u"Levene", None))
        self.comboBox_stat_test_catplot.setItemText(2, QCoreApplication.translate("MainWindow", u"Mann-Whitney", None))
        self.comboBox_stat_test_catplot.setItemText(3, QCoreApplication.translate("MainWindow", u"Mann-Whitney-gt", None))
        self.comboBox_stat_test_catplot.setItemText(4, QCoreApplication.translate("MainWindow", u"Mann-Whitney-ls", None))
        self.comboBox_stat_test_catplot.setItemText(5, QCoreApplication.translate("MainWindow", u"t-test_ind", None))
        self.comboBox_stat_test_catplot.setItemText(6, QCoreApplication.translate("MainWindow", u"t-test_welch", None))
        self.comboBox_stat_test_catplot.setItemText(7, QCoreApplication.translate("MainWindow", u"t-test_paired", None))
        self.comboBox_stat_test_catplot.setItemText(8, QCoreApplication.translate("MainWindow", u"Wilcoxon", None))
        self.comboBox_stat_test_catplot.setItemText(9, QCoreApplication.translate("MainWindow", u"Kruskal", None))

#if QT_CONFIG(tooltip)
        self.lb_stattest_9.setToolTip(QCoreApplication.translate("MainWindow", u"\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_9.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442 \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439 \u0434\u043b\u044f \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438", None))
        self.comboBox_catplot_stat_formatt.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 p", None))
        self.comboBox_catplot_stat_formatt.setItemText(1, QCoreApplication.translate("MainWindow", u"*", None))
        self.comboBox_catplot_stat_formatt.setItemText(2, QCoreApplication.translate("MainWindow", u"\u043f\u043e\u043b\u043d\u044b\u0439", None))

#if QT_CONFIG(tooltip)
        self.lb_stattest_10.setToolTip(QCoreApplication.translate("MainWindow", u"\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043f\u0440\u0430\u0432\u043a\u0430 \u043d\u0430 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0443\u044e \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443 \u0433\u0438\u043f\u043e\u0442\u0435\u0437", None))
        self.comboBox_catplot_mult_stat.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_catplot_mult_stat.setItemText(1, QCoreApplication.translate("MainWindow", u"bonferroni", None))
        self.comboBox_catplot_mult_stat.setItemText(2, QCoreApplication.translate("MainWindow", u"holm-bonferroni", None))
        self.comboBox_catplot_mult_stat.setItemText(3, QCoreApplication.translate("MainWindow", u"benjamini-hochberg", None))
        self.comboBox_catplot_mult_stat.setItemText(4, QCoreApplication.translate("MainWindow", u"Benjamini-Yekutieli", None))

#if QT_CONFIG(tooltip)
        self.lb_stattest_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0441\u043c. seaborn catplot</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_7.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.comboBox_template_catplot.setItemText(0, QCoreApplication.translate("MainWindow", u"bar", None))
        self.comboBox_template_catplot.setItemText(1, QCoreApplication.translate("MainWindow", u"box", None))
        self.comboBox_template_catplot.setItemText(2, QCoreApplication.translate("MainWindow", u"strip", None))
        self.comboBox_template_catplot.setItemText(3, QCoreApplication.translate("MainWindow", u"swarm", None))
        self.comboBox_template_catplot.setItemText(4, QCoreApplication.translate("MainWindow", u"violin", None))
        self.comboBox_template_catplot.setItemText(5, QCoreApplication.translate("MainWindow", u"boxen", None))
        self.comboBox_template_catplot.setItemText(6, QCoreApplication.translate("MainWindow", u"point", None))

#if QT_CONFIG(tooltip)
        self.lb_color_pal_box_15.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.lb_color_pal_box_15.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0438", None))
        self.comboBox_catplot_SD_or_not.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435", None))
        self.comboBox_catplot_SD_or_not.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0448\u0438\u0431\u043a\u0430", None))
        self.comboBox_catplot_SD_or_not.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b", None))
        self.comboBox_catplot_SD_or_not.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0446\u0435\u043d\u0442\u0438\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b", None))

        self.btn_plot_and_save_catplot.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Catplot", None))
#if QT_CONFIG(tooltip)
        self.lb_path_for_plot_7.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f excel \u0444\u0430\u0439\u043b\u044b \u0438\u043b\u0438 \u0444\u0430\u0439\u043b. \u0415\u0441\u043b\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u043e\u0434\u043d\u043e\u043c \u0444\u0430\u0439\u043b\u0435, \u0442\u043e \u043d\u0443\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e. ", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_7.setText(QCoreApplication.translate("MainWindow", u"RheoScan - \u0440\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0440\u0435\u0434\u043d\u0438\u0435 \u0438 SD \u043f\u043e \u0444\u0430\u0439\u043b\u0443 \u0438\u043b\u0438 \u0444\u0430\u0439\u043b\u0430\u043c", None))
#if QT_CONFIG(tooltip)
        self.lb_path_for_plot_5.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f excel \u0444\u0430\u0439\u043b\u044b \u0438\u043b\u0438 \u0444\u0430\u0439\u043b. \u0415\u0441\u043b\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u043e\u0434\u043d\u043e\u043c \u0444\u0430\u0439\u043b\u0435, \u0442\u043e \u043d\u0443\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e. ", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443 \u0438\u043b\u0438 \u0444\u0430\u0439\u043b\u0430\u043c", None))
        self.path_for_RheoScan_describe.setText("")
#if QT_CONFIG(tooltip)
        self.lb_stattest_12.setToolTip(QCoreApplication.translate("MainWindow", u"\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.comboBox_RheoScan_describe.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041e\u0434\u0438\u043d \u0444\u0430\u0439\u043b - \u043e\u0434\u0438\u043d \u043e\u0431\u0440\u0430\u0437\u0435\u0446", None))
        self.comboBox_RheoScan_describe.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0434\u0438\u043d \u0444\u0430\u0439\u043b - \u043c\u043d\u043e\u0433\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432", None))

#if QT_CONFIG(tooltip)
        self.lb_path_for_plot_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lb_path_for_plot_6.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b\u044b \u043d\u0430\u043f\u0438\u0441\u0430\u0442\u044c True \u0438\u043b\u0438 False, \u0438\u043b\u0438 \u0436\u0435 0, 1, \u0442\u0435\u043c \u0441\u0430\u043c\u044b\u043c \u043f\u043e\u043c\u0435\u0442\u0438\u0432 \u043b\u0438\u0441\u0442\u044b.", None))
#endif // QT_CONFIG(statustip)
        self.lb_path_for_plot_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 SD \u043d\u0430 \u0440\u0430\u0437\u043d\u044b\u0445 \u043b\u0438\u0441\u0442\u0430\u0445", None))
        self.RheoScan_describe_mask_sheets.setText("")
        self.btn_RheoScan_describe_file_or_files.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u0441\u0432\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u0444\u0430\u0439\u043b\u0443 \u0438\u043b\u0438 \u0444\u0430\u0439\u043b\u0430\u043c", None))
#if QT_CONFIG(tooltip)
        self.lb_path_for_plot_8.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f excel \u0444\u0430\u0439\u043b\u044b \u0438\u043b\u0438 \u0444\u0430\u0439\u043b. \u0415\u0441\u043b\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u043e\u0434\u043d\u043e\u043c \u0444\u0430\u0439\u043b\u0435, \u0442\u043e \u043d\u0443\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e. ", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_8.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u043c\u0435\u0436\u0434\u0443 2 \u0432\u044b\u0431\u043e\u0440\u043a\u0430\u043c\u0438", None))
#if QT_CONFIG(tooltip)
        self.lb_path_for_plot_4.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443", None))
        self.path_for_dop_stat.setText("")
        self.lb_exel_name_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430", None))
        self.lb_exel_name_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 \u0444\u0430\u0439\u043b\u0435", None))
#if QT_CONFIG(tooltip)
        self.lb_hue_name_9.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430", None))
#if QT_CONFIG(tooltip)
        self.lb_hue_name_10.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430", None))
#if QT_CONFIG(tooltip)
        self.lb_stattest_8.setToolTip(QCoreApplication.translate("MainWindow", u"\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None))
#endif // QT_CONFIG(tooltip)
        self.lb_stattest_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442", None))
        self.comboBox_stat_test_dop_stat.setItemText(0, QCoreApplication.translate("MainWindow", u"U-\u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041c\u0430\u043d\u043d\u0430 \u2014 \u0423\u0438\u0442\u043d\u0438", None))
        self.comboBox_stat_test_dop_stat.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422-\u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0421\u0442\u044c\u044e\u0434\u0435\u043d\u0442\u0430", None))
        self.comboBox_stat_test_dop_stat.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f", None))
        self.comboBox_stat_test_dop_stat.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f (normal)", None))
        self.comboBox_stat_test_dop_stat.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0423\u0438\u043b\u043a\u043e\u043a\u0441\u043e\u043d\u0430", None))
        self.comboBox_stat_test_dop_stat.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041a\u0440\u0430\u0441\u043a\u0435\u043b\u0430 \u2014 \u0423\u043e\u043b\u043b\u0438\u0441\u0430", None))
        self.comboBox_stat_test_dop_stat.setItemText(6, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0430\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439", None))
        self.comboBox_stat_test_dop_stat.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0410\u043d\u0441\u0430\u0440\u0438-\u0411\u0440\u044d\u0434\u043b\u0438", None))
        self.comboBox_stat_test_dop_stat.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0424\u0438\u0448\u0435\u0440\u0430-\u041f\u0438\u0442\u043c\u0430\u043d\u0430", None))
        self.comboBox_stat_test_dop_stat.setItemText(9, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f", None))
        self.comboBox_stat_test_dop_stat.setItemText(10, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041c\u0430\u043d\u043d\u0430 \u2014 \u0423\u0438\u0442\u043d\u0438", None))
        self.comboBox_stat_test_dop_stat.setItemText(11, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0423\u0438\u043b\u043a\u043e\u043a\u0441\u043e\u043d\u0430", None))
        self.comboBox_stat_test_dop_stat.setItemText(12, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0424\u0440\u0438\u0434\u043c\u0430\u043d\u0430", None))

        self.lb__altern_heposisis_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u0433\u0438\u043f\u043e\u0442\u0435\u0437\u0430", None))
        self.comboBox_alter_hep_dop_stat.setItemText(0, QCoreApplication.translate("MainWindow", u"two-sided", None))
        self.comboBox_alter_hep_dop_stat.setItemText(1, QCoreApplication.translate("MainWindow", u"less", None))
        self.comboBox_alter_hep_dop_stat.setItemText(2, QCoreApplication.translate("MainWindow", u"greater", None))

#if QT_CONFIG(tooltip)
        self.lb_hue_name_11.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_11.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 p:", None))
        self.p_value_dop_stat.setText("")
        self.btn_dop_stat_calc.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f. \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.Lab_stuff.setTabText(self.Lab_stuff.indexOf(self.tabWidgetPage4), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
    # retranslateUi

