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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(709, 649)
        icon = QIcon()
        icon.addFile(u"LOGO.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
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
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.Lab_stuff.setFont(font)
        self.Lab_stuff.setStyleSheet(u"/*background-color: rgb(249, 249, 249);")
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.gridLayout_5 = QGridLayout(self.tabWidgetPage1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_3 = QFrame(self.tabWidgetPage1)
        self.line_3.setObjectName(u"line_3")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.line_3.setFont(font1)
        self.line_3.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_3, 6, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.dfd = QFrame(self.tabWidgetPage1)
        self.dfd.setObjectName(u"dfd")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dfd.sizePolicy().hasHeightForWidth())
        self.dfd.setSizePolicy(sizePolicy)
        self.dfd.setStyleSheet(u"QFrame#dfd{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.dfd)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.check_approx_agg = QCheckBox(self.dfd)
        self.check_approx_agg.setObjectName(u"check_approx_agg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.check_approx_agg.sizePolicy().hasHeightForWidth())
        self.check_approx_agg.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        self.check_approx_agg.setFont(font2)
        self.check_approx_agg.setChecked(False)

        self.verticalLayout_5.addWidget(self.check_approx_agg)

        self.check_figs_for_agg = QCheckBox(self.dfd)
        self.check_figs_for_agg.setObjectName(u"check_figs_for_agg")
        self.check_figs_for_agg.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.check_figs_for_agg.sizePolicy().hasHeightForWidth())
        self.check_figs_for_agg.setSizePolicy(sizePolicy1)
        self.check_figs_for_agg.setFont(font2)

        self.verticalLayout_5.addWidget(self.check_figs_for_agg)


        self.horizontalLayout_4.addWidget(self.dfd)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(50, -1, -1, 10)
        self.label_2 = QLabel(self.tabWidgetPage1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.tabWidgetPage1)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tua_1_agg = QLineEdit(self.tabWidgetPage1)
        self.tua_1_agg.setObjectName(u"tua_1_agg")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tua_1_agg.sizePolicy().hasHeightForWidth())
        self.tua_1_agg.setSizePolicy(sizePolicy3)
        self.tua_1_agg.setFont(font2)

        self.verticalLayout.addWidget(self.tua_1_agg)

        self.tau_2_agg = QLineEdit(self.tabWidgetPage1)
        self.tau_2_agg.setObjectName(u"tau_2_agg")
        sizePolicy3.setHeightForWidth(self.tau_2_agg.sizePolicy().hasHeightForWidth())
        self.tau_2_agg.setSizePolicy(sizePolicy3)
        self.tau_2_agg.setFont(font2)

        self.verticalLayout.addWidget(self.tau_2_agg)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_path = QLabel(self.tabWidgetPage1)
        self.lb_path.setObjectName(u"lb_path")
        self.lb_path.setFont(font2)

        self.horizontalLayout_7.addWidget(self.lb_path)

        self.main_path = QLineEdit(self.tabWidgetPage1)
        self.main_path.setObjectName(u"main_path")
        font3 = QFont()
        font3.setPointSize(11)
        self.main_path.setFont(font3)

        self.horizontalLayout_7.addWidget(self.main_path)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qwe = QFrame(self.tabWidgetPage1)
        self.qwe.setObjectName(u"qwe")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.qwe.sizePolicy().hasHeightForWidth())
        self.qwe.setSizePolicy(sizePolicy4)
        self.qwe.setStyleSheet(u"QFrame#qwe{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.qwe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.check_approx_deform = QCheckBox(self.qwe)
        self.check_approx_deform.setObjectName(u"check_approx_deform")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.check_approx_deform.sizePolicy().hasHeightForWidth())
        self.check_approx_deform.setSizePolicy(sizePolicy5)
        self.check_approx_deform.setFont(font2)

        self.verticalLayout_2.addWidget(self.check_approx_deform)

        self.check_for_deform = QCheckBox(self.qwe)
        self.check_for_deform.setObjectName(u"check_for_deform")
        self.check_for_deform.setEnabled(False)
        self.check_for_deform.setFont(font2)

        self.verticalLayout_2.addWidget(self.check_for_deform)


        self.horizontalLayout_2.addWidget(self.qwe)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.label_6 = QLabel(self.tabWidgetPage1)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setFont(font2)

        self.horizontalLayout.addWidget(self.label_6)

        self.r2_def = QLineEdit(self.tabWidgetPage1)
        self.r2_def.setObjectName(u"r2_def")
        sizePolicy3.setHeightForWidth(self.r2_def.sizePolicy().hasHeightForWidth())
        self.r2_def.setSizePolicy(sizePolicy3)
        self.r2_def.setFont(font2)

        self.horizontalLayout.addWidget(self.r2_def)


        self.verticalLayout_32.addLayout(self.horizontalLayout)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_18 = QLabel(self.tabWidgetPage1)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setFont(font2)

        self.horizontalLayout_65.addWidget(self.label_18)

        self.spinBox_n_max_deform = QSpinBox(self.tabWidgetPage1)
        self.spinBox_n_max_deform.setObjectName(u"spinBox_n_max_deform")
        self.spinBox_n_max_deform.setFont(font3)
        self.spinBox_n_max_deform.setMinimum(3)
        self.spinBox_n_max_deform.setMaximum(13)
        self.spinBox_n_max_deform.setValue(10)

        self.horizontalLayout_65.addWidget(self.spinBox_n_max_deform)


        self.verticalLayout_32.addLayout(self.horizontalLayout_65)


        self.horizontalLayout_2.addLayout(self.verticalLayout_32)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(13, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.line_4 = QFrame(self.tabWidgetPage1)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFont(font1)
        self.line_4.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_4, 11, 0, 1, 1)

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
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.btn_save_exel_csv.setFont(font4)
        self.btn_save_exel_csv.setAutoFillBackground(False)
        self.btn_save_exel_csv.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")
        self.btn_save_exel_csv.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_save_exel_csv, 12, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.check_save_exel = QCheckBox(self.tabWidgetPage1)
        self.check_save_exel.setObjectName(u"check_save_exel")
        self.check_save_exel.setFont(font2)
        self.check_save_exel.setChecked(True)

        self.horizontalLayout_8.addWidget(self.check_save_exel)

        self.check_save_csv = QCheckBox(self.tabWidgetPage1)
        self.check_save_csv.setObjectName(u"check_save_csv")
        self.check_save_csv.setFont(font2)

        self.horizontalLayout_8.addWidget(self.check_save_csv)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 10, 0, 1, 1)

        self.line = QFrame(self.tabWidgetPage1)
        self.line.setObjectName(u"line")
        self.line.setFont(font1)
        self.line.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line, 9, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_separator = QLabel(self.tabWidgetPage1)
        self.lb_separator.setObjectName(u"lb_separator")
        sizePolicy2.setHeightForWidth(self.lb_separator.sizePolicy().hasHeightForWidth())
        self.lb_separator.setSizePolicy(sizePolicy2)
        self.lb_separator.setFont(font2)

        self.horizontalLayout_5.addWidget(self.lb_separator)

        self.separator_for_data = QLineEdit(self.tabWidgetPage1)
        self.separator_for_data.setObjectName(u"separator_for_data")
        sizePolicy3.setHeightForWidth(self.separator_for_data.sizePolicy().hasHeightForWidth())
        self.separator_for_data.setSizePolicy(sizePolicy3)
        self.separator_for_data.setFont(font3)
        self.separator_for_data.setToolTipDuration(4)
        self.separator_for_data.setAutoFillBackground(False)

        self.horizontalLayout_5.addWidget(self.separator_for_data)

        self.label = QLabel(self.tabWidgetPage1)
        self.label.setObjectName(u"label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)
        self.label.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label)

        self.spinBox_level = QSpinBox(self.tabWidgetPage1)
        self.spinBox_level.setObjectName(u"spinBox_level")
        sizePolicy3.setHeightForWidth(self.spinBox_level.sizePolicy().hasHeightForWidth())
        self.spinBox_level.setSizePolicy(sizePolicy3)
        self.spinBox_level.setFont(font2)
        self.spinBox_level.setMinimum(1)
        self.spinBox_level.setMaximum(5)
        self.spinBox_level.setValue(1)

        self.horizontalLayout_5.addWidget(self.spinBox_level)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.check_stat_for_column = QCheckBox(self.tabWidgetPage1)
        self.check_stat_for_column.setObjectName(u"check_stat_for_column")
        self.check_stat_for_column.setFont(font2)

        self.horizontalLayout_27.addWidget(self.check_stat_for_column)

        self.vibros_delete = QCheckBox(self.tabWidgetPage1)
        self.vibros_delete.setObjectName(u"vibros_delete")
        self.vibros_delete.setFont(font2)
        self.vibros_delete.setChecked(False)

        self.horizontalLayout_27.addWidget(self.vibros_delete)

        self.iqr_vibros = QDoubleSpinBox(self.tabWidgetPage1)
        self.iqr_vibros.setObjectName(u"iqr_vibros")
        self.iqr_vibros.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.iqr_vibros.sizePolicy().hasHeightForWidth())
        self.iqr_vibros.setSizePolicy(sizePolicy3)
        self.iqr_vibros.setFont(font3)
        self.iqr_vibros.setDecimals(1)
        self.iqr_vibros.setMinimum(0.500000000000000)
        self.iqr_vibros.setMaximum(5.000000000000000)
        self.iqr_vibros.setSingleStep(0.500000000000000)
        self.iqr_vibros.setValue(1.500000000000000)

        self.horizontalLayout_27.addWidget(self.iqr_vibros)

        self.label_11 = QLabel(self.tabWidgetPage1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(False)
        self.label_11.setFont(font3)

        self.horizontalLayout_27.addWidget(self.label_11)


        self.gridLayout_3.addLayout(self.horizontalLayout_27, 7, 0, 1, 1)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(-1, -1, 0, -1)
        self.vbn = QFrame(self.tabWidgetPage1)
        self.vbn.setObjectName(u"vbn")
        sizePolicy2.setHeightForWidth(self.vbn.sizePolicy().hasHeightForWidth())
        self.vbn.setSizePolicy(sizePolicy2)
        self.vbn.setAutoFillBackground(False)
        self.vbn.setStyleSheet(u"QFrame#vbn{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.vbn)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.check_agg = QCheckBox(self.vbn)
        self.check_agg.setObjectName(u"check_agg")
        self.check_agg.setFont(font2)
        self.check_agg.setChecked(True)

        self.verticalLayout_4.addWidget(self.check_agg)

        self.check_stress = QCheckBox(self.vbn)
        self.check_stress.setObjectName(u"check_stress")
        self.check_stress.setFont(font2)
        self.check_stress.setChecked(True)

        self.verticalLayout_4.addWidget(self.check_stress)

        self.check_deform = QCheckBox(self.vbn)
        self.check_deform.setObjectName(u"check_deform")
        self.check_deform.setFont(font2)
        self.check_deform.setChecked(True)

        self.verticalLayout_4.addWidget(self.check_deform)


        self.horizontalLayout_71.addWidget(self.vbn, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_3)

        self.btn_sort_data_RheoScan = QPushButton(self.tabWidgetPage1)
        self.btn_sort_data_RheoScan.setObjectName(u"btn_sort_data_RheoScan")
        sizePolicy3.setHeightForWidth(self.btn_sort_data_RheoScan.sizePolicy().hasHeightForWidth())
        self.btn_sort_data_RheoScan.setSizePolicy(sizePolicy3)
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
        self.btn_sort_data_RheoScan.setFont(font4)
        self.btn_sort_data_RheoScan.setAutoFillBackground(False)
        self.btn_sort_data_RheoScan.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")
        self.btn_sort_data_RheoScan.setFlat(False)

        self.horizontalLayout_71.addWidget(self.btn_sort_data_RheoScan, 0, Qt.AlignLeft)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_71, 3, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.Lab_stuff.addTab(self.tabWidgetPage1, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.formLayout_2 = QFormLayout(self.tab_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.vvvv = QFrame(self.tab_5)
        self.vvvv.setObjectName(u"vvvv")
        sizePolicy.setHeightForWidth(self.vvvv.sizePolicy().hasHeightForWidth())
        self.vvvv.setSizePolicy(sizePolicy)
        self.vvvv.setStyleSheet(u"QFrame#vvvv{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.vvv = QHBoxLayout(self.vvvv)
        self.vvv.setObjectName(u"vvv")
        self.vvv.setContentsMargins(5, 5, 5, 5)
        self.label_15 = QLabel(self.vvvv)
        self.label_15.setObjectName(u"label_15")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy7)
        self.label_15.setFont(font3)

        self.vvv.addWidget(self.label_15)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_16 = QLabel(self.vvvv)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.label_16)

        self.spinBox_biola_born_odd = QSpinBox(self.vvvv)
        self.spinBox_biola_born_odd.setObjectName(u"spinBox_biola_born_odd")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.spinBox_biola_born_odd.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_born_odd.setSizePolicy(sizePolicy8)
        self.spinBox_biola_born_odd.setFont(font3)
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
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.label_17)

        self.spinBox_biola_fluc_odd = QSpinBox(self.vvvv)
        self.spinBox_biola_fluc_odd.setObjectName(u"spinBox_biola_fluc_odd")
        sizePolicy8.setHeightForWidth(self.spinBox_biola_fluc_odd.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_fluc_odd.setSizePolicy(sizePolicy8)
        self.spinBox_biola_fluc_odd.setFont(font3)
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
        sizePolicy.setHeightForWidth(self.lll.sizePolicy().hasHeightForWidth())
        self.lll.setSizePolicy(sizePolicy)
        self.lll.setStyleSheet(u"QFrame#lll{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.horizontalLayout_44 = QHBoxLayout(self.lll)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(self.lll)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)
        self.label_12.setFont(font3)

        self.horizontalLayout_44.addWidget(self.label_12)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_13 = QLabel(self.lll)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.label_13)

        self.spinBox_biola_born = QSpinBox(self.lll)
        self.spinBox_biola_born.setObjectName(u"spinBox_biola_born")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.spinBox_biola_born.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_born.setSizePolicy(sizePolicy9)
        self.spinBox_biola_born.setFont(font3)
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
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setFont(font3)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_14)

        self.spinBox_biola_fluc = QSpinBox(self.lll)
        self.spinBox_biola_fluc.setObjectName(u"spinBox_biola_fluc")
        sizePolicy8.setHeightForWidth(self.spinBox_biola_fluc.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_fluc.setSizePolicy(sizePolicy8)
        self.spinBox_biola_fluc.setFont(font3)
        self.spinBox_biola_fluc.setMinimum(1)
        self.spinBox_biola_fluc.setMaximum(201)
        self.spinBox_biola_fluc.setSingleStep(2)
        self.spinBox_biola_fluc.setValue(61)

        self.horizontalLayout_43.addWidget(self.spinBox_biola_fluc)


        self.verticalLayout_22.addLayout(self.horizontalLayout_43)


        self.horizontalLayout_44.addLayout(self.verticalLayout_22)


        self.verticalLayout_31.addWidget(self.lll)


        self.formLayout_2.setLayout(3, QFormLayout.LabelRole, self.verticalLayout_31)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.btn_biola = QPushButton(self.tab_5)
        self.btn_biola.setObjectName(u"btn_biola")
        self.btn_biola.setFont(font3)
        self.btn_biola.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.horizontalLayout_74.addWidget(self.btn_biola)

        self.btn_biola_concentration = QPushButton(self.tab_5)
        self.btn_biola_concentration.setObjectName(u"btn_biola_concentration")
        self.btn_biola_concentration.setFont(font3)
        self.btn_biola_concentration.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.horizontalLayout_74.addWidget(self.btn_biola_concentration)


        self.formLayout_2.setLayout(5, QFormLayout.LabelRole, self.horizontalLayout_74)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.lb_path_2 = QLabel(self.tab_5)
        self.lb_path_2.setObjectName(u"lb_path_2")
        sizePolicy.setHeightForWidth(self.lb_path_2.sizePolicy().hasHeightForWidth())
        self.lb_path_2.setSizePolicy(sizePolicy)
        self.lb_path_2.setFont(font2)

        self.horizontalLayout_40.addWidget(self.lb_path_2)

        self.path_for_biola = QLineEdit(self.tab_5)
        self.path_for_biola.setObjectName(u"path_for_biola")
        self.path_for_biola.setFont(font3)

        self.horizontalLayout_40.addWidget(self.path_for_biola)


        self.formLayout_2.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_40)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.lb_path_3 = QLabel(self.tab_5)
        self.lb_path_3.setObjectName(u"lb_path_3")
        sizePolicy6.setHeightForWidth(self.lb_path_3.sizePolicy().hasHeightForWidth())
        self.lb_path_3.setSizePolicy(sizePolicy6)
        self.lb_path_3.setFont(font2)
        self.lb_path_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.lb_path_3)

        self.comboBox_biola = QComboBox(self.tab_5)
        self.comboBox_biola.setObjectName(u"comboBox_biola")
        sizePolicy.setHeightForWidth(self.comboBox_biola.sizePolicy().hasHeightForWidth())
        self.comboBox_biola.setSizePolicy(sizePolicy)
        self.comboBox_biola.setFont(font3)

        self.horizontalLayout_41.addWidget(self.comboBox_biola)


        self.horizontalLayout_73.addLayout(self.horizontalLayout_41)


        self.formLayout_2.setLayout(1, QFormLayout.SpanningRole, self.horizontalLayout_73)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.lb_path_16 = QLabel(self.tab_5)
        self.lb_path_16.setObjectName(u"lb_path_16")
        sizePolicy6.setHeightForWidth(self.lb_path_16.sizePolicy().hasHeightForWidth())
        self.lb_path_16.setSizePolicy(sizePolicy6)
        self.lb_path_16.setFont(font2)
        self.lb_path_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_72.addWidget(self.lb_path_16)

        self.comboBox_biola_concentration = QComboBox(self.tab_5)
        self.comboBox_biola_concentration.setObjectName(u"comboBox_biola_concentration")
        sizePolicy.setHeightForWidth(self.comboBox_biola_concentration.sizePolicy().hasHeightForWidth())
        self.comboBox_biola_concentration.setSizePolicy(sizePolicy)
        self.comboBox_biola_concentration.setFont(font3)

        self.horizontalLayout_72.addWidget(self.comboBox_biola_concentration)


        self.formLayout_2.setLayout(2, QFormLayout.SpanningRole, self.horizontalLayout_72)

        self.plp = QFrame(self.tab_5)
        self.plp.setObjectName(u"plp")
        sizePolicy.setHeightForWidth(self.plp.sizePolicy().hasHeightForWidth())
        self.plp.setSizePolicy(sizePolicy)
        self.plp.setStyleSheet(u"QFrame#plp{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.plp)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(6, 6, 6, 6)
        self.lb_color_pal_box_13 = QLabel(self.plp)
        self.lb_color_pal_box_13.setObjectName(u"lb_color_pal_box_13")
        sizePolicy8.setHeightForWidth(self.lb_color_pal_box_13.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_13.setSizePolicy(sizePolicy8)
        font5 = QFont()
        font5.setPointSize(11)
        font5.setUnderline(True)
        self.lb_color_pal_box_13.setFont(font5)
        self.lb_color_pal_box_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.lb_color_pal_box_13)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.lb_color_pal_box_9 = QLabel(self.plp)
        self.lb_color_pal_box_9.setObjectName(u"lb_color_pal_box_9")
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_9.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_9.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_9.setFont(font3)

        self.horizontalLayout_61.addWidget(self.lb_color_pal_box_9)

        self.doubleSpinBox_Biola = QDoubleSpinBox(self.plp)
        self.doubleSpinBox_Biola.setObjectName(u"doubleSpinBox_Biola")
        self.doubleSpinBox_Biola.setFont(font3)
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
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_10.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_10.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_10.setFont(font3)

        self.horizontalLayout_62.addWidget(self.lb_color_pal_box_10)

        self.comboBox_Biola_SD_or = QComboBox(self.plp)
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.setObjectName(u"comboBox_Biola_SD_or")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.comboBox_Biola_SD_or.sizePolicy().hasHeightForWidth())
        self.comboBox_Biola_SD_or.setSizePolicy(sizePolicy10)
        self.comboBox_Biola_SD_or.setFont(font3)

        self.horizontalLayout_62.addWidget(self.comboBox_Biola_SD_or)


        self.verticalLayout_29.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.lb_color_pal_box_11 = QLabel(self.plp)
        self.lb_color_pal_box_11.setObjectName(u"lb_color_pal_box_11")
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_11.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_11.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_11.setFont(font3)

        self.horizontalLayout_63.addWidget(self.lb_color_pal_box_11)

        self.comboBox_Biola_language = QComboBox(self.plp)
        self.comboBox_Biola_language.addItem("")
        self.comboBox_Biola_language.addItem("")
        self.comboBox_Biola_language.setObjectName(u"comboBox_Biola_language")
        sizePolicy10.setHeightForWidth(self.comboBox_Biola_language.sizePolicy().hasHeightForWidth())
        self.comboBox_Biola_language.setSizePolicy(sizePolicy10)
        self.comboBox_Biola_language.setFont(font3)

        self.horizontalLayout_63.addWidget(self.comboBox_Biola_language)


        self.verticalLayout_29.addLayout(self.horizontalLayout_63)

        self.check_setka_biola = QCheckBox(self.plp)
        self.check_setka_biola.setObjectName(u"check_setka_biola")
        sizePolicy2.setHeightForWidth(self.check_setka_biola.sizePolicy().hasHeightForWidth())
        self.check_setka_biola.setSizePolicy(sizePolicy2)
        self.check_setka_biola.setFont(font3)
        self.check_setka_biola.setChecked(True)

        self.verticalLayout_29.addWidget(self.check_setka_biola)


        self.verticalLayout_30.addLayout(self.verticalLayout_29)


        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.plp)

        self.Lab_stuff.addTab(self.tab_5, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_9 = QGridLayout(self.tab_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.lb_path_4 = QLabel(self.tab_7)
        self.lb_path_4.setObjectName(u"lb_path_4")
        sizePolicy.setHeightForWidth(self.lb_path_4.sizePolicy().hasHeightForWidth())
        self.lb_path_4.setSizePolicy(sizePolicy)
        self.lb_path_4.setFont(font2)

        self.horizontalLayout_45.addWidget(self.lb_path_4)

        self.path_for_LT = QLineEdit(self.tab_7)
        self.path_for_LT.setObjectName(u"path_for_LT")
        self.path_for_LT.setFont(font3)

        self.horizontalLayout_45.addWidget(self.path_for_LT)


        self.gridLayout_9.addLayout(self.horizontalLayout_45, 0, 0, 1, 1)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.lb_path_13 = QLabel(self.tab_7)
        self.lb_path_13.setObjectName(u"lb_path_13")
        sizePolicy.setHeightForWidth(self.lb_path_13.sizePolicy().hasHeightForWidth())
        self.lb_path_13.setSizePolicy(sizePolicy)
        self.lb_path_13.setFont(font2)

        self.horizontalLayout_55.addWidget(self.lb_path_13)

        self.sep_for_LT = QLineEdit(self.tab_7)
        self.sep_for_LT.setObjectName(u"sep_for_LT")
        sizePolicy9.setHeightForWidth(self.sep_for_LT.sizePolicy().hasHeightForWidth())
        self.sep_for_LT.setSizePolicy(sizePolicy9)
        self.sep_for_LT.setFont(font3)

        self.horizontalLayout_55.addWidget(self.sep_for_LT)


        self.horizontalLayout_58.addLayout(self.horizontalLayout_55)


        self.verticalLayout_38.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.lb_path_15 = QLabel(self.tab_7)
        self.lb_path_15.setObjectName(u"lb_path_15")
        sizePolicy.setHeightForWidth(self.lb_path_15.sizePolicy().hasHeightForWidth())
        self.lb_path_15.setSizePolicy(sizePolicy)
        self.lb_path_15.setFont(font2)

        self.horizontalLayout_57.addWidget(self.lb_path_15)

        self.position = QSpinBox(self.tab_7)
        self.position.setObjectName(u"position")
        self.position.setEnabled(True)
        self.position.setFont(font3)
        self.position.setMinimum(1)
        self.position.setMaximum(5)
        self.position.setValue(1)

        self.horizontalLayout_57.addWidget(self.position)


        self.verticalLayout_38.addLayout(self.horizontalLayout_57)


        self.gridLayout_9.addLayout(self.verticalLayout_38, 1, 0, 1, 1)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.line_6 = QFrame(self.tab_7)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFont(font1)
        self.line_6.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_28.addWidget(self.line_6)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.lb_path_14 = QLabel(self.tab_7)
        self.lb_path_14.setObjectName(u"lb_path_14")
        sizePolicy.setHeightForWidth(self.lb_path_14.sizePolicy().hasHeightForWidth())
        self.lb_path_14.setSizePolicy(sizePolicy)
        self.lb_path_14.setFont(font2)

        self.horizontalLayout_56.addWidget(self.lb_path_14)

        self.sep_for_LT_values = QLineEdit(self.tab_7)
        self.sep_for_LT_values.setObjectName(u"sep_for_LT_values")
        sizePolicy9.setHeightForWidth(self.sep_for_LT_values.sizePolicy().hasHeightForWidth())
        self.sep_for_LT_values.setSizePolicy(sizePolicy9)
        self.sep_for_LT_values.setFont(font3)

        self.horizontalLayout_56.addWidget(self.sep_for_LT_values)

        self.horizontalSpacer_2 = QSpacerItem(60, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_56)

        self.line_5 = QFrame(self.tab_7)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFont(font1)
        self.line_5.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_28.addWidget(self.line_5)


        self.gridLayout_9.addLayout(self.verticalLayout_28, 2, 0, 1, 1)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.asd = QFrame(self.tab_7)
        self.asd.setObjectName(u"asd")
        sizePolicy.setHeightForWidth(self.asd.sizePolicy().hasHeightForWidth())
        self.asd.setSizePolicy(sizePolicy)
        self.asd.setStyleSheet(u"QFrame#asd{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_26 = QVBoxLayout(self.asd)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.lb_path_5 = QLabel(self.asd)
        self.lb_path_5.setObjectName(u"lb_path_5")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.lb_path_5.sizePolicy().hasHeightForWidth())
        self.lb_path_5.setSizePolicy(sizePolicy11)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(11)
        font6.setUnderline(True)
        self.lb_path_5.setFont(font6)
        self.lb_path_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.lb_path_5)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.lb_path_7 = QLabel(self.asd)
        self.lb_path_7.setObjectName(u"lb_path_7")
        sizePolicy11.setHeightForWidth(self.lb_path_7.sizePolicy().hasHeightForWidth())
        self.lb_path_7.setSizePolicy(sizePolicy11)
        self.lb_path_7.setFont(font2)

        self.horizontalLayout_48.addWidget(self.lb_path_7)

        self.a_main = QDoubleSpinBox(self.asd)
        self.a_main.setObjectName(u"a_main")
        self.a_main.setFont(font3)
        self.a_main.setDecimals(5)
        self.a_main.setMaximum(50.000000000000000)
        self.a_main.setValue(0.220000000000000)

        self.horizontalLayout_48.addWidget(self.a_main)


        self.verticalLayout_25.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.lb_path_8 = QLabel(self.asd)
        self.lb_path_8.setObjectName(u"lb_path_8")
        sizePolicy11.setHeightForWidth(self.lb_path_8.sizePolicy().hasHeightForWidth())
        self.lb_path_8.setSizePolicy(sizePolicy11)
        self.lb_path_8.setFont(font2)

        self.horizontalLayout_49.addWidget(self.lb_path_8)

        self.b_main = QDoubleSpinBox(self.asd)
        self.b_main.setObjectName(u"b_main")
        self.b_main.setFont(font3)
        self.b_main.setDecimals(5)
        self.b_main.setMinimum(-200.000000000000000)
        self.b_main.setMaximum(200.000000000000000)
        self.b_main.setValue(-0.800000000000000)

        self.horizontalLayout_49.addWidget(self.b_main)


        self.verticalLayout_25.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.lb_path_12 = QLabel(self.asd)
        self.lb_path_12.setObjectName(u"lb_path_12")
        sizePolicy11.setHeightForWidth(self.lb_path_12.sizePolicy().hasHeightForWidth())
        self.lb_path_12.setSizePolicy(sizePolicy11)
        self.lb_path_12.setFont(font2)

        self.horizontalLayout_50.addWidget(self.lb_path_12)

        self.dateEdit = QDateEdit(self.asd)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font3)

        self.horizontalLayout_50.addWidget(self.dateEdit)


        self.verticalLayout_25.addLayout(self.horizontalLayout_50)


        self.verticalLayout_26.addLayout(self.verticalLayout_25)


        self.horizontalLayout_54.addWidget(self.asd)

        self.hhhhh = QFrame(self.tab_7)
        self.hhhhh.setObjectName(u"hhhhh")
        sizePolicy.setHeightForWidth(self.hhhhh.sizePolicy().hasHeightForWidth())
        self.hhhhh.setSizePolicy(sizePolicy)
        self.hhhhh.setStyleSheet(u"QFrame#hhhhh{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.hhhhh)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.lb_path_6 = QLabel(self.hhhhh)
        self.lb_path_6.setObjectName(u"lb_path_6")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.lb_path_6.sizePolicy().hasHeightForWidth())
        self.lb_path_6.setSizePolicy(sizePolicy12)
        self.lb_path_6.setFont(font6)
        self.lb_path_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.lb_path_6)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.lb_path_9 = QLabel(self.hhhhh)
        self.lb_path_9.setObjectName(u"lb_path_9")
        sizePolicy11.setHeightForWidth(self.lb_path_9.sizePolicy().hasHeightForWidth())
        self.lb_path_9.setSizePolicy(sizePolicy11)
        self.lb_path_9.setFont(font2)

        self.horizontalLayout_51.addWidget(self.lb_path_9)

        self.a_dop = QDoubleSpinBox(self.hhhhh)
        self.a_dop.setObjectName(u"a_dop")
        self.a_dop.setFont(font3)
        self.a_dop.setDecimals(5)
        self.a_dop.setMaximum(50.000000000000000)
        self.a_dop.setValue(1.410000000000000)

        self.horizontalLayout_51.addWidget(self.a_dop)


        self.verticalLayout_24.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.lb_path_10 = QLabel(self.hhhhh)
        self.lb_path_10.setObjectName(u"lb_path_10")
        sizePolicy11.setHeightForWidth(self.lb_path_10.sizePolicy().hasHeightForWidth())
        self.lb_path_10.setSizePolicy(sizePolicy11)
        self.lb_path_10.setFont(font2)

        self.horizontalLayout_52.addWidget(self.lb_path_10)

        self.b_dop = QDoubleSpinBox(self.hhhhh)
        self.b_dop.setObjectName(u"b_dop")
        self.b_dop.setFont(font3)
        self.b_dop.setDecimals(5)
        self.b_dop.setMinimum(-200.000000000000000)
        self.b_dop.setMaximum(200.000000000000000)
        self.b_dop.setValue(-29.500000000000000)

        self.horizontalLayout_52.addWidget(self.b_dop)


        self.verticalLayout_24.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.lb_path_11 = QLabel(self.hhhhh)
        self.lb_path_11.setObjectName(u"lb_path_11")
        sizePolicy11.setHeightForWidth(self.lb_path_11.sizePolicy().hasHeightForWidth())
        self.lb_path_11.setSizePolicy(sizePolicy11)
        self.lb_path_11.setFont(font2)

        self.horizontalLayout_53.addWidget(self.lb_path_11)

        self.dateEdit_2 = QDateEdit(self.hhhhh)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setFont(font3)

        self.horizontalLayout_53.addWidget(self.dateEdit_2)


        self.verticalLayout_24.addLayout(self.horizontalLayout_53)


        self.verticalLayout_27.addLayout(self.verticalLayout_24)


        self.horizontalLayout_54.addWidget(self.hhhhh)


        self.gridLayout_9.addLayout(self.horizontalLayout_54, 3, 0, 1, 1)

        self.btn_LT = QPushButton(self.tab_7)
        self.btn_LT.setObjectName(u"btn_LT")
        self.btn_LT.setFont(font3)
        self.btn_LT.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.gridLayout_9.addWidget(self.btn_LT, 4, 0, 1, 1)

        self.Lab_stuff.addTab(self.tab_7, "")
        self.tabWidgetPage4 = QWidget()
        self.tabWidgetPage4.setObjectName(u"tabWidgetPage4")
        self.horizontalLayout_64 = QHBoxLayout(self.tabWidgetPage4)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.tabWidget_2 = QTabWidget(self.tabWidgetPage4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setFont(font3)
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
        self.lb_path_for_plot.setFont(font3)

        self.horizontalLayout_13.addWidget(self.lb_path_for_plot)

        self.path_for_plot = QLineEdit(self.tab)
        self.path_for_plot.setObjectName(u"path_for_plot")
        self.path_for_plot.setFont(font3)

        self.horizontalLayout_13.addWidget(self.path_for_plot)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_exel_name = QLabel(self.tab)
        self.lb_exel_name.setObjectName(u"lb_exel_name")
        self.lb_exel_name.setFont(font3)

        self.horizontalLayout_14.addWidget(self.lb_exel_name)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_14.addWidget(self.comboBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lb_hue_name = QLabel(self.tab)
        self.lb_hue_name.setObjectName(u"lb_hue_name")
        self.lb_hue_name.setFont(font3)

        self.horizontalLayout_15.addWidget(self.lb_hue_name)

        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_15.addWidget(self.comboBox_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.nmn = QFrame(self.tab)
        self.nmn.setObjectName(u"nmn")
        sizePolicy2.setHeightForWidth(self.nmn.sizePolicy().hasHeightForWidth())
        self.nmn.setSizePolicy(sizePolicy2)
        self.nmn.setStyleSheet(u"QFrame#nmn{\n"
"border: 5px solid rgb(128, 160, 165);\n"
"border-radius: 17px;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.nmn)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.check_box_plot = QCheckBox(self.nmn)
        self.check_box_plot.setObjectName(u"check_box_plot")
        self.check_box_plot.setFont(font3)
        self.check_box_plot.setChecked(True)

        self.verticalLayout_13.addWidget(self.check_box_plot)

        self.check_corr_matrix = QCheckBox(self.nmn)
        self.check_corr_matrix.setObjectName(u"check_corr_matrix")
        self.check_corr_matrix.setFont(font3)

        self.verticalLayout_13.addWidget(self.check_corr_matrix)

        self.check_corr_figs = QCheckBox(self.nmn)
        self.check_corr_figs.setObjectName(u"check_corr_figs")
        self.check_corr_figs.setFont(font3)

        self.verticalLayout_13.addWidget(self.check_corr_figs)


        self.verticalLayout_14.addWidget(self.nmn)


        self.verticalLayout_17.addLayout(self.verticalLayout_14)

        self.tabWidget = QTabWidget(self.tab)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy13)
        self.tabWidget.setFont(font3)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayout_4 = QFormLayout(self.tab_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(10)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 0, -1, -1)
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.verticalLayout_16 = QVBoxLayout(self.frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lb_color_pal_box = QLabel(self.frame)
        self.lb_color_pal_box.setObjectName(u"lb_color_pal_box")
        sizePolicy2.setHeightForWidth(self.lb_color_pal_box.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box.setSizePolicy(sizePolicy2)
        self.lb_color_pal_box.setFont(font3)

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
        self.comboBox_color_pal_box.setObjectName(u"comboBox_color_pal_box")
        sizePolicy3.setHeightForWidth(self.comboBox_color_pal_box.sizePolicy().hasHeightForWidth())
        self.comboBox_color_pal_box.setSizePolicy(sizePolicy3)
        self.comboBox_color_pal_box.setFont(font3)

        self.horizontalLayout_19.addWidget(self.comboBox_color_pal_box)


        self.verticalLayout_16.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lb_color_pal_points = QLabel(self.frame)
        self.lb_color_pal_points.setObjectName(u"lb_color_pal_points")
        sizePolicy2.setHeightForWidth(self.lb_color_pal_points.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_points.setSizePolicy(sizePolicy2)
        self.lb_color_pal_points.setFont(font3)

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
        self.comboBox_color_pal_points.setObjectName(u"comboBox_color_pal_points")
        sizePolicy3.setHeightForWidth(self.comboBox_color_pal_points.sizePolicy().hasHeightForWidth())
        self.comboBox_color_pal_points.setSizePolicy(sizePolicy3)
        self.comboBox_color_pal_points.setFont(font3)

        self.horizontalLayout_24.addWidget(self.comboBox_color_pal_points)


        self.verticalLayout_16.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lb_color_for_box = QLabel(self.frame)
        self.lb_color_for_box.setObjectName(u"lb_color_for_box")
        sizePolicy2.setHeightForWidth(self.lb_color_for_box.sizePolicy().hasHeightForWidth())
        self.lb_color_for_box.setSizePolicy(sizePolicy2)
        self.lb_color_for_box.setFont(font3)

        self.horizontalLayout_20.addWidget(self.lb_color_for_box)

        self.color_box = QLineEdit(self.frame)
        self.color_box.setObjectName(u"color_box")
        sizePolicy3.setHeightForWidth(self.color_box.sizePolicy().hasHeightForWidth())
        self.color_box.setSizePolicy(sizePolicy3)
        self.color_box.setFont(font3)

        self.horizontalLayout_20.addWidget(self.color_box)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lb_color_forpoints = QLabel(self.frame)
        self.lb_color_forpoints.setObjectName(u"lb_color_forpoints")
        sizePolicy2.setHeightForWidth(self.lb_color_forpoints.sizePolicy().hasHeightForWidth())
        self.lb_color_forpoints.setSizePolicy(sizePolicy2)
        self.lb_color_forpoints.setFont(font3)

        self.horizontalLayout_25.addWidget(self.lb_color_forpoints)

        self.color_points = QLineEdit(self.frame)
        self.color_points.setObjectName(u"color_points")
        sizePolicy3.setHeightForWidth(self.color_points.sizePolicy().hasHeightForWidth())
        self.color_points.setSizePolicy(sizePolicy3)
        self.color_points.setFont(font3)

        self.horizontalLayout_25.addWidget(self.color_points)


        self.verticalLayout_16.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.lb_color_pal_box_7 = QLabel(self.frame)
        self.lb_color_pal_box_7.setObjectName(u"lb_color_pal_box_7")
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_7.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_7.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_7.setFont(font3)

        self.horizontalLayout_59.addWidget(self.lb_color_pal_box_7)

        self.spinBox_mean_val_size = QSpinBox(self.frame)
        self.spinBox_mean_val_size.setObjectName(u"spinBox_mean_val_size")
        sizePolicy3.setHeightForWidth(self.spinBox_mean_val_size.sizePolicy().hasHeightForWidth())
        self.spinBox_mean_val_size.setSizePolicy(sizePolicy3)
        self.spinBox_mean_val_size.setFont(font3)
        self.spinBox_mean_val_size.setMinimum(2)
        self.spinBox_mean_val_size.setMaximum(20)
        self.spinBox_mean_val_size.setValue(4)

        self.horizontalLayout_59.addWidget(self.spinBox_mean_val_size)


        self.verticalLayout_16.addLayout(self.horizontalLayout_59)


        self.horizontalLayout_38.addWidget(self.frame)

        self.frame1 = QFrame(self.tab_3)
        self.frame1.setObjectName(u"frame1")
        sizePolicy2.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy2)
        self.verticalLayout_20 = QVBoxLayout(self.frame1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.lb_color_pal_box_6 = QLabel(self.frame1)
        self.lb_color_pal_box_6.setObjectName(u"lb_color_pal_box_6")
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_6.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_6.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_6.setFont(font3)

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
        self.comboBox_fonts.setFont(font3)

        self.horizontalLayout_39.addWidget(self.comboBox_fonts)


        self.verticalLayout_20.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.lb_color_pal_box_2 = QLabel(self.frame1)
        self.lb_color_pal_box_2.setObjectName(u"lb_color_pal_box_2")
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_2.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_2.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_2.setFont(font3)

        self.horizontalLayout_34.addWidget(self.lb_color_pal_box_2)

        self.spinBox_x_label = QSpinBox(self.frame1)
        self.spinBox_x_label.setObjectName(u"spinBox_x_label")
        sizePolicy3.setHeightForWidth(self.spinBox_x_label.sizePolicy().hasHeightForWidth())
        self.spinBox_x_label.setSizePolicy(sizePolicy3)
        self.spinBox_x_label.setFont(font3)
        self.spinBox_x_label.setMinimum(2)
        self.spinBox_x_label.setMaximum(100)
        self.spinBox_x_label.setValue(14)

        self.horizontalLayout_34.addWidget(self.spinBox_x_label)


        self.verticalLayout_20.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.lb_color_pal_box_3 = QLabel(self.frame1)
        self.lb_color_pal_box_3.setObjectName(u"lb_color_pal_box_3")
        self.lb_color_pal_box_3.setFont(font3)

        self.horizontalLayout_35.addWidget(self.lb_color_pal_box_3)

        self.spinBox_y_label = QSpinBox(self.frame1)
        self.spinBox_y_label.setObjectName(u"spinBox_y_label")
        sizePolicy3.setHeightForWidth(self.spinBox_y_label.sizePolicy().hasHeightForWidth())
        self.spinBox_y_label.setSizePolicy(sizePolicy3)
        self.spinBox_y_label.setFont(font3)
        self.spinBox_y_label.setMinimum(2)
        self.spinBox_y_label.setMaximum(100)
        self.spinBox_y_label.setValue(14)

        self.horizontalLayout_35.addWidget(self.spinBox_y_label)


        self.verticalLayout_20.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.lb_color_pal_box_5 = QLabel(self.frame1)
        self.lb_color_pal_box_5.setObjectName(u"lb_color_pal_box_5")
        self.lb_color_pal_box_5.setFont(font3)

        self.horizontalLayout_36.addWidget(self.lb_color_pal_box_5)

        self.spinBox_x_val = QSpinBox(self.frame1)
        self.spinBox_x_val.setObjectName(u"spinBox_x_val")
        sizePolicy3.setHeightForWidth(self.spinBox_x_val.sizePolicy().hasHeightForWidth())
        self.spinBox_x_val.setSizePolicy(sizePolicy3)
        self.spinBox_x_val.setFont(font3)
        self.spinBox_x_val.setMinimum(2)
        self.spinBox_x_val.setMaximum(100)
        self.spinBox_x_val.setValue(14)

        self.horizontalLayout_36.addWidget(self.spinBox_x_val)


        self.verticalLayout_20.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.lb_color_pal_box_4 = QLabel(self.frame1)
        self.lb_color_pal_box_4.setObjectName(u"lb_color_pal_box_4")
        self.lb_color_pal_box_4.setFont(font3)

        self.horizontalLayout_37.addWidget(self.lb_color_pal_box_4)

        self.spinBox_y_vals = QSpinBox(self.frame1)
        self.spinBox_y_vals.setObjectName(u"spinBox_y_vals")
        sizePolicy3.setHeightForWidth(self.spinBox_y_vals.sizePolicy().hasHeightForWidth())
        self.spinBox_y_vals.setSizePolicy(sizePolicy3)
        self.spinBox_y_vals.setFont(font3)
        self.spinBox_y_vals.setMinimum(2)
        self.spinBox_y_vals.setMaximum(100)
        self.spinBox_y_vals.setValue(14)

        self.horizontalLayout_37.addWidget(self.spinBox_y_vals)


        self.verticalLayout_20.addLayout(self.horizontalLayout_37)


        self.horizontalLayout_38.addWidget(self.frame1)


        self.formLayout_4.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_38)

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
        self.lb_stattest.setFont(font3)

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
        self.comboBox_stat_test.setObjectName(u"comboBox_stat_test")
        self.comboBox_stat_test.setEnabled(True)
        self.comboBox_stat_test.setFont(font3)

        self.horizontalLayout_23.addWidget(self.comboBox_stat_test)


        self.gridLayout_6.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb__altern_heposisis = QLabel(self.tab_4)
        self.lb__altern_heposisis.setObjectName(u"lb__altern_heposisis")
        self.lb__altern_heposisis.setEnabled(True)
        self.lb__altern_heposisis.setFont(font3)

        self.horizontalLayout_18.addWidget(self.lb__altern_heposisis)

        self.comboBox_alter_hep = QComboBox(self.tab_4)
        self.comboBox_alter_hep.addItem("")
        self.comboBox_alter_hep.addItem("")
        self.comboBox_alter_hep.addItem("")
        self.comboBox_alter_hep.setObjectName(u"comboBox_alter_hep")
        self.comboBox_alter_hep.setEnabled(True)
        self.comboBox_alter_hep.setFont(font3)

        self.horizontalLayout_18.addWidget(self.comboBox_alter_hep)


        self.gridLayout_6.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lb_stattest_2 = QLabel(self.tab_4)
        self.lb_stattest_2.setObjectName(u"lb_stattest_2")
        self.lb_stattest_2.setFont(font3)

        self.horizontalLayout_21.addWidget(self.lb_stattest_2)

        self.check_stat_znachimost = QCheckBox(self.tab_4)
        self.check_stat_znachimost.setObjectName(u"check_stat_znachimost")
        self.check_stat_znachimost.setEnabled(True)
        self.check_stat_znachimost.setFont(font3)
        self.check_stat_znachimost.setChecked(True)

        self.horizontalLayout_21.addWidget(self.check_stat_znachimost)


        self.gridLayout_6.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.lb_del_hue_7 = QLabel(self.tab_4)
        self.lb_del_hue_7.setObjectName(u"lb_del_hue_7")
        self.lb_del_hue_7.setFont(font3)
        self.lb_del_hue_7.setWordWrap(True)

        self.horizontalLayout_82.addWidget(self.lb_del_hue_7)

        self.STAT_znachimost_order_box_plot = QLineEdit(self.tab_4)
        self.STAT_znachimost_order_box_plot.setObjectName(u"STAT_znachimost_order_box_plot")
        self.STAT_znachimost_order_box_plot.setFont(font3)

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
        sizePolicy14 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.check_sort_or_not.sizePolicy().hasHeightForWidth())
        self.check_sort_or_not.setSizePolicy(sizePolicy14)
        self.check_sort_or_not.setFont(font3)
        self.check_sort_or_not.setChecked(False)

        self.verticalLayout_18.addWidget(self.check_sort_or_not)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.lb_del_hue_6 = QLabel(self.tab_9)
        self.lb_del_hue_6.setObjectName(u"lb_del_hue_6")
        self.lb_del_hue_6.setFont(font3)

        self.horizontalLayout_81.addWidget(self.lb_del_hue_6)

        self.order_box_plot = QLineEdit(self.tab_9)
        self.order_box_plot.setObjectName(u"order_box_plot")
        self.order_box_plot.setFont(font3)

        self.horizontalLayout_81.addWidget(self.order_box_plot)


        self.verticalLayout_18.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.lb_stattest_3 = QLabel(self.tab_9)
        self.lb_stattest_3.setObjectName(u"lb_stattest_3")
        self.lb_stattest_3.setFont(font3)

        self.horizontalLayout_60.addWidget(self.lb_stattest_3)

        self.check_N_ = QCheckBox(self.tab_9)
        self.check_N_.setObjectName(u"check_N_")
        self.check_N_.setEnabled(True)
        sizePolicy15 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.check_N_.sizePolicy().hasHeightForWidth())
        self.check_N_.setSizePolicy(sizePolicy15)
        self.check_N_.setChecked(True)

        self.horizontalLayout_60.addWidget(self.check_N_)


        self.verticalLayout_18.addLayout(self.horizontalLayout_60)

        self.line_7 = QFrame(self.tab_9)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFont(font1)
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
        self.label_9.setFont(font3)

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
        sizePolicy8.setHeightForWidth(self.comboBox_spin_x_.sizePolicy().hasHeightForWidth())
        self.comboBox_spin_x_.setSizePolicy(sizePolicy8)
        self.comboBox_spin_x_.setFont(font3)

        self.horizontalLayout_22.addWidget(self.comboBox_spin_x_)


        self.horizontalLayout_83.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.lb_stattest_4 = QLabel(self.tab_9)
        self.lb_stattest_4.setObjectName(u"lb_stattest_4")
        sizePolicy14.setHeightForWidth(self.lb_stattest_4.sizePolicy().hasHeightForWidth())
        self.lb_stattest_4.setSizePolicy(sizePolicy14)
        self.lb_stattest_4.setFont(font3)

        self.horizontalLayout_66.addWidget(self.lb_stattest_4)

        self.check_background = QCheckBox(self.tab_9)
        self.check_background.setObjectName(u"check_background")
        self.check_background.setEnabled(True)
        sizePolicy15.setHeightForWidth(self.check_background.sizePolicy().hasHeightForWidth())
        self.check_background.setSizePolicy(sizePolicy15)
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
        self.lb_sd_or_minmax.setFont(font3)

        self.horizontalLayout_17.addWidget(self.lb_sd_or_minmax)

        self.comboBox_sd_or_minmax = QComboBox(self.tab_9)
        self.comboBox_sd_or_minmax.addItem("")
        self.comboBox_sd_or_minmax.addItem("")
        self.comboBox_sd_or_minmax.setObjectName(u"comboBox_sd_or_minmax")
        sizePolicy8.setHeightForWidth(self.comboBox_sd_or_minmax.sizePolicy().hasHeightForWidth())
        self.comboBox_sd_or_minmax.setSizePolicy(sizePolicy8)
        self.comboBox_sd_or_minmax.setFont(font3)

        self.horizontalLayout_17.addWidget(self.comboBox_sd_or_minmax)


        self.horizontalLayout_84.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lb_bottom_lim = QLabel(self.tab_9)
        self.lb_bottom_lim.setObjectName(u"lb_bottom_lim")
        sizePolicy.setHeightForWidth(self.lb_bottom_lim.sizePolicy().hasHeightForWidth())
        self.lb_bottom_lim.setSizePolicy(sizePolicy)
        self.lb_bottom_lim.setFont(font3)

        self.horizontalLayout_16.addWidget(self.lb_bottom_lim)

        self.bottom_lim = QLineEdit(self.tab_9)
        self.bottom_lim.setObjectName(u"bottom_lim")
        self.bottom_lim.setFont(font3)

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
        self.lb_corr_color_pallete_3.setFont(font3)

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
        self.comboBox_color_pal_corr.setFont(font3)

        self.horizontalLayout_32.addWidget(self.comboBox_color_pal_corr)


        self.verticalLayout_33.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.lb_del_hue_4 = QLabel(self.tab_2)
        self.lb_del_hue_4.setObjectName(u"lb_del_hue_4")
        self.lb_del_hue_4.setFont(font3)

        self.horizontalLayout_67.addWidget(self.lb_del_hue_4)

        self.check_change_corr_fig_down_limit = QCheckBox(self.tab_2)
        self.check_change_corr_fig_down_limit.setObjectName(u"check_change_corr_fig_down_limit")
        self.check_change_corr_fig_down_limit.setEnabled(True)
        self.check_change_corr_fig_down_limit.setFont(font3)
        self.check_change_corr_fig_down_limit.setChecked(False)

        self.horizontalLayout_67.addWidget(self.check_change_corr_fig_down_limit)

        self.doubleSpinBox_corr_figs = QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_corr_figs.setObjectName(u"doubleSpinBox_corr_figs")
        self.doubleSpinBox_corr_figs.setEnabled(False)
        self.doubleSpinBox_corr_figs.setFont(font3)
        self.doubleSpinBox_corr_figs.setMinimum(-100000.000000000000000)
        self.doubleSpinBox_corr_figs.setMaximum(1000000.000000000000000)

        self.horizontalLayout_67.addWidget(self.doubleSpinBox_corr_figs)


        self.verticalLayout_33.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.lb_del_hue_3 = QLabel(self.tab_2)
        self.lb_del_hue_3.setObjectName(u"lb_del_hue_3")
        self.lb_del_hue_3.setFont(font3)

        self.horizontalLayout_33.addWidget(self.lb_del_hue_3)

        self.del_hue = QLineEdit(self.tab_2)
        self.del_hue.setObjectName(u"del_hue")
        self.del_hue.setFont(font3)

        self.horizontalLayout_33.addWidget(self.del_hue)


        self.verticalLayout_33.addLayout(self.horizontalLayout_33)


        self.horizontalLayout_70.addLayout(self.verticalLayout_33)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.lb_del_hue_5 = QLabel(self.tab_2)
        self.lb_del_hue_5.setObjectName(u"lb_del_hue_5")
        self.lb_del_hue_5.setFont(font3)

        self.horizontalLayout_68.addWidget(self.lb_del_hue_5)

        self.spinBox_points_corrFIGS = QSpinBox(self.tab_2)
        self.spinBox_points_corrFIGS.setObjectName(u"spinBox_points_corrFIGS")
        sizePolicy3.setHeightForWidth(self.spinBox_points_corrFIGS.sizePolicy().hasHeightForWidth())
        self.spinBox_points_corrFIGS.setSizePolicy(sizePolicy3)
        self.spinBox_points_corrFIGS.setFont(font3)
        self.spinBox_points_corrFIGS.setMinimum(1)
        self.spinBox_points_corrFIGS.setMaximum(150)
        self.spinBox_points_corrFIGS.setValue(8)

        self.horizontalLayout_68.addWidget(self.spinBox_points_corrFIGS)


        self.verticalLayout_21.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.lb_color_pal_box_12 = QLabel(self.tab_2)
        self.lb_color_pal_box_12.setObjectName(u"lb_color_pal_box_12")
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_12.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_12.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_12.setFont(font3)

        self.horizontalLayout_69.addWidget(self.lb_color_pal_box_12)

        self.doubleSpinBox_corr_figs_fontscale = QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_corr_figs_fontscale.setObjectName(u"doubleSpinBox_corr_figs_fontscale")
        self.doubleSpinBox_corr_figs_fontscale.setFont(font3)
        self.doubleSpinBox_corr_figs_fontscale.setDecimals(1)
        self.doubleSpinBox_corr_figs_fontscale.setMinimum(0.100000000000000)
        self.doubleSpinBox_corr_figs_fontscale.setMaximum(25.000000000000000)
        self.doubleSpinBox_corr_figs_fontscale.setSingleStep(0.100000000000000)
        self.doubleSpinBox_corr_figs_fontscale.setValue(1.000000000000000)

        self.horizontalLayout_69.addWidget(self.doubleSpinBox_corr_figs_fontscale)


        self.verticalLayout_21.addLayout(self.horizontalLayout_69)

        self.check_sort_or_not_corr_figs = QCheckBox(self.tab_2)
        self.check_sort_or_not_corr_figs.setObjectName(u"check_sort_or_not_corr_figs")
        self.check_sort_or_not_corr_figs.setFont(font3)
        self.check_sort_or_not_corr_figs.setChecked(False)

        self.verticalLayout_21.addWidget(self.check_sort_or_not_corr_figs)

        self.check_setka = QCheckBox(self.tab_2)
        self.check_setka.setObjectName(u"check_setka")
        self.check_setka.setFont(font3)
        self.check_setka.setChecked(False)

        self.verticalLayout_21.addWidget(self.check_setka)


        self.horizontalLayout_70.addLayout(self.verticalLayout_21)


        self.gridLayout_8.addLayout(self.horizontalLayout_70, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.formLayout_3 = QFormLayout(self.tab_6)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.frame2 = QFrame(self.tab_6)
        self.frame2.setObjectName(u"frame2")
        sizePolicy2.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy2)
        self.frame2.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_19 = QVBoxLayout(self.frame2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lb_size_corr_matrix = QLabel(self.frame2)
        self.lb_size_corr_matrix.setObjectName(u"lb_size_corr_matrix")
        self.lb_size_corr_matrix.setFont(font3)
        self.lb_size_corr_matrix.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.lb_size_corr_matrix)

        self.corr_mat_figsize = QLineEdit(self.frame2)
        self.corr_mat_figsize.setObjectName(u"corr_mat_figsize")
        sizePolicy3.setHeightForWidth(self.corr_mat_figsize.sizePolicy().hasHeightForWidth())
        self.corr_mat_figsize.setSizePolicy(sizePolicy3)
        self.corr_mat_figsize.setFont(font3)

        self.horizontalLayout_28.addWidget(self.corr_mat_figsize)


        self.verticalLayout_19.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lb_font_in = QLabel(self.frame2)
        self.lb_font_in.setObjectName(u"lb_font_in")
        self.lb_font_in.setFont(font3)
        self.lb_font_in.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.lb_font_in)

        self.font_for_in = QLineEdit(self.frame2)
        self.font_for_in.setObjectName(u"font_for_in")
        sizePolicy3.setHeightForWidth(self.font_for_in.sizePolicy().hasHeightForWidth())
        self.font_for_in.setSizePolicy(sizePolicy3)
        self.font_for_in.setFont(font3)

        self.horizontalLayout_29.addWidget(self.font_for_in)


        self.verticalLayout_19.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lb_font_out = QLabel(self.frame2)
        self.lb_font_out.setObjectName(u"lb_font_out")
        self.lb_font_out.setFont(font3)
        self.lb_font_out.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.lb_font_out)

        self.font_for_out = QLineEdit(self.frame2)
        self.font_for_out.setObjectName(u"font_for_out")
        sizePolicy3.setHeightForWidth(self.font_for_out.sizePolicy().hasHeightForWidth())
        self.font_for_out.setSizePolicy(sizePolicy3)
        self.font_for_out.setFont(font3)

        self.horizontalLayout_30.addWidget(self.font_for_out)


        self.verticalLayout_19.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lb_name_of_title = QLabel(self.frame2)
        self.lb_name_of_title.setObjectName(u"lb_name_of_title")
        self.lb_name_of_title.setFont(font3)
        self.lb_name_of_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.lb_name_of_title)

        self.name_of_corr_matrix = QLineEdit(self.frame2)
        self.name_of_corr_matrix.setObjectName(u"name_of_corr_matrix")
        sizePolicy3.setHeightForWidth(self.name_of_corr_matrix.sizePolicy().hasHeightForWidth())
        self.name_of_corr_matrix.setSizePolicy(sizePolicy3)
        self.name_of_corr_matrix.setFont(font3)

        self.horizontalLayout_31.addWidget(self.name_of_corr_matrix)


        self.verticalLayout_19.addLayout(self.horizontalLayout_31)


        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.frame2)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_17.addWidget(self.tabWidget)


        self.gridLayout_4.addLayout(self.verticalLayout_17, 0, 0, 2, 2)

        self.btn_plot_and_save_figs = QPushButton(self.tab)
        self.btn_plot_and_save_figs.setObjectName(u"btn_plot_and_save_figs")
        self.btn_plot_and_save_figs.setFont(font3)
        self.btn_plot_and_save_figs.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.gridLayout_4.addWidget(self.btn_plot_and_save_figs, 2, 0, 1, 2)

        self.tabWidget_2.addTab(self.tab, "")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame3 = QFrame(self.widget)
        self.frame3.setObjectName(u"frame3")
        sizePolicy.setHeightForWidth(self.frame3.sizePolicy().hasHeightForWidth())
        self.frame3.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.frame3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_path_for_profile = QLabel(self.frame3)
        self.lb_path_for_profile.setObjectName(u"lb_path_for_profile")
        sizePolicy.setHeightForWidth(self.lb_path_for_profile.sizePolicy().hasHeightForWidth())
        self.lb_path_for_profile.setSizePolicy(sizePolicy)
        self.lb_path_for_profile.setFont(font3)

        self.horizontalLayout_10.addWidget(self.lb_path_for_profile)

        self.path_for_profile = QLineEdit(self.frame3)
        self.path_for_profile.setObjectName(u"path_for_profile")
        self.path_for_profile.setFont(font3)

        self.horizontalLayout_10.addWidget(self.path_for_profile)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_patient_data = QLabel(self.frame3)
        self.lb_patient_data.setObjectName(u"lb_patient_data")
        sizePolicy.setHeightForWidth(self.lb_patient_data.sizePolicy().hasHeightForWidth())
        self.lb_patient_data.setSizePolicy(sizePolicy)
        self.lb_patient_data.setFont(font3)

        self.horizontalLayout_11.addWidget(self.lb_patient_data)

        self.patient_data = QLineEdit(self.frame3)
        self.patient_data.setObjectName(u"patient_data")
        self.patient_data.setFont(font3)

        self.horizontalLayout_11.addWidget(self.patient_data)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_norm_data = QLabel(self.frame3)
        self.lb_norm_data.setObjectName(u"lb_norm_data")
        sizePolicy.setHeightForWidth(self.lb_norm_data.sizePolicy().hasHeightForWidth())
        self.lb_norm_data.setSizePolicy(sizePolicy)
        self.lb_norm_data.setFont(font3)

        self.horizontalLayout_12.addWidget(self.lb_norm_data)

        self.norm_data = QLineEdit(self.frame3)
        self.norm_data.setObjectName(u"norm_data")
        self.norm_data.setFont(font3)

        self.horizontalLayout_12.addWidget(self.norm_data)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)


        self.verticalLayout_11.addWidget(self.frame3)

        self.tyt = QFrame(self.widget)
        self.tyt.setObjectName(u"tyt")
        sizePolicy.setHeightForWidth(self.tyt.sizePolicy().hasHeightForWidth())
        self.tyt.setSizePolicy(sizePolicy)
        self.tyt.setFont(font3)
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
        self.label_5.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_4 = QLabel(self.tyt)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.patient_prof = QLineEdit(self.tyt)
        self.patient_prof.setObjectName(u"patient_prof")
        self.patient_prof.setFont(font3)

        self.verticalLayout_7.addWidget(self.patient_prof)

        self.color_for_patient = QLineEdit(self.tyt)
        self.color_for_patient.setObjectName(u"color_for_patient")
        self.color_for_patient.setFont(font3)

        self.verticalLayout_7.addWidget(self.color_for_patient)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.check_profile_pat_line = QCheckBox(self.tyt)
        self.check_profile_pat_line.setObjectName(u"check_profile_pat_line")
        self.check_profile_pat_line.setEnabled(True)
        self.check_profile_pat_line.setFont(font3)
        self.check_profile_pat_line.setChecked(True)

        self.verticalLayout_34.addWidget(self.check_profile_pat_line)

        self.check_profile_pat_sd = QCheckBox(self.tyt)
        self.check_profile_pat_sd.setObjectName(u"check_profile_pat_sd")
        self.check_profile_pat_sd.setEnabled(True)
        self.check_profile_pat_sd.setFont(font3)
        self.check_profile_pat_sd.setChecked(True)

        self.verticalLayout_34.addWidget(self.check_profile_pat_sd)


        self.horizontalLayout_9.addLayout(self.verticalLayout_34)


        self.verticalLayout_11.addWidget(self.tyt)

        self.opo = QFrame(self.widget)
        self.opo.setObjectName(u"opo")
        sizePolicy.setHeightForWidth(self.opo.sizePolicy().hasHeightForWidth())
        self.opo.setSizePolicy(sizePolicy)
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
        self.label_8.setFont(font3)

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_7 = QLabel(self.opo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_9.addWidget(self.label_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.norm_prof = QLineEdit(self.opo)
        self.norm_prof.setObjectName(u"norm_prof")
        self.norm_prof.setFont(font3)

        self.verticalLayout_8.addWidget(self.norm_prof)

        self.color_for_norm = QLineEdit(self.opo)
        self.color_for_norm.setObjectName(u"color_for_norm")
        self.color_for_norm.setFont(font3)

        self.verticalLayout_8.addWidget(self.color_for_norm)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.check_profile_norm_line = QCheckBox(self.opo)
        self.check_profile_norm_line.setObjectName(u"check_profile_norm_line")
        self.check_profile_norm_line.setEnabled(True)
        self.check_profile_norm_line.setFont(font3)
        self.check_profile_norm_line.setChecked(False)

        self.verticalLayout_35.addWidget(self.check_profile_norm_line)

        self.check_profile_norm_sd = QCheckBox(self.opo)
        self.check_profile_norm_sd.setObjectName(u"check_profile_norm_sd")
        self.check_profile_norm_sd.setEnabled(True)
        self.check_profile_norm_sd.setFont(font3)
        self.check_profile_norm_sd.setChecked(True)

        self.verticalLayout_35.addWidget(self.check_profile_norm_sd)


        self.horizontalLayout_6.addLayout(self.verticalLayout_35)


        self.verticalLayout_11.addWidget(self.opo)

        self.btn_plot_and_save_profile = QPushButton(self.widget)
        self.btn_plot_and_save_profile.setObjectName(u"btn_plot_and_save_profile")
        self.btn_plot_and_save_profile.setFont(font3)
        self.btn_plot_and_save_profile.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.verticalLayout_11.addWidget(self.btn_plot_and_save_profile)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.widget, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.formLayout = QFormLayout(self.tab_8)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.lb_path_for_plot_2 = QLabel(self.tab_8)
        self.lb_path_for_plot_2.setObjectName(u"lb_path_for_plot_2")
        self.lb_path_for_plot_2.setFont(font3)

        self.horizontalLayout_75.addWidget(self.lb_path_for_plot_2)

        self.path_for_pivot_table = QLineEdit(self.tab_8)
        self.path_for_pivot_table.setObjectName(u"path_for_pivot_table")
        self.path_for_pivot_table.setFont(font3)

        self.horizontalLayout_75.addWidget(self.path_for_pivot_table)


        self.verticalLayout_36.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.lb_exel_name_2 = QLabel(self.tab_8)
        self.lb_exel_name_2.setObjectName(u"lb_exel_name_2")
        self.lb_exel_name_2.setFont(font3)

        self.horizontalLayout_76.addWidget(self.lb_exel_name_2)

        self.comboBox_pivot_table = QComboBox(self.tab_8)
        self.comboBox_pivot_table.setObjectName(u"comboBox_pivot_table")

        self.horizontalLayout_76.addWidget(self.comboBox_pivot_table)


        self.verticalLayout_36.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.lb_hue_name_2 = QLabel(self.tab_8)
        self.lb_hue_name_2.setObjectName(u"lb_hue_name_2")
        self.lb_hue_name_2.setFont(font3)

        self.horizontalLayout_77.addWidget(self.lb_hue_name_2)

        self.comboBox_pivot_hue = QComboBox(self.tab_8)
        self.comboBox_pivot_hue.setObjectName(u"comboBox_pivot_hue")

        self.horizontalLayout_77.addWidget(self.comboBox_pivot_hue)


        self.verticalLayout_36.addLayout(self.horizontalLayout_77)


        self.verticalLayout_37.addLayout(self.verticalLayout_36)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.lb_color_pal_box_8 = QLabel(self.tab_8)
        self.lb_color_pal_box_8.setObjectName(u"lb_color_pal_box_8")
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_8.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_8.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_8.setFont(font3)

        self.horizontalLayout_79.addWidget(self.lb_color_pal_box_8)

        self.spinBox_pivot_table = QSpinBox(self.tab_8)
        self.spinBox_pivot_table.setObjectName(u"spinBox_pivot_table")
        sizePolicy3.setHeightForWidth(self.spinBox_pivot_table.sizePolicy().hasHeightForWidth())
        self.spinBox_pivot_table.setSizePolicy(sizePolicy3)
        self.spinBox_pivot_table.setFont(font3)
        self.spinBox_pivot_table.setMinimum(0)
        self.spinBox_pivot_table.setMaximum(10)
        self.spinBox_pivot_table.setValue(1)

        self.horizontalLayout_79.addWidget(self.spinBox_pivot_table)


        self.horizontalLayout_80.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.lb_sd_or_minmax_2 = QLabel(self.tab_8)
        self.lb_sd_or_minmax_2.setObjectName(u"lb_sd_or_minmax_2")
        self.lb_sd_or_minmax_2.setFont(font3)

        self.horizontalLayout_78.addWidget(self.lb_sd_or_minmax_2)

        self.comboBox_sd_or_se_pivot = QComboBox(self.tab_8)
        self.comboBox_sd_or_se_pivot.addItem("")
        self.comboBox_sd_or_se_pivot.addItem("")
        self.comboBox_sd_or_se_pivot.setObjectName(u"comboBox_sd_or_se_pivot")
        sizePolicy8.setHeightForWidth(self.comboBox_sd_or_se_pivot.sizePolicy().hasHeightForWidth())
        self.comboBox_sd_or_se_pivot.setSizePolicy(sizePolicy8)
        self.comboBox_sd_or_se_pivot.setFont(font3)

        self.horizontalLayout_78.addWidget(self.comboBox_sd_or_se_pivot)


        self.horizontalLayout_80.addLayout(self.horizontalLayout_78)


        self.verticalLayout_37.addLayout(self.horizontalLayout_80)

        self.line_2 = QFrame(self.tab_8)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font1)
        self.line_2.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_37.addWidget(self.line_2)

        self.btn_plot_and_save_pivot_table = QPushButton(self.tab_8)
        self.btn_plot_and_save_pivot_table.setObjectName(u"btn_plot_and_save_pivot_table")
        self.btn_plot_and_save_pivot_table.setFont(font3)
        self.btn_plot_and_save_pivot_table.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.verticalLayout_37.addWidget(self.btn_plot_and_save_pivot_table)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setSpacing(10)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.lb_sd_or_minmax_3 = QLabel(self.tab_8)
        self.lb_sd_or_minmax_3.setObjectName(u"lb_sd_or_minmax_3")
        sizePolicy3.setHeightForWidth(self.lb_sd_or_minmax_3.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_3.setSizePolicy(sizePolicy3)
        self.lb_sd_or_minmax_3.setFont(font3)

        self.horizontalLayout_85.addWidget(self.lb_sd_or_minmax_3)

        self.comboBox_correlation_person_or_not = QComboBox(self.tab_8)
        self.comboBox_correlation_person_or_not.addItem("")
        self.comboBox_correlation_person_or_not.addItem("")
        self.comboBox_correlation_person_or_not.addItem("")
        self.comboBox_correlation_person_or_not.setObjectName(u"comboBox_correlation_person_or_not")
        sizePolicy8.setHeightForWidth(self.comboBox_correlation_person_or_not.sizePolicy().hasHeightForWidth())
        self.comboBox_correlation_person_or_not.setSizePolicy(sizePolicy8)
        self.comboBox_correlation_person_or_not.setFont(font3)

        self.horizontalLayout_85.addWidget(self.comboBox_correlation_person_or_not)


        self.verticalLayout_37.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lb_sd_or_minmax_4 = QLabel(self.tab_8)
        self.lb_sd_or_minmax_4.setObjectName(u"lb_sd_or_minmax_4")
        sizePolicy3.setHeightForWidth(self.lb_sd_or_minmax_4.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_4.setSizePolicy(sizePolicy3)
        self.lb_sd_or_minmax_4.setFont(font3)

        self.horizontalLayout_26.addWidget(self.lb_sd_or_minmax_4)

        self.check_color_for_corr_pivot = QCheckBox(self.tab_8)
        self.check_color_for_corr_pivot.setObjectName(u"check_color_for_corr_pivot")
        self.check_color_for_corr_pivot.setEnabled(True)
        self.check_color_for_corr_pivot.setFont(font3)
        self.check_color_for_corr_pivot.setChecked(True)

        self.horizontalLayout_26.addWidget(self.check_color_for_corr_pivot)


        self.verticalLayout_37.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(10)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.lb_sd_or_minmax_5 = QLabel(self.tab_8)
        self.lb_sd_or_minmax_5.setObjectName(u"lb_sd_or_minmax_5")
        sizePolicy3.setHeightForWidth(self.lb_sd_or_minmax_5.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_5.setSizePolicy(sizePolicy3)
        self.lb_sd_or_minmax_5.setFont(font3)

        self.horizontalLayout_86.addWidget(self.lb_sd_or_minmax_5)

        self.comboBox_correlation_color_map = QComboBox(self.tab_8)
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
        sizePolicy8.setHeightForWidth(self.comboBox_correlation_color_map.sizePolicy().hasHeightForWidth())
        self.comboBox_correlation_color_map.setSizePolicy(sizePolicy8)
        self.comboBox_correlation_color_map.setFont(font3)

        self.horizontalLayout_86.addWidget(self.comboBox_correlation_color_map)


        self.verticalLayout_37.addLayout(self.horizontalLayout_86)

        self.btn_plot_and_save_corr_table = QPushButton(self.tab_8)
        self.btn_plot_and_save_corr_table.setObjectName(u"btn_plot_and_save_corr_table")
        self.btn_plot_and_save_corr_table.setFont(font3)
        self.btn_plot_and_save_corr_table.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.verticalLayout_37.addWidget(self.btn_plot_and_save_corr_table)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_37)

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
        self.lb_path_for_plot_3.setFont(font3)

        self.horizontalLayout_87.addWidget(self.lb_path_for_plot_3)

        self.path_for_catplot = QLineEdit(self.tab_10)
        self.path_for_catplot.setObjectName(u"path_for_catplot")
        self.path_for_catplot.setFont(font3)

        self.horizontalLayout_87.addWidget(self.path_for_catplot)


        self.formLayout_5.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_87)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.lb_exel_name_3 = QLabel(self.tab_10)
        self.lb_exel_name_3.setObjectName(u"lb_exel_name_3")
        self.lb_exel_name_3.setFont(font3)

        self.horizontalLayout_88.addWidget(self.lb_exel_name_3)

        self.comboBox_excel_catplot = QComboBox(self.tab_10)
        self.comboBox_excel_catplot.setObjectName(u"comboBox_excel_catplot")

        self.horizontalLayout_88.addWidget(self.comboBox_excel_catplot)


        self.formLayout_5.setLayout(1, QFormLayout.SpanningRole, self.horizontalLayout_88)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.lb_exel_name_4 = QLabel(self.tab_10)
        self.lb_exel_name_4.setObjectName(u"lb_exel_name_4")
        self.lb_exel_name_4.setFont(font3)

        self.horizontalLayout_99.addWidget(self.lb_exel_name_4)

        self.comboBox_excel_sheet_catplot = QComboBox(self.tab_10)
        self.comboBox_excel_sheet_catplot.setObjectName(u"comboBox_excel_sheet_catplot")

        self.horizontalLayout_99.addWidget(self.comboBox_excel_sheet_catplot)


        self.formLayout_5.setLayout(2, QFormLayout.SpanningRole, self.horizontalLayout_99)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.line_9 = QFrame(self.tab_10)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFont(font1)
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
        self.lb_hue_name_3.setFont(font3)

        self.horizontalLayout_89.addWidget(self.lb_hue_name_3)

        self.comboBox_catplot_x = QComboBox(self.tab_10)
        self.comboBox_catplot_x.setObjectName(u"comboBox_catplot_x")

        self.horizontalLayout_89.addWidget(self.comboBox_catplot_x)


        self.horizontalLayout_100.addLayout(self.horizontalLayout_89)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.lb_hue_name_7 = QLabel(self.tab_10)
        self.lb_hue_name_7.setObjectName(u"lb_hue_name_7")
        self.lb_hue_name_7.setFont(font3)

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
        self.lb_hue_name_4.setFont(font3)

        self.horizontalLayout_90.addWidget(self.lb_hue_name_4)

        self.comboBox_catplot_y = QComboBox(self.tab_10)
        self.comboBox_catplot_y.setObjectName(u"comboBox_catplot_y")

        self.horizontalLayout_90.addWidget(self.comboBox_catplot_y)


        self.horizontalLayout_101.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.lb_hue_name_6 = QLabel(self.tab_10)
        self.lb_hue_name_6.setObjectName(u"lb_hue_name_6")
        self.lb_hue_name_6.setFont(font3)

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
        self.lb_hue_name_5.setFont(font3)

        self.horizontalLayout_91.addWidget(self.lb_hue_name_5)

        self.comboBox_catplot_hue = QComboBox(self.tab_10)
        self.comboBox_catplot_hue.setObjectName(u"comboBox_catplot_hue")

        self.horizontalLayout_91.addWidget(self.comboBox_catplot_hue)


        self.horizontalLayout_102.addLayout(self.horizontalLayout_91)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.lb_hue_name_8 = QLabel(self.tab_10)
        self.lb_hue_name_8.setObjectName(u"lb_hue_name_8")
        self.lb_hue_name_8.setFont(font3)

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
        self.line_8.setFont(font1)
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
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_14.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_14.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_14.setFont(font3)

        self.horizontalLayout_93.addWidget(self.lb_color_pal_box_14)

        self.doubleSpinBox_catplot = QDoubleSpinBox(self.tab_10)
        self.doubleSpinBox_catplot.setObjectName(u"doubleSpinBox_catplot")
        self.doubleSpinBox_catplot.setFont(font3)
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
        sizePolicy2.setHeightForWidth(self.lb_color_pal_box_16.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_16.setSizePolicy(sizePolicy2)
        self.lb_color_pal_box_16.setFont(font3)

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
        sizePolicy3.setHeightForWidth(self.comboBox_color_catplot.sizePolicy().hasHeightForWidth())
        self.comboBox_color_catplot.setSizePolicy(sizePolicy3)
        self.comboBox_color_catplot.setFont(font3)

        self.horizontalLayout_105.addWidget(self.comboBox_color_catplot)


        self.horizontalLayout_106.addLayout(self.horizontalLayout_105)


        self.formLayout_5.setLayout(4, QFormLayout.SpanningRole, self.horizontalLayout_106)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.line_11 = QFrame(self.tab_10)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFont(font1)
        self.line_11.setStyleSheet(u"color: rgb(128, 160, 165);")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QFrame.HLine)

        self.verticalLayout_39.addWidget(self.line_11)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.lb_stattest_6 = QLabel(self.tab_10)
        self.lb_stattest_6.setObjectName(u"lb_stattest_6")
        self.lb_stattest_6.setFont(font3)

        self.horizontalLayout_94.addWidget(self.lb_stattest_6)

        self.check_stat_znachimost_catplot = QCheckBox(self.tab_10)
        self.check_stat_znachimost_catplot.setObjectName(u"check_stat_znachimost_catplot")
        self.check_stat_znachimost_catplot.setEnabled(True)
        self.check_stat_znachimost_catplot.setFont(font3)
        self.check_stat_znachimost_catplot.setChecked(True)

        self.horizontalLayout_94.addWidget(self.check_stat_znachimost_catplot)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.lb_stattest_5 = QLabel(self.tab_10)
        self.lb_stattest_5.setObjectName(u"lb_stattest_5")
        self.lb_stattest_5.setEnabled(True)
        self.lb_stattest_5.setFont(font3)

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
        self.comboBox_stat_test_catplot.setFont(font3)

        self.horizontalLayout_92.addWidget(self.comboBox_stat_test_catplot)


        self.horizontalLayout_94.addLayout(self.horizontalLayout_92)


        self.verticalLayout_39.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.lb_stattest_9 = QLabel(self.tab_10)
        self.lb_stattest_9.setObjectName(u"lb_stattest_9")
        self.lb_stattest_9.setEnabled(True)
        self.lb_stattest_9.setFont(font3)

        self.horizontalLayout_108.addWidget(self.lb_stattest_9)

        self.comboBox_catplot_stat_formatt = QComboBox(self.tab_10)
        self.comboBox_catplot_stat_formatt.addItem("")
        self.comboBox_catplot_stat_formatt.addItem("")
        self.comboBox_catplot_stat_formatt.addItem("")
        self.comboBox_catplot_stat_formatt.setObjectName(u"comboBox_catplot_stat_formatt")
        self.comboBox_catplot_stat_formatt.setEnabled(True)
        self.comboBox_catplot_stat_formatt.setFont(font3)

        self.horizontalLayout_108.addWidget(self.comboBox_catplot_stat_formatt)


        self.verticalLayout_39.addLayout(self.horizontalLayout_108)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.lb_stattest_10 = QLabel(self.tab_10)
        self.lb_stattest_10.setObjectName(u"lb_stattest_10")
        self.lb_stattest_10.setEnabled(True)
        self.lb_stattest_10.setFont(font3)

        self.horizontalLayout_109.addWidget(self.lb_stattest_10)

        self.comboBox_catplot_mult_stat = QComboBox(self.tab_10)
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.setObjectName(u"comboBox_catplot_mult_stat")
        self.comboBox_catplot_mult_stat.setEnabled(True)
        self.comboBox_catplot_mult_stat.setFont(font3)

        self.horizontalLayout_109.addWidget(self.comboBox_catplot_mult_stat)


        self.verticalLayout_39.addLayout(self.horizontalLayout_109)

        self.line_10 = QFrame(self.tab_10)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFont(font1)
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
        self.lb_stattest_7.setFont(font3)

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
        self.comboBox_template_catplot.setFont(font3)

        self.horizontalLayout_98.addWidget(self.comboBox_template_catplot)


        self.horizontalLayout_104.addLayout(self.horizontalLayout_98)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.lb_color_pal_box_15 = QLabel(self.tab_10)
        self.lb_color_pal_box_15.setObjectName(u"lb_color_pal_box_15")
        sizePolicy4.setHeightForWidth(self.lb_color_pal_box_15.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_15.setSizePolicy(sizePolicy4)
        self.lb_color_pal_box_15.setFont(font3)

        self.horizontalLayout_103.addWidget(self.lb_color_pal_box_15)

        self.comboBox_catplot_SD_or_not = QComboBox(self.tab_10)
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.setObjectName(u"comboBox_catplot_SD_or_not")
        sizePolicy10.setHeightForWidth(self.comboBox_catplot_SD_or_not.sizePolicy().hasHeightForWidth())
        self.comboBox_catplot_SD_or_not.setSizePolicy(sizePolicy10)
        self.comboBox_catplot_SD_or_not.setFont(font3)

        self.horizontalLayout_103.addWidget(self.comboBox_catplot_SD_or_not)


        self.horizontalLayout_104.addLayout(self.horizontalLayout_103)


        self.formLayout_5.setLayout(6, QFormLayout.SpanningRole, self.horizontalLayout_104)

        self.btn_plot_and_save_catplot = QPushButton(self.tab_10)
        self.btn_plot_and_save_catplot.setObjectName(u"btn_plot_and_save_catplot")
        self.btn_plot_and_save_catplot.setFont(font3)
        self.btn_plot_and_save_catplot.setStyleSheet(u"background-color: rgba(128, 160, 165, 50);\n"
"border: 3px solid rgb(128, 160, 165);\n"
"border-radius: 10px;")

        self.formLayout_5.setWidget(7, QFormLayout.SpanningRole, self.btn_plot_and_save_catplot)

        self.tabWidget_2.addTab(self.tab_10, "")

        self.horizontalLayout_64.addWidget(self.tabWidget_2)

        self.Lab_stuff.addTab(self.tabWidgetPage4, "")

        self.gridLayout.addWidget(self.Lab_stuff, 0, 0, 1, 2)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(9)
        font7.setBold(True)
        self.label_10.setFont(font7)
        self.label_10.setStyleSheet(u"color: rgb(128, 160, 165);")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.comboBox_style_sheet = QComboBox(self.centralwidget)
        self.comboBox_style_sheet.addItem("")
        self.comboBox_style_sheet.addItem("")
        self.comboBox_style_sheet.addItem("")
        self.comboBox_style_sheet.addItem("")
        self.comboBox_style_sheet.setObjectName(u"comboBox_style_sheet")
        self.comboBox_style_sheet.setFont(font7)
        self.comboBox_style_sheet.setStyleSheet(u"color: rgb(128, 160, 165);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.comboBox_style_sheet, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.check_change_corr_fig_down_limit.toggled.connect(self.doubleSpinBox_corr_figs.setEnabled)
        self.vibros_delete.toggled.connect(self.iqr_vibros.setEnabled)
        self.check_approx_agg.toggled.connect(self.check_figs_for_agg.setEnabled)
        self.check_approx_deform.toggled.connect(self.check_for_deform.setEnabled)
        self.check_color_for_corr_pivot.toggled.connect(self.comboBox_correlation_color_map.setEnabled)
        self.check_stat_znachimost.toggled.connect(self.comboBox_stat_test.setEnabled)
        self.check_stat_znachimost.toggled.connect(self.comboBox_alter_hep.setEnabled)
        self.check_stat_znachimost_catplot.toggled.connect(self.comboBox_stat_test_catplot.setEnabled)
        self.check_stat_znachimost_catplot.toggled.connect(self.comboBox_catplot_stat_formatt.setEnabled)
        self.check_stat_znachimost_catplot.toggled.connect(self.comboBox_catplot_mult_stat.setEnabled)

        self.Lab_stuff.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432", None))
        self.check_approx_agg.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u0434\u043b\u044f agg", None))
        self.check_figs_for_agg.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0439 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:18pt; color:#202122;\">\u03c4</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:18pt; color:#202122; vertical-align:sub;\">1</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 3D \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:18pt; color:#202122;\">\u03c4</span><span style=\" font-family:'palatino linotype','new athena unicode','athena','gentium','code2000','serif'; font-size:18pt; color:#202122; vertical-align:sub;\">2</span></p></body></html>", None))
        self.tua_1_agg.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.tau_2_agg.setText(QCoreApplication.translate("MainWindow", u"200", None))
#if QT_CONFIG(tooltip)
        self.lb_path.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u043e \u0434\u0430\u043d\u043d\u043e\u043c\u0443 \u043f\u0443\u0442\u0438 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c 3 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 (agg, stress, deform), \u0435\u0441\u043b\u0438 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a 1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c\u0438", None))
        self.main_path.setText("")
        self.check_approx_deform.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u0434\u043b\u044f deform", None))
        self.check_for_deform.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421 \u043a\u0430\u043a\u043e\u0439 \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c\u044e \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 -- \u0435\u0441\u043b\u0438 \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c \u043d\u0435 \u043f\u043e\u0434\u0445\u043e\u0434\u0438\u0442, \u0442\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0432\u044b\u043a\u0438\u0434\u044b\u0432\u0430\u0435\u0442 \u0442\u043e\u0447\u043a\u0443 \u0441 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0439 \u043e\u0448\u0438\u0431\u043a\u043e\u0439 \u0438 \u0437\u0430\u043d\u043e\u0432\u043e \u043f\u043e\u0432\u0442\u043e\u0440\u044f\u0435\u0442 \u0440\u0430\u0441\u0447\u0435\u0442</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">R</span><span style=\" font-size:14pt; vertical-align:super;\">2</span></p></body></html>", None))
        self.r2_def.setText(QCoreApplication.translate("MainWindow", u"0.95", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0442\u043e\u0447\u0435\u043a \u0442\u043e\u0447\u043d\u043e \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0434\u043b\u044f \u0430\u043f\u0440\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438. \u0415\u0441\u043b\u0438 R<span style=\" vertical-align:super;\">2</span> \u0431\u0443\u0434\u0435\u0442 \u043c\u0435\u043d\u044c\u0448\u0435, \u0447\u0435\u043c \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u043d\u044b\u0439, \u043d\u043e \u0442\u043e\u0447\u0435\u043a \u0443\u0436\u0435 \u043c\u0435\u043d\u044c\u0448\u0435, \u0442\u043e \u0434\u0430\u043b\u044c\u043d\u0435\u0439\u0448\u0435\u0433\u043e \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u0438\u044f \u043d\u0435 \u0431\u0443\u0434\u0435\u0442. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>N<span style=\" vertical-align:sub;\">max</span></p></body></html>", None))
        self.btn_save_exel_csv.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.check_save_exel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b", None))
        self.check_save_csv.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c csv \u0444\u0430\u0439\u043b(\u044b)", None))
#if QT_CONFIG(tooltip)
        self.lb_separator.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u042d\u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0438 \u0444\u0430\u0439\u043b\u043e\u0432. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u0444\u0430\u0439\u043b\u044b \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c: &quot;NAME-##-#&quot;, \u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c &quot;-&quot;.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_separator.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.separator_for_data.setText("")
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u043f\u0430\u043f\u043a\u0430 \u0441 \u043f\u0430\u043f\u043a\u0430\u043c\u0438, \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0435\u0441\u0442\u044c 3 \u043f\u0430\u043f\u043a\u0438, \u0442\u043e \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c 2, \u0438 \u0442.\u0434.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a           ", None))
        self.check_stat_for_column.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430\u043c", None))
#if QT_CONFIG(tooltip)
        self.vibros_delete.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u044b\u0431\u0440\u043e\u0441\u044b \u0443\u0431\u0438\u0440\u0430\u044e\u0442\u0441\u044f \u043f\u043e \u0438\u043d\u0442\u0435\u0440\u043a\u0430\u043d\u0442\u0438\u043b\u044c\u043d\u043e\u043c\u0443 \u0440\u0430\u0437\u043c\u0430\u0445\u0443 -- \u0441\u043c. \u0438\u043d\u0444\u0443 \u043f\u043e \u0442\u043e\u043c\u0443, \u0447\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u0432\u044b\u0431\u0440\u043e\u0441\u044b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vibros_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c \u0432\u044b\u0431\u0440\u043e\u0441\u044b", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0438\u043d\u0442\u0435\u0440\u043a\u0432\u0430\u0440\u0442\u0438\u043b\u044c\u043d\u044b\u0445 \u0440\u0430\u0437\u043c\u0430\u0445\u0430", None))
        self.check_agg.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 agg", None))
        self.check_stress.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 stress", None))
        self.check_deform.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 deform", None))
#if QT_CONFIG(tooltip)
        self.btn_sort_data_RheoScan.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">\u0415\u0441\u043b\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u0440\u043e\u0441\u0442\u043e \u043d\u0430\u0433\u0440\u043e\u043c\u043e\u0436\u0434\u0435\u043d\u044b \u0432 \u043e\u0434\u043d\u0443 \u043f\u0430\u043f\u043a\u0443, \u0442\u043e \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u044d\u0442\u0443 \u043a\u043d\u043e\u043f\u043a\u0443. \u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0442\u0443\u0442</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_sort_data_RheoScan.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0435\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c", None))
        self.Lab_stuff.setTabText(self.Lab_stuff.indexOf(self.tabWidgetPage1), QCoreApplication.translate("MainWindow", u" RheoScan", None))
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
        self.btn_biola.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435, \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0438\u0441\u0443\u043d\u043a\u0438 \u0438 excel \u0444\u0430\u0439\u043b", None))
        self.btn_biola_concentration.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430 pdf", None))
        self.lb_path_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0444\u0430\u0439\u043b\u043e\u043c", None))
#if QT_CONFIG(tooltip)
        self.path_for_biola.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0444\u0430\u0439\u043b\u043e\u043c txt, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0431\u044b\u043b \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d \u0438\u0437 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0434\u043b\u044f \u0411\u0438\u043e\u043b\u044b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.path_for_biola.setText("")
        self.lb_path_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0433\u0440\u0430\u043c\u043c (txt)", None))
        self.lb_path_16.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u0438 \u0442\u0440\u043e\u043c\u0431\u043e\u0446\u0438\u0442\u043e\u0432 (pdf)", None))
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

        self.lb_color_pal_box_11.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a", None))
        self.comboBox_Biola_language.setItemText(0, QCoreApplication.translate("MainWindow", u"Rus", None))
        self.comboBox_Biola_language.setItemText(1, QCoreApplication.translate("MainWindow", u"Eng", None))

#if QT_CONFIG(tooltip)
        self.check_setka_biola.setToolTip(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u0444\u043b\u0430\u0436\u043a\u0430 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0431\u0443\u0434\u0435\u0442 \u0442\u0430\u043a\u0438\u043c, \u043a\u0430\u043a\u043e\u0439 \u043e\u043d \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.check_setka_biola.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0442\u043a\u0430", None))
        self.Lab_stuff.setTabText(self.Lab_stuff.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u0411\u0438\u043e\u043b\u0430", None))
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
#if QT_CONFIG(tooltip)
        self.lb_path_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0441\u0435 \u0441\u0438\u043b\u044b \u043c\u0435\u0436\u0434\u0443 \u044d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u0430\u043c\u0438 \u0438 \u044d\u043d\u0434\u043e\u0442\u0435\u043b\u0438\u0435\u043c \u0447\u0435\u0440\u0435\u0437 \u044d\u0442\u043e \u043f\u0440\u043e\u0433\u043e\u043d\u044f\u044e\u0442\u0441\u044f. \u0421\u0438\u043b\u044b  \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u044e\u0442\u0441\u044f End...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0443\u0447\u043e\u043a", None))
#if QT_CONFIG(tooltip)
        self.lb_path_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_7.setText(QCoreApplication.translate("MainWindow", u"a", None))
#if QT_CONFIG(tooltip)
        self.lb_path_8.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_8.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.lb_path_12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.lb_path_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0441\u0435 \u0441\u0438\u043b\u044b \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u0438 \u0434\u0435\u0437\u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u0447\u0435\u0440\u0435\u0437 \u044d\u0442\u043e \u043f\u0440\u043e\u0433\u043e\u043d\u044f\u044e\u0442\u0441\u044f. \u0421\u0438\u043b\u044b \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u044e\u0442\u0441\u044f FA..., FD...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0443\u0447\u043e\u043a", None))
#if QT_CONFIG(tooltip)
        self.lb_path_9.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_9.setText(QCoreApplication.translate("MainWindow", u"a", None))
#if QT_CONFIG(tooltip)
        self.lb_path_10.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_10.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.lb_path_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438", None))
        self.btn_LT.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b", None))
        self.Lab_stuff.setTabText(self.Lab_stuff.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0437\u0435\u0440\u043d\u044b\u0439 \u043f\u0438\u043d\u0446\u0435\u0442", None))
#if QT_CONFIG(tooltip)
        self.lb_path_for_plot.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443", None))
        self.path_for_plot.setText("")
        self.lb_exel_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430", None))
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

#if QT_CONFIG(tooltip)
        self.lb_color_for_box.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u043b\u0438 \u043f\u043e\u043b\u0435 \u043f\u0443\u0441\u0442\u043e\u0435, \u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u0446\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430. \u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0446\u0432\u0435\u0442 \u0431\u044b\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX: #......</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_color_for_box.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u044f box (HEX)", None))
#if QT_CONFIG(tooltip)
        self.lb_color_forpoints.setToolTip(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u043b\u0438 \u043f\u043e\u043b\u0435 \u043f\u0443\u0441\u0442\u043e\u0435, \u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u0446\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430. \u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0446\u0432\u0435\u0442 \u0431\u044b\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX: #......", None))
#endif // QT_CONFIG(tooltip)
        self.lb_color_forpoints.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u0442\u043e\u0447\u0435\u043a (HEX)", None))
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
        self.lb_size_corr_matrix.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0440\u0438\u0441\u0443\u043d\u043a\u0430", None))
        self.corr_mat_figsize.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.lb_font_in.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0444 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439", None))
        self.font_for_in.setText(QCoreApplication.translate("MainWindow", u"1.3", None))
        self.lb_font_out.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430", None))
        self.font_for_out.setText(QCoreApplication.translate("MainWindow", u"26", None))
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
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043a\u0440\u043e\u0440\u0435\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.lb_path_for_plot_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443", None))
        self.path_for_pivot_table.setText("")
        self.lb_exel_name_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430", None))
#if QT_CONFIG(tooltip)
        self.lb_hue_name_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u0435\u043d\u043d\u043e \u043f\u043e\u0441\u043b\u0435 \u044d\u0442\u043e\u0433\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043e\u043b\u0436\u043d\u044b \u0438\u0434\u0442\u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.lb_hue_name_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f", None))
        self.lb_color_pal_box_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0433\u043b\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0434\u043e \u0437\u043d\u0430\u043a\u0430 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439", None))
        self.lb_sd_or_minmax_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439", None))
        self.comboBox_sd_or_se_pivot.setItemText(0, QCoreApplication.translate("MainWindow", u"SD", None))
        self.comboBox_sd_or_se_pivot.setItemText(1, QCoreApplication.translate("MainWindow", u"SE", None))

        self.btn_plot_and_save_pivot_table.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0432\u043e\u0434\u043d\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.lb_sd_or_minmax_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043f\u043e", None))
        self.comboBox_correlation_person_or_not.setItemText(0, QCoreApplication.translate("MainWindow", u"pearson", None))
        self.comboBox_correlation_person_or_not.setItemText(1, QCoreApplication.translate("MainWindow", u"kendall", None))
        self.comboBox_correlation_person_or_not.setItemText(2, QCoreApplication.translate("MainWindow", u"spearman", None))

        self.lb_sd_or_minmax_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u044f\u0447\u0435\u0439\u043a\u0438 \u0446\u0432\u0435\u0442\u043e\u043c", None))
        self.check_color_for_corr_pivot.setText("")
        self.lb_sd_or_minmax_5.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u0441\u0445\u0435\u043c\u0430", None))
        self.comboBox_correlation_color_map.setItemText(0, QCoreApplication.translate("MainWindow", u"coolwarm", None))
        self.comboBox_correlation_color_map.setItemText(1, QCoreApplication.translate("MainWindow", u"YlGn", None))
        self.comboBox_correlation_color_map.setItemText(2, QCoreApplication.translate("MainWindow", u"BuGn", None))
        self.comboBox_correlation_color_map.setItemText(3, QCoreApplication.translate("MainWindow", u"GnBu", None))
        self.comboBox_correlation_color_map.setItemText(4, QCoreApplication.translate("MainWindow", u"bwr", None))
        self.comboBox_correlation_color_map.setItemText(5, QCoreApplication.translate("MainWindow", u"seismic", None))
        self.comboBox_correlation_color_map.setItemText(6, QCoreApplication.translate("MainWindow", u"PiYG", None))
        self.comboBox_correlation_color_map.setItemText(7, QCoreApplication.translate("MainWindow", u"RdGy", None))
        self.comboBox_correlation_color_map.setItemText(8, QCoreApplication.translate("MainWindow", u"seismic", None))
        self.comboBox_correlation_color_map.setItemText(9, QCoreApplication.translate("MainWindow", u"hot", None))
        self.comboBox_correlation_color_map.setItemText(10, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.comboBox_correlation_color_map.setItemText(11, QCoreApplication.translate("MainWindow", u"gist_heat", None))

        self.btn_plot_and_save_corr_table.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0443\u044e \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u043f\u043e \u0432\u0441\u0435\u043c \u0434\u0430\u043d\u043d\u044b\u043c", None))
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
        self.Lab_stuff.setTabText(self.Lab_stuff.indexOf(self.tabWidgetPage4), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0440\u043c\u043e\u043b\u0438\u043d\u0441\u043a\u0438\u0439 \u041f\u0435\u0442\u0440 \u2014 \u0432\u0435\u0440\u0441\u0438\u044f 3.0", None))
        self.comboBox_style_sheet.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.comboBox_style_sheet.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.comboBox_style_sheet.setItemText(2, QCoreApplication.translate("MainWindow", u"Mac", None))
        self.comboBox_style_sheet.setItemText(3, QCoreApplication.translate("MainWindow", u"Aqua", None))

    # retranslateUi

