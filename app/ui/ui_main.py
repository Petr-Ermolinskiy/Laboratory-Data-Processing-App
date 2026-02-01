# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QCalendarWidget,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QStatusBar,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QToolBox,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 773)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_style_sheet = QComboBox(self.centralwidget)
        self.comboBox_style_sheet.addItem("")
        self.comboBox_style_sheet.addItem("")
        self.comboBox_style_sheet.addItem("")
        self.comboBox_style_sheet.setObjectName("comboBox_style_sheet")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_style_sheet.sizePolicy().hasHeightForWidth())
        self.comboBox_style_sheet.setSizePolicy(sizePolicy1)
        self.comboBox_style_sheet.setMinimumSize(QSize(120, 0))
        font = QFont()
        font.setFamilies(["Segoe UI"])
        font.setPointSize(9)
        font.setBold(True)
        self.comboBox_style_sheet.setFont(font)
        self.comboBox_style_sheet.setStyleSheet(
            "color: rgb(128, 160, 165);\nbackground-color: rgba(255, 255, 255, 0);"
        )

        self.gridLayout.addWidget(self.comboBox_style_sheet, 1, 1, 1, 1, Qt.AlignRight)

        self.horizontalLayout_167 = QHBoxLayout()
        self.horizontalLayout_167.setObjectName("horizontalLayout_167")
        self.label_info = QLabel(self.centralwidget)
        self.label_info.setObjectName("label_info")
        self.label_info.setFont(font)
        self.label_info.setStyleSheet("color: rgb(128, 160, 165);")

        self.horizontalLayout_167.addWidget(self.label_info)

        self.label_version = QLabel(self.centralwidget)
        self.label_version.setObjectName("label_version")
        font1 = QFont()
        font1.setBold(True)
        self.label_version.setFont(font1)
        self.label_version.setStyleSheet("color: rgb(128, 160, 165);")

        self.horizontalLayout_167.addWidget(self.label_version)

        self.gridLayout.addLayout(self.horizontalLayout_167, 1, 0, 1, 1)

        self.Lab_stuff = QTabWidget(self.centralwidget)
        self.Lab_stuff.setObjectName("Lab_stuff")
        sizePolicy.setHeightForWidth(self.Lab_stuff.sizePolicy().hasHeightForWidth())
        self.Lab_stuff.setSizePolicy(sizePolicy)
        self.Lab_stuff.setMaximumSize(QSize(16777215, 700))
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
        font2 = QFont()
        font2.setFamilies(["Segoe UI"])
        font2.setPointSize(14)
        self.Lab_stuff.setFont(font2)
        self.Lab_stuff.setStyleSheet("/*background-color: rgb(249, 249, 249);")
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.gridLayout_5 = QGridLayout(self.tabWidgetPage1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_save_exel_csv = QPushButton(self.tabWidgetPage1)
        self.btn_save_exel_csv.setObjectName("btn_save_exel_csv")
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
        font3 = QFont()
        font3.setFamilies(["Segoe UI"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.btn_save_exel_csv.setFont(font3)
        self.btn_save_exel_csv.setAutoFillBackground(False)
        self.btn_save_exel_csv.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )
        self.btn_save_exel_csv.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_save_exel_csv, 16, 0, 1, 1)

        self.line_14 = QFrame(self.tabWidgetPage1)
        self.line_14.setObjectName("line_14")
        font4 = QFont()
        font4.setFamilies(["Segoe UI"])
        font4.setPointSize(10)
        self.line_14.setFont(font4)
        self.line_14.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_14.setFrameShadow(QFrame.Plain)
        self.line_14.setLineWidth(3)
        self.line_14.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_14, 1, 0, 1, 1)

        self.line_3 = QFrame(self.tabWidgetPage1)
        self.line_3.setObjectName("line_3")
        self.line_3.setFont(font4)
        self.line_3.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_3, 8, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(13, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lb_path = QLabel(self.tabWidgetPage1)
        self.lb_path.setObjectName("lb_path")
        font5 = QFont()
        font5.setFamilies(["Segoe UI"])
        font5.setPointSize(11)
        self.lb_path.setFont(font5)

        self.horizontalLayout_7.addWidget(self.lb_path)

        self.main_path = QLineEdit(self.tabWidgetPage1)
        self.main_path.setObjectName("main_path")
        font6 = QFont()
        font6.setPointSize(11)
        self.main_path.setFont(font6)

        self.horizontalLayout_7.addWidget(self.main_path)

        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.comboBox_RheoScan_path_save = QComboBox(self.tabWidgetPage1)
        self.comboBox_RheoScan_path_save.addItem("")
        self.comboBox_RheoScan_path_save.addItem("")
        self.comboBox_RheoScan_path_save.setObjectName("comboBox_RheoScan_path_save")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.comboBox_RheoScan_path_save.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_RheoScan_path_save.setSizePolicy(sizePolicy2)
        self.comboBox_RheoScan_path_save.setFont(font6)

        self.horizontalLayout_71.addWidget(self.comboBox_RheoScan_path_save)

        self.check_approx_deform_raw_data = QCheckBox(self.tabWidgetPage1)
        self.check_approx_deform_raw_data.setObjectName("check_approx_deform_raw_data")
        self.check_approx_deform_raw_data.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.check_approx_deform_raw_data.sizePolicy().hasHeightForWidth()
        )
        self.check_approx_deform_raw_data.setSizePolicy(sizePolicy3)
        self.check_approx_deform_raw_data.setFont(font5)

        self.horizontalLayout_71.addWidget(self.check_approx_deform_raw_data, 0, Qt.AlignHCenter)

        self.gridLayout_3.addLayout(self.horizontalLayout_71, 14, 0, 1, 1)

        self.line = QFrame(self.tabWidgetPage1)
        self.line.setObjectName("line")
        self.line.setFont(font4)
        self.line.setStyleSheet("color: rgb(128, 160, 165);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line, 11, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget = QWidget(self.tabWidgetPage1)
        self.widget.setObjectName("widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.label_20.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)
        self.label_20.setMaximumSize(QSize(16777215, 61))
        font7 = QFont()
        font7.setFamilies(["Segoe UI"])
        font7.setPointSize(12)
        font7.setStrikeOut(False)
        font7.setHintingPreference(QFont.PreferNoHinting)
        self.label_20.setFont(font7)
        self.label_20.setTextFormat(Qt.RichText)
        self.label_20.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setMargin(0)
        self.label_20.setIndent(1)

        self.horizontalLayout_2.addWidget(self.label_20)

        self.tua_1_agg = QSpinBox(self.widget)
        self.tua_1_agg.setObjectName("tua_1_agg")
        self.tua_1_agg.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.tua_1_agg.sizePolicy().hasHeightForWidth())
        self.tua_1_agg.setSizePolicy(sizePolicy2)
        self.tua_1_agg.setFont(font6)
        self.tua_1_agg.setMinimum(1)
        self.tua_1_agg.setMaximum(200)
        self.tua_1_agg.setValue(20)

        self.horizontalLayout_2.addWidget(self.tua_1_agg)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.label_21.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy5)
        self.label_21.setMaximumSize(QSize(16777215, 61))
        font8 = QFont()
        font8.setFamilies(["Segoe UI"])
        font8.setPointSize(12)
        self.label_21.setFont(font8)
        self.label_21.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_21.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_21)

        self.tua_2_agg = QSpinBox(self.widget)
        self.tua_2_agg.setObjectName("tua_2_agg")
        self.tua_2_agg.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.tua_2_agg.sizePolicy().hasHeightForWidth())
        self.tua_2_agg.setSizePolicy(sizePolicy2)
        self.tua_2_agg.setFont(font6)
        self.tua_2_agg.setMinimum(1)
        self.tua_2_agg.setMaximum(10000)
        self.tua_2_agg.setValue(200)

        self.horizontalLayout_3.addWidget(self.tua_2_agg)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4.addWidget(self.widget)

        self.widget1 = QWidget(self.tabWidgetPage1)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.label_23 = QLabel(self.widget1)
        self.label_23.setObjectName("label_23")
        self.label_23.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy6)
        self.label_23.setFont(font6)
        self.label_23.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_23)

        self.r2_def = QDoubleSpinBox(self.widget1)
        self.r2_def.setObjectName("r2_def")
        self.r2_def.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.r2_def.sizePolicy().hasHeightForWidth())
        self.r2_def.setSizePolicy(sizePolicy2)
        self.r2_def.setFont(font6)
        self.r2_def.setDecimals(3)
        self.r2_def.setMinimum(0.600000000000000)
        self.r2_def.setMaximum(0.999000000000000)
        self.r2_def.setSingleStep(0.001000000000000)
        self.r2_def.setValue(0.950000000000000)

        self.horizontalLayout.addWidget(self.r2_def, 0, Qt.AlignRight)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName("horizontalLayout_118")
        self.label_18 = QLabel(self.widget1)
        self.label_18.setObjectName("label_18")
        self.label_18.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy6)
        self.label_18.setFont(font6)
        self.label_18.setWordWrap(True)

        self.horizontalLayout_118.addWidget(self.label_18)

        self.spinBox_n_max_deform = QSpinBox(self.widget1)
        self.spinBox_n_max_deform.setObjectName("spinBox_n_max_deform")
        self.spinBox_n_max_deform.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.spinBox_n_max_deform.sizePolicy().hasHeightForWidth())
        self.spinBox_n_max_deform.setSizePolicy(sizePolicy2)
        self.spinBox_n_max_deform.setFont(font6)
        self.spinBox_n_max_deform.setMinimum(3)
        self.spinBox_n_max_deform.setMaximum(13)
        self.spinBox_n_max_deform.setValue(10)

        self.horizontalLayout_118.addWidget(self.spinBox_n_max_deform)

        self.verticalLayout_3.addLayout(self.horizontalLayout_118)

        self.horizontalLayout_4.addWidget(self.widget1)

        self.gridLayout_3.addLayout(self.horizontalLayout_4, 7, 0, 1, 1)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setObjectName("horizontalLayout_117")
        self.dfd = QFrame(self.tabWidgetPage1)
        self.dfd.setObjectName("dfd")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.dfd.sizePolicy().hasHeightForWidth())
        self.dfd.setSizePolicy(sizePolicy7)
        self.dfd.setStyleSheet(
            "QFrame#dfd{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_5 = QVBoxLayout(self.dfd)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.check_approx_agg = QCheckBox(self.dfd)
        self.check_approx_agg.setObjectName("check_approx_agg")
        self.check_approx_agg.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.check_approx_agg.sizePolicy().hasHeightForWidth())
        self.check_approx_agg.setSizePolicy(sizePolicy8)
        self.check_approx_agg.setFont(font5)
        self.check_approx_agg.setChecked(False)

        self.verticalLayout_5.addWidget(self.check_approx_agg)

        self.check_figs_for_agg = QCheckBox(self.dfd)
        self.check_figs_for_agg.setObjectName("check_figs_for_agg")
        self.check_figs_for_agg.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.check_figs_for_agg.sizePolicy().hasHeightForWidth())
        self.check_figs_for_agg.setSizePolicy(sizePolicy8)
        self.check_figs_for_agg.setFont(font5)

        self.verticalLayout_5.addWidget(self.check_figs_for_agg)

        self.horizontalLayout_117.addWidget(self.dfd)

        self.qwe = QFrame(self.tabWidgetPage1)
        self.qwe.setObjectName("qwe")
        sizePolicy3.setHeightForWidth(self.qwe.sizePolicy().hasHeightForWidth())
        self.qwe.setSizePolicy(sizePolicy3)
        self.qwe.setStyleSheet(
            "QFrame#qwe{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_2 = QVBoxLayout(self.qwe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.check_approx_deform = QCheckBox(self.qwe)
        self.check_approx_deform.setObjectName("check_approx_deform")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.check_approx_deform.sizePolicy().hasHeightForWidth())
        self.check_approx_deform.setSizePolicy(sizePolicy9)
        self.check_approx_deform.setFont(font5)

        self.verticalLayout_2.addWidget(self.check_approx_deform)

        self.check_for_deform = QCheckBox(self.qwe)
        self.check_for_deform.setObjectName("check_for_deform")
        self.check_for_deform.setEnabled(False)
        self.check_for_deform.setFont(font5)

        self.verticalLayout_2.addWidget(self.check_for_deform)

        self.horizontalLayout_117.addWidget(self.qwe)

        self.gridLayout_3.addLayout(self.horizontalLayout_117, 5, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.check_stat_for_column = QCheckBox(self.tabWidgetPage1)
        self.check_stat_for_column.setObjectName("check_stat_for_column")
        self.check_stat_for_column.setFont(font5)

        self.horizontalLayout_27.addWidget(self.check_stat_for_column)

        self.vibros_delete = QCheckBox(self.tabWidgetPage1)
        self.vibros_delete.setObjectName("vibros_delete")
        self.vibros_delete.setFont(font5)
        self.vibros_delete.setChecked(False)

        self.horizontalLayout_27.addWidget(self.vibros_delete)

        self.iqr_vibros = QDoubleSpinBox(self.tabWidgetPage1)
        self.iqr_vibros.setObjectName("iqr_vibros")
        self.iqr_vibros.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.iqr_vibros.sizePolicy().hasHeightForWidth())
        self.iqr_vibros.setSizePolicy(sizePolicy2)
        self.iqr_vibros.setFont(font6)
        self.iqr_vibros.setDecimals(1)
        self.iqr_vibros.setMinimum(0.500000000000000)
        self.iqr_vibros.setMaximum(5.000000000000000)
        self.iqr_vibros.setSingleStep(0.500000000000000)
        self.iqr_vibros.setValue(1.500000000000000)

        self.horizontalLayout_27.addWidget(self.iqr_vibros)

        self.label_11 = QLabel(self.tabWidgetPage1)
        self.label_11.setObjectName("label_11")
        self.label_11.setEnabled(False)
        self.label_11.setFont(font6)

        self.horizontalLayout_27.addWidget(self.label_11)

        self.gridLayout_3.addLayout(self.horizontalLayout_27, 9, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_sort_data_RheoScan = QPushButton(self.tabWidgetPage1)
        self.btn_sort_data_RheoScan.setObjectName("btn_sort_data_RheoScan")
        sizePolicy2.setHeightForWidth(self.btn_sort_data_RheoScan.sizePolicy().hasHeightForWidth())
        self.btn_sort_data_RheoScan.setSizePolicy(sizePolicy2)
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
        self.btn_sort_data_RheoScan.setFont(font3)
        self.btn_sort_data_RheoScan.setAutoFillBackground(False)
        self.btn_sort_data_RheoScan.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )
        self.btn_sort_data_RheoScan.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_sort_data_RheoScan)

        self.label = QLabel(self.tabWidgetPage1)
        self.label.setObjectName("label")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy10)
        self.label.setFont(font5)

        self.horizontalLayout_5.addWidget(self.label)

        self.spinBox_level = QSpinBox(self.tabWidgetPage1)
        self.spinBox_level.setObjectName("spinBox_level")
        sizePolicy2.setHeightForWidth(self.spinBox_level.sizePolicy().hasHeightForWidth())
        self.spinBox_level.setSizePolicy(sizePolicy2)
        self.spinBox_level.setFont(font5)
        self.spinBox_level.setMinimum(1)
        self.spinBox_level.setMaximum(5)
        self.spinBox_level.setValue(1)

        self.horizontalLayout_5.addWidget(self.spinBox_level)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.line_4 = QFrame(self.tabWidgetPage1)
        self.line_4.setObjectName("line_4")
        self.line_4.setFont(font4)
        self.line_4.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_4, 15, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.check_save_exel = QCheckBox(self.tabWidgetPage1)
        self.check_save_exel.setObjectName("check_save_exel")
        self.check_save_exel.setFont(font5)
        self.check_save_exel.setChecked(True)

        self.horizontalLayout_8.addWidget(self.check_save_exel)

        self.check_save_csv = QCheckBox(self.tabWidgetPage1)
        self.check_save_csv.setObjectName("check_save_csv")
        self.check_save_csv.setFont(font5)

        self.horizontalLayout_8.addWidget(self.check_save_csv)

        self.check_save_RheoScan_overall = QCheckBox(self.tabWidgetPage1)
        self.check_save_RheoScan_overall.setObjectName("check_save_RheoScan_overall")
        self.check_save_RheoScan_overall.setFont(font5)
        self.check_save_RheoScan_overall.setChecked(False)

        self.horizontalLayout_8.addWidget(self.check_save_RheoScan_overall)

        self.gridLayout_3.addLayout(self.horizontalLayout_8, 12, 0, 1, 1)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setObjectName("horizontalLayout_119")
        self.hjgf = QFrame(self.tabWidgetPage1)
        self.hjgf.setObjectName("hjgf")
        sizePolicy3.setHeightForWidth(self.hjgf.sizePolicy().hasHeightForWidth())
        self.hjgf.setSizePolicy(sizePolicy3)
        self.hjgf.setStyleSheet(
            "QFrame#hjgf{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_32 = QVBoxLayout(self.hjgf)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.lb_separator = QLabel(self.hjgf)
        self.lb_separator.setObjectName("lb_separator")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.lb_separator.sizePolicy().hasHeightForWidth())
        self.lb_separator.setSizePolicy(sizePolicy11)
        self.lb_separator.setFont(font5)

        self.horizontalLayout_65.addWidget(self.lb_separator, 0, Qt.AlignLeft)

        self.separator_for_data = QLineEdit(self.hjgf)
        self.separator_for_data.setObjectName("separator_for_data")
        sizePolicy2.setHeightForWidth(self.separator_for_data.sizePolicy().hasHeightForWidth())
        self.separator_for_data.setSizePolicy(sizePolicy2)
        self.separator_for_data.setFont(font6)
        self.separator_for_data.setToolTipDuration(4)
        self.separator_for_data.setAutoFillBackground(False)

        self.horizontalLayout_65.addWidget(self.separator_for_data)

        self.verticalLayout_32.addLayout(self.horizontalLayout_65)

        self.check_name_rheoscan = QCheckBox(self.hjgf)
        self.check_name_rheoscan.setObjectName("check_name_rheoscan")
        self.check_name_rheoscan.setEnabled(True)
        self.check_name_rheoscan.setFont(font5)
        self.check_name_rheoscan.setChecked(False)

        self.verticalLayout_32.addWidget(self.check_name_rheoscan, 0, Qt.AlignHCenter)

        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName("horizontalLayout_116")
        self.label_19 = QLabel(self.hjgf)
        self.label_19.setObjectName("label_19")
        self.label_19.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy10)
        self.label_19.setFont(font5)

        self.horizontalLayout_116.addWidget(self.label_19)

        self.spinBox_check_name_rheoscan = QSpinBox(self.hjgf)
        self.spinBox_check_name_rheoscan.setObjectName("spinBox_check_name_rheoscan")
        self.spinBox_check_name_rheoscan.setEnabled(False)
        sizePolicy2.setHeightForWidth(
            self.spinBox_check_name_rheoscan.sizePolicy().hasHeightForWidth()
        )
        self.spinBox_check_name_rheoscan.setSizePolicy(sizePolicy2)
        self.spinBox_check_name_rheoscan.setFont(font5)
        self.spinBox_check_name_rheoscan.setMinimum(1)
        self.spinBox_check_name_rheoscan.setMaximum(3)
        self.spinBox_check_name_rheoscan.setValue(1)

        self.horizontalLayout_116.addWidget(self.spinBox_check_name_rheoscan)

        self.verticalLayout_32.addLayout(self.horizontalLayout_116)

        self.horizontalLayout_119.addWidget(self.hjgf)

        self.vbn = QFrame(self.tabWidgetPage1)
        self.vbn.setObjectName("vbn")
        sizePolicy3.setHeightForWidth(self.vbn.sizePolicy().hasHeightForWidth())
        self.vbn.setSizePolicy(sizePolicy3)
        self.vbn.setAutoFillBackground(False)
        self.vbn.setStyleSheet(
            "QFrame#vbn{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}\n"
        )
        self.verticalLayout_4 = QVBoxLayout(self.vbn)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setObjectName("horizontalLayout_136")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.check_agg = QCheckBox(self.vbn)
        self.check_agg.setObjectName("check_agg")
        self.check_agg.setFont(font5)
        self.check_agg.setChecked(True)

        self.verticalLayout_11.addWidget(self.check_agg)

        self.check_stress = QCheckBox(self.vbn)
        self.check_stress.setObjectName("check_stress")
        self.check_stress.setFont(font5)
        self.check_stress.setChecked(True)

        self.verticalLayout_11.addWidget(self.check_stress)

        self.check_deform = QCheckBox(self.vbn)
        self.check_deform.setObjectName("check_deform")
        self.check_deform.setFont(font5)
        self.check_deform.setChecked(True)

        self.verticalLayout_11.addWidget(self.check_deform)

        self.horizontalLayout_136.addLayout(self.verticalLayout_11)

        self.line_22 = QFrame(self.vbn)
        self.line_22.setObjectName("line_22")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.line_22.sizePolicy().hasHeightForWidth())
        self.line_22.setSizePolicy(sizePolicy12)
        self.line_22.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_22.setFrameShadow(QFrame.Plain)
        self.line_22.setLineWidth(4)
        self.line_22.setFrameShape(QFrame.VLine)

        self.horizontalLayout_136.addWidget(self.line_22)

        self.check_dop_CSS_parameter = QCheckBox(self.vbn)
        self.check_dop_CSS_parameter.setObjectName("check_dop_CSS_parameter")
        self.check_dop_CSS_parameter.setFont(font5)
        self.check_dop_CSS_parameter.setChecked(False)

        self.horizontalLayout_136.addWidget(self.check_dop_CSS_parameter)

        self.verticalLayout_4.addLayout(self.horizontalLayout_136)

        self.horizontalLayout_119.addWidget(self.vbn)

        self.gridLayout_3.addLayout(self.horizontalLayout_119, 4, 0, 1, 1)

        self.line_15 = QFrame(self.tabWidgetPage1)
        self.line_15.setObjectName("line_15")
        self.line_15.setFont(font4)
        self.line_15.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setLineWidth(3)
        self.line_15.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_15, 13, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.Lab_stuff.addTab(self.tabWidgetPage1, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_10 = QGridLayout(self.tab_5)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.lb_path_2 = QLabel(self.tab_5)
        self.lb_path_2.setObjectName("lb_path_2")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.lb_path_2.sizePolicy().hasHeightForWidth())
        self.lb_path_2.setSizePolicy(sizePolicy13)
        self.lb_path_2.setFont(font5)

        self.horizontalLayout_40.addWidget(self.lb_path_2)

        self.path_for_biola = QLineEdit(self.tab_5)
        self.path_for_biola.setObjectName("path_for_biola")
        self.path_for_biola.setFont(font6)

        self.horizontalLayout_40.addWidget(self.path_for_biola)

        self.gridLayout_10.addLayout(self.horizontalLayout_40, 0, 0, 1, 1)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName("horizontalLayout_73")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.lb_path_3 = QLabel(self.tab_5)
        self.lb_path_3.setObjectName("lb_path_3")
        sizePolicy10.setHeightForWidth(self.lb_path_3.sizePolicy().hasHeightForWidth())
        self.lb_path_3.setSizePolicy(sizePolicy10)
        self.lb_path_3.setFont(font5)
        self.lb_path_3.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.lb_path_3)

        self.comboBox_biola = QComboBox(self.tab_5)
        self.comboBox_biola.setObjectName("comboBox_biola")
        sizePolicy13.setHeightForWidth(self.comboBox_biola.sizePolicy().hasHeightForWidth())
        self.comboBox_biola.setSizePolicy(sizePolicy13)
        self.comboBox_biola.setFont(font6)

        self.horizontalLayout_41.addWidget(self.comboBox_biola)

        self.horizontalLayout_73.addLayout(self.horizontalLayout_41)

        self.gridLayout_10.addLayout(self.horizontalLayout_73, 1, 0, 1, 1)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName("horizontalLayout_72")
        self.lb_path_16 = QLabel(self.tab_5)
        self.lb_path_16.setObjectName("lb_path_16")
        sizePolicy10.setHeightForWidth(self.lb_path_16.sizePolicy().hasHeightForWidth())
        self.lb_path_16.setSizePolicy(sizePolicy10)
        self.lb_path_16.setFont(font5)
        self.lb_path_16.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_72.addWidget(self.lb_path_16)

        self.comboBox_biola_concentration = QComboBox(self.tab_5)
        self.comboBox_biola_concentration.setObjectName("comboBox_biola_concentration")
        sizePolicy13.setHeightForWidth(
            self.comboBox_biola_concentration.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_biola_concentration.setSizePolicy(sizePolicy13)
        self.comboBox_biola_concentration.setFont(font6)

        self.horizontalLayout_72.addWidget(self.comboBox_biola_concentration)

        self.gridLayout_10.addLayout(self.horizontalLayout_72, 2, 0, 1, 1)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.vvvv = QFrame(self.tab_5)
        self.vvvv.setObjectName("vvvv")
        sizePolicy13.setHeightForWidth(self.vvvv.sizePolicy().hasHeightForWidth())
        self.vvvv.setSizePolicy(sizePolicy13)
        self.vvvv.setStyleSheet(
            "QFrame#vvvv{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.vvv = QHBoxLayout(self.vvvv)
        self.vvv.setObjectName("vvv")
        self.vvv.setContentsMargins(5, 5, 5, 5)
        self.label_15 = QLabel(self.vvvv)
        self.label_15.setObjectName("label_15")
        sizePolicy14 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy14)
        self.label_15.setFont(font6)

        self.vvv.addWidget(self.label_15)

        self.line_16 = QFrame(self.vvvv)
        self.line_16.setObjectName("line_16")
        sizePolicy12.setHeightForWidth(self.line_16.sizePolicy().hasHeightForWidth())
        self.line_16.setSizePolicy(sizePolicy12)
        self.line_16.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_16.setFrameShadow(QFrame.Plain)
        self.line_16.setLineWidth(4)
        self.line_16.setFrameShape(QFrame.VLine)

        self.vvv.addWidget(self.line_16)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.label_16 = QLabel(self.vvvv)
        self.label_16.setObjectName("label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setFont(font6)
        self.label_16.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.label_16)

        self.spinBox_biola_born_odd = QSpinBox(self.vvvv)
        self.spinBox_biola_born_odd.setObjectName("spinBox_biola_born_odd")
        sizePolicy7.setHeightForWidth(self.spinBox_biola_born_odd.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_born_odd.setSizePolicy(sizePolicy7)
        self.spinBox_biola_born_odd.setFont(font6)
        self.spinBox_biola_born_odd.setMinimum(1)
        self.spinBox_biola_born_odd.setMaximum(201)
        self.spinBox_biola_born_odd.setSingleStep(2)
        self.spinBox_biola_born_odd.setValue(41)

        self.horizontalLayout_46.addWidget(self.spinBox_biola_born_odd)

        self.verticalLayout_23.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.label_17 = QLabel(self.vvvv)
        self.label_17.setObjectName("label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setFont(font6)
        self.label_17.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.label_17)

        self.spinBox_biola_fluc_odd = QSpinBox(self.vvvv)
        self.spinBox_biola_fluc_odd.setObjectName("spinBox_biola_fluc_odd")
        sizePolicy7.setHeightForWidth(self.spinBox_biola_fluc_odd.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_fluc_odd.setSizePolicy(sizePolicy7)
        self.spinBox_biola_fluc_odd.setFont(font6)
        self.spinBox_biola_fluc_odd.setMinimum(1)
        self.spinBox_biola_fluc_odd.setMaximum(201)
        self.spinBox_biola_fluc_odd.setSingleStep(2)
        self.spinBox_biola_fluc_odd.setValue(41)

        self.horizontalLayout_47.addWidget(self.spinBox_biola_fluc_odd)

        self.verticalLayout_23.addLayout(self.horizontalLayout_47)

        self.vvv.addLayout(self.verticalLayout_23)

        self.verticalLayout_31.addWidget(self.vvvv)

        self.lll = QFrame(self.tab_5)
        self.lll.setObjectName("lll")
        sizePolicy13.setHeightForWidth(self.lll.sizePolicy().hasHeightForWidth())
        self.lll.setSizePolicy(sizePolicy13)
        self.lll.setStyleSheet(
            "QFrame#lll{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.horizontalLayout_44 = QHBoxLayout(self.lll)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(self.lll)
        self.label_12.setObjectName("label_12")
        sizePolicy14.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy14)
        self.label_12.setFont(font6)

        self.horizontalLayout_44.addWidget(self.label_12)

        self.line_17 = QFrame(self.lll)
        self.line_17.setObjectName("line_17")
        sizePolicy12.setHeightForWidth(self.line_17.sizePolicy().hasHeightForWidth())
        self.line_17.setSizePolicy(sizePolicy12)
        self.line_17.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_17.setFrameShadow(QFrame.Plain)
        self.line_17.setLineWidth(4)
        self.line_17.setFrameShape(QFrame.VLine)

        self.horizontalLayout_44.addWidget(self.line_17)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.label_13 = QLabel(self.lll)
        self.label_13.setObjectName("label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setFont(font6)
        self.label_13.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.label_13)

        self.spinBox_biola_born = QSpinBox(self.lll)
        self.spinBox_biola_born.setObjectName("spinBox_biola_born")
        sizePolicy1.setHeightForWidth(self.spinBox_biola_born.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_born.setSizePolicy(sizePolicy1)
        self.spinBox_biola_born.setFont(font6)
        self.spinBox_biola_born.setMinimum(1)
        self.spinBox_biola_born.setMaximum(201)
        self.spinBox_biola_born.setSingleStep(2)
        self.spinBox_biola_born.setValue(71)

        self.horizontalLayout_42.addWidget(self.spinBox_biola_born)

        self.verticalLayout_22.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.label_14 = QLabel(self.lll)
        self.label_14.setObjectName("label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setFont(font6)
        self.label_14.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_14)

        self.spinBox_biola_fluc = QSpinBox(self.lll)
        self.spinBox_biola_fluc.setObjectName("spinBox_biola_fluc")
        sizePolicy7.setHeightForWidth(self.spinBox_biola_fluc.sizePolicy().hasHeightForWidth())
        self.spinBox_biola_fluc.setSizePolicy(sizePolicy7)
        self.spinBox_biola_fluc.setFont(font6)
        self.spinBox_biola_fluc.setMinimum(1)
        self.spinBox_biola_fluc.setMaximum(201)
        self.spinBox_biola_fluc.setSingleStep(2)
        self.spinBox_biola_fluc.setValue(61)

        self.horizontalLayout_43.addWidget(self.spinBox_biola_fluc)

        self.verticalLayout_22.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44.addLayout(self.verticalLayout_22)

        self.verticalLayout_31.addWidget(self.lll)

        self.check_biola_plot_figs = QCheckBox(self.tab_5)
        self.check_biola_plot_figs.setObjectName("check_biola_plot_figs")
        self.check_biola_plot_figs.setEnabled(True)
        self.check_biola_plot_figs.setFont(font5)
        self.check_biola_plot_figs.setChecked(True)
        self.check_biola_plot_figs.setTristate(False)

        self.verticalLayout_31.addWidget(self.check_biola_plot_figs, 0, Qt.AlignHCenter)

        self.plp = QFrame(self.tab_5)
        self.plp.setObjectName("plp")
        self.plp.setEnabled(True)
        sizePolicy13.setHeightForWidth(self.plp.sizePolicy().hasHeightForWidth())
        self.plp.setSizePolicy(sizePolicy13)
        self.plp.setStyleSheet(
            "QFrame#plp{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_30 = QVBoxLayout(self.plp)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(6, 6, 6, 6)
        self.lb_color_pal_box_13 = QLabel(self.plp)
        self.lb_color_pal_box_13.setObjectName("lb_color_pal_box_13")
        sizePolicy7.setHeightForWidth(self.lb_color_pal_box_13.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_13.setSizePolicy(sizePolicy7)
        font9 = QFont()
        font9.setPointSize(11)
        font9.setUnderline(True)
        self.lb_color_pal_box_13.setFont(font9)
        self.lb_color_pal_box_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.lb_color_pal_box_13)

        self.line_18 = QFrame(self.plp)
        self.line_18.setObjectName("line_18")
        self.line_18.setFont(font4)
        self.line_18.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_18.setFrameShadow(QFrame.Plain)
        self.line_18.setLineWidth(4)
        self.line_18.setFrameShape(QFrame.HLine)

        self.verticalLayout_30.addWidget(self.line_18)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.lb_color_pal_box_9 = QLabel(self.plp)
        self.lb_color_pal_box_9.setObjectName("lb_color_pal_box_9")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_9.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_9.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_9.setFont(font6)

        self.horizontalLayout_61.addWidget(self.lb_color_pal_box_9)

        self.doubleSpinBox_Biola = QDoubleSpinBox(self.plp)
        self.doubleSpinBox_Biola.setObjectName("doubleSpinBox_Biola")
        self.doubleSpinBox_Biola.setFont(font6)
        self.doubleSpinBox_Biola.setDecimals(1)
        self.doubleSpinBox_Biola.setMinimum(0.100000000000000)
        self.doubleSpinBox_Biola.setSingleStep(0.100000000000000)
        self.doubleSpinBox_Biola.setValue(1.000000000000000)

        self.horizontalLayout_61.addWidget(self.doubleSpinBox_Biola)

        self.verticalLayout_29.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.lb_color_pal_box_10 = QLabel(self.plp)
        self.lb_color_pal_box_10.setObjectName("lb_color_pal_box_10")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_10.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_10.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_10.setFont(font6)

        self.horizontalLayout_62.addWidget(self.lb_color_pal_box_10)

        self.comboBox_Biola_SD_or = QComboBox(self.plp)
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.addItem("")
        self.comboBox_Biola_SD_or.setObjectName("comboBox_Biola_SD_or")
        sizePolicy15 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.comboBox_Biola_SD_or.sizePolicy().hasHeightForWidth())
        self.comboBox_Biola_SD_or.setSizePolicy(sizePolicy15)
        self.comboBox_Biola_SD_or.setFont(font6)

        self.horizontalLayout_62.addWidget(self.comboBox_Biola_SD_or)

        self.verticalLayout_29.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.check_setka_biola = QCheckBox(self.plp)
        self.check_setka_biola.setObjectName("check_setka_biola")
        self.check_setka_biola.setEnabled(True)
        sizePolicy11.setHeightForWidth(self.check_setka_biola.sizePolicy().hasHeightForWidth())
        self.check_setka_biola.setSizePolicy(sizePolicy11)
        self.check_setka_biola.setFont(font6)
        self.check_setka_biola.setChecked(True)

        self.horizontalLayout_63.addWidget(self.check_setka_biola)

        self.lb_color_pal_box_11 = QLabel(self.plp)
        self.lb_color_pal_box_11.setObjectName("lb_color_pal_box_11")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_11.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_11.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_11.setFont(font6)

        self.horizontalLayout_63.addWidget(self.lb_color_pal_box_11, 0, Qt.AlignRight)

        self.comboBox_Biola_language = QComboBox(self.plp)
        self.comboBox_Biola_language.addItem("")
        self.comboBox_Biola_language.addItem("")
        self.comboBox_Biola_language.setObjectName("comboBox_Biola_language")
        sizePolicy15.setHeightForWidth(
            self.comboBox_Biola_language.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_Biola_language.setSizePolicy(sizePolicy15)
        self.comboBox_Biola_language.setFont(font6)

        self.horizontalLayout_63.addWidget(self.comboBox_Biola_language)

        self.verticalLayout_29.addLayout(self.horizontalLayout_63)

        self.verticalLayout_30.addLayout(self.verticalLayout_29)

        self.verticalLayout_31.addWidget(self.plp)

        self.gridLayout_10.addLayout(self.verticalLayout_31, 3, 0, 1, 1)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName("horizontalLayout_74")
        self.btn_biola = QPushButton(self.tab_5)
        self.btn_biola.setObjectName("btn_biola")
        self.btn_biola.setFont(font6)
        self.btn_biola.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.horizontalLayout_74.addWidget(self.btn_biola)

        self.btn_biola_concentration = QPushButton(self.tab_5)
        self.btn_biola_concentration.setObjectName("btn_biola_concentration")
        self.btn_biola_concentration.setFont(font6)
        self.btn_biola_concentration.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.horizontalLayout_74.addWidget(self.btn_biola_concentration)

        self.gridLayout_10.addLayout(self.horizontalLayout_74, 4, 0, 1, 1)

        self.Lab_stuff.addTab(self.tab_5, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_16 = QGridLayout(self.tab_7)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.lb_path_4 = QLabel(self.tab_7)
        self.lb_path_4.setObjectName("lb_path_4")
        sizePolicy13.setHeightForWidth(self.lb_path_4.sizePolicy().hasHeightForWidth())
        self.lb_path_4.setSizePolicy(sizePolicy13)
        self.lb_path_4.setFont(font5)

        self.horizontalLayout_45.addWidget(self.lb_path_4)

        self.path_for_LT = QLineEdit(self.tab_7)
        self.path_for_LT.setObjectName("path_for_LT")
        self.path_for_LT.setFont(font6)

        self.horizontalLayout_45.addWidget(self.path_for_LT)

        self.verticalLayout_24.addLayout(self.horizontalLayout_45)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.lb_path_13 = QLabel(self.tab_7)
        self.lb_path_13.setObjectName("lb_path_13")
        sizePolicy13.setHeightForWidth(self.lb_path_13.sizePolicy().hasHeightForWidth())
        self.lb_path_13.setSizePolicy(sizePolicy13)
        self.lb_path_13.setFont(font5)

        self.horizontalLayout_55.addWidget(self.lb_path_13)

        self.sep_for_LT = QLineEdit(self.tab_7)
        self.sep_for_LT.setObjectName("sep_for_LT")
        sizePolicy1.setHeightForWidth(self.sep_for_LT.sizePolicy().hasHeightForWidth())
        self.sep_for_LT.setSizePolicy(sizePolicy1)
        self.sep_for_LT.setFont(font6)

        self.horizontalLayout_55.addWidget(self.sep_for_LT)

        self.horizontalSpacer_3 = QSpacerItem(60, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_58.addLayout(self.horizontalLayout_55)

        self.verticalLayout_38.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.lb_path_15 = QLabel(self.tab_7)
        self.lb_path_15.setObjectName("lb_path_15")
        sizePolicy13.setHeightForWidth(self.lb_path_15.sizePolicy().hasHeightForWidth())
        self.lb_path_15.setSizePolicy(sizePolicy13)
        self.lb_path_15.setFont(font5)

        self.horizontalLayout_57.addWidget(self.lb_path_15)

        self.position = QSpinBox(self.tab_7)
        self.position.setObjectName("position")
        self.position.setEnabled(True)
        self.position.setFont(font6)
        self.position.setMinimum(1)
        self.position.setMaximum(5)
        self.position.setValue(1)

        self.horizontalLayout_57.addWidget(self.position)

        self.horizontalSpacer_4 = QSpacerItem(60, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_4)

        self.verticalLayout_38.addLayout(self.horizontalLayout_57)

        self.verticalLayout_24.addLayout(self.verticalLayout_38)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.line_6 = QFrame(self.tab_7)
        self.line_6.setObjectName("line_6")
        self.line_6.setFont(font4)
        self.line_6.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_28.addWidget(self.line_6)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.lb_path_14 = QLabel(self.tab_7)
        self.lb_path_14.setObjectName("lb_path_14")
        sizePolicy13.setHeightForWidth(self.lb_path_14.sizePolicy().hasHeightForWidth())
        self.lb_path_14.setSizePolicy(sizePolicy13)
        self.lb_path_14.setFont(font5)

        self.horizontalLayout_56.addWidget(self.lb_path_14)

        self.sep_for_LT_values = QLineEdit(self.tab_7)
        self.sep_for_LT_values.setObjectName("sep_for_LT_values")
        sizePolicy1.setHeightForWidth(self.sep_for_LT_values.sizePolicy().hasHeightForWidth())
        self.sep_for_LT_values.setSizePolicy(sizePolicy1)
        self.sep_for_LT_values.setFont(font6)

        self.horizontalLayout_56.addWidget(self.sep_for_LT_values)

        self.horizontalSpacer_2 = QSpacerItem(60, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_2)

        self.verticalLayout_28.addLayout(self.horizontalLayout_56)

        self.line_5 = QFrame(self.tab_7)
        self.line_5.setObjectName("line_5")
        self.line_5.setFont(font4)
        self.line_5.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_28.addWidget(self.line_5)

        self.verticalLayout_24.addLayout(self.verticalLayout_28)

        self.gridLayout_16.addLayout(self.verticalLayout_24, 0, 0, 1, 1)

        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName("horizontalLayout_131")
        self.lb_stattest_13 = QLabel(self.tab_7)
        self.lb_stattest_13.setObjectName("lb_stattest_13")
        self.lb_stattest_13.setEnabled(True)
        self.lb_stattest_13.setFont(font6)

        self.horizontalLayout_131.addWidget(self.lb_stattest_13)

        self.comboBox_LT_calibration = QComboBox(self.tab_7)
        self.comboBox_LT_calibration.addItem("")
        self.comboBox_LT_calibration.addItem("")
        self.comboBox_LT_calibration.setObjectName("comboBox_LT_calibration")
        self.comboBox_LT_calibration.setEnabled(True)
        self.comboBox_LT_calibration.setFont(font6)

        self.horizontalLayout_131.addWidget(self.comboBox_LT_calibration)

        self.gridLayout_16.addLayout(self.horizontalLayout_131, 1, 0, 1, 1)

        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setObjectName("horizontalLayout_149")
        self.btn_LT = QPushButton(self.tab_7)
        self.btn_LT.setObjectName("btn_LT")
        self.btn_LT.setFont(font6)
        self.btn_LT.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.horizontalLayout_149.addWidget(self.btn_LT)

        self.check_LT_raw_data = QCheckBox(self.tab_7)
        self.check_LT_raw_data.setObjectName("check_LT_raw_data")
        self.check_LT_raw_data.setEnabled(True)
        sizePolicy11.setHeightForWidth(self.check_LT_raw_data.sizePolicy().hasHeightForWidth())
        self.check_LT_raw_data.setSizePolicy(sizePolicy11)
        self.check_LT_raw_data.setFont(font6)
        self.check_LT_raw_data.setChecked(True)

        self.horizontalLayout_149.addWidget(self.check_LT_raw_data)

        self.gridLayout_16.addLayout(self.horizontalLayout_149, 3, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.formLayout_4.setLabelAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.asd = QFrame(self.tab_7)
        self.asd.setObjectName("asd")
        sizePolicy16 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.asd.sizePolicy().hasHeightForWidth())
        self.asd.setSizePolicy(sizePolicy16)
        self.asd.setStyleSheet(
            "QFrame#asd{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_26 = QVBoxLayout(self.asd)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.lb_path_5 = QLabel(self.asd)
        self.lb_path_5.setObjectName("lb_path_5")
        sizePolicy17 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.lb_path_5.sizePolicy().hasHeightForWidth())
        self.lb_path_5.setSizePolicy(sizePolicy17)
        font10 = QFont()
        font10.setFamilies(["Segoe UI"])
        font10.setPointSize(11)
        font10.setUnderline(True)
        self.lb_path_5.setFont(font10)
        self.lb_path_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.lb_path_5)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.lb_path_17 = QLabel(self.asd)
        self.lb_path_17.setObjectName("lb_path_17")
        sizePolicy17.setHeightForWidth(self.lb_path_17.sizePolicy().hasHeightForWidth())
        self.lb_path_17.setSizePolicy(sizePolicy17)
        self.lb_path_17.setFont(font5)

        self.horizontalLayout_48.addWidget(self.lb_path_17)

        self.lb_path_7 = QLabel(self.asd)
        self.lb_path_7.setObjectName("lb_path_7")
        sizePolicy17.setHeightForWidth(self.lb_path_7.sizePolicy().hasHeightForWidth())
        self.lb_path_7.setSizePolicy(sizePolicy17)
        self.lb_path_7.setFont(font5)

        self.horizontalLayout_48.addWidget(self.lb_path_7)

        self.a_main = QDoubleSpinBox(self.asd)
        self.a_main.setObjectName("a_main")
        self.a_main.setFont(font6)
        self.a_main.setDecimals(5)
        self.a_main.setMaximum(50.000000000000000)
        self.a_main.setValue(0.220000000000000)

        self.horizontalLayout_48.addWidget(self.a_main)

        self.lb_path_18 = QLabel(self.asd)
        self.lb_path_18.setObjectName("lb_path_18")
        sizePolicy17.setHeightForWidth(self.lb_path_18.sizePolicy().hasHeightForWidth())
        self.lb_path_18.setSizePolicy(sizePolicy17)
        self.lb_path_18.setFont(font5)

        self.horizontalLayout_48.addWidget(self.lb_path_18)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.lb_path_8 = QLabel(self.asd)
        self.lb_path_8.setObjectName("lb_path_8")
        sizePolicy17.setHeightForWidth(self.lb_path_8.sizePolicy().hasHeightForWidth())
        self.lb_path_8.setSizePolicy(sizePolicy17)
        self.lb_path_8.setFont(font5)

        self.horizontalLayout_49.addWidget(self.lb_path_8)

        self.b_main = QDoubleSpinBox(self.asd)
        self.b_main.setObjectName("b_main")
        self.b_main.setFont(font6)
        self.b_main.setDecimals(5)
        self.b_main.setMinimum(-200.000000000000000)
        self.b_main.setMaximum(200.000000000000000)
        self.b_main.setValue(-0.800000000000000)

        self.horizontalLayout_49.addWidget(self.b_main)

        self.horizontalLayout_48.addLayout(self.horizontalLayout_49)

        self.verticalLayout_25.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.lb_path_12 = QLabel(self.asd)
        self.lb_path_12.setObjectName("lb_path_12")
        sizePolicy17.setHeightForWidth(self.lb_path_12.sizePolicy().hasHeightForWidth())
        self.lb_path_12.setSizePolicy(sizePolicy17)
        self.lb_path_12.setFont(font5)

        self.horizontalLayout_50.addWidget(self.lb_path_12)

        self.dateEdit = QDateEdit(self.asd)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setFont(font6)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_50.addWidget(self.dateEdit)

        self.verticalLayout_25.addLayout(self.horizontalLayout_50)

        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.asd)

        self.hhhhh = QFrame(self.tab_7)
        self.hhhhh.setObjectName("hhhhh")
        sizePolicy16.setHeightForWidth(self.hhhhh.sizePolicy().hasHeightForWidth())
        self.hhhhh.setSizePolicy(sizePolicy16)
        self.hhhhh.setStyleSheet(
            "QFrame#hhhhh{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_27 = QVBoxLayout(self.hhhhh)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.lb_path_6 = QLabel(self.hhhhh)
        self.lb_path_6.setObjectName("lb_path_6")
        sizePolicy18 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.lb_path_6.sizePolicy().hasHeightForWidth())
        self.lb_path_6.setSizePolicy(sizePolicy18)
        self.lb_path_6.setFont(font10)
        self.lb_path_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.lb_path_6)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName("horizontalLayout_115")
        self.lb_path_19 = QLabel(self.hhhhh)
        self.lb_path_19.setObjectName("lb_path_19")
        sizePolicy17.setHeightForWidth(self.lb_path_19.sizePolicy().hasHeightForWidth())
        self.lb_path_19.setSizePolicy(sizePolicy17)
        self.lb_path_19.setFont(font5)

        self.horizontalLayout_115.addWidget(self.lb_path_19)

        self.lb_path_9 = QLabel(self.hhhhh)
        self.lb_path_9.setObjectName("lb_path_9")
        sizePolicy17.setHeightForWidth(self.lb_path_9.sizePolicy().hasHeightForWidth())
        self.lb_path_9.setSizePolicy(sizePolicy17)
        self.lb_path_9.setFont(font5)

        self.horizontalLayout_115.addWidget(self.lb_path_9)

        self.a_dop = QDoubleSpinBox(self.hhhhh)
        self.a_dop.setObjectName("a_dop")
        self.a_dop.setFont(font6)
        self.a_dop.setDecimals(5)
        self.a_dop.setMaximum(50.000000000000000)
        self.a_dop.setValue(1.410000000000000)

        self.horizontalLayout_115.addWidget(self.a_dop)

        self.lb_path_20 = QLabel(self.hhhhh)
        self.lb_path_20.setObjectName("lb_path_20")
        sizePolicy17.setHeightForWidth(self.lb_path_20.sizePolicy().hasHeightForWidth())
        self.lb_path_20.setSizePolicy(sizePolicy17)
        self.lb_path_20.setFont(font5)

        self.horizontalLayout_115.addWidget(self.lb_path_20)

        self.lb_path_21 = QLabel(self.hhhhh)
        self.lb_path_21.setObjectName("lb_path_21")
        sizePolicy17.setHeightForWidth(self.lb_path_21.sizePolicy().hasHeightForWidth())
        self.lb_path_21.setSizePolicy(sizePolicy17)
        self.lb_path_21.setFont(font5)

        self.horizontalLayout_115.addWidget(self.lb_path_21)

        self.b_dop = QDoubleSpinBox(self.hhhhh)
        self.b_dop.setObjectName("b_dop")
        self.b_dop.setFont(font6)
        self.b_dop.setDecimals(5)
        self.b_dop.setMinimum(-200.000000000000000)
        self.b_dop.setMaximum(200.000000000000000)
        self.b_dop.setValue(-29.500000000000000)

        self.horizontalLayout_115.addWidget(self.b_dop)

        self.verticalLayout_46.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.lb_path_11 = QLabel(self.hhhhh)
        self.lb_path_11.setObjectName("lb_path_11")
        sizePolicy17.setHeightForWidth(self.lb_path_11.sizePolicy().hasHeightForWidth())
        self.lb_path_11.setSizePolicy(sizePolicy17)
        self.lb_path_11.setFont(font5)

        self.horizontalLayout_53.addWidget(self.lb_path_11)

        self.dateEdit_2 = QDateEdit(self.hhhhh)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setFont(font6)
        self.dateEdit_2.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_53.addWidget(self.dateEdit_2)

        self.verticalLayout_46.addLayout(self.horizontalLayout_53)

        self.verticalLayout_27.addLayout(self.verticalLayout_46)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.hhhhh)

        self.hhhhh_exp = QFrame(self.tab_7)
        self.hhhhh_exp.setObjectName("hhhhh_exp")
        self.hhhhh_exp.setEnabled(False)
        sizePolicy12.setHeightForWidth(self.hhhhh_exp.sizePolicy().hasHeightForWidth())
        self.hhhhh_exp.setSizePolicy(sizePolicy12)
        self.hhhhh_exp.setStyleSheet(
            "QFrame#hhhhh_exp{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_47 = QVBoxLayout(self.hhhhh_exp)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(5, 5, 5, 5)
        self.lb_path_10 = QLabel(self.hhhhh_exp)
        self.lb_path_10.setObjectName("lb_path_10")
        sizePolicy18.setHeightForWidth(self.lb_path_10.sizePolicy().hasHeightForWidth())
        self.lb_path_10.setSizePolicy(sizePolicy18)
        self.lb_path_10.setFont(font10)
        self.lb_path_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.lb_path_10)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.lb_path_22 = QLabel(self.hhhhh_exp)
        self.lb_path_22.setObjectName("lb_path_22")
        sizePolicy17.setHeightForWidth(self.lb_path_22.sizePolicy().hasHeightForWidth())
        self.lb_path_22.setSizePolicy(sizePolicy17)
        self.lb_path_22.setFont(font5)

        self.horizontalLayout_51.addWidget(self.lb_path_22)

        self.lb_path_23 = QLabel(self.hhhhh_exp)
        self.lb_path_23.setObjectName("lb_path_23")
        sizePolicy17.setHeightForWidth(self.lb_path_23.sizePolicy().hasHeightForWidth())
        self.lb_path_23.setSizePolicy(sizePolicy17)
        self.lb_path_23.setFont(font5)

        self.horizontalLayout_51.addWidget(self.lb_path_23, 0, Qt.AlignHCenter)

        self.dop_cal_k = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_k.setObjectName("dop_cal_k")
        self.dop_cal_k.setFont(font6)
        self.dop_cal_k.setDecimals(5)
        self.dop_cal_k.setMinimum(-50.000000000000000)
        self.dop_cal_k.setMaximum(50.000000000000000)
        self.dop_cal_k.setValue(0.500000000000000)

        self.horizontalLayout_51.addWidget(self.dop_cal_k)

        self.lb_path_27 = QLabel(self.hhhhh_exp)
        self.lb_path_27.setObjectName("lb_path_27")
        sizePolicy17.setHeightForWidth(self.lb_path_27.sizePolicy().hasHeightForWidth())
        self.lb_path_27.setSizePolicy(sizePolicy17)
        self.lb_path_27.setFont(font5)

        self.horizontalLayout_51.addWidget(self.lb_path_27, 0, Qt.AlignHCenter)

        self.dop_cal_y0 = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_y0.setObjectName("dop_cal_y0")
        self.dop_cal_y0.setFont(font6)
        self.dop_cal_y0.setDecimals(5)
        self.dop_cal_y0.setMinimum(-50.000000000000000)
        self.dop_cal_y0.setMaximum(50.000000000000000)
        self.dop_cal_y0.setValue(-1.000000000000000)

        self.horizontalLayout_51.addWidget(self.dop_cal_y0)

        self.lb_path_28 = QLabel(self.hhhhh_exp)
        self.lb_path_28.setObjectName("lb_path_28")
        sizePolicy17.setHeightForWidth(self.lb_path_28.sizePolicy().hasHeightForWidth())
        self.lb_path_28.setSizePolicy(sizePolicy17)
        self.lb_path_28.setFont(font5)

        self.horizontalLayout_51.addWidget(self.lb_path_28, 0, Qt.AlignHCenter)

        self.dop_cal_A = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_A.setObjectName("dop_cal_A")
        self.dop_cal_A.setFont(font6)
        self.dop_cal_A.setDecimals(5)
        self.dop_cal_A.setMinimum(-50.000000000000000)
        self.dop_cal_A.setMaximum(50.000000000000000)
        self.dop_cal_A.setValue(1.000000000000000)

        self.horizontalLayout_51.addWidget(self.dop_cal_A)

        self.verticalLayout_49.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.lb_path_29 = QLabel(self.hhhhh_exp)
        self.lb_path_29.setObjectName("lb_path_29")
        sizePolicy17.setHeightForWidth(self.lb_path_29.sizePolicy().hasHeightForWidth())
        self.lb_path_29.setSizePolicy(sizePolicy17)
        self.lb_path_29.setFont(font5)

        self.horizontalLayout_52.addWidget(self.lb_path_29)

        self.lb_path_30 = QLabel(self.hhhhh_exp)
        self.lb_path_30.setObjectName("lb_path_30")
        sizePolicy17.setHeightForWidth(self.lb_path_30.sizePolicy().hasHeightForWidth())
        self.lb_path_30.setSizePolicy(sizePolicy17)
        self.lb_path_30.setFont(font5)

        self.horizontalLayout_52.addWidget(self.lb_path_30, 0, Qt.AlignHCenter)

        self.dop_cal_R0 = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_R0.setObjectName("dop_cal_R0")
        self.dop_cal_R0.setFont(font6)
        self.dop_cal_R0.setDecimals(5)
        self.dop_cal_R0.setMinimum(-50.000000000000000)
        self.dop_cal_R0.setMaximum(50.000000000000000)
        self.dop_cal_R0.setValue(0.100000000000000)

        self.horizontalLayout_52.addWidget(self.dop_cal_R0)

        self.lb_path_31 = QLabel(self.hhhhh_exp)
        self.lb_path_31.setObjectName("lb_path_31")
        sizePolicy17.setHeightForWidth(self.lb_path_31.sizePolicy().hasHeightForWidth())
        self.lb_path_31.setSizePolicy(sizePolicy17)
        self.lb_path_31.setFont(font5)

        self.horizontalLayout_52.addWidget(self.lb_path_31, 0, Qt.AlignHCenter)

        self.dop_cal_b = QDoubleSpinBox(self.hhhhh_exp)
        self.dop_cal_b.setObjectName("dop_cal_b")
        self.dop_cal_b.setFont(font6)
        self.dop_cal_b.setDecimals(5)
        self.dop_cal_b.setMinimum(-1000.000000000000000)
        self.dop_cal_b.setMaximum(1000.000000000000000)
        self.dop_cal_b.setValue(-1.000000000000000)

        self.horizontalLayout_52.addWidget(self.dop_cal_b)

        self.verticalLayout_49.addLayout(self.horizontalLayout_52)

        self.verticalLayout_47.addLayout(self.verticalLayout_49)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.lb_path_26 = QLabel(self.hhhhh_exp)
        self.lb_path_26.setObjectName("lb_path_26")
        sizePolicy17.setHeightForWidth(self.lb_path_26.sizePolicy().hasHeightForWidth())
        self.lb_path_26.setSizePolicy(sizePolicy17)
        self.lb_path_26.setFont(font5)

        self.horizontalLayout_54.addWidget(self.lb_path_26)

        self.dateEdit_3 = QDateEdit(self.hhhhh_exp)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.dateEdit_3.setFont(font6)
        self.dateEdit_3.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_54.addWidget(self.dateEdit_3)

        self.verticalLayout_48.addLayout(self.horizontalLayout_54)

        self.verticalLayout_47.addLayout(self.verticalLayout_48)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.hhhhh_exp)

        self.gridLayout_16.addLayout(self.formLayout_4, 2, 0, 1, 1)

        self.Lab_stuff.addTab(self.tab_7, "")
        self.tabWidgetPage4 = QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.gridLayout_9 = QGridLayout(self.tabWidgetPage4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tabWidget_2 = QTabWidget(self.tabWidgetPage4)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2.setFont(font6)
        self.tabWidget_2.setUsesScrollButtons(False)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lb_path_for_plot = QLabel(self.tab)
        self.lb_path_for_plot.setObjectName("lb_path_for_plot")
        self.lb_path_for_plot.setFont(font6)

        self.horizontalLayout_13.addWidget(self.lb_path_for_plot)

        self.path_for_plot = QLineEdit(self.tab)
        self.path_for_plot.setObjectName("path_for_plot")
        self.path_for_plot.setFont(font6)

        self.horizontalLayout_13.addWidget(self.path_for_plot)

        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lb_exel_name = QLabel(self.tab)
        self.lb_exel_name.setObjectName("lb_exel_name")
        self.lb_exel_name.setFont(font6)

        self.horizontalLayout_14.addWidget(self.lb_exel_name)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")

        self.horizontalLayout_14.addWidget(self.comboBox)

        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName("horizontalLayout_138")
        self.check_box_figs_all_sheets = QCheckBox(self.tab)
        self.check_box_figs_all_sheets.setObjectName("check_box_figs_all_sheets")
        self.check_box_figs_all_sheets.setFont(font6)
        self.check_box_figs_all_sheets.setChecked(True)

        self.horizontalLayout_138.addWidget(self.check_box_figs_all_sheets)

        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName("horizontalLayout_137")
        self.lb_exel_name_8 = QLabel(self.tab)
        self.lb_exel_name_8.setObjectName("lb_exel_name_8")
        self.lb_exel_name_8.setEnabled(False)
        self.lb_exel_name_8.setFont(font6)

        self.horizontalLayout_137.addWidget(self.lb_exel_name_8)

        self.comboBox_figs_sheets = QComboBox(self.tab)
        self.comboBox_figs_sheets.setObjectName("comboBox_figs_sheets")
        self.comboBox_figs_sheets.setEnabled(False)

        self.horizontalLayout_137.addWidget(self.comboBox_figs_sheets)

        self.horizontalLayout_138.addLayout(self.horizontalLayout_137)

        self.verticalLayout_12.addLayout(self.horizontalLayout_138)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lb_hue_name = QLabel(self.tab)
        self.lb_hue_name.setObjectName("lb_hue_name")
        self.lb_hue_name.setFont(font6)

        self.horizontalLayout_15.addWidget(self.lb_hue_name)

        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.setObjectName("comboBox_2")

        self.horizontalLayout_15.addWidget(self.comboBox_2)

        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.verticalLayout_17.addLayout(self.verticalLayout_14)

        self.line_25 = QFrame(self.tab)
        self.line_25.setObjectName("line_25")
        self.line_25.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_25.setFrameShadow(QFrame.Plain)
        self.line_25.setLineWidth(3)
        self.line_25.setFrameShape(QFrame.HLine)

        self.verticalLayout_17.addWidget(self.line_25)

        self.checkBox_point_comma_separator = QCheckBox(self.tab)
        self.checkBox_point_comma_separator.setObjectName("checkBox_point_comma_separator")
        sizePolicy12.setHeightForWidth(
            self.checkBox_point_comma_separator.sizePolicy().hasHeightForWidth()
        )
        self.checkBox_point_comma_separator.setSizePolicy(sizePolicy12)

        self.verticalLayout_17.addWidget(self.checkBox_point_comma_separator)

        self.nmn = QFrame(self.tab)
        self.nmn.setObjectName("nmn")
        sizePolicy7.setHeightForWidth(self.nmn.sizePolicy().hasHeightForWidth())
        self.nmn.setSizePolicy(sizePolicy7)
        self.nmn.setStyleSheet(
            "QFrame#nmn{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_13 = QVBoxLayout(self.nmn)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setObjectName("horizontalLayout_156")
        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.check_box_plot = QCheckBox(self.nmn)
        self.check_box_plot.setObjectName("check_box_plot")
        self.check_box_plot.setFont(font6)
        self.check_box_plot.setChecked(True)

        self.verticalLayout_54.addWidget(self.check_box_plot)

        self.check_corr_matrix = QCheckBox(self.nmn)
        self.check_corr_matrix.setObjectName("check_corr_matrix")
        self.check_corr_matrix.setFont(font6)

        self.verticalLayout_54.addWidget(self.check_corr_matrix)

        self.check_corr_figs = QCheckBox(self.nmn)
        self.check_corr_figs.setObjectName("check_corr_figs")
        self.check_corr_figs.setFont(font6)

        self.verticalLayout_54.addWidget(self.check_corr_figs)

        self.horizontalLayout_156.addLayout(self.verticalLayout_54)

        self.horizontalSpacer_5 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_156.addItem(self.horizontalSpacer_5)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.check_box_pairplot = QCheckBox(self.nmn)
        self.check_box_pairplot.setObjectName("check_box_pairplot")
        self.check_box_pairplot.setFont(font6)
        self.check_box_pairplot.setCheckable(True)
        self.check_box_pairplot.setChecked(False)

        self.verticalLayout_52.addWidget(self.check_box_pairplot)

        self.check_jointplot = QCheckBox(self.nmn)
        self.check_jointplot.setObjectName("check_jointplot")
        self.check_jointplot.setFont(font6)

        self.verticalLayout_52.addWidget(self.check_jointplot)

        self.check_corr_one_parameter = QCheckBox(self.nmn)
        self.check_corr_one_parameter.setObjectName("check_corr_one_parameter")
        self.check_corr_one_parameter.setFont(font6)

        self.verticalLayout_52.addWidget(self.check_corr_one_parameter)

        self.horizontalLayout_156.addLayout(self.verticalLayout_52)

        self.verticalLayout_13.addLayout(self.horizontalLayout_156)

        self.verticalLayout_17.addWidget(self.nmn)

        self.tabWidget = QTabWidget(self.tab)
        self.tabWidget.setObjectName("tabWidget")
        sizePolicy19 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy19.setHorizontalStretch(0)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy19)
        self.tabWidget.setFont(font6)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget_3 = QTabWidget(self.tab_3)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName("tab_15")
        self.gridLayout_18 = QGridLayout(self.tab_15)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.scrollArea_2 = QScrollArea(self.tab_15)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 170))
        self.scrollArea_2.setFrameShadow(QFrame.Sunken)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 582, 248))
        self.gridLayout_21 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName("frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_16 = QVBoxLayout(self.frame_2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lb_color_pal_box = QLabel(self.frame_2)
        self.lb_color_pal_box.setObjectName("lb_color_pal_box")
        sizePolicy11.setHeightForWidth(self.lb_color_pal_box.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box.setSizePolicy(sizePolicy11)
        self.lb_color_pal_box.setFont(font6)

        self.horizontalLayout_19.addWidget(self.lb_color_pal_box)

        self.comboBox_color_pal_box = QComboBox(self.frame_2)
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
        self.comboBox_color_pal_box.setObjectName("comboBox_color_pal_box")
        sizePolicy7.setHeightForWidth(self.comboBox_color_pal_box.sizePolicy().hasHeightForWidth())
        self.comboBox_color_pal_box.setSizePolicy(sizePolicy7)
        self.comboBox_color_pal_box.setFont(font6)

        self.horizontalLayout_19.addWidget(self.comboBox_color_pal_box)

        self.verticalLayout_16.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.lb_color_pal_points = QLabel(self.frame_2)
        self.lb_color_pal_points.setObjectName("lb_color_pal_points")
        sizePolicy11.setHeightForWidth(self.lb_color_pal_points.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_points.setSizePolicy(sizePolicy11)
        self.lb_color_pal_points.setFont(font6)

        self.horizontalLayout_24.addWidget(self.lb_color_pal_points)

        self.comboBox_color_pal_points = QComboBox(self.frame_2)
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
        self.comboBox_color_pal_points.setObjectName("comboBox_color_pal_points")
        sizePolicy7.setHeightForWidth(
            self.comboBox_color_pal_points.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_color_pal_points.setSizePolicy(sizePolicy7)
        self.comboBox_color_pal_points.setFont(font6)

        self.horizontalLayout_24.addWidget(self.comboBox_color_pal_points)

        self.verticalLayout_16.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lb_color_for_box = QLabel(self.frame_2)
        self.lb_color_for_box.setObjectName("lb_color_for_box")
        sizePolicy11.setHeightForWidth(self.lb_color_for_box.sizePolicy().hasHeightForWidth())
        self.lb_color_for_box.setSizePolicy(sizePolicy11)
        self.lb_color_for_box.setFont(font6)

        self.horizontalLayout_20.addWidget(self.lb_color_for_box)

        self.color_box = QLineEdit(self.frame_2)
        self.color_box.setObjectName("color_box")
        sizePolicy7.setHeightForWidth(self.color_box.sizePolicy().hasHeightForWidth())
        self.color_box.setSizePolicy(sizePolicy7)
        self.color_box.setFont(font6)

        self.horizontalLayout_20.addWidget(self.color_box)

        self.pushButton_HEX_box = QPushButton(self.frame_2)
        self.pushButton_HEX_box.setObjectName("pushButton_HEX_box")
        sizePolicy2.setHeightForWidth(self.pushButton_HEX_box.sizePolicy().hasHeightForWidth())
        self.pushButton_HEX_box.setSizePolicy(sizePolicy2)
        self.pushButton_HEX_box.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_20.addWidget(self.pushButton_HEX_box)

        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.lb_color_forpoints = QLabel(self.frame_2)
        self.lb_color_forpoints.setObjectName("lb_color_forpoints")
        sizePolicy11.setHeightForWidth(self.lb_color_forpoints.sizePolicy().hasHeightForWidth())
        self.lb_color_forpoints.setSizePolicy(sizePolicy11)
        self.lb_color_forpoints.setFont(font6)

        self.horizontalLayout_25.addWidget(self.lb_color_forpoints)

        self.color_points = QLineEdit(self.frame_2)
        self.color_points.setObjectName("color_points")
        sizePolicy7.setHeightForWidth(self.color_points.sizePolicy().hasHeightForWidth())
        self.color_points.setSizePolicy(sizePolicy7)
        self.color_points.setFont(font6)

        self.horizontalLayout_25.addWidget(self.color_points)

        self.pushButton_HEX_points = QPushButton(self.frame_2)
        self.pushButton_HEX_points.setObjectName("pushButton_HEX_points")
        self.pushButton_HEX_points.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_25.addWidget(self.pushButton_HEX_points)

        self.verticalLayout_16.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName("horizontalLayout_122")
        self.lb_color_pal_box_19 = QLabel(self.frame_2)
        self.lb_color_pal_box_19.setObjectName("lb_color_pal_box_19")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_19.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_19.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_19.setFont(font6)

        self.horizontalLayout_122.addWidget(self.lb_color_pal_box_19)

        self.spinBox_point_size = QSpinBox(self.frame_2)
        self.spinBox_point_size.setObjectName("spinBox_point_size")
        sizePolicy2.setHeightForWidth(self.spinBox_point_size.sizePolicy().hasHeightForWidth())
        self.spinBox_point_size.setSizePolicy(sizePolicy2)
        self.spinBox_point_size.setFont(font6)
        self.spinBox_point_size.setMinimum(0)
        self.spinBox_point_size.setMaximum(20)
        self.spinBox_point_size.setValue(4)

        self.horizontalLayout_122.addWidget(self.spinBox_point_size)

        self.horizontalLayout_147 = QHBoxLayout()
        self.horizontalLayout_147.setObjectName("horizontalLayout_147")
        self.lb_color_pal_box_23 = QLabel(self.frame_2)
        self.lb_color_pal_box_23.setObjectName("lb_color_pal_box_23")
        self.lb_color_pal_box_23.setFont(font6)

        self.horizontalLayout_147.addWidget(self.lb_color_pal_box_23)

        self.doubleSpinBox_points_opasity = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_points_opasity.setObjectName("doubleSpinBox_points_opasity")
        self.doubleSpinBox_points_opasity.setFont(font6)
        self.doubleSpinBox_points_opasity.setDecimals(1)
        self.doubleSpinBox_points_opasity.setMinimum(0.100000000000000)
        self.doubleSpinBox_points_opasity.setMaximum(1.000000000000000)
        self.doubleSpinBox_points_opasity.setSingleStep(0.100000000000000)
        self.doubleSpinBox_points_opasity.setValue(0.600000000000000)

        self.horizontalLayout_147.addWidget(self.doubleSpinBox_points_opasity)

        self.horizontalLayout_122.addLayout(self.horizontalLayout_147)

        self.verticalLayout_16.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.lb_color_pal_box_7 = QLabel(self.frame_2)
        self.lb_color_pal_box_7.setObjectName("lb_color_pal_box_7")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_7.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_7.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_7.setFont(font6)

        self.horizontalLayout_59.addWidget(self.lb_color_pal_box_7)

        self.spinBox_mean_val_size = QSpinBox(self.frame_2)
        self.spinBox_mean_val_size.setObjectName("spinBox_mean_val_size")
        sizePolicy2.setHeightForWidth(self.spinBox_mean_val_size.sizePolicy().hasHeightForWidth())
        self.spinBox_mean_val_size.setSizePolicy(sizePolicy2)
        self.spinBox_mean_val_size.setFont(font6)
        self.spinBox_mean_val_size.setMinimum(2)
        self.spinBox_mean_val_size.setMaximum(20)
        self.spinBox_mean_val_size.setValue(4)

        self.horizontalLayout_59.addWidget(self.spinBox_mean_val_size)

        self.verticalLayout_16.addLayout(self.horizontalLayout_59)

        self.gridLayout_20.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName("frame_3")
        sizePolicy14.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy14)
        self.verticalLayout_20 = QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.lb_color_pal_box_6 = QLabel(self.frame_3)
        self.lb_color_pal_box_6.setObjectName("lb_color_pal_box_6")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_6.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_6.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_6.setFont(font6)

        self.horizontalLayout_39.addWidget(self.lb_color_pal_box_6)

        self.comboBox_fonts = QComboBox(self.frame_3)
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.addItem("")
        self.comboBox_fonts.setObjectName("comboBox_fonts")
        self.comboBox_fonts.setFont(font6)

        self.horizontalLayout_39.addWidget(self.comboBox_fonts)

        self.verticalLayout_20.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.lb_color_pal_box_2 = QLabel(self.frame_3)
        self.lb_color_pal_box_2.setObjectName("lb_color_pal_box_2")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_2.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_2.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_2.setFont(font6)

        self.horizontalLayout_34.addWidget(self.lb_color_pal_box_2)

        self.spinBox_x_label = QSpinBox(self.frame_3)
        self.spinBox_x_label.setObjectName("spinBox_x_label")
        sizePolicy2.setHeightForWidth(self.spinBox_x_label.sizePolicy().hasHeightForWidth())
        self.spinBox_x_label.setSizePolicy(sizePolicy2)
        self.spinBox_x_label.setFont(font6)
        self.spinBox_x_label.setMinimum(2)
        self.spinBox_x_label.setMaximum(100)
        self.spinBox_x_label.setValue(14)

        self.horizontalLayout_34.addWidget(self.spinBox_x_label)

        self.verticalLayout_20.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.lb_color_pal_box_3 = QLabel(self.frame_3)
        self.lb_color_pal_box_3.setObjectName("lb_color_pal_box_3")
        self.lb_color_pal_box_3.setFont(font6)

        self.horizontalLayout_35.addWidget(self.lb_color_pal_box_3)

        self.spinBox_y_label = QSpinBox(self.frame_3)
        self.spinBox_y_label.setObjectName("spinBox_y_label")
        sizePolicy2.setHeightForWidth(self.spinBox_y_label.sizePolicy().hasHeightForWidth())
        self.spinBox_y_label.setSizePolicy(sizePolicy2)
        self.spinBox_y_label.setFont(font6)
        self.spinBox_y_label.setMinimum(2)
        self.spinBox_y_label.setMaximum(100)
        self.spinBox_y_label.setValue(14)

        self.horizontalLayout_35.addWidget(self.spinBox_y_label)

        self.verticalLayout_20.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.lb_color_pal_box_5 = QLabel(self.frame_3)
        self.lb_color_pal_box_5.setObjectName("lb_color_pal_box_5")
        self.lb_color_pal_box_5.setFont(font6)

        self.horizontalLayout_36.addWidget(self.lb_color_pal_box_5)

        self.spinBox_x_val = QSpinBox(self.frame_3)
        self.spinBox_x_val.setObjectName("spinBox_x_val")
        sizePolicy2.setHeightForWidth(self.spinBox_x_val.sizePolicy().hasHeightForWidth())
        self.spinBox_x_val.setSizePolicy(sizePolicy2)
        self.spinBox_x_val.setFont(font6)
        self.spinBox_x_val.setMinimum(2)
        self.spinBox_x_val.setMaximum(100)
        self.spinBox_x_val.setValue(14)

        self.horizontalLayout_36.addWidget(self.spinBox_x_val)

        self.verticalLayout_20.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.lb_color_pal_box_4 = QLabel(self.frame_3)
        self.lb_color_pal_box_4.setObjectName("lb_color_pal_box_4")
        self.lb_color_pal_box_4.setFont(font6)

        self.horizontalLayout_37.addWidget(self.lb_color_pal_box_4)

        self.spinBox_y_vals = QSpinBox(self.frame_3)
        self.spinBox_y_vals.setObjectName("spinBox_y_vals")
        sizePolicy2.setHeightForWidth(self.spinBox_y_vals.sizePolicy().hasHeightForWidth())
        self.spinBox_y_vals.setSizePolicy(sizePolicy2)
        self.spinBox_y_vals.setFont(font6)
        self.spinBox_y_vals.setMinimum(2)
        self.spinBox_y_vals.setMaximum(100)
        self.spinBox_y_vals.setValue(14)

        self.horizontalLayout_37.addWidget(self.spinBox_y_vals)

        self.verticalLayout_20.addLayout(self.horizontalLayout_37)

        self.gridLayout_20.addWidget(self.frame_3, 0, 1, 1, 1)

        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_18.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_17 = QGridLayout(self.tab_16)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.scrollArea_3 = QScrollArea(self.tab_16)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 170))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 492, 260))
        self.gridLayout_19 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 6, -1, 6)
        self.horizontalLayout_144 = QHBoxLayout()
        self.horizontalLayout_144.setObjectName("horizontalLayout_144")
        self.check_sort_or_not = QCheckBox(self.scrollAreaWidgetContents_3)
        self.check_sort_or_not.setObjectName("check_sort_or_not")
        sizePolicy20 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy20.setHorizontalStretch(0)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.check_sort_or_not.sizePolicy().hasHeightForWidth())
        self.check_sort_or_not.setSizePolicy(sizePolicy20)
        self.check_sort_or_not.setFont(font6)
        self.check_sort_or_not.setChecked(False)

        self.horizontalLayout_144.addWidget(self.check_sort_or_not)

        self.check_sort_or_not_ascending = QCheckBox(self.scrollAreaWidgetContents_3)
        self.check_sort_or_not_ascending.setObjectName("check_sort_or_not_ascending")
        self.check_sort_or_not_ascending.setEnabled(False)
        sizePolicy20.setHeightForWidth(
            self.check_sort_or_not_ascending.sizePolicy().hasHeightForWidth()
        )
        self.check_sort_or_not_ascending.setSizePolicy(sizePolicy20)
        self.check_sort_or_not_ascending.setFont(font6)
        self.check_sort_or_not_ascending.setChecked(True)

        self.horizontalLayout_144.addWidget(self.check_sort_or_not_ascending)

        self.verticalLayout_18.addLayout(self.horizontalLayout_144)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        self.lb_del_hue_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.lb_del_hue_6.setObjectName("lb_del_hue_6")
        sizePolicy13.setHeightForWidth(self.lb_del_hue_6.sizePolicy().hasHeightForWidth())
        self.lb_del_hue_6.setSizePolicy(sizePolicy13)
        self.lb_del_hue_6.setFont(font6)

        self.horizontalLayout_81.addWidget(self.lb_del_hue_6)

        self.order_box_plot = QLineEdit(self.scrollAreaWidgetContents_3)
        self.order_box_plot.setObjectName("order_box_plot")
        self.order_box_plot.setFont(font6)

        self.horizontalLayout_81.addWidget(self.order_box_plot)

        self.verticalLayout_18.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_146 = QHBoxLayout()
        self.horizontalLayout_146.setObjectName("horizontalLayout_146")
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.lb_stattest_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.lb_stattest_3.setObjectName("lb_stattest_3")
        self.lb_stattest_3.setFont(font6)

        self.horizontalLayout_60.addWidget(self.lb_stattest_3)

        self.check_N_ = QCheckBox(self.scrollAreaWidgetContents_3)
        self.check_N_.setObjectName("check_N_")
        self.check_N_.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.check_N_.sizePolicy().hasHeightForWidth())
        self.check_N_.setSizePolicy(sizePolicy2)
        self.check_N_.setChecked(True)

        self.horizontalLayout_60.addWidget(self.check_N_)

        self.horizontalLayout_146.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_145 = QHBoxLayout()
        self.horizontalLayout_145.setObjectName("horizontalLayout_145")
        self.lb__altern_heposisis_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.lb__altern_heposisis_5.setObjectName("lb__altern_heposisis_5")
        self.lb__altern_heposisis_5.setEnabled(True)
        self.lb__altern_heposisis_5.setFont(font6)

        self.horizontalLayout_145.addWidget(self.lb__altern_heposisis_5, 0, Qt.AlignRight)

        self.comboBox_box_check_N_ = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_box_check_N_.addItem("")
        self.comboBox_box_check_N_.addItem("")
        self.comboBox_box_check_N_.addItem("")
        self.comboBox_box_check_N_.addItem("")
        self.comboBox_box_check_N_.addItem("")
        self.comboBox_box_check_N_.addItem("")
        self.comboBox_box_check_N_.addItem("")
        self.comboBox_box_check_N_.setObjectName("comboBox_box_check_N_")
        self.comboBox_box_check_N_.setEnabled(True)
        self.comboBox_box_check_N_.setFont(font6)

        self.horizontalLayout_145.addWidget(self.comboBox_box_check_N_)

        self.horizontalLayout_146.addLayout(self.horizontalLayout_145)

        self.verticalLayout_18.addLayout(self.horizontalLayout_146)

        self.line_7 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_7.setObjectName("line_7")
        self.line_7.setFont(font4)
        self.line_7.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout_18.addWidget(self.line_7)

        self.verticalLayout_55.addLayout(self.verticalLayout_18)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_9 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(font6)

        self.horizontalLayout_22.addWidget(self.label_9)

        self.comboBox_spin_x_ = QComboBox(self.scrollAreaWidgetContents_3)
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
        self.comboBox_spin_x_.setObjectName("comboBox_spin_x_")
        sizePolicy7.setHeightForWidth(self.comboBox_spin_x_.sizePolicy().hasHeightForWidth())
        self.comboBox_spin_x_.setSizePolicy(sizePolicy7)
        self.comboBox_spin_x_.setFont(font6)

        self.horizontalLayout_22.addWidget(self.comboBox_spin_x_)

        self.horizontalLayout_83.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.lb_stattest_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.lb_stattest_4.setObjectName("lb_stattest_4")
        sizePolicy6.setHeightForWidth(self.lb_stattest_4.sizePolicy().hasHeightForWidth())
        self.lb_stattest_4.setSizePolicy(sizePolicy6)
        self.lb_stattest_4.setFont(font6)

        self.horizontalLayout_66.addWidget(self.lb_stattest_4)

        self.check_background = QCheckBox(self.scrollAreaWidgetContents_3)
        self.check_background.setObjectName("check_background")
        self.check_background.setEnabled(True)
        sizePolicy20.setHeightForWidth(self.check_background.sizePolicy().hasHeightForWidth())
        self.check_background.setSizePolicy(sizePolicy20)
        self.check_background.setChecked(False)

        self.horizontalLayout_66.addWidget(self.check_background)

        self.horizontalLayout_83.addLayout(self.horizontalLayout_66)

        self.verticalLayout_55.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lb_sd_or_minmax = QLabel(self.scrollAreaWidgetContents_3)
        self.lb_sd_or_minmax.setObjectName("lb_sd_or_minmax")
        self.lb_sd_or_minmax.setFont(font6)

        self.horizontalLayout_17.addWidget(self.lb_sd_or_minmax)

        self.comboBox_sd_or_minmax = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_sd_or_minmax.addItem("")
        self.comboBox_sd_or_minmax.addItem("")
        self.comboBox_sd_or_minmax.setObjectName("comboBox_sd_or_minmax")
        sizePolicy7.setHeightForWidth(self.comboBox_sd_or_minmax.sizePolicy().hasHeightForWidth())
        self.comboBox_sd_or_minmax.setSizePolicy(sizePolicy7)
        self.comboBox_sd_or_minmax.setFont(font6)

        self.horizontalLayout_17.addWidget(self.comboBox_sd_or_minmax)

        self.horizontalLayout_84.addLayout(self.horizontalLayout_17)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lb_bottom_lim = QLabel(self.scrollAreaWidgetContents_3)
        self.lb_bottom_lim.setObjectName("lb_bottom_lim")
        sizePolicy13.setHeightForWidth(self.lb_bottom_lim.sizePolicy().hasHeightForWidth())
        self.lb_bottom_lim.setSizePolicy(sizePolicy13)
        self.lb_bottom_lim.setFont(font6)

        self.horizontalLayout_16.addWidget(self.lb_bottom_lim)

        self.bottom_lim = QLineEdit(self.scrollAreaWidgetContents_3)
        self.bottom_lim.setObjectName("bottom_lim")
        self.bottom_lim.setFont(font6)

        self.horizontalLayout_16.addWidget(self.bottom_lim)

        self.verticalLayout_51.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_139 = QHBoxLayout()
        self.horizontalLayout_139.setObjectName("horizontalLayout_139")
        self.lb_bottom_lim_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.lb_bottom_lim_2.setObjectName("lb_bottom_lim_2")
        sizePolicy13.setHeightForWidth(self.lb_bottom_lim_2.sizePolicy().hasHeightForWidth())
        self.lb_bottom_lim_2.setSizePolicy(sizePolicy13)
        self.lb_bottom_lim_2.setFont(font6)

        self.horizontalLayout_139.addWidget(self.lb_bottom_lim_2)

        self.upper_lim = QLineEdit(self.scrollAreaWidgetContents_3)
        self.upper_lim.setObjectName("upper_lim")
        self.upper_lim.setFont(font6)

        self.horizontalLayout_139.addWidget(self.upper_lim)

        self.verticalLayout_51.addLayout(self.horizontalLayout_139)

        self.horizontalLayout_84.addLayout(self.verticalLayout_51)

        self.verticalLayout_55.addLayout(self.horizontalLayout_84)

        self.gridLayout_19.addLayout(self.verticalLayout_55, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_17.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_16, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName("tab_17")
        self.gridLayout_12 = QGridLayout(self.tab_17)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.scrollArea_4 = QScrollArea(self.tab_17)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollArea_4.setMinimumSize(QSize(0, 170))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 530, 212))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setObjectName("horizontalLayout_141")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lb_stattest_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.lb_stattest_2.setObjectName("lb_stattest_2")
        self.lb_stattest_2.setFont(font6)

        self.horizontalLayout_21.addWidget(self.lb_stattest_2)

        self.check_stat_znachimost = QCheckBox(self.scrollAreaWidgetContents_4)
        self.check_stat_znachimost.setObjectName("check_stat_znachimost")
        self.check_stat_znachimost.setEnabled(True)
        self.check_stat_znachimost.setFont(font6)
        self.check_stat_znachimost.setChecked(True)

        self.horizontalLayout_21.addWidget(self.check_stat_znachimost)

        self.horizontalLayout_141.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_140 = QHBoxLayout()
        self.horizontalLayout_140.setObjectName("horizontalLayout_140")
        self.lb_color_pal_box_21 = QLabel(self.scrollAreaWidgetContents_4)
        self.lb_color_pal_box_21.setObjectName("lb_color_pal_box_21")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_21.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_21.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_21.setFont(font6)

        self.horizontalLayout_140.addWidget(self.lb_color_pal_box_21, 0, Qt.AlignRight)

        self.spinBox_size_stat_znachimost = QSpinBox(self.scrollAreaWidgetContents_4)
        self.spinBox_size_stat_znachimost.setObjectName("spinBox_size_stat_znachimost")
        sizePolicy2.setHeightForWidth(
            self.spinBox_size_stat_znachimost.sizePolicy().hasHeightForWidth()
        )
        self.spinBox_size_stat_znachimost.setSizePolicy(sizePolicy2)
        self.spinBox_size_stat_znachimost.setFont(font6)
        self.spinBox_size_stat_znachimost.setMinimum(1)
        self.spinBox_size_stat_znachimost.setMaximum(100)
        self.spinBox_size_stat_znachimost.setValue(10)

        self.horizontalLayout_140.addWidget(self.spinBox_size_stat_znachimost)

        self.horizontalLayout_141.addLayout(self.horizontalLayout_140)

        self.verticalLayout_56.addLayout(self.horizontalLayout_141)

        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName("horizontalLayout_142")
        self.lb__altern_heposisis_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.lb__altern_heposisis_4.setObjectName("lb__altern_heposisis_4")
        self.lb__altern_heposisis_4.setEnabled(True)
        self.lb__altern_heposisis_4.setFont(font6)

        self.horizontalLayout_142.addWidget(self.lb__altern_heposisis_4)

        self.comboBox_box_plot_sign_stat_znachimost = QComboBox(self.scrollAreaWidgetContents_4)
        self.comboBox_box_plot_sign_stat_znachimost.addItem("")
        self.comboBox_box_plot_sign_stat_znachimost.addItem("")
        self.comboBox_box_plot_sign_stat_znachimost.addItem("")
        self.comboBox_box_plot_sign_stat_znachimost.setObjectName(
            "comboBox_box_plot_sign_stat_znachimost"
        )
        self.comboBox_box_plot_sign_stat_znachimost.setEnabled(True)
        self.comboBox_box_plot_sign_stat_znachimost.setFont(font6)

        self.horizontalLayout_142.addWidget(self.comboBox_box_plot_sign_stat_znachimost)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_25.setObjectName("label_25")
        self.label_25.setFont(font6)

        self.horizontalLayout_142.addWidget(self.label_25)

        self.spinBox_max_n_stars = QSpinBox(self.scrollAreaWidgetContents_4)
        self.spinBox_max_n_stars.setObjectName("spinBox_max_n_stars")
        self.spinBox_max_n_stars.setFont(font6)
        self.spinBox_max_n_stars.setMinimum(1)
        self.spinBox_max_n_stars.setMaximum(4)
        self.spinBox_max_n_stars.setValue(4)

        self.horizontalLayout_142.addWidget(self.spinBox_max_n_stars)

        self.verticalLayout_56.addLayout(self.horizontalLayout_142)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.lb__altern_heposisis = QLabel(self.scrollAreaWidgetContents_4)
        self.lb__altern_heposisis.setObjectName("lb__altern_heposisis")
        self.lb__altern_heposisis.setEnabled(True)
        self.lb__altern_heposisis.setFont(font6)

        self.horizontalLayout_18.addWidget(self.lb__altern_heposisis)

        self.comboBox_alter_hep = QComboBox(self.scrollAreaWidgetContents_4)
        self.comboBox_alter_hep.addItem("")
        self.comboBox_alter_hep.addItem("")
        self.comboBox_alter_hep.addItem("")
        self.comboBox_alter_hep.setObjectName("comboBox_alter_hep")
        self.comboBox_alter_hep.setEnabled(True)
        self.comboBox_alter_hep.setFont(font6)

        self.horizontalLayout_18.addWidget(self.comboBox_alter_hep)

        self.verticalLayout_56.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.lb_stattest = QLabel(self.scrollAreaWidgetContents_4)
        self.lb_stattest.setObjectName("lb_stattest")
        self.lb_stattest.setEnabled(True)
        self.lb_stattest.setFont(font6)

        self.horizontalLayout_23.addWidget(self.lb_stattest)

        self.comboBox_stat_test = QComboBox(self.scrollAreaWidgetContents_4)
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
        self.comboBox_stat_test.setObjectName("comboBox_stat_test")
        self.comboBox_stat_test.setEnabled(True)
        self.comboBox_stat_test.setFont(font6)

        self.horizontalLayout_23.addWidget(self.comboBox_stat_test)

        self.verticalLayout_56.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        self.lb_del_hue_7 = QLabel(self.scrollAreaWidgetContents_4)
        self.lb_del_hue_7.setObjectName("lb_del_hue_7")
        self.lb_del_hue_7.setFont(font6)
        self.lb_del_hue_7.setWordWrap(True)

        self.horizontalLayout_82.addWidget(self.lb_del_hue_7)

        self.STAT_znachimost_order_box_plot = QLineEdit(self.scrollAreaWidgetContents_4)
        self.STAT_znachimost_order_box_plot.setObjectName("STAT_znachimost_order_box_plot")
        self.STAT_znachimost_order_box_plot.setFont(font6)

        self.horizontalLayout_82.addWidget(self.STAT_znachimost_order_box_plot)

        self.verticalLayout_56.addLayout(self.horizontalLayout_82)

        self.gridLayout_7.addLayout(self.verticalLayout_56, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_12.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_17, "")

        self.gridLayout_6.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName("tab_6")
        self.formLayout_2 = QFormLayout(self.tab_6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.frame = QFrame(self.tab_6)
        self.frame.setObjectName("frame")
        sizePolicy11.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy11)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_19 = QVBoxLayout(self.frame)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setSpacing(10)
        self.horizontalLayout_123.setObjectName("horizontalLayout_123")
        self.lb_sd_or_minmax_6 = QLabel(self.frame)
        self.lb_sd_or_minmax_6.setObjectName("lb_sd_or_minmax_6")
        sizePolicy2.setHeightForWidth(self.lb_sd_or_minmax_6.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_6.setSizePolicy(sizePolicy2)
        self.lb_sd_or_minmax_6.setFont(font6)

        self.horizontalLayout_123.addWidget(self.lb_sd_or_minmax_6)

        self.comboBox_correlation_figs_matrix = QComboBox(self.frame)
        self.comboBox_correlation_figs_matrix.addItem("")
        self.comboBox_correlation_figs_matrix.addItem("")
        self.comboBox_correlation_figs_matrix.addItem("")
        self.comboBox_correlation_figs_matrix.setObjectName("comboBox_correlation_figs_matrix")
        sizePolicy7.setHeightForWidth(
            self.comboBox_correlation_figs_matrix.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_correlation_figs_matrix.setSizePolicy(sizePolicy7)
        self.comboBox_correlation_figs_matrix.setFont(font6)

        self.horizontalLayout_123.addWidget(self.comboBox_correlation_figs_matrix)

        self.verticalLayout_19.addLayout(self.horizontalLayout_123)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setSpacing(10)
        self.horizontalLayout_124.setObjectName("horizontalLayout_124")
        self.lb_sd_or_minmax_7 = QLabel(self.frame)
        self.lb_sd_or_minmax_7.setObjectName("lb_sd_or_minmax_7")
        sizePolicy2.setHeightForWidth(self.lb_sd_or_minmax_7.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_7.setSizePolicy(sizePolicy2)
        self.lb_sd_or_minmax_7.setFont(font6)

        self.horizontalLayout_124.addWidget(self.lb_sd_or_minmax_7)

        self.comboBox_correlation_color_map_for_figs = QComboBox(self.frame)
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
        self.comboBox_correlation_color_map_for_figs.setObjectName(
            "comboBox_correlation_color_map_for_figs"
        )
        sizePolicy7.setHeightForWidth(
            self.comboBox_correlation_color_map_for_figs.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_correlation_color_map_for_figs.setSizePolicy(sizePolicy7)
        self.comboBox_correlation_color_map_for_figs.setFont(font6)

        self.horizontalLayout_124.addWidget(self.comboBox_correlation_color_map_for_figs)

        self.verticalLayout_19.addLayout(self.horizontalLayout_124)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.lb_size_corr_matrix = QLabel(self.frame)
        self.lb_size_corr_matrix.setObjectName("lb_size_corr_matrix")
        self.lb_size_corr_matrix.setFont(font6)
        self.lb_size_corr_matrix.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.lb_size_corr_matrix)

        self.corr_mat_figsize = QDoubleSpinBox(self.frame)
        self.corr_mat_figsize.setObjectName("corr_mat_figsize")
        self.corr_mat_figsize.setFont(font6)
        self.corr_mat_figsize.setDecimals(0)
        self.corr_mat_figsize.setMinimum(1.000000000000000)
        self.corr_mat_figsize.setMaximum(100.000000000000000)
        self.corr_mat_figsize.setSingleStep(1.000000000000000)
        self.corr_mat_figsize.setValue(20.000000000000000)

        self.horizontalLayout_28.addWidget(self.corr_mat_figsize)

        self.verticalLayout_19.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.lb_font_in = QLabel(self.frame)
        self.lb_font_in.setObjectName("lb_font_in")
        self.lb_font_in.setFont(font6)
        self.lb_font_in.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.lb_font_in)

        self.font_for_in = QDoubleSpinBox(self.frame)
        self.font_for_in.setObjectName("font_for_in")
        self.font_for_in.setFont(font6)
        self.font_for_in.setDecimals(1)
        self.font_for_in.setMinimum(0.100000000000000)
        self.font_for_in.setSingleStep(0.100000000000000)
        self.font_for_in.setValue(1.300000000000000)

        self.horizontalLayout_29.addWidget(self.font_for_in)

        self.verticalLayout_19.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.lb_font_out = QLabel(self.frame)
        self.lb_font_out.setObjectName("lb_font_out")
        self.lb_font_out.setFont(font6)
        self.lb_font_out.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.lb_font_out)

        self.font_for_out = QDoubleSpinBox(self.frame)
        self.font_for_out.setObjectName("font_for_out")
        self.font_for_out.setFont(font6)
        self.font_for_out.setDecimals(0)
        self.font_for_out.setMinimum(1.000000000000000)
        self.font_for_out.setMaximum(100.000000000000000)
        self.font_for_out.setSingleStep(1.000000000000000)
        self.font_for_out.setValue(26.000000000000000)

        self.horizontalLayout_30.addWidget(self.font_for_out)

        self.verticalLayout_19.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.lb_name_of_title = QLabel(self.frame)
        self.lb_name_of_title.setObjectName("lb_name_of_title")
        self.lb_name_of_title.setFont(font6)
        self.lb_name_of_title.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.lb_name_of_title)

        self.name_of_corr_matrix = QLineEdit(self.frame)
        self.name_of_corr_matrix.setObjectName("name_of_corr_matrix")
        sizePolicy2.setHeightForWidth(self.name_of_corr_matrix.sizePolicy().hasHeightForWidth())
        self.name_of_corr_matrix.setSizePolicy(sizePolicy2)
        self.name_of_corr_matrix.setFont(font6)

        self.horizontalLayout_31.addWidget(self.name_of_corr_matrix)

        self.verticalLayout_19.addLayout(self.horizontalLayout_31)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.frame)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.lb_corr_color_pallete_3 = QLabel(self.tab_2)
        self.lb_corr_color_pallete_3.setObjectName("lb_corr_color_pallete_3")
        self.lb_corr_color_pallete_3.setFont(font6)

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
        self.comboBox_color_pal_corr.setObjectName("comboBox_color_pal_corr")
        self.comboBox_color_pal_corr.setFont(font6)

        self.horizontalLayout_32.addWidget(self.comboBox_color_pal_corr)

        self.verticalLayout_33.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.lb_del_hue_4 = QLabel(self.tab_2)
        self.lb_del_hue_4.setObjectName("lb_del_hue_4")
        self.lb_del_hue_4.setFont(font6)

        self.horizontalLayout_67.addWidget(self.lb_del_hue_4)

        self.check_change_corr_fig_down_limit = QCheckBox(self.tab_2)
        self.check_change_corr_fig_down_limit.setObjectName("check_change_corr_fig_down_limit")
        self.check_change_corr_fig_down_limit.setEnabled(True)
        self.check_change_corr_fig_down_limit.setFont(font6)
        self.check_change_corr_fig_down_limit.setChecked(False)

        self.horizontalLayout_67.addWidget(self.check_change_corr_fig_down_limit)

        self.doubleSpinBox_corr_figs = QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_corr_figs.setObjectName("doubleSpinBox_corr_figs")
        self.doubleSpinBox_corr_figs.setEnabled(False)
        self.doubleSpinBox_corr_figs.setFont(font6)
        self.doubleSpinBox_corr_figs.setMinimum(-100000.000000000000000)
        self.doubleSpinBox_corr_figs.setMaximum(1000000.000000000000000)

        self.horizontalLayout_67.addWidget(self.doubleSpinBox_corr_figs)

        self.verticalLayout_33.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.lb_del_hue_3 = QLabel(self.tab_2)
        self.lb_del_hue_3.setObjectName("lb_del_hue_3")
        self.lb_del_hue_3.setFont(font6)

        self.horizontalLayout_33.addWidget(self.lb_del_hue_3)

        self.del_hue = QLineEdit(self.tab_2)
        self.del_hue.setObjectName("del_hue")
        self.del_hue.setFont(font6)

        self.horizontalLayout_33.addWidget(self.del_hue)

        self.verticalLayout_33.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_70.addLayout(self.verticalLayout_33)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        self.lb_del_hue_5 = QLabel(self.tab_2)
        self.lb_del_hue_5.setObjectName("lb_del_hue_5")
        self.lb_del_hue_5.setFont(font6)

        self.horizontalLayout_68.addWidget(self.lb_del_hue_5)

        self.spinBox_points_corrFIGS = QSpinBox(self.tab_2)
        self.spinBox_points_corrFIGS.setObjectName("spinBox_points_corrFIGS")
        sizePolicy2.setHeightForWidth(self.spinBox_points_corrFIGS.sizePolicy().hasHeightForWidth())
        self.spinBox_points_corrFIGS.setSizePolicy(sizePolicy2)
        self.spinBox_points_corrFIGS.setFont(font6)
        self.spinBox_points_corrFIGS.setMinimum(1)
        self.spinBox_points_corrFIGS.setMaximum(150)
        self.spinBox_points_corrFIGS.setValue(8)

        self.horizontalLayout_68.addWidget(self.spinBox_points_corrFIGS)

        self.verticalLayout_21.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        self.lb_color_pal_box_12 = QLabel(self.tab_2)
        self.lb_color_pal_box_12.setObjectName("lb_color_pal_box_12")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_12.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_12.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_12.setFont(font6)

        self.horizontalLayout_69.addWidget(self.lb_color_pal_box_12)

        self.doubleSpinBox_corr_figs_fontscale = QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_corr_figs_fontscale.setObjectName("doubleSpinBox_corr_figs_fontscale")
        self.doubleSpinBox_corr_figs_fontscale.setFont(font6)
        self.doubleSpinBox_corr_figs_fontscale.setDecimals(1)
        self.doubleSpinBox_corr_figs_fontscale.setMinimum(0.100000000000000)
        self.doubleSpinBox_corr_figs_fontscale.setMaximum(25.000000000000000)
        self.doubleSpinBox_corr_figs_fontscale.setSingleStep(0.100000000000000)
        self.doubleSpinBox_corr_figs_fontscale.setValue(1.000000000000000)

        self.horizontalLayout_69.addWidget(self.doubleSpinBox_corr_figs_fontscale)

        self.verticalLayout_21.addLayout(self.horizontalLayout_69)

        self.check_sort_or_not_corr_figs = QCheckBox(self.tab_2)
        self.check_sort_or_not_corr_figs.setObjectName("check_sort_or_not_corr_figs")
        self.check_sort_or_not_corr_figs.setFont(font6)
        self.check_sort_or_not_corr_figs.setChecked(False)

        self.verticalLayout_21.addWidget(self.check_sort_or_not_corr_figs)

        self.check_setka = QCheckBox(self.tab_2)
        self.check_setka.setObjectName("check_setka")
        self.check_setka.setFont(font6)
        self.check_setka.setChecked(False)

        self.verticalLayout_21.addWidget(self.check_setka)

        self.horizontalLayout_70.addLayout(self.verticalLayout_21)

        self.gridLayout_8.addLayout(self.horizontalLayout_70, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName("tab_11")
        self.formLayout = QFormLayout(self.tab_11)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.horizontalLayout_151 = QHBoxLayout()
        self.horizontalLayout_151.setObjectName("horizontalLayout_151")
        self.lb_stattest_11 = QLabel(self.tab_11)
        self.lb_stattest_11.setObjectName("lb_stattest_11")
        self.lb_stattest_11.setFont(font6)

        self.horizontalLayout_151.addWidget(self.lb_stattest_11)

        self.check_pairplot = QCheckBox(self.tab_11)
        self.check_pairplot.setObjectName("check_pairplot")
        self.check_pairplot.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.check_pairplot.sizePolicy().hasHeightForWidth())
        self.check_pairplot.setSizePolicy(sizePolicy2)
        self.check_pairplot.setChecked(False)

        self.horizontalLayout_151.addWidget(self.check_pairplot)

        self.verticalLayout_58.addLayout(self.horizontalLayout_151)

        self.horizontalLayout_148 = QHBoxLayout()
        self.horizontalLayout_148.setObjectName("horizontalLayout_148")
        self.lb_color_pal_box_24 = QLabel(self.tab_11)
        self.lb_color_pal_box_24.setObjectName("lb_color_pal_box_24")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_24.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_24.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_24.setFont(font6)

        self.horizontalLayout_148.addWidget(self.lb_color_pal_box_24)

        self.doubleSpinBox_pairplot = QDoubleSpinBox(self.tab_11)
        self.doubleSpinBox_pairplot.setObjectName("doubleSpinBox_pairplot")
        self.doubleSpinBox_pairplot.setFont(font6)
        self.doubleSpinBox_pairplot.setDecimals(1)
        self.doubleSpinBox_pairplot.setMinimum(0.100000000000000)
        self.doubleSpinBox_pairplot.setSingleStep(0.100000000000000)
        self.doubleSpinBox_pairplot.setValue(1.000000000000000)

        self.horizontalLayout_148.addWidget(self.doubleSpinBox_pairplot)

        self.verticalLayout_58.addLayout(self.horizontalLayout_148)

        self.horizontalLayout_150 = QHBoxLayout()
        self.horizontalLayout_150.setObjectName("horizontalLayout_150")
        self.lb_color_pal_box_25 = QLabel(self.tab_11)
        self.lb_color_pal_box_25.setObjectName("lb_color_pal_box_25")
        sizePolicy11.setHeightForWidth(self.lb_color_pal_box_25.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_25.setSizePolicy(sizePolicy11)
        self.lb_color_pal_box_25.setFont(font6)

        self.horizontalLayout_150.addWidget(self.lb_color_pal_box_25)

        self.comboBox_color_pairplot = QComboBox(self.tab_11)
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.addItem("")
        self.comboBox_color_pairplot.setObjectName("comboBox_color_pairplot")
        sizePolicy2.setHeightForWidth(self.comboBox_color_pairplot.sizePolicy().hasHeightForWidth())
        self.comboBox_color_pairplot.setSizePolicy(sizePolicy2)
        self.comboBox_color_pairplot.setFont(font6)

        self.horizontalLayout_150.addWidget(self.comboBox_color_pairplot)

        self.verticalLayout_58.addLayout(self.horizontalLayout_150)

        self.horizontalLayout_154 = QHBoxLayout()
        self.horizontalLayout_154.setObjectName("horizontalLayout_154")
        self.lb_color_pal_box_28 = QLabel(self.tab_11)
        self.lb_color_pal_box_28.setObjectName("lb_color_pal_box_28")
        sizePolicy11.setHeightForWidth(self.lb_color_pal_box_28.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_28.setSizePolicy(sizePolicy11)
        self.lb_color_pal_box_28.setFont(font6)

        self.horizontalLayout_154.addWidget(self.lb_color_pal_box_28)

        self.comboBox_pairplot_kind = QComboBox(self.tab_11)
        self.comboBox_pairplot_kind.addItem("")
        self.comboBox_pairplot_kind.addItem("")
        self.comboBox_pairplot_kind.addItem("")
        self.comboBox_pairplot_kind.addItem("")
        self.comboBox_pairplot_kind.setObjectName("comboBox_pairplot_kind")
        sizePolicy2.setHeightForWidth(self.comboBox_pairplot_kind.sizePolicy().hasHeightForWidth())
        self.comboBox_pairplot_kind.setSizePolicy(sizePolicy2)
        self.comboBox_pairplot_kind.setFont(font6)

        self.horizontalLayout_154.addWidget(self.comboBox_pairplot_kind)

        self.verticalLayout_58.addLayout(self.horizontalLayout_154)

        self.horizontalLayout_153 = QHBoxLayout()
        self.horizontalLayout_153.setObjectName("horizontalLayout_153")
        self.lb_color_pal_box_27 = QLabel(self.tab_11)
        self.lb_color_pal_box_27.setObjectName("lb_color_pal_box_27")
        sizePolicy11.setHeightForWidth(self.lb_color_pal_box_27.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_27.setSizePolicy(sizePolicy11)
        self.lb_color_pal_box_27.setFont(font6)

        self.horizontalLayout_153.addWidget(self.lb_color_pal_box_27)

        self.comboBox_style_pairplot = QComboBox(self.tab_11)
        self.comboBox_style_pairplot.addItem("")
        self.comboBox_style_pairplot.addItem("")
        self.comboBox_style_pairplot.addItem("")
        self.comboBox_style_pairplot.addItem("")
        self.comboBox_style_pairplot.addItem("")
        self.comboBox_style_pairplot.setObjectName("comboBox_style_pairplot")
        sizePolicy2.setHeightForWidth(self.comboBox_style_pairplot.sizePolicy().hasHeightForWidth())
        self.comboBox_style_pairplot.setSizePolicy(sizePolicy2)
        self.comboBox_style_pairplot.setFont(font6)

        self.horizontalLayout_153.addWidget(self.comboBox_style_pairplot)

        self.verticalLayout_58.addLayout(self.horizontalLayout_153)

        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setObjectName("horizontalLayout_152")
        self.lb_color_pal_box_26 = QLabel(self.tab_11)
        self.lb_color_pal_box_26.setObjectName("lb_color_pal_box_26")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_26.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_26.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_26.setFont(font6)

        self.horizontalLayout_152.addWidget(self.lb_color_pal_box_26)

        self.spinBox_point_size_for_pairplot = QSpinBox(self.tab_11)
        self.spinBox_point_size_for_pairplot.setObjectName("spinBox_point_size_for_pairplot")
        sizePolicy2.setHeightForWidth(
            self.spinBox_point_size_for_pairplot.sizePolicy().hasHeightForWidth()
        )
        self.spinBox_point_size_for_pairplot.setSizePolicy(sizePolicy2)
        self.spinBox_point_size_for_pairplot.setFont(font6)
        self.spinBox_point_size_for_pairplot.setMinimum(1)
        self.spinBox_point_size_for_pairplot.setMaximum(1000)
        self.spinBox_point_size_for_pairplot.setValue(25)

        self.horizontalLayout_152.addWidget(self.spinBox_point_size_for_pairplot)

        self.verticalLayout_58.addLayout(self.horizontalLayout_152)

        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_58)

        self.tabWidget.addTab(self.tab_11, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName("tab_13")
        self.formLayout_3 = QFormLayout(self.tab_13)
        self.formLayout_3.setObjectName("formLayout_3")
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.lb_color_pal_box_29 = QLabel(self.tab_13)
        self.lb_color_pal_box_29.setObjectName("lb_color_pal_box_29")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_29.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_29.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_29.setFont(font6)

        self.horizontalLayout_38.addWidget(self.lb_color_pal_box_29)

        self.doubleSpinBox_jointplot = QDoubleSpinBox(self.tab_13)
        self.doubleSpinBox_jointplot.setObjectName("doubleSpinBox_jointplot")
        self.doubleSpinBox_jointplot.setFont(font6)
        self.doubleSpinBox_jointplot.setDecimals(1)
        self.doubleSpinBox_jointplot.setMinimum(0.100000000000000)
        self.doubleSpinBox_jointplot.setSingleStep(0.100000000000000)
        self.doubleSpinBox_jointplot.setValue(1.000000000000000)

        self.horizontalLayout_38.addWidget(self.doubleSpinBox_jointplot)

        self.verticalLayout_57.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setObjectName("horizontalLayout_157")
        self.lb_color_pal_box_30 = QLabel(self.tab_13)
        self.lb_color_pal_box_30.setObjectName("lb_color_pal_box_30")
        sizePolicy11.setHeightForWidth(self.lb_color_pal_box_30.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_30.setSizePolicy(sizePolicy11)
        self.lb_color_pal_box_30.setFont(font6)

        self.horizontalLayout_157.addWidget(self.lb_color_pal_box_30)

        self.comboBox_color_jointplot = QComboBox(self.tab_13)
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.addItem("")
        self.comboBox_color_jointplot.setObjectName("comboBox_color_jointplot")
        sizePolicy2.setHeightForWidth(
            self.comboBox_color_jointplot.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_color_jointplot.setSizePolicy(sizePolicy2)
        self.comboBox_color_jointplot.setFont(font6)

        self.horizontalLayout_157.addWidget(self.comboBox_color_jointplot)

        self.verticalLayout_57.addLayout(self.horizontalLayout_157)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName("horizontalLayout_158")
        self.lb_color_pal_box_32 = QLabel(self.tab_13)
        self.lb_color_pal_box_32.setObjectName("lb_color_pal_box_32")
        sizePolicy11.setHeightForWidth(self.lb_color_pal_box_32.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_32.setSizePolicy(sizePolicy11)
        self.lb_color_pal_box_32.setFont(font6)

        self.horizontalLayout_158.addWidget(self.lb_color_pal_box_32)

        self.comboBox_pairplot_jointplot = QComboBox(self.tab_13)
        self.comboBox_pairplot_jointplot.addItem("")
        self.comboBox_pairplot_jointplot.addItem("")
        self.comboBox_pairplot_jointplot.addItem("")
        self.comboBox_pairplot_jointplot.setObjectName("comboBox_pairplot_jointplot")
        sizePolicy2.setHeightForWidth(
            self.comboBox_pairplot_jointplot.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_pairplot_jointplot.setSizePolicy(sizePolicy2)
        self.comboBox_pairplot_jointplot.setFont(font6)

        self.horizontalLayout_158.addWidget(self.comboBox_pairplot_jointplot)

        self.verticalLayout_57.addLayout(self.horizontalLayout_158)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setObjectName("horizontalLayout_159")
        self.lb_color_pal_box_33 = QLabel(self.tab_13)
        self.lb_color_pal_box_33.setObjectName("lb_color_pal_box_33")
        sizePolicy11.setHeightForWidth(self.lb_color_pal_box_33.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_33.setSizePolicy(sizePolicy11)
        self.lb_color_pal_box_33.setFont(font6)

        self.horizontalLayout_159.addWidget(self.lb_color_pal_box_33)

        self.comboBox_style_jointplot = QComboBox(self.tab_13)
        self.comboBox_style_jointplot.addItem("")
        self.comboBox_style_jointplot.addItem("")
        self.comboBox_style_jointplot.addItem("")
        self.comboBox_style_jointplot.addItem("")
        self.comboBox_style_jointplot.addItem("")
        self.comboBox_style_jointplot.setObjectName("comboBox_style_jointplot")
        sizePolicy2.setHeightForWidth(
            self.comboBox_style_jointplot.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_style_jointplot.setSizePolicy(sizePolicy2)
        self.comboBox_style_jointplot.setFont(font6)

        self.horizontalLayout_159.addWidget(self.comboBox_style_jointplot)

        self.verticalLayout_57.addLayout(self.horizontalLayout_159)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName("horizontalLayout_160")
        self.lb_color_pal_box_31 = QLabel(self.tab_13)
        self.lb_color_pal_box_31.setObjectName("lb_color_pal_box_31")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_31.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_31.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_31.setFont(font6)

        self.horizontalLayout_160.addWidget(self.lb_color_pal_box_31)

        self.spinBox_point_size_for_jointplot = QSpinBox(self.tab_13)
        self.spinBox_point_size_for_jointplot.setObjectName("spinBox_point_size_for_jointplot")
        sizePolicy2.setHeightForWidth(
            self.spinBox_point_size_for_jointplot.sizePolicy().hasHeightForWidth()
        )
        self.spinBox_point_size_for_jointplot.setSizePolicy(sizePolicy2)
        self.spinBox_point_size_for_jointplot.setFont(font6)
        self.spinBox_point_size_for_jointplot.setMinimum(25)
        self.spinBox_point_size_for_jointplot.setMaximum(1000)
        self.spinBox_point_size_for_jointplot.setValue(25)

        self.horizontalLayout_160.addWidget(self.spinBox_point_size_for_jointplot)

        self.verticalLayout_57.addLayout(self.horizontalLayout_160)

        self.formLayout_3.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_57)

        self.tabWidget.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName("tab_14")
        self.gridLayout_14 = QGridLayout(self.tab_14)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_164 = QHBoxLayout()
        self.horizontalLayout_164.setSpacing(10)
        self.horizontalLayout_164.setObjectName("horizontalLayout_164")
        self.lb_sd_or_minmax_8 = QLabel(self.tab_14)
        self.lb_sd_or_minmax_8.setObjectName("lb_sd_or_minmax_8")
        sizePolicy2.setHeightForWidth(self.lb_sd_or_minmax_8.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_8.setSizePolicy(sizePolicy2)
        self.lb_sd_or_minmax_8.setFont(font6)

        self.horizontalLayout_164.addWidget(self.lb_sd_or_minmax_8)

        self.comboBox_correlation_one_parameter = QComboBox(self.tab_14)
        self.comboBox_correlation_one_parameter.addItem("")
        self.comboBox_correlation_one_parameter.addItem("")
        self.comboBox_correlation_one_parameter.addItem("")
        self.comboBox_correlation_one_parameter.setObjectName("comboBox_correlation_one_parameter")
        sizePolicy7.setHeightForWidth(
            self.comboBox_correlation_one_parameter.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_correlation_one_parameter.setSizePolicy(sizePolicy7)
        self.comboBox_correlation_one_parameter.setFont(font6)

        self.horizontalLayout_164.addWidget(self.comboBox_correlation_one_parameter)

        self.gridLayout_14.addLayout(self.horizontalLayout_164, 6, 0, 1, 1)

        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setObjectName("horizontalLayout_162")
        self.lb_color_pal_box_34 = QLabel(self.tab_14)
        self.lb_color_pal_box_34.setObjectName("lb_color_pal_box_34")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_34.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_34.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_34.setFont(font6)

        self.horizontalLayout_162.addWidget(self.lb_color_pal_box_34)

        self.doubleSpinBox_size_for_one_correlation = QDoubleSpinBox(self.tab_14)
        self.doubleSpinBox_size_for_one_correlation.setObjectName(
            "doubleSpinBox_size_for_one_correlation"
        )
        self.doubleSpinBox_size_for_one_correlation.setFont(font6)
        self.doubleSpinBox_size_for_one_correlation.setDecimals(1)
        self.doubleSpinBox_size_for_one_correlation.setMinimum(0.100000000000000)
        self.doubleSpinBox_size_for_one_correlation.setSingleStep(0.100000000000000)
        self.doubleSpinBox_size_for_one_correlation.setValue(1.000000000000000)

        self.horizontalLayout_162.addWidget(self.doubleSpinBox_size_for_one_correlation)

        self.horizontalSpacer_6 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_6)

        self.gridLayout_14.addLayout(self.horizontalLayout_162, 2, 0, 1, 1)

        self.horizontalLayout_163 = QHBoxLayout()
        self.horizontalLayout_163.setObjectName("horizontalLayout_163")
        self.lb_color_pal_box_35 = QLabel(self.tab_14)
        self.lb_color_pal_box_35.setObjectName("lb_color_pal_box_35")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_35.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_35.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_35.setFont(font6)

        self.horizontalLayout_163.addWidget(self.lb_color_pal_box_35)

        self.doubleSpinBox_one_correlation = QDoubleSpinBox(self.tab_14)
        self.doubleSpinBox_one_correlation.setObjectName("doubleSpinBox_one_correlation")
        self.doubleSpinBox_one_correlation.setFont(font6)
        self.doubleSpinBox_one_correlation.setDecimals(2)
        self.doubleSpinBox_one_correlation.setMinimum(0.000000000000000)
        self.doubleSpinBox_one_correlation.setMaximum(1.000000000000000)
        self.doubleSpinBox_one_correlation.setSingleStep(0.050000000000000)
        self.doubleSpinBox_one_correlation.setValue(0.300000000000000)

        self.horizontalLayout_163.addWidget(self.doubleSpinBox_one_correlation)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_7)

        self.gridLayout_14.addLayout(self.horizontalLayout_163, 5, 0, 1, 1)

        self.check_corr_one_parameter_only_one = QCheckBox(self.tab_14)
        self.check_corr_one_parameter_only_one.setObjectName("check_corr_one_parameter_only_one")
        self.check_corr_one_parameter_only_one.setFont(font6)
        self.check_corr_one_parameter_only_one.setChecked(True)

        self.gridLayout_14.addWidget(self.check_corr_one_parameter_only_one, 0, 0, 1, 1)

        self.check_corr_one_parameter_plot_sep_wind = QCheckBox(self.tab_14)
        self.check_corr_one_parameter_plot_sep_wind.setObjectName(
            "check_corr_one_parameter_plot_sep_wind"
        )
        self.check_corr_one_parameter_plot_sep_wind.setFont(font6)
        self.check_corr_one_parameter_plot_sep_wind.setChecked(False)

        self.gridLayout_14.addWidget(self.check_corr_one_parameter_plot_sep_wind, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_14, "")

        self.verticalLayout_17.addWidget(self.tabWidget)

        self.gridLayout_4.addLayout(self.verticalLayout_17, 0, 0, 1, 1)

        self.btn_plot_and_save_figs = QPushButton(self.tab)
        self.btn_plot_and_save_figs.setObjectName("btn_plot_and_save_figs")
        self.btn_plot_and_save_figs.setFont(font6)
        self.btn_plot_and_save_figs.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.gridLayout_4.addWidget(self.btn_plot_and_save_figs, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab, "")
        self.widget2 = QWidget()
        self.widget2.setObjectName("widget2")
        self.gridLayout_11 = QGridLayout(self.widget2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame1 = QFrame(self.widget2)
        self.frame1.setObjectName("frame1")
        sizePolicy13.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy13)
        self.verticalLayout_10 = QVBoxLayout(self.frame1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lb_path_for_profile = QLabel(self.frame1)
        self.lb_path_for_profile.setObjectName("lb_path_for_profile")
        sizePolicy13.setHeightForWidth(self.lb_path_for_profile.sizePolicy().hasHeightForWidth())
        self.lb_path_for_profile.setSizePolicy(sizePolicy13)
        self.lb_path_for_profile.setFont(font6)

        self.horizontalLayout_10.addWidget(self.lb_path_for_profile)

        self.path_for_profile = QLineEdit(self.frame1)
        self.path_for_profile.setObjectName("path_for_profile")
        self.path_for_profile.setFont(font6)

        self.horizontalLayout_10.addWidget(self.path_for_profile)

        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lb_patient_data = QLabel(self.frame1)
        self.lb_patient_data.setObjectName("lb_patient_data")
        sizePolicy13.setHeightForWidth(self.lb_patient_data.sizePolicy().hasHeightForWidth())
        self.lb_patient_data.setSizePolicy(sizePolicy13)
        self.lb_patient_data.setFont(font6)

        self.horizontalLayout_11.addWidget(self.lb_patient_data)

        self.patient_data = QLineEdit(self.frame1)
        self.patient_data.setObjectName("patient_data")
        self.patient_data.setFont(font6)

        self.horizontalLayout_11.addWidget(self.patient_data)

        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lb_norm_data = QLabel(self.frame1)
        self.lb_norm_data.setObjectName("lb_norm_data")
        sizePolicy13.setHeightForWidth(self.lb_norm_data.sizePolicy().hasHeightForWidth())
        self.lb_norm_data.setSizePolicy(sizePolicy13)
        self.lb_norm_data.setFont(font6)

        self.horizontalLayout_12.addWidget(self.lb_norm_data)

        self.norm_data = QLineEdit(self.frame1)
        self.norm_data.setObjectName("norm_data")
        self.norm_data.setFont(font6)

        self.horizontalLayout_12.addWidget(self.norm_data)

        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.line_19 = QFrame(self.frame1)
        self.line_19.setObjectName("line_19")
        self.line_19.setFont(font4)
        self.line_19.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_19.setFrameShadow(QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QFrame.HLine)

        self.verticalLayout_10.addWidget(self.line_19)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setObjectName("horizontalLayout_132")
        self.lb_norm_data_2 = QLabel(self.frame1)
        self.lb_norm_data_2.setObjectName("lb_norm_data_2")
        sizePolicy13.setHeightForWidth(self.lb_norm_data_2.sizePolicy().hasHeightForWidth())
        self.lb_norm_data_2.setSizePolicy(sizePolicy13)
        self.lb_norm_data_2.setFont(font6)

        self.horizontalLayout_132.addWidget(self.lb_norm_data_2)

        self.profile_title_rad = QLineEdit(self.frame1)
        self.profile_title_rad.setObjectName("profile_title_rad")
        self.profile_title_rad.setFont(font6)

        self.horizontalLayout_132.addWidget(self.profile_title_rad)

        self.verticalLayout_10.addLayout(self.horizontalLayout_132)

        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setObjectName("horizontalLayout_133")
        self.lb_norm_data_3 = QLabel(self.frame1)
        self.lb_norm_data_3.setObjectName("lb_norm_data_3")
        sizePolicy13.setHeightForWidth(self.lb_norm_data_3.sizePolicy().hasHeightForWidth())
        self.lb_norm_data_3.setSizePolicy(sizePolicy13)
        self.lb_norm_data_3.setFont(font6)

        self.horizontalLayout_133.addWidget(self.lb_norm_data_3)

        self.profile_title_lin = QLineEdit(self.frame1)
        self.profile_title_lin.setObjectName("profile_title_lin")
        self.profile_title_lin.setFont(font6)

        self.horizontalLayout_133.addWidget(self.profile_title_lin)

        self.check_profile_legend = QCheckBox(self.frame1)
        self.check_profile_legend.setObjectName("check_profile_legend")
        self.check_profile_legend.setEnabled(True)
        self.check_profile_legend.setFont(font6)
        self.check_profile_legend.setChecked(True)

        self.horizontalLayout_133.addWidget(self.check_profile_legend)

        self.verticalLayout_10.addLayout(self.horizontalLayout_133)

        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setObjectName("horizontalLayout_134")
        self.lb__altern_heposisis_3 = QLabel(self.frame1)
        self.lb__altern_heposisis_3.setObjectName("lb__altern_heposisis_3")
        self.lb__altern_heposisis_3.setEnabled(True)
        self.lb__altern_heposisis_3.setFont(font6)

        self.horizontalLayout_134.addWidget(self.lb__altern_heposisis_3)

        self.comboBox_profile_lin_spin = QComboBox(self.frame1)
        self.comboBox_profile_lin_spin.addItem("")
        self.comboBox_profile_lin_spin.addItem("")
        self.comboBox_profile_lin_spin.setObjectName("comboBox_profile_lin_spin")
        self.comboBox_profile_lin_spin.setEnabled(True)
        sizePolicy2.setHeightForWidth(
            self.comboBox_profile_lin_spin.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_profile_lin_spin.setSizePolicy(sizePolicy2)
        self.comboBox_profile_lin_spin.setFont(font6)

        self.horizontalLayout_134.addWidget(self.comboBox_profile_lin_spin)

        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName("horizontalLayout_135")
        self.lb_color_pal_box_20 = QLabel(self.frame1)
        self.lb_color_pal_box_20.setObjectName("lb_color_pal_box_20")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_20.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_20.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_20.setFont(font6)

        self.horizontalLayout_135.addWidget(self.lb_color_pal_box_20)

        self.doubleSpinBoX_profile = QDoubleSpinBox(self.frame1)
        self.doubleSpinBoX_profile.setObjectName("doubleSpinBoX_profile")
        self.doubleSpinBoX_profile.setFont(font6)
        self.doubleSpinBoX_profile.setDecimals(1)
        self.doubleSpinBoX_profile.setMinimum(0.100000000000000)
        self.doubleSpinBoX_profile.setSingleStep(0.100000000000000)
        self.doubleSpinBoX_profile.setValue(1.000000000000000)

        self.horizontalLayout_135.addWidget(self.doubleSpinBoX_profile)

        self.horizontalLayout_134.addLayout(self.horizontalLayout_135)

        self.verticalLayout_10.addLayout(self.horizontalLayout_134)

        self.gridLayout_11.addWidget(self.frame1, 0, 0, 1, 1)

        self.tyt = QFrame(self.widget2)
        self.tyt.setObjectName("tyt")
        sizePolicy13.setHeightForWidth(self.tyt.sizePolicy().hasHeightForWidth())
        self.tyt.setSizePolicy(sizePolicy13)
        self.tyt.setFont(font6)
        self.tyt.setStyleSheet(
            "QFrame#tyt{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.horizontalLayout_9 = QHBoxLayout(self.tyt)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QLabel(self.tyt)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font6)

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_4 = QLabel(self.tyt)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font6)

        self.verticalLayout_6.addWidget(self.label_4)

        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.patient_prof = QLineEdit(self.tyt)
        self.patient_prof.setObjectName("patient_prof")
        self.patient_prof.setFont(font6)

        self.verticalLayout_7.addWidget(self.patient_prof)

        self.color_for_patient = QLineEdit(self.tyt)
        self.color_for_patient.setObjectName("color_for_patient")
        self.color_for_patient.setFont(font6)

        self.verticalLayout_7.addWidget(self.color_for_patient)

        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.check_profile_pat_line = QCheckBox(self.tyt)
        self.check_profile_pat_line.setObjectName("check_profile_pat_line")
        self.check_profile_pat_line.setEnabled(True)
        self.check_profile_pat_line.setFont(font6)
        self.check_profile_pat_line.setChecked(True)

        self.verticalLayout_34.addWidget(self.check_profile_pat_line)

        self.check_profile_pat_sd = QCheckBox(self.tyt)
        self.check_profile_pat_sd.setObjectName("check_profile_pat_sd")
        self.check_profile_pat_sd.setEnabled(True)
        self.check_profile_pat_sd.setFont(font6)
        self.check_profile_pat_sd.setChecked(True)

        self.verticalLayout_34.addWidget(self.check_profile_pat_sd)

        self.horizontalLayout_9.addLayout(self.verticalLayout_34)

        self.gridLayout_11.addWidget(self.tyt, 1, 0, 1, 1)

        self.opo = QFrame(self.widget2)
        self.opo.setObjectName("opo")
        sizePolicy13.setHeightForWidth(self.opo.sizePolicy().hasHeightForWidth())
        self.opo.setSizePolicy(sizePolicy13)
        self.opo.setStyleSheet(
            "QFrame#opo{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.horizontalLayout_6 = QHBoxLayout(self.opo)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QLabel(self.opo)
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font6)

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_7 = QLabel(self.opo)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font6)

        self.verticalLayout_9.addWidget(self.label_7)

        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.norm_prof = QLineEdit(self.opo)
        self.norm_prof.setObjectName("norm_prof")
        self.norm_prof.setFont(font6)

        self.verticalLayout_8.addWidget(self.norm_prof)

        self.color_for_norm = QLineEdit(self.opo)
        self.color_for_norm.setObjectName("color_for_norm")
        self.color_for_norm.setFont(font6)

        self.verticalLayout_8.addWidget(self.color_for_norm)

        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.check_profile_norm_line = QCheckBox(self.opo)
        self.check_profile_norm_line.setObjectName("check_profile_norm_line")
        self.check_profile_norm_line.setEnabled(True)
        self.check_profile_norm_line.setFont(font6)
        self.check_profile_norm_line.setChecked(False)

        self.verticalLayout_35.addWidget(self.check_profile_norm_line)

        self.check_profile_norm_sd = QCheckBox(self.opo)
        self.check_profile_norm_sd.setObjectName("check_profile_norm_sd")
        self.check_profile_norm_sd.setEnabled(True)
        self.check_profile_norm_sd.setFont(font6)
        self.check_profile_norm_sd.setChecked(True)

        self.verticalLayout_35.addWidget(self.check_profile_norm_sd)

        self.horizontalLayout_6.addLayout(self.verticalLayout_35)

        self.gridLayout_11.addWidget(self.opo, 2, 0, 1, 1)

        self.horizontalLayout_155 = QHBoxLayout()
        self.horizontalLayout_155.setObjectName("horizontalLayout_155")
        self.btn_plot_and_save_profile = QPushButton(self.widget2)
        self.btn_plot_and_save_profile.setObjectName("btn_plot_and_save_profile")
        self.btn_plot_and_save_profile.setFont(font6)
        self.btn_plot_and_save_profile.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.horizontalLayout_155.addWidget(self.btn_plot_and_save_profile)

        self.check_profile_relative = QCheckBox(self.widget2)
        self.check_profile_relative.setObjectName("check_profile_relative")
        self.check_profile_relative.setEnabled(True)
        self.check_profile_relative.setFont(font6)
        self.check_profile_relative.setChecked(False)

        self.horizontalLayout_155.addWidget(self.check_profile_relative)

        self.gridLayout_11.addLayout(self.horizontalLayout_155, 3, 0, 1, 1)

        self.scrollArea = QScrollArea(self.widget2)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 633, 206))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if self.tableWidget.columnCount() < 3:
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if self.tableWidget.rowCount() < 4:
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setBackground(QColor(255, 255, 255))
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(255, 255, 255))
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
        self.tableWidget.setObjectName("tableWidget")
        sizePolicy12.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy12)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setFrameShape(QFrame.HLine)
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.verticalHeader().setMinimumSectionSize(15)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.lb_norm_data_4 = QLabel(self.scrollAreaWidgetContents)
        self.lb_norm_data_4.setObjectName("lb_norm_data_4")
        sizePolicy13.setHeightForWidth(self.lb_norm_data_4.sizePolicy().hasHeightForWidth())
        self.lb_norm_data_4.setSizePolicy(sizePolicy13)
        self.lb_norm_data_4.setFont(font6)

        self.gridLayout_2.addWidget(self.lb_norm_data_4, 0, 0, 1, 1, Qt.AlignHCenter)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 4, 0, 1, 1)

        self.tabWidget_2.addTab(self.widget2, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_13 = QGridLayout(self.tab_8)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName("horizontalLayout_75")
        self.lb_path_for_plot_2 = QLabel(self.tab_8)
        self.lb_path_for_plot_2.setObjectName("lb_path_for_plot_2")
        self.lb_path_for_plot_2.setFont(font6)

        self.horizontalLayout_75.addWidget(self.lb_path_for_plot_2)

        self.path_for_pivot_table = QLineEdit(self.tab_8)
        self.path_for_pivot_table.setObjectName("path_for_pivot_table")
        self.path_for_pivot_table.setFont(font6)

        self.horizontalLayout_75.addWidget(self.path_for_pivot_table)

        self.verticalLayout_36.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName("horizontalLayout_76")
        self.lb_exel_name_2 = QLabel(self.tab_8)
        self.lb_exel_name_2.setObjectName("lb_exel_name_2")
        self.lb_exel_name_2.setFont(font6)

        self.horizontalLayout_76.addWidget(self.lb_exel_name_2)

        self.comboBox_pivot_table = QComboBox(self.tab_8)
        self.comboBox_pivot_table.setObjectName("comboBox_pivot_table")

        self.horizontalLayout_76.addWidget(self.comboBox_pivot_table)

        self.verticalLayout_36.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName("horizontalLayout_120")
        self.lb_exel_name_7 = QLabel(self.tab_8)
        self.lb_exel_name_7.setObjectName("lb_exel_name_7")
        self.lb_exel_name_7.setFont(font6)

        self.horizontalLayout_120.addWidget(self.lb_exel_name_7)

        self.comboBox_pivot_table_excel_sheet = QComboBox(self.tab_8)
        self.comboBox_pivot_table_excel_sheet.setObjectName("comboBox_pivot_table_excel_sheet")

        self.horizontalLayout_120.addWidget(self.comboBox_pivot_table_excel_sheet)

        self.verticalLayout_36.addLayout(self.horizontalLayout_120)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        self.lb_hue_name_2 = QLabel(self.tab_8)
        self.lb_hue_name_2.setObjectName("lb_hue_name_2")
        self.lb_hue_name_2.setFont(font6)

        self.horizontalLayout_77.addWidget(self.lb_hue_name_2)

        self.comboBox_pivot_hue = QComboBox(self.tab_8)
        self.comboBox_pivot_hue.setObjectName("comboBox_pivot_hue")

        self.horizontalLayout_77.addWidget(self.comboBox_pivot_hue)

        self.verticalLayout_36.addLayout(self.horizontalLayout_77)

        self.verticalLayout_37.addLayout(self.verticalLayout_36)

        self.verticalLayout_43.addLayout(self.verticalLayout_37)

        self.line_2 = QFrame(self.tab_8)
        self.line_2.setObjectName("line_2")
        self.line_2.setFont(font4)
        self.line_2.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(10)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_43.addWidget(self.line_2)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_43.addItem(self.verticalSpacer_6)

        self.yyy = QFrame(self.tab_8)
        self.yyy.setObjectName("yyy")
        self.yyy.setStyleSheet(
            "QFrame#yyy{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_40 = QVBoxLayout(self.yyy)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(8, 8, 8, 8)
        self.lb_color_pal_box_17 = QLabel(self.yyy)
        self.lb_color_pal_box_17.setObjectName("lb_color_pal_box_17")
        sizePolicy.setHeightForWidth(self.lb_color_pal_box_17.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_17.setSizePolicy(sizePolicy)
        font11 = QFont()
        font11.setPointSize(11)
        font11.setBold(False)
        font11.setUnderline(True)
        self.lb_color_pal_box_17.setFont(font11)

        self.verticalLayout_40.addWidget(self.lb_color_pal_box_17, 0, Qt.AlignHCenter)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        self.lb_color_pal_box_8 = QLabel(self.yyy)
        self.lb_color_pal_box_8.setObjectName("lb_color_pal_box_8")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_8.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_8.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_8.setFont(font6)

        self.horizontalLayout_79.addWidget(self.lb_color_pal_box_8)

        self.spinBox_pivot_table = QSpinBox(self.yyy)
        self.spinBox_pivot_table.setObjectName("spinBox_pivot_table")
        sizePolicy2.setHeightForWidth(self.spinBox_pivot_table.sizePolicy().hasHeightForWidth())
        self.spinBox_pivot_table.setSizePolicy(sizePolicy2)
        self.spinBox_pivot_table.setFont(font6)
        self.spinBox_pivot_table.setMinimum(0)
        self.spinBox_pivot_table.setMaximum(10)
        self.spinBox_pivot_table.setValue(1)

        self.horizontalLayout_79.addWidget(self.spinBox_pivot_table)

        self.horizontalLayout_80.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName("horizontalLayout_78")
        self.lb_sd_or_minmax_2 = QLabel(self.yyy)
        self.lb_sd_or_minmax_2.setObjectName("lb_sd_or_minmax_2")
        self.lb_sd_or_minmax_2.setFont(font6)

        self.horizontalLayout_78.addWidget(self.lb_sd_or_minmax_2)

        self.comboBox_sd_or_se_pivot = QComboBox(self.yyy)
        self.comboBox_sd_or_se_pivot.addItem("")
        self.comboBox_sd_or_se_pivot.addItem("")
        self.comboBox_sd_or_se_pivot.setObjectName("comboBox_sd_or_se_pivot")
        sizePolicy7.setHeightForWidth(self.comboBox_sd_or_se_pivot.sizePolicy().hasHeightForWidth())
        self.comboBox_sd_or_se_pivot.setSizePolicy(sizePolicy7)
        self.comboBox_sd_or_se_pivot.setFont(font6)

        self.horizontalLayout_78.addWidget(self.comboBox_sd_or_se_pivot)

        self.horizontalLayout_80.addLayout(self.horizontalLayout_78)

        self.verticalLayout_40.addLayout(self.horizontalLayout_80)

        self.btn_plot_and_save_pivot_table = QPushButton(self.yyy)
        self.btn_plot_and_save_pivot_table.setObjectName("btn_plot_and_save_pivot_table")
        self.btn_plot_and_save_pivot_table.setFont(font6)
        self.btn_plot_and_save_pivot_table.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.verticalLayout_40.addWidget(self.btn_plot_and_save_pivot_table)

        self.verticalLayout_43.addWidget(self.yyy)

        self.verticalSpacer_5 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_43.addItem(self.verticalSpacer_5)

        self.ppp = QFrame(self.tab_8)
        self.ppp.setObjectName("ppp")
        self.ppp.setStyleSheet(
            "QFrame#ppp{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_42 = QVBoxLayout(self.ppp)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(8, 8, 8, 8)
        self.lb_color_pal_box_18 = QLabel(self.ppp)
        self.lb_color_pal_box_18.setObjectName("lb_color_pal_box_18")
        sizePolicy.setHeightForWidth(self.lb_color_pal_box_18.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_18.setSizePolicy(sizePolicy)
        self.lb_color_pal_box_18.setFont(font11)

        self.verticalLayout_42.addWidget(self.lb_color_pal_box_18, 0, Qt.AlignHCenter)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setSpacing(10)
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.lb_sd_or_minmax_3 = QLabel(self.ppp)
        self.lb_sd_or_minmax_3.setObjectName("lb_sd_or_minmax_3")
        sizePolicy2.setHeightForWidth(self.lb_sd_or_minmax_3.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_3.setSizePolicy(sizePolicy2)
        self.lb_sd_or_minmax_3.setFont(font6)

        self.horizontalLayout_85.addWidget(self.lb_sd_or_minmax_3)

        self.comboBox_correlation_person_or_not = QComboBox(self.ppp)
        self.comboBox_correlation_person_or_not.addItem("")
        self.comboBox_correlation_person_or_not.addItem("")
        self.comboBox_correlation_person_or_not.addItem("")
        self.comboBox_correlation_person_or_not.setObjectName("comboBox_correlation_person_or_not")
        sizePolicy7.setHeightForWidth(
            self.comboBox_correlation_person_or_not.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_correlation_person_or_not.setSizePolicy(sizePolicy7)
        self.comboBox_correlation_person_or_not.setFont(font6)

        self.horizontalLayout_85.addWidget(self.comboBox_correlation_person_or_not)

        self.verticalLayout_41.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName("horizontalLayout_121")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.lb_sd_or_minmax_4 = QLabel(self.ppp)
        self.lb_sd_or_minmax_4.setObjectName("lb_sd_or_minmax_4")
        sizePolicy2.setHeightForWidth(self.lb_sd_or_minmax_4.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_4.setSizePolicy(sizePolicy2)
        self.lb_sd_or_minmax_4.setFont(font6)

        self.horizontalLayout_26.addWidget(self.lb_sd_or_minmax_4)

        self.check_color_for_corr_pivot = QCheckBox(self.ppp)
        self.check_color_for_corr_pivot.setObjectName("check_color_for_corr_pivot")
        self.check_color_for_corr_pivot.setEnabled(True)
        self.check_color_for_corr_pivot.setFont(font6)
        self.check_color_for_corr_pivot.setChecked(True)

        self.horizontalLayout_26.addWidget(self.check_color_for_corr_pivot)

        self.horizontalLayout_121.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(10)
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.lb_sd_or_minmax_5 = QLabel(self.ppp)
        self.lb_sd_or_minmax_5.setObjectName("lb_sd_or_minmax_5")
        sizePolicy2.setHeightForWidth(self.lb_sd_or_minmax_5.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_5.setSizePolicy(sizePolicy2)
        self.lb_sd_or_minmax_5.setFont(font6)

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
        self.comboBox_correlation_color_map.setObjectName("comboBox_correlation_color_map")
        sizePolicy7.setHeightForWidth(
            self.comboBox_correlation_color_map.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_correlation_color_map.setSizePolicy(sizePolicy7)
        self.comboBox_correlation_color_map.setFont(font6)

        self.horizontalLayout_86.addWidget(self.comboBox_correlation_color_map)

        self.horizontalLayout_121.addLayout(self.horizontalLayout_86)

        self.verticalLayout_41.addLayout(self.horizontalLayout_121)

        self.verticalLayout_42.addLayout(self.verticalLayout_41)

        self.btn_plot_and_save_corr_table = QPushButton(self.ppp)
        self.btn_plot_and_save_corr_table.setObjectName("btn_plot_and_save_corr_table")
        self.btn_plot_and_save_corr_table.setFont(font6)
        self.btn_plot_and_save_corr_table.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.verticalLayout_42.addWidget(self.btn_plot_and_save_corr_table)

        self.verticalLayout_43.addWidget(self.ppp)

        self.verticalSpacer_7 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_43.addItem(self.verticalSpacer_7)

        self.ppp_2 = QFrame(self.tab_8)
        self.ppp_2.setObjectName("ppp_2")
        self.ppp_2.setStyleSheet(
            "QFrame#ppp_2{\nborder: 5px solid rgb(128, 160, 165);\nborder-radius: 17px;\n}"
        )
        self.verticalLayout_53 = QVBoxLayout(self.ppp_2)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(8, 8, 8, 8)
        self.lb_color_pal_box_22 = QLabel(self.ppp_2)
        self.lb_color_pal_box_22.setObjectName("lb_color_pal_box_22")
        sizePolicy.setHeightForWidth(self.lb_color_pal_box_22.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_22.setSizePolicy(sizePolicy)
        self.lb_color_pal_box_22.setFont(font11)

        self.verticalLayout_53.addWidget(self.lb_color_pal_box_22, 0, Qt.AlignHCenter)

        self.horizontalLayout_143 = QHBoxLayout()
        self.horizontalLayout_143.setSpacing(10)
        self.horizontalLayout_143.setObjectName("horizontalLayout_143")
        self.lb_sd_or_minmax_11 = QLabel(self.ppp_2)
        self.lb_sd_or_minmax_11.setObjectName("lb_sd_or_minmax_11")
        sizePolicy2.setHeightForWidth(self.lb_sd_or_minmax_11.sizePolicy().hasHeightForWidth())
        self.lb_sd_or_minmax_11.setSizePolicy(sizePolicy2)
        self.lb_sd_or_minmax_11.setFont(font6)

        self.horizontalLayout_143.addWidget(self.lb_sd_or_minmax_11)

        self.comboBox_index_data_or_raw = QComboBox(self.ppp_2)
        self.comboBox_index_data_or_raw.addItem("")
        self.comboBox_index_data_or_raw.addItem("")
        self.comboBox_index_data_or_raw.setObjectName("comboBox_index_data_or_raw")
        sizePolicy7.setHeightForWidth(
            self.comboBox_index_data_or_raw.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_index_data_or_raw.setSizePolicy(sizePolicy7)
        self.comboBox_index_data_or_raw.setFont(font6)

        self.horizontalLayout_143.addWidget(self.comboBox_index_data_or_raw)

        self.verticalLayout_53.addLayout(self.horizontalLayout_143)

        self.btn_save_pivot_or_melt = QPushButton(self.ppp_2)
        self.btn_save_pivot_or_melt.setObjectName("btn_save_pivot_or_melt")
        self.btn_save_pivot_or_melt.setFont(font6)
        self.btn_save_pivot_or_melt.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.verticalLayout_53.addWidget(self.btn_save_pivot_or_melt)

        self.verticalLayout_43.addWidget(self.ppp_2)

        self.gridLayout_13.addLayout(self.verticalLayout_43, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_15 = QGridLayout(self.tab_10)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.lb_path_for_plot_3 = QLabel(self.tab_10)
        self.lb_path_for_plot_3.setObjectName("lb_path_for_plot_3")
        self.lb_path_for_plot_3.setFont(font6)

        self.horizontalLayout_87.addWidget(self.lb_path_for_plot_3)

        self.path_for_catplot = QLineEdit(self.tab_10)
        self.path_for_catplot.setObjectName("path_for_catplot")
        self.path_for_catplot.setFont(font6)

        self.horizontalLayout_87.addWidget(self.path_for_catplot)

        self.gridLayout_15.addLayout(self.horizontalLayout_87, 0, 0, 1, 1)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.lb_exel_name_3 = QLabel(self.tab_10)
        self.lb_exel_name_3.setObjectName("lb_exel_name_3")
        self.lb_exel_name_3.setFont(font6)

        self.horizontalLayout_88.addWidget(self.lb_exel_name_3)

        self.comboBox_excel_catplot = QComboBox(self.tab_10)
        self.comboBox_excel_catplot.setObjectName("comboBox_excel_catplot")

        self.horizontalLayout_88.addWidget(self.comboBox_excel_catplot)

        self.gridLayout_15.addLayout(self.horizontalLayout_88, 1, 0, 1, 1)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName("horizontalLayout_99")
        self.lb_exel_name_4 = QLabel(self.tab_10)
        self.lb_exel_name_4.setObjectName("lb_exel_name_4")
        self.lb_exel_name_4.setFont(font6)

        self.horizontalLayout_99.addWidget(self.lb_exel_name_4)

        self.comboBox_excel_sheet_catplot = QComboBox(self.tab_10)
        self.comboBox_excel_sheet_catplot.setObjectName("comboBox_excel_sheet_catplot")

        self.horizontalLayout_99.addWidget(self.comboBox_excel_sheet_catplot)

        self.gridLayout_15.addLayout(self.horizontalLayout_99, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.line_9 = QFrame(self.tab_10)
        self.line_9.setObjectName("line_9")
        self.line_9.setFont(font4)
        self.line_9.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QFrame.HLine)

        self.verticalLayout_15.addWidget(self.line_9)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName("horizontalLayout_100")
        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.lb_hue_name_3 = QLabel(self.tab_10)
        self.lb_hue_name_3.setObjectName("lb_hue_name_3")
        self.lb_hue_name_3.setFont(font6)

        self.horizontalLayout_89.addWidget(self.lb_hue_name_3)

        self.comboBox_catplot_x = QComboBox(self.tab_10)
        self.comboBox_catplot_x.setObjectName("comboBox_catplot_x")

        self.horizontalLayout_89.addWidget(self.comboBox_catplot_x)

        self.horizontalLayout_100.addLayout(self.horizontalLayout_89)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName("horizontalLayout_96")
        self.lb_hue_name_7 = QLabel(self.tab_10)
        self.lb_hue_name_7.setObjectName("lb_hue_name_7")
        self.lb_hue_name_7.setFont(font6)

        self.horizontalLayout_96.addWidget(self.lb_hue_name_7)

        self.comboBox_catplot_form_x = QComboBox(self.tab_10)
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.addItem("")
        self.comboBox_catplot_form_x.setObjectName("comboBox_catplot_form_x")

        self.horizontalLayout_96.addWidget(self.comboBox_catplot_form_x)

        self.horizontalLayout_100.addLayout(self.horizontalLayout_96)

        self.verticalLayout_15.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        self.lb_hue_name_4 = QLabel(self.tab_10)
        self.lb_hue_name_4.setObjectName("lb_hue_name_4")
        self.lb_hue_name_4.setFont(font6)

        self.horizontalLayout_90.addWidget(self.lb_hue_name_4)

        self.comboBox_catplot_y = QComboBox(self.tab_10)
        self.comboBox_catplot_y.setObjectName("comboBox_catplot_y")

        self.horizontalLayout_90.addWidget(self.comboBox_catplot_y)

        self.horizontalLayout_101.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName("horizontalLayout_95")
        self.lb_hue_name_6 = QLabel(self.tab_10)
        self.lb_hue_name_6.setObjectName("lb_hue_name_6")
        self.lb_hue_name_6.setFont(font6)

        self.horizontalLayout_95.addWidget(self.lb_hue_name_6)

        self.comboBox_catplot_form_y = QComboBox(self.tab_10)
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.addItem("")
        self.comboBox_catplot_form_y.setObjectName("comboBox_catplot_form_y")

        self.horizontalLayout_95.addWidget(self.comboBox_catplot_form_y)

        self.horizontalLayout_101.addLayout(self.horizontalLayout_95)

        self.verticalLayout_15.addLayout(self.horizontalLayout_101)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName("horizontalLayout_102")
        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.lb_hue_name_5 = QLabel(self.tab_10)
        self.lb_hue_name_5.setObjectName("lb_hue_name_5")
        self.lb_hue_name_5.setFont(font6)

        self.horizontalLayout_91.addWidget(self.lb_hue_name_5)

        self.comboBox_catplot_hue = QComboBox(self.tab_10)
        self.comboBox_catplot_hue.setObjectName("comboBox_catplot_hue")

        self.horizontalLayout_91.addWidget(self.comboBox_catplot_hue)

        self.horizontalLayout_102.addLayout(self.horizontalLayout_91)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName("horizontalLayout_97")
        self.lb_hue_name_8 = QLabel(self.tab_10)
        self.lb_hue_name_8.setObjectName("lb_hue_name_8")
        self.lb_hue_name_8.setFont(font6)

        self.horizontalLayout_97.addWidget(self.lb_hue_name_8)

        self.comboBox_catplot_form_hue = QComboBox(self.tab_10)
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.addItem("")
        self.comboBox_catplot_form_hue.setObjectName("comboBox_catplot_form_hue")

        self.horizontalLayout_97.addWidget(self.comboBox_catplot_form_hue)

        self.horizontalLayout_102.addLayout(self.horizontalLayout_97)

        self.verticalLayout_15.addLayout(self.horizontalLayout_102)

        self.line_8 = QFrame(self.tab_10)
        self.line_8.setObjectName("line_8")
        self.line_8.setFont(font4)
        self.line_8.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QFrame.HLine)

        self.verticalLayout_15.addWidget(self.line_8)

        self.gridLayout_15.addLayout(self.verticalLayout_15, 3, 0, 1, 2)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName("horizontalLayout_106")
        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName("horizontalLayout_93")
        self.lb_color_pal_box_14 = QLabel(self.tab_10)
        self.lb_color_pal_box_14.setObjectName("lb_color_pal_box_14")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_14.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_14.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_14.setFont(font6)

        self.horizontalLayout_93.addWidget(self.lb_color_pal_box_14)

        self.doubleSpinBox_catplot = QDoubleSpinBox(self.tab_10)
        self.doubleSpinBox_catplot.setObjectName("doubleSpinBox_catplot")
        self.doubleSpinBox_catplot.setFont(font6)
        self.doubleSpinBox_catplot.setDecimals(1)
        self.doubleSpinBox_catplot.setMinimum(0.100000000000000)
        self.doubleSpinBox_catplot.setSingleStep(0.100000000000000)
        self.doubleSpinBox_catplot.setValue(1.000000000000000)

        self.horizontalLayout_93.addWidget(self.doubleSpinBox_catplot)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_106.addLayout(self.horizontalLayout_93)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName("horizontalLayout_105")
        self.lb_color_pal_box_16 = QLabel(self.tab_10)
        self.lb_color_pal_box_16.setObjectName("lb_color_pal_box_16")
        sizePolicy11.setHeightForWidth(self.lb_color_pal_box_16.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_16.setSizePolicy(sizePolicy11)
        self.lb_color_pal_box_16.setFont(font6)

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
        self.comboBox_color_catplot.setObjectName("comboBox_color_catplot")
        sizePolicy2.setHeightForWidth(self.comboBox_color_catplot.sizePolicy().hasHeightForWidth())
        self.comboBox_color_catplot.setSizePolicy(sizePolicy2)
        self.comboBox_color_catplot.setFont(font6)

        self.horizontalLayout_105.addWidget(self.comboBox_color_catplot)

        self.horizontalLayout_106.addLayout(self.horizontalLayout_105)

        self.gridLayout_15.addLayout(self.horizontalLayout_106, 4, 0, 1, 2)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName("horizontalLayout_104")
        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName("horizontalLayout_98")
        self.lb_stattest_7 = QLabel(self.tab_10)
        self.lb_stattest_7.setObjectName("lb_stattest_7")
        self.lb_stattest_7.setEnabled(True)
        self.lb_stattest_7.setFont(font6)

        self.horizontalLayout_98.addWidget(self.lb_stattest_7)

        self.comboBox_template_catplot = QComboBox(self.tab_10)
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.addItem("")
        self.comboBox_template_catplot.setObjectName("comboBox_template_catplot")
        self.comboBox_template_catplot.setEnabled(True)
        self.comboBox_template_catplot.setFont(font6)

        self.horizontalLayout_98.addWidget(self.comboBox_template_catplot)

        self.horizontalLayout_104.addLayout(self.horizontalLayout_98)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName("horizontalLayout_103")
        self.lb_color_pal_box_15 = QLabel(self.tab_10)
        self.lb_color_pal_box_15.setObjectName("lb_color_pal_box_15")
        sizePolicy3.setHeightForWidth(self.lb_color_pal_box_15.sizePolicy().hasHeightForWidth())
        self.lb_color_pal_box_15.setSizePolicy(sizePolicy3)
        self.lb_color_pal_box_15.setFont(font6)

        self.horizontalLayout_103.addWidget(self.lb_color_pal_box_15)

        self.comboBox_catplot_SD_or_not = QComboBox(self.tab_10)
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.addItem("")
        self.comboBox_catplot_SD_or_not.setObjectName("comboBox_catplot_SD_or_not")
        sizePolicy15.setHeightForWidth(
            self.comboBox_catplot_SD_or_not.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_catplot_SD_or_not.setSizePolicy(sizePolicy15)
        self.comboBox_catplot_SD_or_not.setFont(font6)

        self.horizontalLayout_103.addWidget(self.comboBox_catplot_SD_or_not)

        self.horizontalLayout_104.addLayout(self.horizontalLayout_103)

        self.verticalLayout_39.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_166 = QHBoxLayout()
        self.horizontalLayout_166.setObjectName("horizontalLayout_166")
        self.label_10 = QLabel(self.tab_10)
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(font6)

        self.horizontalLayout_166.addWidget(self.label_10)

        self.spinBox_catplot_angle = QSpinBox(self.tab_10)
        self.spinBox_catplot_angle.setObjectName("spinBox_catplot_angle")
        self.spinBox_catplot_angle.setFont(font6)
        self.spinBox_catplot_angle.setMinimum(-90)
        self.spinBox_catplot_angle.setMaximum(90)
        self.spinBox_catplot_angle.setSingleStep(5)
        self.spinBox_catplot_angle.setValue(0)
        self.spinBox_catplot_angle.setDisplayIntegerBase(10)

        self.horizontalLayout_166.addWidget(self.spinBox_catplot_angle)

        self.horizontalSpacer_9 = QSpacerItem(900, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_166.addItem(self.horizontalSpacer_9)

        self.verticalLayout_39.addLayout(self.horizontalLayout_166)

        self.line_11 = QFrame(self.tab_10)
        self.line_11.setObjectName("line_11")
        self.line_11.setFont(font4)
        self.line_11.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QFrame.HLine)

        self.verticalLayout_39.addWidget(self.line_11)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName("horizontalLayout_94")
        self.lb_stattest_6 = QLabel(self.tab_10)
        self.lb_stattest_6.setObjectName("lb_stattest_6")
        self.lb_stattest_6.setFont(font6)

        self.horizontalLayout_94.addWidget(self.lb_stattest_6)

        self.check_stat_znachimost_catplot = QCheckBox(self.tab_10)
        self.check_stat_znachimost_catplot.setObjectName("check_stat_znachimost_catplot")
        self.check_stat_znachimost_catplot.setEnabled(True)
        self.check_stat_znachimost_catplot.setFont(font6)
        self.check_stat_znachimost_catplot.setChecked(True)

        self.horizontalLayout_94.addWidget(self.check_stat_znachimost_catplot)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")
        self.lb_stattest_5 = QLabel(self.tab_10)
        self.lb_stattest_5.setObjectName("lb_stattest_5")
        self.lb_stattest_5.setEnabled(True)
        self.lb_stattest_5.setFont(font6)

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
        self.comboBox_stat_test_catplot.setObjectName("comboBox_stat_test_catplot")
        self.comboBox_stat_test_catplot.setEnabled(True)
        self.comboBox_stat_test_catplot.setFont(font6)

        self.horizontalLayout_92.addWidget(self.comboBox_stat_test_catplot)

        self.horizontalLayout_94.addLayout(self.horizontalLayout_92)

        self.verticalLayout_39.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_165 = QHBoxLayout()
        self.horizontalLayout_165.setObjectName("horizontalLayout_165")
        self.lb_stattest_14 = QLabel(self.tab_10)
        self.lb_stattest_14.setObjectName("lb_stattest_14")
        self.lb_stattest_14.setFont(font6)

        self.horizontalLayout_165.addWidget(self.lb_stattest_14)

        self.check_stat_znachimost_catplot_inside_subgroup = QCheckBox(self.tab_10)
        self.check_stat_znachimost_catplot_inside_subgroup.setObjectName(
            "check_stat_znachimost_catplot_inside_subgroup"
        )
        self.check_stat_znachimost_catplot_inside_subgroup.setEnabled(True)
        self.check_stat_znachimost_catplot_inside_subgroup.setFont(font6)
        self.check_stat_znachimost_catplot_inside_subgroup.setChecked(False)

        self.horizontalLayout_165.addWidget(self.check_stat_znachimost_catplot_inside_subgroup)

        self.verticalLayout_39.addLayout(self.horizontalLayout_165)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName("horizontalLayout_108")
        self.lb_stattest_9 = QLabel(self.tab_10)
        self.lb_stattest_9.setObjectName("lb_stattest_9")
        self.lb_stattest_9.setEnabled(True)
        self.lb_stattest_9.setFont(font6)

        self.horizontalLayout_108.addWidget(self.lb_stattest_9)

        self.comboBox_catplot_stat_formatt = QComboBox(self.tab_10)
        self.comboBox_catplot_stat_formatt.addItem("")
        self.comboBox_catplot_stat_formatt.addItem("")
        self.comboBox_catplot_stat_formatt.addItem("")
        self.comboBox_catplot_stat_formatt.setObjectName("comboBox_catplot_stat_formatt")
        self.comboBox_catplot_stat_formatt.setEnabled(True)
        self.comboBox_catplot_stat_formatt.setFont(font6)

        self.horizontalLayout_108.addWidget(self.comboBox_catplot_stat_formatt)

        self.verticalLayout_39.addLayout(self.horizontalLayout_108)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName("horizontalLayout_109")
        self.lb_stattest_10 = QLabel(self.tab_10)
        self.lb_stattest_10.setObjectName("lb_stattest_10")
        self.lb_stattest_10.setEnabled(True)
        self.lb_stattest_10.setFont(font6)

        self.horizontalLayout_109.addWidget(self.lb_stattest_10)

        self.comboBox_catplot_mult_stat = QComboBox(self.tab_10)
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.addItem("")
        self.comboBox_catplot_mult_stat.setObjectName("comboBox_catplot_mult_stat")
        self.comboBox_catplot_mult_stat.setEnabled(True)
        self.comboBox_catplot_mult_stat.setFont(font6)

        self.horizontalLayout_109.addWidget(self.comboBox_catplot_mult_stat)

        self.verticalLayout_39.addLayout(self.horizontalLayout_109)

        self.line_10 = QFrame(self.tab_10)
        self.line_10.setObjectName("line_10")
        self.line_10.setFont(font4)
        self.line_10.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QFrame.HLine)

        self.verticalLayout_39.addWidget(self.line_10)

        self.gridLayout_15.addLayout(self.verticalLayout_39, 5, 0, 1, 2)

        self.btn_plot_and_save_catplot = QPushButton(self.tab_10)
        self.btn_plot_and_save_catplot.setObjectName("btn_plot_and_save_catplot")
        self.btn_plot_and_save_catplot.setFont(font6)
        self.btn_plot_and_save_catplot.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.gridLayout_15.addWidget(self.btn_plot_and_save_catplot, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_3, 7, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_22 = QGridLayout(self.tab_4)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.lb_path_for_plot_7 = QLabel(self.tab_4)
        self.lb_path_for_plot_7.setObjectName("lb_path_for_plot_7")
        font12 = QFont()
        font12.setPointSize(11)
        font12.setBold(True)
        font12.setUnderline(True)
        self.lb_path_for_plot_7.setFont(font12)

        self.verticalLayout_44.addWidget(self.lb_path_for_plot_7, 0, Qt.AlignHCenter)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName("horizontalLayout_128")
        self.lb_path_for_plot_5 = QLabel(self.tab_4)
        self.lb_path_for_plot_5.setObjectName("lb_path_for_plot_5")
        self.lb_path_for_plot_5.setFont(font6)

        self.horizontalLayout_128.addWidget(self.lb_path_for_plot_5)

        self.path_for_RheoScan_describe = QLineEdit(self.tab_4)
        self.path_for_RheoScan_describe.setObjectName("path_for_RheoScan_describe")
        self.path_for_RheoScan_describe.setFont(font6)

        self.horizontalLayout_128.addWidget(self.path_for_RheoScan_describe)

        self.toolButton_RheoScan = QToolButton(self.tab_4)
        self.toolButton_RheoScan.setObjectName("toolButton_RheoScan")

        self.horizontalLayout_128.addWidget(self.toolButton_RheoScan)

        self.verticalLayout_44.addLayout(self.horizontalLayout_128)

        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName("horizontalLayout_129")
        self.lb_stattest_12 = QLabel(self.tab_4)
        self.lb_stattest_12.setObjectName("lb_stattest_12")
        self.lb_stattest_12.setEnabled(True)
        self.lb_stattest_12.setFont(font6)

        self.horizontalLayout_129.addWidget(self.lb_stattest_12)

        self.comboBox_RheoScan_describe = QComboBox(self.tab_4)
        self.comboBox_RheoScan_describe.addItem("")
        self.comboBox_RheoScan_describe.addItem("")
        self.comboBox_RheoScan_describe.setObjectName("comboBox_RheoScan_describe")
        self.comboBox_RheoScan_describe.setEnabled(True)
        self.comboBox_RheoScan_describe.setFont(font6)

        self.horizontalLayout_129.addWidget(self.comboBox_RheoScan_describe)

        self.verticalLayout_44.addLayout(self.horizontalLayout_129)

        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName("horizontalLayout_130")
        self.lb_path_for_plot_6 = QLabel(self.tab_4)
        self.lb_path_for_plot_6.setObjectName("lb_path_for_plot_6")
        self.lb_path_for_plot_6.setFont(font6)

        self.horizontalLayout_130.addWidget(self.lb_path_for_plot_6)

        self.RheoScan_describe_mask_sheets = QLineEdit(self.tab_4)
        self.RheoScan_describe_mask_sheets.setObjectName("RheoScan_describe_mask_sheets")
        self.RheoScan_describe_mask_sheets.setFont(font6)

        self.horizontalLayout_130.addWidget(self.RheoScan_describe_mask_sheets)

        self.verticalLayout_44.addLayout(self.horizontalLayout_130)

        self.btn_RheoScan_describe_file_or_files = QPushButton(self.tab_4)
        self.btn_RheoScan_describe_file_or_files.setObjectName(
            "btn_RheoScan_describe_file_or_files"
        )
        self.btn_RheoScan_describe_file_or_files.setFont(font6)
        self.btn_RheoScan_describe_file_or_files.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.verticalLayout_44.addWidget(self.btn_RheoScan_describe_file_or_files)

        self.gridLayout_22.addLayout(self.verticalLayout_44, 0, 0, 1, 2)

        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.line_21 = QFrame(self.tab_4)
        self.line_21.setObjectName("line_21")
        self.line_21.setFont(font4)
        self.line_21.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_21.setFrameShadow(QFrame.Plain)
        self.line_21.setLineWidth(3)
        self.line_21.setFrameShape(QFrame.HLine)

        self.verticalLayout_66.addWidget(self.line_21)

        self.line_23 = QFrame(self.tab_4)
        self.line_23.setObjectName("line_23")
        self.line_23.setFont(font4)
        self.line_23.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_23.setFrameShadow(QFrame.Plain)
        self.line_23.setLineWidth(3)
        self.line_23.setFrameShape(QFrame.HLine)

        self.verticalLayout_66.addWidget(self.line_23)

        self.line_24 = QFrame(self.tab_4)
        self.line_24.setObjectName("line_24")
        self.line_24.setFont(font4)
        self.line_24.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_24.setFrameShadow(QFrame.Plain)
        self.line_24.setLineWidth(3)
        self.line_24.setFrameShape(QFrame.HLine)

        self.verticalLayout_66.addWidget(self.line_24)

        self.gridLayout_22.addLayout(self.verticalLayout_66, 1, 0, 1, 2)

        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.lb_path_for_plot_10 = QLabel(self.tab_4)
        self.lb_path_for_plot_10.setObjectName("lb_path_for_plot_10")
        self.lb_path_for_plot_10.setFont(font12)
        self.lb_path_for_plot_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.lb_path_for_plot_10)

        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.horizontalLayout_171 = QHBoxLayout()
        self.horizontalLayout_171.setObjectName("horizontalLayout_171")
        self.lb_path_for_plot_9 = QLabel(self.tab_4)
        self.lb_path_for_plot_9.setObjectName("lb_path_for_plot_9")
        self.lb_path_for_plot_9.setFont(font6)

        self.horizontalLayout_171.addWidget(self.lb_path_for_plot_9)

        self.path_for_rheoscan_report = QLineEdit(self.tab_4)
        self.path_for_rheoscan_report.setObjectName("path_for_rheoscan_report")
        self.path_for_rheoscan_report.setFont(font6)

        self.horizontalLayout_171.addWidget(self.path_for_rheoscan_report)

        self.verticalLayout_64.addLayout(self.horizontalLayout_171)

        self.horizontalLayout_170 = QHBoxLayout()
        self.horizontalLayout_170.setObjectName("horizontalLayout_170")
        self.lb_exel_name_9 = QLabel(self.tab_4)
        self.lb_exel_name_9.setObjectName("lb_exel_name_9")
        self.lb_exel_name_9.setFont(font6)

        self.horizontalLayout_170.addWidget(self.lb_exel_name_9)

        self.comboBox_rheoscan_report = QComboBox(self.tab_4)
        self.comboBox_rheoscan_report.setObjectName("comboBox_rheoscan_report")

        self.horizontalLayout_170.addWidget(self.comboBox_rheoscan_report)

        self.verticalLayout_64.addLayout(self.horizontalLayout_170)

        self.verticalLayout_65.addLayout(self.verticalLayout_64)

        self.horizontalLayout_161 = QHBoxLayout()
        self.horizontalLayout_161.setObjectName("horizontalLayout_161")
        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.label_3 = QLabel(self.tab_4)
        self.label_3.setObjectName("label_3")

        self.verticalLayout_59.addWidget(self.label_3)

        self.calendarWidget_rheoscan_report = QCalendarWidget(self.tab_4)
        self.calendarWidget_rheoscan_report.setObjectName("calendarWidget_rheoscan_report")
        self.calendarWidget_rheoscan_report.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.calendarWidget_rheoscan_report.setSelectedDate(QDate(2026, 1, 1))

        self.verticalLayout_59.addWidget(self.calendarWidget_rheoscan_report)

        self.horizontalLayout_161.addLayout(self.verticalLayout_59)

        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.horizontalLayout_168 = QHBoxLayout()
        self.horizontalLayout_168.setObjectName("horizontalLayout_168")
        self.label_22 = QLabel(self.tab_4)
        self.label_22.setObjectName("label_22")

        self.horizontalLayout_168.addWidget(self.label_22)

        self.rheoscan_report_name_exp = QLineEdit(self.tab_4)
        self.rheoscan_report_name_exp.setObjectName("rheoscan_report_name_exp")

        self.horizontalLayout_168.addWidget(self.rheoscan_report_name_exp)

        self.verticalLayout_63.addLayout(self.horizontalLayout_168)

        self.horizontalLayout_169 = QHBoxLayout()
        self.horizontalLayout_169.setObjectName("horizontalLayout_169")
        self.label_24 = QLabel(self.tab_4)
        self.label_24.setObjectName("label_24")

        self.horizontalLayout_169.addWidget(self.label_24)

        self.rheoscan_report_name_process = QLineEdit(self.tab_4)
        self.rheoscan_report_name_process.setObjectName("rheoscan_report_name_process")

        self.horizontalLayout_169.addWidget(self.rheoscan_report_name_process)

        self.verticalLayout_63.addLayout(self.horizontalLayout_169)

        self.toolBox = QToolBox(self.tab_4)
        self.toolBox.setObjectName("toolBox")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.page.setGeometry(QRect(0, 0, 372, 100))
        self.gridLayout_23 = QGridLayout(self.page)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.rheoscan_report_parameters_dict = QPlainTextEdit(self.page)
        self.rheoscan_report_parameters_dict.setObjectName("rheoscan_report_parameters_dict")
        sizePolicy19.setHeightForWidth(
            self.rheoscan_report_parameters_dict.sizePolicy().hasHeightForWidth()
        )
        self.rheoscan_report_parameters_dict.setSizePolicy(sizePolicy19)

        self.verticalLayout_50.addWidget(self.rheoscan_report_parameters_dict)

        self.gridLayout_23.addLayout(self.verticalLayout_50, 0, 0, 1, 1)

        self.toolBox.addItem(
            self.page,
            "\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432",
        )
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.page_2.setGeometry(QRect(0, 0, 100, 100))
        self.gridLayout_24 = QGridLayout(self.page_2)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.rheoscan_report_norm_dict = QPlainTextEdit(self.page_2)
        self.rheoscan_report_norm_dict.setObjectName("rheoscan_report_norm_dict")
        sizePolicy19.setHeightForWidth(
            self.rheoscan_report_norm_dict.sizePolicy().hasHeightForWidth()
        )
        self.rheoscan_report_norm_dict.setSizePolicy(sizePolicy19)

        self.verticalLayout_61.addWidget(self.rheoscan_report_norm_dict)

        self.gridLayout_24.addLayout(self.verticalLayout_61, 0, 0, 1, 1)

        self.toolBox.addItem(
            self.page_2,
            "\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u043d\u043e\u0440\u043c\u044b (\u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u00b1 SD)",
        )
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.page_3.setGeometry(QRect(0, 0, 100, 98))
        self.gridLayout_25 = QGridLayout(self.page_3)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.rheoscan_report_comment = QPlainTextEdit(self.page_3)
        self.rheoscan_report_comment.setObjectName("rheoscan_report_comment")
        sizePolicy19.setHeightForWidth(
            self.rheoscan_report_comment.sizePolicy().hasHeightForWidth()
        )
        self.rheoscan_report_comment.setSizePolicy(sizePolicy19)

        self.gridLayout_25.addWidget(self.rheoscan_report_comment, 0, 0, 1, 1)

        self.toolBox.addItem(
            self.page_3,
            "\u0414\u043e\u043f.\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439",
        )

        self.verticalLayout_63.addWidget(self.toolBox)

        self.horizontalLayout_161.addLayout(self.verticalLayout_63)

        self.verticalLayout_65.addLayout(self.horizontalLayout_161)

        self.btn_make_rheoscan_report = QPushButton(self.tab_4)
        self.btn_make_rheoscan_report.setObjectName("btn_make_rheoscan_report")
        self.btn_make_rheoscan_report.setFont(font6)
        self.btn_make_rheoscan_report.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.verticalLayout_65.addWidget(self.btn_make_rheoscan_report)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer)

        self.gridLayout_22.addLayout(self.verticalLayout_65, 2, 0, 1, 2)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_28 = QGridLayout(self.tab_12)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.tabWidget_4 = QTabWidget(self.tab_12)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName("tab_19")
        self.gridLayout_26 = QGridLayout(self.tab_19)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.lb_path_for_plot_8 = QLabel(self.tab_19)
        self.lb_path_for_plot_8.setObjectName("lb_path_for_plot_8")
        self.lb_path_for_plot_8.setFont(font12)

        self.verticalLayout_45.addWidget(self.lb_path_for_plot_8, 0, Qt.AlignHCenter)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName("horizontalLayout_107")
        self.lb_path_for_plot_4 = QLabel(self.tab_19)
        self.lb_path_for_plot_4.setObjectName("lb_path_for_plot_4")
        self.lb_path_for_plot_4.setFont(font6)

        self.horizontalLayout_107.addWidget(self.lb_path_for_plot_4)

        self.path_for_dop_stat = QLineEdit(self.tab_19)
        self.path_for_dop_stat.setObjectName("path_for_dop_stat")
        self.path_for_dop_stat.setFont(font6)

        self.horizontalLayout_107.addWidget(self.path_for_dop_stat)

        self.verticalLayout_45.addLayout(self.horizontalLayout_107)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName("horizontalLayout_110")
        self.lb_exel_name_5 = QLabel(self.tab_19)
        self.lb_exel_name_5.setObjectName("lb_exel_name_5")
        self.lb_exel_name_5.setFont(font6)

        self.horizontalLayout_110.addWidget(self.lb_exel_name_5)

        self.comboBox_excel_dop_stat = QComboBox(self.tab_19)
        self.comboBox_excel_dop_stat.setObjectName("comboBox_excel_dop_stat")

        self.horizontalLayout_110.addWidget(self.comboBox_excel_dop_stat)

        self.verticalLayout_45.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName("horizontalLayout_112")
        self.lb_exel_name_6 = QLabel(self.tab_19)
        self.lb_exel_name_6.setObjectName("lb_exel_name_6")
        self.lb_exel_name_6.setFont(font6)

        self.horizontalLayout_112.addWidget(self.lb_exel_name_6)

        self.comboBox_excel_sheet_dop_stat = QComboBox(self.tab_19)
        self.comboBox_excel_sheet_dop_stat.setObjectName("comboBox_excel_sheet_dop_stat")

        self.horizontalLayout_112.addWidget(self.comboBox_excel_sheet_dop_stat)

        self.verticalLayout_45.addLayout(self.horizontalLayout_112)

        self.line_12 = QFrame(self.tab_19)
        self.line_12.setObjectName("line_12")
        self.line_12.setFont(font4)
        self.line_12.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QFrame.HLine)

        self.verticalLayout_45.addWidget(self.line_12)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName("horizontalLayout_111")
        self.lb_hue_name_9 = QLabel(self.tab_19)
        self.lb_hue_name_9.setObjectName("lb_hue_name_9")
        self.lb_hue_name_9.setFont(font6)

        self.horizontalLayout_111.addWidget(self.lb_hue_name_9)

        self.comboBox_dop_stat_x = QComboBox(self.tab_19)
        self.comboBox_dop_stat_x.setObjectName("comboBox_dop_stat_x")

        self.horizontalLayout_111.addWidget(self.comboBox_dop_stat_x)

        self.verticalLayout_45.addLayout(self.horizontalLayout_111)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName("horizontalLayout_114")
        self.lb_hue_name_10 = QLabel(self.tab_19)
        self.lb_hue_name_10.setObjectName("lb_hue_name_10")
        self.lb_hue_name_10.setFont(font6)

        self.horizontalLayout_114.addWidget(self.lb_hue_name_10)

        self.comboBox_dop_stat_y = QComboBox(self.tab_19)
        self.comboBox_dop_stat_y.setObjectName("comboBox_dop_stat_y")

        self.horizontalLayout_114.addWidget(self.comboBox_dop_stat_y)

        self.verticalLayout_45.addLayout(self.horizontalLayout_114)

        self.line_13 = QFrame(self.tab_19)
        self.line_13.setObjectName("line_13")
        self.line_13.setFont(font4)
        self.line_13.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QFrame.HLine)

        self.verticalLayout_45.addWidget(self.line_13)

        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName("horizontalLayout_127")
        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setObjectName("horizontalLayout_113")
        self.lb_stattest_8 = QLabel(self.tab_19)
        self.lb_stattest_8.setObjectName("lb_stattest_8")
        self.lb_stattest_8.setEnabled(True)
        self.lb_stattest_8.setFont(font6)

        self.horizontalLayout_113.addWidget(self.lb_stattest_8)

        self.comboBox_stat_test_dop_stat = QComboBox(self.tab_19)
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
        self.comboBox_stat_test_dop_stat.setObjectName("comboBox_stat_test_dop_stat")
        self.comboBox_stat_test_dop_stat.setEnabled(True)
        self.comboBox_stat_test_dop_stat.setFont(font6)

        self.horizontalLayout_113.addWidget(self.comboBox_stat_test_dop_stat)

        self.horizontalLayout_127.addLayout(self.horizontalLayout_113)

        self.verticalLayout_45.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName("horizontalLayout_126")
        self.lb__altern_heposisis_2 = QLabel(self.tab_19)
        self.lb__altern_heposisis_2.setObjectName("lb__altern_heposisis_2")
        self.lb__altern_heposisis_2.setEnabled(True)
        self.lb__altern_heposisis_2.setFont(font6)

        self.horizontalLayout_126.addWidget(self.lb__altern_heposisis_2)

        self.comboBox_alter_hep_dop_stat = QComboBox(self.tab_19)
        self.comboBox_alter_hep_dop_stat.addItem("")
        self.comboBox_alter_hep_dop_stat.addItem("")
        self.comboBox_alter_hep_dop_stat.addItem("")
        self.comboBox_alter_hep_dop_stat.setObjectName("comboBox_alter_hep_dop_stat")
        self.comboBox_alter_hep_dop_stat.setEnabled(True)
        self.comboBox_alter_hep_dop_stat.setFont(font6)

        self.horizontalLayout_126.addWidget(self.comboBox_alter_hep_dop_stat)

        self.verticalLayout_45.addLayout(self.horizontalLayout_126)

        self.line_20 = QFrame(self.tab_19)
        self.line_20.setObjectName("line_20")
        self.line_20.setFont(font4)
        self.line_20.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_20.setFrameShadow(QFrame.Plain)
        self.line_20.setLineWidth(3)
        self.line_20.setFrameShape(QFrame.HLine)

        self.verticalLayout_45.addWidget(self.line_20)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName("horizontalLayout_125")
        self.lb_hue_name_11 = QLabel(self.tab_19)
        self.lb_hue_name_11.setObjectName("lb_hue_name_11")
        self.lb_hue_name_11.setFont(font6)

        self.horizontalLayout_125.addWidget(self.lb_hue_name_11)

        self.p_value_dop_stat = QLineEdit(self.tab_19)
        self.p_value_dop_stat.setObjectName("p_value_dop_stat")
        self.p_value_dop_stat.setFont(font6)

        self.horizontalLayout_125.addWidget(self.p_value_dop_stat)

        self.verticalLayout_45.addLayout(self.horizontalLayout_125)

        self.btn_dop_stat_calc = QPushButton(self.tab_19)
        self.btn_dop_stat_calc.setObjectName("btn_dop_stat_calc")
        self.btn_dop_stat_calc.setFont(font6)
        self.btn_dop_stat_calc.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.verticalLayout_45.addWidget(self.btn_dop_stat_calc)

        self.gridLayout_26.addLayout(self.verticalLayout_45, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_19, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName("tab_20")
        self.gridLayout_27 = QGridLayout(self.tab_20)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.lb_path_for_plot_11 = QLabel(self.tab_20)
        self.lb_path_for_plot_11.setObjectName("lb_path_for_plot_11")
        self.lb_path_for_plot_11.setFont(font12)
        self.lb_path_for_plot_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.lb_path_for_plot_11)

        self.horizontalLayout_176 = QHBoxLayout()
        self.horizontalLayout_176.setObjectName("horizontalLayout_176")
        self.lb_path_for_plot_12 = QLabel(self.tab_20)
        self.lb_path_for_plot_12.setObjectName("lb_path_for_plot_12")
        self.lb_path_for_plot_12.setFont(font6)

        self.horizontalLayout_176.addWidget(self.lb_path_for_plot_12)

        self.path_for_excel_cluster = QLineEdit(self.tab_20)
        self.path_for_excel_cluster.setObjectName("path_for_excel_cluster")
        self.path_for_excel_cluster.setFont(font6)

        self.horizontalLayout_176.addWidget(self.path_for_excel_cluster)

        self.verticalLayout_62.addLayout(self.horizontalLayout_176)

        self.horizontalLayout_177 = QHBoxLayout()
        self.horizontalLayout_177.setObjectName("horizontalLayout_177")
        self.lb_exel_name_10 = QLabel(self.tab_20)
        self.lb_exel_name_10.setObjectName("lb_exel_name_10")
        self.lb_exel_name_10.setFont(font6)

        self.horizontalLayout_177.addWidget(self.lb_exel_name_10)

        self.comboBox_cluster_file = QComboBox(self.tab_20)
        self.comboBox_cluster_file.setObjectName("comboBox_cluster_file")

        self.horizontalLayout_177.addWidget(self.comboBox_cluster_file)

        self.verticalLayout_62.addLayout(self.horizontalLayout_177)

        self.horizontalLayout_178 = QHBoxLayout()
        self.horizontalLayout_178.setObjectName("horizontalLayout_178")
        self.lb_exel_name_11 = QLabel(self.tab_20)
        self.lb_exel_name_11.setObjectName("lb_exel_name_11")
        self.lb_exel_name_11.setFont(font6)

        self.horizontalLayout_178.addWidget(self.lb_exel_name_11)

        self.comboBox_cluster_excel_sheet = QComboBox(self.tab_20)
        self.comboBox_cluster_excel_sheet.setObjectName("comboBox_cluster_excel_sheet")

        self.horizontalLayout_178.addWidget(self.comboBox_cluster_excel_sheet)

        self.verticalLayout_62.addLayout(self.horizontalLayout_178)

        self.line_26 = QFrame(self.tab_20)
        self.line_26.setObjectName("line_26")
        self.line_26.setFont(font4)
        self.line_26.setStyleSheet("color: rgb(128, 160, 165);")
        self.line_26.setFrameShadow(QFrame.Plain)
        self.line_26.setLineWidth(3)
        self.line_26.setFrameShape(QFrame.HLine)

        self.verticalLayout_62.addWidget(self.line_26)

        self.horizontalLayout_173 = QHBoxLayout()
        self.horizontalLayout_173.setObjectName("horizontalLayout_173")
        self.lb_hue_name_12 = QLabel(self.tab_20)
        self.lb_hue_name_12.setObjectName("lb_hue_name_12")
        self.lb_hue_name_12.setFont(font6)

        self.horizontalLayout_173.addWidget(self.lb_hue_name_12)

        self.spinBox_cluster_n = QSpinBox(self.tab_20)
        self.spinBox_cluster_n.setObjectName("spinBox_cluster_n")
        self.spinBox_cluster_n.setFont(font6)
        self.spinBox_cluster_n.setMinimum(2)
        self.spinBox_cluster_n.setMaximum(50)
        self.spinBox_cluster_n.setValue(3)

        self.horizontalLayout_173.addWidget(self.spinBox_cluster_n)

        self.verticalLayout_62.addLayout(self.horizontalLayout_173)

        self.horizontalLayout_174 = QHBoxLayout()
        self.horizontalLayout_174.setObjectName("horizontalLayout_174")
        self.lb_hue_name_13 = QLabel(self.tab_20)
        self.lb_hue_name_13.setObjectName("lb_hue_name_13")
        self.lb_hue_name_13.setFont(font6)

        self.horizontalLayout_174.addWidget(self.lb_hue_name_13)

        self.comboBox_cluster_coord = QComboBox(self.tab_20)
        self.comboBox_cluster_coord.addItem("")
        self.comboBox_cluster_coord.addItem("")
        self.comboBox_cluster_coord.setObjectName("comboBox_cluster_coord")
        self.comboBox_cluster_coord.setEnabled(True)
        self.comboBox_cluster_coord.setFont(font6)

        self.horizontalLayout_174.addWidget(self.comboBox_cluster_coord)

        self.verticalLayout_62.addLayout(self.horizontalLayout_174)

        self.horizontalLayout_175 = QHBoxLayout()
        self.horizontalLayout_175.setObjectName("horizontalLayout_175")
        self.lb_hue_name_14 = QLabel(self.tab_20)
        self.lb_hue_name_14.setObjectName("lb_hue_name_14")
        self.lb_hue_name_14.setFont(font6)

        self.horizontalLayout_175.addWidget(self.lb_hue_name_14)

        self.spinBox_cluster_buble_size = QSpinBox(self.tab_20)
        self.spinBox_cluster_buble_size.setObjectName("spinBox_cluster_buble_size")
        self.spinBox_cluster_buble_size.setFont(font6)
        self.spinBox_cluster_buble_size.setMinimum(1)
        self.spinBox_cluster_buble_size.setMaximum(50)
        self.spinBox_cluster_buble_size.setValue(10)

        self.horizontalLayout_175.addWidget(self.spinBox_cluster_buble_size)

        self.verticalLayout_62.addLayout(self.horizontalLayout_175)

        self.btn_cluster_save_file = QPushButton(self.tab_20)
        self.btn_cluster_save_file.setObjectName("btn_cluster_save_file")
        self.btn_cluster_save_file.setFont(font6)
        self.btn_cluster_save_file.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.verticalLayout_62.addWidget(self.btn_cluster_save_file)

        self.gridLayout_27.addLayout(self.verticalLayout_62, 0, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding
        )

        self.gridLayout_27.addItem(self.verticalSpacer_8, 1, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_20, "")

        self.gridLayout_28.addWidget(self.tabWidget_4, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_12, "")

        self.gridLayout_9.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.Lab_stuff.addTab(self.tabWidgetPage4, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName("tab_9")
        self.formLayout_5 = QFormLayout(self.tab_9)
        self.formLayout_5.setObjectName("formLayout_5")
        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.label_2 = QLabel(self.tab_9)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_60.addWidget(self.label_2)

        self.horizontalLayout_172 = QHBoxLayout()
        self.horizontalLayout_172.setObjectName("horizontalLayout_172")
        self.label_6 = QLabel(self.tab_9)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_172.addWidget(self.label_6)

        self.lineEdit_json_load = QLineEdit(self.tab_9)
        self.lineEdit_json_load.setObjectName("lineEdit_json_load")

        self.horizontalLayout_172.addWidget(self.lineEdit_json_load)

        self.verticalLayout_60.addLayout(self.horizontalLayout_172)

        self.btn_json_load = QPushButton(self.tab_9)
        self.btn_json_load.setObjectName("btn_json_load")
        self.btn_json_load.setFont(font6)
        self.btn_json_load.setStyleSheet(
            "background-color: rgba(128, 160, 165, 50);\n"
            "border: 3px solid rgb(128, 160, 165);\n"
            "border-radius: 10px;"
        )

        self.verticalLayout_60.addWidget(self.btn_json_load)

        self.formLayout_5.setLayout(0, QFormLayout.SpanningRole, self.verticalLayout_60)

        self.Lab_stuff.addTab(self.tab_9, "")

        self.gridLayout.addWidget(self.Lab_stuff, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
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
        QWidget.setTabOrder(self.comboBox_2, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.comboBox_color_pal_corr)
        QWidget.setTabOrder(self.comboBox_color_pal_corr, self.check_change_corr_fig_down_limit)
        QWidget.setTabOrder(self.check_change_corr_fig_down_limit, self.doubleSpinBox_corr_figs)
        QWidget.setTabOrder(self.doubleSpinBox_corr_figs, self.del_hue)
        QWidget.setTabOrder(self.del_hue, self.spinBox_points_corrFIGS)
        QWidget.setTabOrder(self.spinBox_points_corrFIGS, self.doubleSpinBox_corr_figs_fontscale)
        QWidget.setTabOrder(
            self.doubleSpinBox_corr_figs_fontscale, self.check_sort_or_not_corr_figs
        )
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
        QWidget.setTabOrder(
            self.comboBox_correlation_person_or_not, self.check_color_for_corr_pivot
        )
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
        self.check_stat_znachimost_catplot.toggled.connect(
            self.comboBox_stat_test_catplot.setEnabled
        )
        self.check_stat_znachimost_catplot.toggled.connect(
            self.comboBox_catplot_stat_formatt.setEnabled
        )
        self.check_stat_znachimost_catplot.toggled.connect(
            self.comboBox_catplot_mult_stat.setEnabled
        )
        self.check_biola_plot_figs.toggled.connect(self.plp.setEnabled)
        self.check_box_figs_all_sheets.toggled.connect(self.comboBox_figs_sheets.setDisabled)
        self.check_box_figs_all_sheets.toggled.connect(self.lb_exel_name_8.setDisabled)
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
        self.check_corr_one_parameter.toggled.connect(self.check_corr_figs.setDisabled)
        self.check_corr_one_parameter.toggled.connect(self.check_corr_matrix.setDisabled)
        self.check_corr_one_parameter.toggled.connect(self.check_box_plot.setDisabled)
        self.check_corr_one_parameter.toggled.connect(self.check_box_pairplot.setDisabled)
        self.check_corr_one_parameter.toggled.connect(self.check_jointplot.setDisabled)
        self.check_corr_one_parameter_only_one.toggled.connect(
            self.check_corr_one_parameter_plot_sep_wind.setEnabled
        )
        self.check_stat_znachimost_catplot.toggled.connect(
            self.check_stat_znachimost_catplot_inside_subgroup.setEnabled
        )
        self.check_stat_znachimost.toggled.connect(self.spinBox_size_stat_znachimost.setEnabled)
        self.check_stat_znachimost.toggled.connect(
            self.comboBox_box_plot_sign_stat_znachimost.setEnabled
        )
        self.check_stat_znachimost.toggled.connect(self.comboBox_alter_hep.setEnabled)
        self.check_stat_znachimost.toggled.connect(self.comboBox_stat_test.setEnabled)
        self.check_sort_or_not.toggled.connect(self.check_sort_or_not_ascending.setEnabled)
        self.check_N_.toggled.connect(self.comboBox_box_check_N_.setEnabled)

        self.Lab_stuff.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432",
                None,
            )
        )
        self.comboBox_style_sheet.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0442\u0435\u043c\u0430",
                None,
            ),
        )
        self.comboBox_style_sheet.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow", "\u0422\u0435\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None
            ),
        )
        self.comboBox_style_sheet.setItemText(
            2,
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0432\u0435\u0442\u043b\u0430\u044f \u0442\u0435\u043c\u0430",
                None,
            ),
        )

        # if QT_CONFIG(tooltip)
        self.label_info.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_info.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u044f \u0411\u0438\u043e\u043c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0439 \u0444\u043e\u0442\u043e\u043d\u0438\u043a\u0438 \u041c\u0413\u0423 \u2014 \u0415\u0440\u043c\u043e\u043b\u0438\u043d\u0441\u043a\u0438\u0439 \u041f\u0435\u0442\u0440 \u2014 \u0432\u0435\u0440\u0441\u0438\u044f",
                None,
            )
        )
        self.label_version.setText(QCoreApplication.translate("MainWindow", "_._._", None))
        # if QT_CONFIG(whatsthis)
        self.Lab_stuff.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "\u043f\u043e\u0440\u043f\u043e\u043b\u0430\u0432", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.tabWidgetPage1.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "\u041f\u0440\u0438\u0440\u0440\u0440\u0432", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.btn_save_exel_csv.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438\u0441\u0445\u043e\u0434\u044f \u0438\u0437 \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0445 \u043f\u0443\u0442\u0435\u0439 \u0438 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_save_exel_csv.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e \u0434\u0430\u043d\u043d\u043e\u043c\u0443 \u043f\u0443\u0442\u0438 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c 3 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 (agg, stress, deform), \u0435\u0441\u043b\u0438 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a 1</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c\u0438",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.main_path.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c\u0438 \u0441 \u0444\u0430\u0439\u043b\u0430\u043c\u0438 RheoScan. </p><p>\u0412 \u0441\u043b\u0443\u0447\u0430\u0435 <span style=" text-decoration: underline;">\u0443\u0440\u043e\u0432\u0435\u043d\u044f \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a = 1</span> \u044d\u0442\u043e \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0430 \u0441 3 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c\u0438: </p><p><span style=" font-style:italic;">- agg</span></p><p><span style=" font-style:italic;">- deform</span></p><p><span style=" font-style:italic;">- stress</span></p><p>\u0424\u0430\u0439\u043b\u044b \u0443\u0436\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0440\u0430\u0441\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u044b. \u0415\u0441\u043b\u0438 \u044d\u0442\u043e \u043d\u0435'
                " \u0442\u0430\u043a, \u0442\u043e \u0432\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u043f\u0443\u0442\u044c \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u043d\u0438\u0436\u0435 \u0434\u043b\u044f \u0440\u0430\u0441\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438. </p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.main_path.setText("")
        self.comboBox_RheoScan_path_save.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel/cvs \u0444\u0430\u0439\u043b\u044b \u043f\u043e \u043f\u0430\u043f\u043a\u0430\u043c",
                None,
            ),
        )
        self.comboBox_RheoScan_path_save.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel/cvs \u0444\u0430\u0439\u043b\u044b \u0432 \u043e\u0434\u043d\u043e\u043c \u043c\u0435\u0441\u0442\u0435",
                None,
            ),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_RheoScan_path_save.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u043f\u043e \u0432\u0441\u0435\u043c \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c (\u0432 \u0441\u043b\u0443\u0447\u0430\u0435, \u0435\u0441\u043b\u0438 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a &gt; 1), \u043b\u0438\u0431\u043e \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u043a\u043e\u0440\u043d\u0435\u0432\u043e\u0439 \u0434\u0438\u0440\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438 (\u0432\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0439 \u043f\u0443\u0442\u044c). \u0424\u0430\u0439\u043b\u044b excel \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u0441\u044f \u0441 \u0442\u0435\u043c\u0438 \u0438\u043c\u0435\u043d\u0430\u043c\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e"
                "\u0442 \u043f\u0430\u043f\u043a\u0430\u043c, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043b\u0435\u0436\u0430\u0442 3 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_approx_deform_raw_data.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u044b\u0440\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e deform",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_20.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0439 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_20.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Max \u0432\u0440\u0435\u043c\u044f \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u043b\u0438\u043d\u0435\u0439\u043d\u044b\u0445 \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0432</p></body></html>',
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.tua_1_agg.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0418\u043d\u043e\u0433\u0434\u0430 \u043d\u0430\u0434\u043e \u043f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0439 \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438 \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0433\u0440\u0430\u043c\u043c\u044b. </p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.label_21.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0434\u043b\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0439 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_21.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Max \u0432\u0440\u0435\u043c\u044f \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f 3D \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0432</p></body></html>',
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.tua_2_agg.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0418\u043d\u043e\u0433\u0434\u0430 \u043d\u0430\u0434\u043e \u043f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0439 \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438 \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0433\u0440\u0430\u043c\u043c\u044b. </p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.label_23.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0442\u043e\u0447\u0435\u043a \u0442\u043e\u0447\u043d\u043e \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0434\u043b\u044f \u0430\u043f\u0440\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438. \u0415\u0441\u043b\u0438 R<span style=" vertical-align:super;">2</span> \u0431\u0443\u0434\u0435\u0442 \u043c\u0435\u043d\u044c\u0448\u0435, \u0447\u0435\u043c \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u043d\u044b\u0439, \u043d\u043e \u0442\u043e\u0447\u0435\u043a \u0443\u0436\u0435 \u043c\u0435\u043d\u044c\u0448\u0435, \u0442\u043e \u0434\u0430\u043b\u044c\u043d\u0435\u0439\u0448\u0435\u0433\u043e \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u0438\u044f \u043d\u0435 \u0431\u0443\u0434\u0435\u0442. </p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_23.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>R-\u043a\u0432\u0430\u0434\u0440\u0430\u0442 \u0434\u043b\u044f \u043e\u0442\u0441\u0435\u0447\u043a\u0438</p></body></html>",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.r2_def.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0418\u043d\u043e\u0433\u0434\u0430 \u043d\u0430\u0434\u043e \u043f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0439 \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438. </p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.label_18.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0442\u043e\u0447\u0435\u043a \u0442\u043e\u0447\u043d\u043e \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0434\u043b\u044f \u0430\u043f\u0440\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438. \u0415\u0441\u043b\u0438 R<span style=" vertical-align:super;">2</span> \u0431\u0443\u0434\u0435\u0442 \u043c\u0435\u043d\u044c\u0448\u0435, \u0447\u0435\u043c \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u043d\u044b\u0439, \u043d\u043e \u0442\u043e\u0447\u0435\u043a \u0443\u0436\u0435 \u043c\u0435\u043d\u044c\u0448\u0435, \u0442\u043e \u0434\u0430\u043b\u044c\u043d\u0435\u0439\u0448\u0435\u0433\u043e \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u0438\u044f \u043d\u0435 \u0431\u0443\u0434\u0435\u0442. </p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_18.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b-\u0432\u043e \u0442\u043e\u0447\u0435\u043a \u0434\u043b\u044f \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438</p></body></html>",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_n_max_deform.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0418\u043d\u043e\u0433\u0434\u0430 \u043d\u0430\u0434\u043e \u043f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0439 \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438. </p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.check_approx_agg.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u041f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044e \u043a\u0440\u0438\u0432\u043e\u0439 \u0441\u0432\u0435\u0442\u043e\u0440\u0430\u0441\u0441\u0435\u044f\u043d\u0438\u044f \u0434\u043b\u044f \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0439 \u043a\u044e\u0432\u0435\u0442\u044b?</p><p>\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e 2 \u044d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0442 \u0441 \u0440\u0430\u0437\u043d\u044b\u043c\u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u043d\u044b\u043c\u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0430\u043c\u0438:</p><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind'
                "ent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#6a9955;\"># \u0444\u0443\u043d\u043a\u0446\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u043a\u0440\u0438\u0432\u0430\u044f</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;\">def </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#dcdcaa;\">f</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">(</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">x</span><span style=\" font-family:'Menlo'"
                ",'Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">y0</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">A1</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">A2</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">t1</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco"
                "','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">t2</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">):</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#c586c0;\">return </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">y0</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">+</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">A1</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">*</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;\">np</span><span"
                " style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">.</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">exp</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">(</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">-</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">(</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">x</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">/</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">t1</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">)) </span><span style=\" fo"
                "nt-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">+</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">A2</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">*</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;\">np</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">.</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">exp</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">(</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">-</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">(</span><span style=\" font-family:'Me"
                "nlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">x</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">/</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">t2</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">))</span></pre><pre style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc; background-color:#1f1f1f;\"><br/></pre><p>\u0418\u0434\u0435\u0442 \u0440\u0430\u0441\u0447\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0435\u0439, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0438\u043d\u0434\u0435\u043a\u0441 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u0434\u043b\u044f \u0440\u0430"
                "\u0437\u043d\u044b\u0445 \u0432\u0440\u0435\u043c\u0435\u043d: 2.5, 5, 10, 50, 100 \u0438 MAX \u043a\u043e\u043b-\u0432\u0430 \u0441\u0435\u043a\u0443\u043d\u0434.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_approx_agg.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u0434\u043b\u044f agg",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_figs_for_agg.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0434\u043b\u044f \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438 \u043a\u0440\u0438\u0432\u044b\u0445?</p><p>\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u0432\u0441\u0435\u0433\u0434\u0430 \u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043d\u0430 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e\u0441\u0442\u044c \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_figs_for_agg.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_approx_deform.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044e \u043a\u0440\u0438\u0432\u043e\u0439 \u0438\u043d\u0434\u0435\u043a\u0441\u0430 \u0434\u0435\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u043c\u043e\u0441\u0442\u0438 \u0438 \u0441\u0434\u0432\u0438\u0433\u043e\u0432\u043e\u0433\u043e \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u043a\u044e\u0432\u0435\u0442\u044b?</p><p>\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438, \u0433\u0434\u0435 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f"
                " \u043f\u0440\u0438\u0432\u0435\u0434\u0435\u043d\u044b \u0432 \u043b\u043e\u0433\u0430\u0440\u0438\u0444\u043c:</p><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#6a9955;\"># \u0444\u0443\u043d\u043a\u0446\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0431\u0443\u0434\u0435\u043c \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c - \u043b\u0438\u043d\u0435\u0439\u043d\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u043e\u0442 \u043b\u043e\u0433\u0430\u0440\u0438\u0444\u043c\u0430 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0439 \u0441\u0434\u0432\u0438\u0433\u0430</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0"
                "px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;\">def</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#dcdcaa;\">f</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">(</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">x</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">: </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;\">float</span><span style=\" font-family:'Menlo','Monaco','Cour"
                "ier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">a</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">: </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;\">float</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">b</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">: </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;\">float</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">):</span></pre><pre style=\" margin-top:0px; margin-bottom:0px"
                "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;&quot;&quot;\u041b\u0438\u043d\u0435\u0439\u043d\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f.&quot;&quot;&quot;</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#c586c0;\">return</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cd"
                "cfe;\">a</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">*</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">x</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">+</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">b</span></pre><p>\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440"
                '\u044b \u043f\u0440\u0435\u0434\u0435\u043b\u0430 \u0442\u0435\u043a\u0443\u0447\u0435\u0441\u0442\u0438 (<span style=" font-weight:700;">b</span>) \u0438 \u0432\u044f\u0437\u043a\u043e\u0441\u0442\u0438 \u0432\u043d\u0443\u0442\u0440\u0435\u043a\u043b\u0435\u0442\u043e\u0447\u043d\u043e\u0433\u043e \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0433\u043e (<span style=" font-weight:700;">1/a</span>).</p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_approx_deform.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0410\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u0434\u043b\u044f deform",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_for_deform.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0434\u043b\u044f \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438 \u043a\u0440\u0438\u0432\u044b\u0445?</p><p>\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u0432\u0441\u0435\u0433\u0434\u0430 \u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043d\u0430 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e\u0441\u0442\u044c \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_for_deform.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_stat_for_column.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0434\u043e\u043f. \u043b\u0438\u0441\u0442\u043e\u0432, \u0433\u0434\u0435 \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u0438\u0432\u0435\u0434\u0435\u043d\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430\u043c.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_stat_for_column.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430\u043c",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.vibros_delete.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u044b\u0431\u0440\u043e\u0441\u044b \u0443\u0431\u0438\u0440\u0430\u044e\u0442\u0441\u044f \u043f\u043e \u0438\u043d\u0442\u0435\u0440\u043a\u0430\u043d\u0442\u0438\u043b\u044c\u043d\u043e\u043c\u0443 \u0440\u0430\u0437\u043c\u0430\u0445\u0443 -- \u0441\u043c. \u0438\u043d\u0444\u0443 \u043f\u043e \u0442\u043e\u043c\u0443, \u0447\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u0432\u044b\u0431\u0440\u043e\u0441\u044b</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.vibros_delete.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u0423\u0431\u0440\u0430\u0442\u044c \u0432\u044b\u0431\u0440\u043e\u0441\u044b. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c, \u043a\u043e\u0433\u0434\u0430 \u0432\u044b \u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0435\u0442\u0435 <span style=" font-weight:700;">\u0442\u043e\u043b\u044c\u043a\u043e 1 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430</span>! </p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.vibros_delete.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u0431\u0440\u0430\u0442\u044c \u0432\u044b\u0431\u0440\u043e\u0441\u044b",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.iqr_vibros.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043a\u043e\u043b-\u0432\u0430 \u0438\u043d\u0442\u0435\u0440\u043a\u0432\u0430\u043d\u0442\u0438\u043b\u044c\u043d\u044b\u0445 \u0440\u0430\u0437\u043c\u0430\u0445\u043e\u0432 \u0434\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0432\u044b\u0431\u0440\u043e\u0441\u043e\u0432.</p><p>\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f, \u0442\u043e\u043b\u044c\u043a\u043e \u043a\u043e\u0433\u0434\u0430 \u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0435\u0442\u0435 1 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430 \u0438\u043b\u0438 1 \u043e\u0431\u0440\u0430\u0437\u0435\u0446.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0438\u043d\u0442\u0435\u0440\u043a\u0432\u0430\u0440\u0442\u0438\u043b\u044c\u043d\u044b\u0445 \u0440\u0430\u0437\u043c\u0430\u0445\u0430",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.btn_sort_data_RheoScan.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">\u0415\u0441\u043b\u0438 \u0432\u0441\u0435 \u0444\u0430\u0439\u043b\u044b txt \u0432 \u043e\u0434\u043d\u043e\u0439 \u043f\u0430\u043f\u043a\u0435, \u0442\u043e \u0434\u0430\u043d\u043d\u044b\u0439 \u043c\u0435\u0442\u043e\u0434 \u0440\u0430\u0441\u0441\u043e\u0440\u0442\u0438\u0440\u0443\u0435\u0442 \u0438\u0445 \u043f\u043e \u043f\u0430\u043f\u043a\u0430\u043c agg, stress, deform. \u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0442\u0443\u0442 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442\u0441\u044f.</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_sort_data_RheoScan.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0435\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.label.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u043f\u0430\u043f\u043a\u0430 \u0441 \u043f\u0430\u043f\u043a\u0430\u043c\u0438, \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0435\u0441\u0442\u044c 3 \u043f\u0430\u043f\u043a\u0438, \u0442\u043e \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c 2, \u0438 \u0442.\u0434.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a           ",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_level.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0442\u044c \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043f\u0430\u043f\u043e\u043a \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432/\u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432 \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u0432\u044b \u0432\u0432\u0435\u043b\u0438 \u0432\u044b\u0448\u0435 \u043f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u0430\u043f\u043a\u0430\u043c\u0438, \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u0435\u0442 \u0441 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435\u043c \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432"
                ', \u0438 \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0442\u0430\u043a\u043e\u0439 \u043f\u0430\u043f\u043a\u0435 \u0435\u0441\u0442\u044c 3 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 (agg, stress, deform), \u0442\u043e \u0434\u043b\u044f \u043e\u0431\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u043d\u0443\u0436\u043d\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c <span style=" font-weight:700;">\u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a=2</span>. \u0421\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e, \u0447\u0435\u043c \u0431\u043e\u043b\u044c\u0448\u0435 \u0443 \u0432\u0430\u0441 \u0432\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0445 \u043f\u0430\u043f\u043e\u043a \u0434\u043e 3 \u0438\u0441\u043a\u043e\u043c\u044b\u0445 \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a, \u0442\u0435\u043c \u0431\u043e\u043b\u044c'
                "\u0448\u0435 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0432\u0430\u043c \u043d\u0443\u0436\u043d\u043e \u0441\u043b\u0435\u043b\u0430\u0442\u044c.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.check_save_exel.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b/\u0444\u0430\u0439\u043b\u044b. \u0411\u0443\u0434\u0435\u0442 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043b\u0438\u0441\u0442\u043e\u0432 \u0432 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_save_exel.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_save_csv.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c csv \u0444\u0430\u0439\u043b/\u0444\u0430\u0439\u043b\u044b. \u0411\u0443\u0434\u0435\u0442 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0444\u0430\u0439\u043b\u043e\u0432 \u0432 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_save_csv.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c csv \u0444\u0430\u0439\u043b(\u044b)",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_save_RheoScan_overall.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430 \u043f\u043e \u0432\u0441\u0435\u043c \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f\u043c. \u041f\u043e \u0431\u043e\u043b\u044c\u0448\u0435\u0439 \u0447\u0430\u0441\u0442\u0438 \u043d\u0435 \u043d\u0443\u0436\u043d\u0430 \u0438\u0437-\u0437\u0430 \u043d\u0430\u043b\u0438\u0447\u0438\u044f \u0434\u043e\u043f. \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0434\u0430\u043d\u043d\u044b\u0445 RheoScan (\u0441\u043c. 4 \u0432\u043a\u043b\u0430\u0434\u043a\u0443).</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_save_RheoScan_overall.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0432\u043e\u0434\u043d\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_separator.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u042d\u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0438 \u0444\u0430\u0439\u043b\u043e\u0432. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u0444\u0430\u0439\u043b\u044b \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c: &quot;NAME-##-#&quot;, \u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c &quot;-&quot;.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_separator.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u0430\u043d\u043d\u044b\u0445",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.separator_for_data.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u0430\u043d\u043d\u044b\u0445. \u0411\u044b\u0432\u0430\u0435\u0442 \u043f\u043e\u043b\u0435\u0437\u043d\u043e \u0434\u043b\u044f \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0443 \u0432\u0430\u0441 \u0432\u0441\u0435 \u043e\u0431\u0440\u0430\u0437\u0446\u044b \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0441\u044f \u043f\u043e \u0442\u0438\u043f\u0443 &quot;sample-##-##&quot;.</p><p>\u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0435\u043c \u0434\u0435\u0444\u0438\u0441 &quot;-&quot; \u0438 \u0443 \u0432\u0430\u0441 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0440\u043e\u043b\u0431\u0446\u044b.</p></bod"
                "y></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.separator_for_data.setText("")
        self.check_name_rheoscan.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u043d\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_19.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u043f\u0430\u043f\u043a\u0430 \u0441 \u043f\u0430\u043f\u043a\u0430\u043c\u0438, \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0435\u0441\u0442\u044c 3 \u043f\u0430\u043f\u043a\u0438, \u0442\u043e \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c 2, \u0438 \u0442.\u0434.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_19.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u0438\u043c\u0435\u043d\u0438",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_agg.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043b\u0438 \u043f\u0430\u043f\u043a\u0443 <span style=" font-weight:700;">agg</span>. \u0418\u043d\u043e\u0433\u0434\u0430 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u043d\u0443 \u043a\u0430\u043a\u0443\u044e-\u0442\u043e \u043f\u0430\u043f\u043a\u0443, \u0430 \u043d\u0435 \u0432\u0441\u0435 \u0441\u0440\u0430\u0437\u0443.</p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_agg.setText(
            QCoreApplication.translate("MainWindow", "\u041f\u0430\u043f\u043a\u0430 agg", None)
        )
        # if QT_CONFIG(whatsthis)
        self.check_stress.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043b\u0438 \u043f\u0430\u043f\u043a\u0443 <span style=" font-weight:700;">stress</span>. \u0418\u043d\u043e\u0433\u0434\u0430 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u043d\u0443 \u043a\u0430\u043a\u0443\u044e-\u0442\u043e \u043f\u0430\u043f\u043a\u0443, \u0430 \u043d\u0435 \u0432\u0441\u0435 \u0441\u0440\u0430\u0437\u0443.</p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_stress.setText(
            QCoreApplication.translate("MainWindow", "\u041f\u0430\u043f\u043a\u0430 stress", None)
        )
        # if QT_CONFIG(whatsthis)
        self.check_deform.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043b\u0438 \u043f\u0430\u043f\u043a\u0443 <span style=" font-weight:700;">deform</span>. \u0418\u043d\u043e\u0433\u0434\u0430 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u043d\u0443 \u043a\u0430\u043a\u0443\u044e-\u0442\u043e \u043f\u0430\u043f\u043a\u0443, \u0430 \u043d\u0435 \u0432\u0441\u0435 \u0441\u0440\u0430\u0437\u0443.</p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_deform.setText(
            QCoreApplication.translate("MainWindow", "\u041f\u0430\u043f\u043a\u0430 deform", None)
        )
        # if QT_CONFIG(tooltip)
        self.check_dop_CSS_parameter.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u042d\u0442\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u0438 \u043a\u0440\u0438\u0432\u043e\u0439 CSS - \u0441\u043c. \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u0432 \u043e\u0431\u0443\u0447\u0430\u044e\u0449\u0435\u043c \u0432\u0438\u0434\u0435\u043e",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_dop_CSS_parameter.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 CSS, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u044b\u0442\u0430\u0441\u043a\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0438\u0437 \u0433\u0440\u0430\u0444\u0438\u043a\u0430: \u0441\u0432\u0435\u0442\u043e\u0440\u0430\u0441\u0441\u0435\u044f\u043d\u0438\u0435 VS \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u044f \u0441\u0434\u0432\u0438\u0433\u0430. </p><p>\u0418\u0434\u0435\u0442 \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u044d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0442\u043d\u043e\u0439 \u0438 \u0432\u044b\u0442\u0430\u0441\u043a\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0437\u0430\u0442\u0443\u0445\u0430\u043d\u0438\u044f (<span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; font-weight:700; color:#000000;\">ne"
                "w_parameter</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">)</span>.</p><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">                    (</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">_</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">_</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">new_parameter</span><span style=\" font-family:'Menlo',"
                "'Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">), </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">_</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">=</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;\">opt</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">.</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#dcdcaa;\">curve_fit</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">(</span></pre><pre style=\" margin-top:0px; margin-bottom:0px;"
                " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;\">lambda</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">t</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">a</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">b</span><span style=\" font-family:'Menlo',"
                "'Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">c</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">: </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">a</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">+</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">b</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; "
                "font-size:12px; color:#d4d4d4;\">*</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;\">np</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">.</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">exp</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">(</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;\">-</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">t</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d"
                "4;\">/</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">c</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">),</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">                        \u0441\u0434\u0432\u0438\u0433\u043e\u0432\u043e\u0435 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435,</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">                 "
                "       \u0438\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u044c \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0433\u043e \u0441\u0432\u0435\u0442\u043e\u0440\u0430\u0441\u0441\u0435\u044f\u043d\u0438\u044f,</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">                    )</span></pre></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_dop_CSS_parameter.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u043f. \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 CSS",
                None,
            )
        )
        self.Lab_stuff.setTabText(
            self.Lab_stuff.indexOf(self.tabWidgetPage1),
            QCoreApplication.translate("MainWindow", "RheoScan", None),
        )
        self.lb_path_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0444\u0430\u0439\u043b\u043e\u043c",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.path_for_biola.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0444\u0430\u0439\u043b\u043e\u043c txt, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0431\u044b\u043b \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d \u0438\u0437 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0434\u043b\u044f \u0411\u0438\u043e\u043b\u044b</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.path_for_biola.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412 \u0434\u0430\u043d\u043d\u043e\u0435 \u043f\u043e\u043b\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u043f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f txt \u0444\u0430\u0439\u043b \u0441 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f\u043c\u0438 biola (\u0431\u043e\u0440\u043d \u0438 \u0444\u043b\u0443\u043a\u0442\u0443\u0430\u0446\u0438\u0438) \u0438\u043b\u0438 pdf \u0444\u0430\u0439\u043b \u0441 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f\u043c\u0438 \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u0438 \u0442\u0440\u043e\u043c\u0431\u043e\u0446\u0438\u0442\u043e\u0432.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_biola.setText("")
        # if QT_CONFIG(tooltip)
        self.lb_path_3.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0424\u0430\u0439\u043b \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d \u0438\u0437 \u043e\u0444\u0438\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0411\u0438\u043e\u043b\u044b.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0433\u0440\u0430\u043c\u043c (txt)",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_biola.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 txt \u0444\u0430\u0439\u043b, \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0438\u0437 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0434\u043b\u044f \u0411\u0438\u043e\u043b\u044b.</p><p>\u0424\u0430\u0439\u043b\u044b \u043f\u043e\u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0438 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0438 \u043f\u0443\u0442\u044f \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0444\u0430\u0439\u043b\u043e\u043c</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_path_16.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u0438 \u0442\u0440\u043e\u043c\u0431\u043e\u0446\u0438\u0442\u043e\u0432 (pdf)",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_biola_concentration.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 pdf \u0444\u0430\u0439\u043b \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438 \u043a\u0430\u0441\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u0438 \u0442\u0440\u043e\u043c\u0431\u043e\u0446\u0438\u0442\u043e\u0432.</p><p>\u0424\u0430\u0439\u043b\u044b \u043f\u043e\u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0438 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0438 \u043f\u0443\u0442\u044f \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0444\u0430\u0439\u043b\u043e\u043c</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.label_15.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u042d\u0442\u043e \u0444\u0438\u043b\u044c\u0442\u0440 \u0421\u0430\u0432\u0438\u0446\u043a\u043e\u0433\u043e-\u0413\u043e\u043b\u0435\u044f</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_15.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043b\u0438\u043d\u0430 \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u043a\u0440\u0438\u0432\u044b\u0445",
                None,
            )
        )
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "\u0411\u043e\u0440\u043d", None)
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_biola_born_odd.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043b\u0438\u043d\u0430 \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u0434\u043b\u044f \u0434\u0430\u043d\u043d\u044b\u0445 \u0441\u0432\u0435\u0442\u043e\u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u043d\u0438\u044f \u043f\u043e \u0411\u043e\u0440\u043d\u0443. \u041f\u043e\u0434\u0431\u0438\u0440\u0430\u043b\u043e\u0441\u044c \u044d\u043c\u043f\u0438\u0440\u0438\u0447\u0435\u0441\u043a\u0438, \u0447\u0442\u043e\u0431\u044b \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u043c, \u0440\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u043c \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u0411\u0438\u043e\u043b\u0430",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_17.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0424\u043b\u0443\u043a\u0442\u0430\u0446\u0438\u0438", None
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_biola_fluc_odd.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u043b\u0438\u043d\u0430 \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u0434\u043b\u044f \u0434\u0430\u043d\u043d\u044b\u0445 \u0444\u043b\u0443\u043a\u0442\u0443\u0430\u0446\u0438\u0439 \u0441\u0432\u0435\u0442\u043e\u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u043d\u0438\u044f. \u041f\u043e\u0434\u0431\u0438\u0440\u0430\u043b\u043e\u0441\u044c \u044d\u043c\u043f\u0438\u0440\u0438\u0447\u0435\u0441\u043a\u0438, \u0447\u0442\u043e\u0431\u044b \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u043c, \u0440\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u043c \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u0411\u0438\u043e\u043b\u0430</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.label_12.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u042d\u0442\u043e \u0444\u0438\u043b\u044c\u0442\u0440 \u0421\u0430\u0432\u0438\u0446\u043a\u043e\u0433\u043e-\u0413\u043e\u043b\u0435\u044f</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_12.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043b\u0438\u043d\u0430 \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u044b\u0445",
                None,
            )
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", "\u0411\u043e\u0440\u043d", None)
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_biola_born.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u043b\u0438\u043d\u0430 \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u0434\u043b\u044f \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u043e\u0439 \u0441\u0432\u0435\u0442\u043e\u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u043d\u0438\u044f \u043f\u043e \u0411\u043e\u0440\u043d\u0443. \u041f\u043e\u0434\u0431\u0438\u0440\u0430\u043b\u043e\u0441\u044c \u044d\u043c\u043f\u0438\u0440\u0438\u0447\u0435\u0441\u043a\u0438, \u0447\u0442\u043e\u0431\u044b \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u043c, \u0440\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u043c \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u0411\u0438\u043e\u043b\u0430</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_14.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0424\u043b\u0443\u043a\u0442\u0430\u0446\u0438\u0438", None
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_biola_fluc.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u043b\u0438\u043d\u0430 \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u0434\u043b\u044f \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u043e\u0439 \u0444\u043b\u0443\u043a\u0442\u0443\u0430\u0446\u0438\u0439 \u0441\u0432\u0435\u0442\u043e\u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u043d\u0438\u044f. \u041f\u043e\u0434\u0431\u0438\u0440\u0430\u043b\u043e\u0441\u044c \u044d\u043c\u043f\u0438\u0440\u0438\u0447\u0435\u0441\u043a\u0438, \u0447\u0442\u043e\u0431\u044b \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u043c, \u0440\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u043c \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u0411\u0438\u043e\u043b\u0430</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.check_biola_plot_figs.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041d\u0430\u0447\u0435\u0440\u0442\u0438\u0442\u044c \u043b\u0438 \u0443\u0441\u0440\u0435\u0434\u043d\u0435\u043d\u043d\u044b\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u043f\u043e \u0411\u043e\u0440\u043d\u0443 \u0438 \u0444\u043b\u0443\u043a\u0442\u0443\u0430\u0446\u0438\u044f\u043c, \u0430 \u0442\u0430\u043a\u0436\u0435 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u044b\u043c?</p><p>\u0418\u043c\u0435\u0435\u0442 \u043c\u0435\u0441\u0442\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f\u044b \u043e\u0434\u043d\u0430\u043a\u043e\u0432\u044b\u0445 \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432 \u0438\u043b\u0438 \u043e\u0434\u043d\u043e\u0433\u043e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430.</p><p><br/></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_biola_plot_figs.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0447\u0435\u0440\u0442\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438",
                None,
            )
        )
        self.lb_color_pal_box_13.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043b\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432",
                None,
            )
        )
        self.lb_color_pal_box_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.doubleSpinBox_Biola.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_color_pal_box_10.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_color_pal_box_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0438",
                None,
            )
        )
        self.comboBox_Biola_SD_or.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435",
                None,
            ),
        )
        self.comboBox_Biola_SD_or.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0448\u0438\u0431\u043a\u0430",
                None,
            ),
        )
        self.comboBox_Biola_SD_or.setItemText(
            2,
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b",
                None,
            ),
        )
        self.comboBox_Biola_SD_or.setItemText(
            3,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u0446\u0435\u043d\u0442\u0438\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b",
                None,
            ),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_Biola_SD_or.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0445",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.check_setka_biola.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u0441\u0435\u0442\u043a\u0443 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0445?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_setka_biola.setText(
            QCoreApplication.translate("MainWindow", "\u0421\u0435\u0442\u043a\u0430", None)
        )
        self.lb_color_pal_box_11.setText(
            QCoreApplication.translate("MainWindow", "\u042f\u0437\u044b\u043a  ", None)
        )
        self.comboBox_Biola_language.setItemText(
            0, QCoreApplication.translate("MainWindow", "Rus", None)
        )
        self.comboBox_Biola_language.setItemText(
            1, QCoreApplication.translate("MainWindow", "Eng", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_Biola_language.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u042f\u0437\u044b\u043a \u0434\u043b\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.btn_biola.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 txt \u0444\u0430\u0439\u043b\u0430",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_biola.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435, \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0438\u0441\u0443\u043d\u043a\u0438 \u0438 excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.btn_biola_concentration.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 pdf \u0444\u0430\u0439\u043b\u0430",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_biola_concentration.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430 pdf",
                None,
            )
        )
        self.Lab_stuff.setTabText(
            self.Lab_stuff.indexOf(self.tab_5),
            QCoreApplication.translate("MainWindow", "\u0411\u0438\u043e\u043b\u0430", None),
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_4.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0435\u0441\u0442\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 \u0441 \u0432\u0438\u0434\u0435\u043e AVI</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c\u0438",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.path_for_LT.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-family:'Helvetica';\">\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432 \u0434\u0430\u043d\u043d\u043e\u0435 \u043f\u043e\u043b\u0435 \u0432\u0432\u0435\u0441\u0442\u0438 \u043f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430\u043c\u0438 \u0440\u0430\u0437\u043d\u044b\u0445 \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u0439/\u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432/\u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432.</span></p><p><span style=\" font-family:'Helvetica';\">\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0432 \u0434\u0430\u043d\u043d\u043e\u0439 \u043f\u0430\u043f\u043a\u0435 \u043c\u043e\u0433\u0443\u0442 \u0431\u044b\u0442\u044c \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 \u0441 \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u044f\u043c\u0438:</span></p><p><span style=\" font-family:'Helvetica';\">0</span></p><p"
                "><span style=\" font-family:'Helvetica';\">1</span></p><p><span style=\" font-family:'Helvetica';\">10</span></p><p><span style=\" font-family:'Helvetica';\">100</span></p><p><br/></p><p><span style=\" font-family:'Helvetica';\">\u0412 \u043a\u0430\u0436\u0434\u043e\u0439 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0432\u0438\u0434\u0435\u043e, \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0435 \u0447\u0435\u0440\u0435\u0437 \u043a\u0430\u043a\u043e\u0439-\u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c. \u0421\u0438\u043b\u0430 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u0435\u0442\u0441\u044f, \u043a\u0430\u043a FA/fa/Fa; \u0441\u0438\u043b\u0430 \u0434\u0435\u0437\u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438, \u043a\u0430\u043a FD/fd/Fd. \u0421\u0438\u043b\u0430 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432"
                "\u0438\u044f \u044d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u0430 \u0438 \u044d\u043d\u0434\u043e\u0442\u0435\u043b\u0438\u044f, \u043a\u0430\u043a End/end. \u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u043f\u0435\u0440\u0432\u044b\u0435 2 \u0431\u0443\u043a\u0432\u044b \u0438\u043c\u0435\u043d\u0438 \u0441\u0438\u043b\u044b \u0431\u044b\u043b\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u043c. \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441\u0438\u043b\u044b \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u043e \u0431\u0435\u0437 \u0434\u043e\u043f. \u0417\u043d\u0430\u043a\u043e\u0432 (\u043a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0442\u0430\u043a \u043d\u0435\u043b\u044c\u0437\u044f: \u00abFd3-12.2+.avi\u00bb. \u0411\u0443\u0434\u0443\u0442 \u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u0442\u043e\u043b\u044c"
                "\u043a\u043e \u0432\u0438\u0434\u0435\u043e\u0444\u0430\u0439\u043b\u043e\u0432. \u0422.\u0435. \u043c\u0435\u0436\u0434\u0443 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0435\u043c \u0438 \u00ab.avi\u00bb \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u0441\u0438\u043b\u0430.\u00a0</span></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_LT.setText("")
        # if QT_CONFIG(tooltip)
        self.lb_path_13.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0415\u0441\u043b\u0438 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f '1-Name1-Name2', \u0442\u043e \u043c\u043e\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c '-' \u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u044e '2', \u0442\u043e\u0433\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043e \u0442\u043e\u043b\u044c\u043a\u043e 'Name1'.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_13.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0438 \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.sep_for_LT.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-family:'Helvetica';\">\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0438 \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a. \u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c, \u0447\u0442\u043e\u0431\u044b \u0432 excel \u0444\u0430\u0439\u043b\u0435 \u0431\u044b\u043b\u0438 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u044b \u0438\u043d\u0442\u0435\u0440\u0438\u0441\u0443\u044e\u0449\u0438\u0435 \u0438\u043c\u0435\u043d\u0430. </span></p><p><span style=\" font-family:'Helvetica';\">\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 \u043d\u0430\u0437\u044b\u0432\u0430\u043b\u0438\u0441\u044c \u043f\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0443 &quot;\u043e\u0431\u0440\u0430\u0437\u0435\u0446-\u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u044f&quot;:</span></p><p><span style=\" font-family:'Helvetica';\">de"
                "xtran-0</span></p><p><span style=\" font-family:'Helvetica';\">dextran-10</span></p><p><span style=\" font-family:'Helvetica';\">dextran-100</span></p><p><span style=\" font-family:'Helvetica';\">\u0422\u043e \u0441 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0435\u043c &quot;-&quot; \u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0435\u0439 \u0438\u043c\u0435\u043d\u0438 &quot;2&quot; \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432 \u0432 excel \u0431\u0443\u0434\u0443\u0442: [0, 10, 100]</span></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.sep_for_LT.setText("")
        # if QT_CONFIG(tooltip)
        self.lb_path_15.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0415\u0441\u043b\u0438 \u0432\u044b\u0431\u0440\u0430\u043d \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c '-' \u0434\u043b\u044f \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a '1-Name1-Name2', \u0442\u043e \u043f\u0440\u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u0438 2 \u0431\u0443\u0434\u0435\u0442 Name1</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_15.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0437\u0438\u0446\u0438\u044f, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u0438\u043d\u0442\u0435\u0440\u0438\u0441\u0443\u044e\u0449\u0435\u0435 \u0438\u043c\u044f",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.position.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-family:\'Helvetica\';">\u041f\u043e\u0437\u0438\u0446\u0438\u044f, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u0438\u043c\u044f \u043f\u0440\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0438 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044f \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0438 \u043f\u043e\u0434\u043f\u0430\u043f\u043e\u043a. </span></p><p><span style=" font-family:\'Helvetica\';">\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0438 \u043d\u0430\u0437\u044b\u0432\u0430\u043b\u0438\u0441\u044c \u043f\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0443 &quot;\u043e\u0431\u0440\u0430\u0437\u0435\u0446-\u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u044f&quot;:</span></p><p><span style=" font-family:\'Helvetica\';">dextran-0</span></p><p><span style=" fo'
                "nt-family:'Helvetica';\">dextran-10</span></p><p><span style=\" font-family:'Helvetica';\">dextran-100</span></p><p><span style=\" font-family:'Helvetica';\">\u0422\u043e \u0441 \u043f\u043e\u0437\u0438\u0446\u0438\u0435\u0439 &quot;2&quot; \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432 \u0432 excel \u0431\u0443\u0434\u0443\u0442: [0, 10, 100]</span></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_path_14.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0432\u0441\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0441\u0438\u043b \u0432 \u0432\u0438\u0434\u0435 &quot;FA-18.9.avi&quot;, \u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0435\u043c \u0431\u0443\u0434\u0435\u0442 &quot;-&quot;. \u0422\u0430\u043a \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0434\u043b\u044f \u0432\u0441\u0435\u0445. </p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_14.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u043c\u0435\u0436\u0434\u0443 \u0441\u0438\u043b\u043e\u0439 \u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u043c",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.sep_for_LT_values.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-family:'Helvetica';\">\u0412\u0430\u0436\u043d\u043e \u0432\u043d\u0435\u0441\u0442\u0438 \u0432 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0441\u0438\u043b\u044b.</span></p><p><span style=\" font-family:'Helvetica';\">\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0447\u0430\u0449\u0435 \u0432\u0441\u0435\u0433\u043e \u044d\u0442\u043e &quot;-&quot;. \u0421\u0438\u043b\u044b \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0432 \u044d\u0442\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435 \u0434\u043b\u044f \u043f\u0440\u0438\u043c\u0435\u0440\u0430:</span></p><p><span style=\" font-family:'Helvetica';\">FA-19.9.avi</span></p><p><span style=\" font-family:'Helvetica';\">fa-17.0.avi</span></p><p><span style"
                "=\" font-family:'Helvetica';\">Fd-11.1.avi</span></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.sep_for_LT_values.setText(QCoreApplication.translate("MainWindow", "-", None))
        # if QT_CONFIG(tooltip)
        self.lb_stattest_13.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430 \u0434\u043b\u044f \u0434\u043e\u043f. \u043f\u0443\u0447\u043a\u0430 \u0441\u0435\u0439\u0447\u0430\u0441 \u0434\u0435\u043b\u0430\u0435\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u044d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439, \u043e\u0434\u043d\u0430\u043a\u043e \u043c\u043e\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0438 \u043b\u0438\u043d\u0435\u0439\u043d\u0443\u044e",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_13.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430 \u0434\u043b\u044f \u0434\u043e\u043f. \u043f\u0443\u0447\u043a\u0430",
                None,
            )
        )
        self.comboBox_LT_calibration.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow", "\u041b\u0438\u043d\u0435\u0439\u043d\u0430\u044f", None
            ),
        )
        self.comboBox_LT_calibration.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u0430\u044f",
                None,
            ),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_LT_calibration.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430 \u0434\u043b\u044f \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0443\u0447\u043a\u0430 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043a\u0430\u043a \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0439, \u0442\u0430\u043a \u0438 \u044d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439. \u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u043e\u0434\u043d\u043e</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.btn_LT.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u043b\u0430\u0437\u0435\u0440\u043d\u043e\u0433\u043e \u043f\u0438\u043d\u0446\u0435\u0442\u0430",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_LT.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_LT_raw_data.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u0440\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u043c \u0432\u0438\u0434\u0435? ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_LT_raw_data.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430\u043c",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_5.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u0438\u043b\u044b \u043c\u0435\u0436\u0434\u0443 \u044d\u043d\u0434\u043e\u0442\u0435\u043b\u0438\u0435\u043c \u0438 \u044d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u0430\u043c\u0438 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u044e\u0442\u0441\u044f End, END, \u0438\u043b\u0438 end</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0443\u0447\u043e\u043a",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_17.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0438\u043b\u0430 = k*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_17.setText(
            QCoreApplication.translate("MainWindow", "\u0421\u0438\u043b\u0430 = ", None)
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_7.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_7.setText(QCoreApplication.translate("MainWindow", "k", None))
        # if QT_CONFIG(tooltip)
        self.lb_path_18.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_18.setText(
            QCoreApplication.translate(
                "MainWindow",
                "*\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u043d\u0430 \u0444\u043e\u0442\u043e\u0434\u0435\u0442\u0435\u043a\u0442\u043e\u0440\u0435",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_8.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_8.setText(QCoreApplication.translate("MainWindow", " + b", None))
        # if QT_CONFIG(tooltip)
        self.lb_path_12.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u043a\u0430\u0437\u044b\u0432\u0430\u0439\u0442\u0435 \u0434\u0430\u0442\u0443, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u0437\u0430\u043f\u0443\u0442\u0430\u0442\u044c\u0441\u044f",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_12.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_6.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u0438\u043b\u044b \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u044e\u0442\u0441\u044f FA (\u0438\u043b\u0438 Fa, fa), \u0430 \u0441\u0438\u043b\u044b \u0434\u0435\u0437\u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438, \u043a\u0430\u043a FD (\u0438\u043b\u0438 Fd, fd)</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0443\u0447\u043e\u043a",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_19.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0438\u043b\u0430 = k*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_19.setText(
            QCoreApplication.translate("MainWindow", "\u0421\u0438\u043b\u0430 = ", None)
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_9.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0438\u043b\u0430 = a*(\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438)+b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_9.setText(QCoreApplication.translate("MainWindow", "k", None))
        # if QT_CONFIG(tooltip)
        self.lb_path_20.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_20.setText(
            QCoreApplication.translate(
                "MainWindow",
                "*\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u043d\u0430 \u0444\u043e\u0442\u043e\u0434\u0435\u0442\u0435\u043a\u0442\u043e\u0440\u0435",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_21.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_path_21.setText(QCoreApplication.translate("MainWindow", " + b", None))
        # if QT_CONFIG(tooltip)
        self.lb_path_11.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u043a\u0430\u0437\u044b\u0432\u0430\u0439\u0442\u0435 \u0434\u0430\u0442\u0443, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u0437\u0430\u043f\u0443\u0442\u0430\u0442\u044c\u0441\u044f",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_10.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u0438\u043b\u044b \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u044e\u0442\u0441\u044f FA (\u0438\u043b\u0438 Fa, fa), \u0430 \u0441\u0438\u043b\u044b \u0434\u0435\u0437\u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438, \u043a\u0430\u043a FD (\u0438\u043b\u0438 Fd, fd)</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0443\u0447\u043e\u043a",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_22.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_path_22.setText(
            QCoreApplication.translate("MainWindow", "\u0421\u0438\u043b\u0430 = ", None)
        )
        self.lb_path_23.setText(QCoreApplication.translate("MainWindow", "k", None))
        self.lb_path_27.setText(QCoreApplication.translate("MainWindow", "*( y0", None))
        self.lb_path_28.setText(QCoreApplication.translate("MainWindow", "+ A", None))
        self.lb_path_29.setText(
            QCoreApplication.translate(
                "MainWindow", "* EXP( \u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c * ", None
            )
        )
        self.lb_path_30.setText(QCoreApplication.translate("MainWindow", "R0", None))
        self.lb_path_31.setText(QCoreApplication.translate("MainWindow", ")) + b", None))
        # if QT_CONFIG(tooltip)
        self.lb_path_26.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u043a\u0430\u0437\u044b\u0432\u0430\u0439\u0442\u0435 \u0434\u0430\u0442\u0443, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u0437\u0430\u043f\u0443\u0442\u0430\u0442\u044c\u0441\u044f",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_26.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438",
                None,
            )
        )
        self.Lab_stuff.setTabText(
            self.Lab_stuff.indexOf(self.tab_7),
            QCoreApplication.translate(
                "MainWindow",
                "\u041b\u0430\u0437\u0435\u0440\u043d\u044b\u0439 \u043f\u0438\u043d\u0446\u0435\u0442",
                None,
            ),
        )
        # if QT_CONFIG(whatsthis)
        self.tabWidget_2.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 excel \u0444\u0430\u0439\u043b\u043e\u043c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.path_for_plot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 excel \u0444\u0430\u0439\u043b\u043e\u043c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_plot.setText("")
        self.lb_exel_name.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.check_box_figs_all_sheets.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0415\u0441\u043b\u0438 \u0432\u044b\u0434\u0435\u043b\u0430\u043d\u0430 \u0433\u0430\u043b\u043e\u0447\u043a\u0430, \u0442\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u043e\u0439\u0434\u0435\u0442\u0441\u044f \u043f\u043e \u0432\u0441\u0435\u043c \u043b\u0438\u0441\u0442\u0430\u043c",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_box_figs_all_sheets.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443 \u043f\u043e \u0432\u0441\u0435\u043c \u043b\u0438\u0441\u0442\u0430\u043c \u0432 excel \u0444\u0430\u0439\u043b\u0435?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_box_figs_all_sheets.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e \u0432\u0441\u0435\u043c \u043b\u0438\u0441\u0442\u0430\u043c",
                None,
            )
        )
        self.lb_exel_name_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 \u0444\u0430\u0439\u043b\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_figs_sheets.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 excel \u0444\u0430\u0439\u043b\u0435 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u043c\u0435\u043d\u043d\u043e \u043f\u043e\u0441\u043b\u0435 \u044d\u0442\u043e\u0433\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043e\u043b\u0436\u043d\u044b \u0438\u0434\u0442\u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_2.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043b\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0433\u0440\u0443\u043f\u043f.</p><p>\u042d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043b\u044e\u0431\u0430\u044f \u043a\u043e\u043b\u043e\u043d\u043a\u0430, \u0433\u0434\u0435 \u0435\u0441\u0442\u044c \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, &quot;\u041f\u043e\u043b&quot;.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.checkBox_point_comma_separator.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435 \u0437\u0430\u043f\u044f\u0442\u0430\u044f?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.checkBox_point_comma_separator.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0437\u0430\u043f\u044f\u0442\u0430\u044f \u0432\u043c\u0435\u0441\u0442\u043e \u0442\u043e\u0447\u043a\u0438",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_box_plot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a box plot, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u044b \u0440\u0430\u0437\u043d\u044b\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438?</p><p>\u0412 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u0432\u043d\u0438\u0437\u0443 \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_box_plot.setText(QCoreApplication.translate("MainWindow", "Box plot", None))
        # if QT_CONFIG(tooltip)
        self.check_corr_matrix.setToolTip(
            QCoreApplication.translate("MainWindow", "seaborn.heatmap", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_corr_matrix.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u044b? \u041e\u0434\u043d\u0430 \u043c\u0430\u0442\u0440\u0438\u0446\u0430 \u043d\u0430 \u043a\u0430\u0436\u0434\u0443\u044e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e.</p><p>\u0412 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u0432\u043d\u0438\u0437\u0443 \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_corr_matrix.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_corr_figs.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a, \u0433\u0434\u0435 \u0446\u0432\u0435\u0442\u0430\u043c\u0438 \u0431\u0443\u0434\u0443\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u044b \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438?</p><p>\u0412 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u0432\u043d\u0438\u0437\u0443 \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_corr_figs.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.check_box_pairplot.setToolTip(
            QCoreApplication.translate("MainWindow", "\u0441\u043c. seaborn.pairplot", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_box_pairplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u0440\u0430\u0441\u0441\u0435\u044f\u043d\u0438\u044f, \u0433\u0434\u0435 \u0446\u0432\u0435\u0442\u0430\u043c\u0438 \u0431\u0443\u0434\u0443\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u044b \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438?</p><p>\u0412 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u0432\u043d\u0438\u0437\u0443 \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_box_pairplot.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0440\u0430\u0441\u0441\u0435\u044f\u043d\u0438\u044f",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.check_jointplot.setToolTip(
            QCoreApplication.translate("MainWindow", "\u0441\u043c. seaborn.jointplot", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_jointplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043f\u043e \u0434\u0432\u0443\u043c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c?</p><p>\u0412 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u0432\u043d\u0438\u0437\u0443 \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_jointplot.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043f\u043e \u0434\u0432\u0443\u043c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_corr_one_parameter.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044e \u043e\u0434\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430? </p><p>\u0422\u043e \u0435\u0441\u0442\u044c \u0441\u0442\u0440\u043e\u0438\u0442\u0441\u044f \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u043a\u043e\u043b\u043e\u043d\u043a\u0438 \u0438 \u0432\u0441\u0435\u043c\u0438 \u043e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u043c\u0438.</p><p>\u0421\u0442\u0440\u043e\u0438\u0442\u0441\u044f \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e \u043e\u0442 \u0434\u0440\u0443\u0433\u0438\u0445 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432. </p><p>\u0412 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u0432\u043d\u0438\u0437\u0443 \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438"
                "\u0442\u044c \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_corr_one_parameter.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043e\u0434\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_color_pal_box.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430 \u0434\u043b\u044f box",
                None,
            )
        )
        self.comboBox_color_pal_box.setItemText(
            0, QCoreApplication.translate("MainWindow", "Set1", None)
        )
        self.comboBox_color_pal_box.setItemText(
            1, QCoreApplication.translate("MainWindow", "Set2", None)
        )
        self.comboBox_color_pal_box.setItemText(
            2, QCoreApplication.translate("MainWindow", "Set3", None)
        )
        self.comboBox_color_pal_box.setItemText(
            3, QCoreApplication.translate("MainWindow", "Paired", None)
        )
        self.comboBox_color_pal_box.setItemText(
            4, QCoreApplication.translate("MainWindow", "Accent", None)
        )
        self.comboBox_color_pal_box.setItemText(
            5, QCoreApplication.translate("MainWindow", "Pastel1", None)
        )
        self.comboBox_color_pal_box.setItemText(
            6, QCoreApplication.translate("MainWindow", "Pastel2", None)
        )
        self.comboBox_color_pal_box.setItemText(
            7, QCoreApplication.translate("MainWindow", "Dark2", None)
        )
        self.comboBox_color_pal_box.setItemText(
            8, QCoreApplication.translate("MainWindow", "rocket", None)
        )
        self.comboBox_color_pal_box.setItemText(
            9, QCoreApplication.translate("MainWindow", "mako", None)
        )
        self.comboBox_color_pal_box.setItemText(
            10, QCoreApplication.translate("MainWindow", "flare", None)
        )
        self.comboBox_color_pal_box.setItemText(
            11, QCoreApplication.translate("MainWindow", "crest", None)
        )
        self.comboBox_color_pal_box.setItemText(
            12, QCoreApplication.translate("MainWindow", "viridis", None)
        )
        self.comboBox_color_pal_box.setItemText(
            13, QCoreApplication.translate("MainWindow", "plasma", None)
        )
        self.comboBox_color_pal_box.setItemText(
            14, QCoreApplication.translate("MainWindow", "inferno", None)
        )
        self.comboBox_color_pal_box.setItemText(
            15, QCoreApplication.translate("MainWindow", "magma", None)
        )
        self.comboBox_color_pal_box.setItemText(
            16, QCoreApplication.translate("MainWindow", "cividis", None)
        )
        self.comboBox_color_pal_box.setItemText(
            17, QCoreApplication.translate("MainWindow", "Greys", None)
        )
        self.comboBox_color_pal_box.setItemText(
            18, QCoreApplication.translate("MainWindow", "Reds", None)
        )
        self.comboBox_color_pal_box.setItemText(
            19, QCoreApplication.translate("MainWindow", "Greens", None)
        )
        self.comboBox_color_pal_box.setItemText(
            20, QCoreApplication.translate("MainWindow", "Blues", None)
        )
        self.comboBox_color_pal_box.setItemText(
            21, QCoreApplication.translate("MainWindow", "Oranges", None)
        )
        self.comboBox_color_pal_box.setItemText(
            22, QCoreApplication.translate("MainWindow", "Purples", None)
        )
        self.comboBox_color_pal_box.setItemText(
            23, QCoreApplication.translate("MainWindow", "YlOrRd", None)
        )
        self.comboBox_color_pal_box.setItemText(
            24, QCoreApplication.translate("MainWindow", "tab10", None)
        )
        self.comboBox_color_pal_box.setItemText(
            25, QCoreApplication.translate("MainWindow", "deep", None)
        )
        self.comboBox_color_pal_box.setItemText(
            26, QCoreApplication.translate("MainWindow", "muted", None)
        )
        self.comboBox_color_pal_box.setItemText(
            27, QCoreApplication.translate("MainWindow", "pastel", None)
        )
        self.comboBox_color_pal_box.setItemText(
            28, QCoreApplication.translate("MainWindow", "bright", None)
        )
        self.comboBox_color_pal_box.setItemText(
            29, QCoreApplication.translate("MainWindow", "dark", None)
        )
        self.comboBox_color_pal_box.setItemText(
            30, QCoreApplication.translate("MainWindow", "colorblind", None)
        )
        self.comboBox_color_pal_box.setItemText(
            31, QCoreApplication.translate("MainWindow", "tab20", None)
        )
        self.comboBox_color_pal_box.setItemText(
            32, QCoreApplication.translate("MainWindow", "tab20b", None)
        )
        self.comboBox_color_pal_box.setItemText(
            33, QCoreApplication.translate("MainWindow", "tab20c", None)
        )
        self.comboBox_color_pal_box.setItemText(
            34, QCoreApplication.translate("MainWindow", "BuPu", None)
        )
        self.comboBox_color_pal_box.setItemText(
            35, QCoreApplication.translate("MainWindow", "BuPu_r", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_color_pal_box.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430 \u0434\u043b\u044f box</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_points.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430 \u0434\u043b\u044f \u0442\u043e\u0447\u0435\u043a",
                None,
            )
        )
        self.comboBox_color_pal_points.setItemText(
            0, QCoreApplication.translate("MainWindow", "Set1", None)
        )
        self.comboBox_color_pal_points.setItemText(
            1, QCoreApplication.translate("MainWindow", "Set2", None)
        )
        self.comboBox_color_pal_points.setItemText(
            2, QCoreApplication.translate("MainWindow", "Set3", None)
        )
        self.comboBox_color_pal_points.setItemText(
            3, QCoreApplication.translate("MainWindow", "Paired", None)
        )
        self.comboBox_color_pal_points.setItemText(
            4, QCoreApplication.translate("MainWindow", "Accent", None)
        )
        self.comboBox_color_pal_points.setItemText(
            5, QCoreApplication.translate("MainWindow", "Pastel1", None)
        )
        self.comboBox_color_pal_points.setItemText(
            6, QCoreApplication.translate("MainWindow", "Pastel2", None)
        )
        self.comboBox_color_pal_points.setItemText(
            7, QCoreApplication.translate("MainWindow", "Dark2", None)
        )
        self.comboBox_color_pal_points.setItemText(
            8, QCoreApplication.translate("MainWindow", "rocket", None)
        )
        self.comboBox_color_pal_points.setItemText(
            9, QCoreApplication.translate("MainWindow", "mako", None)
        )
        self.comboBox_color_pal_points.setItemText(
            10, QCoreApplication.translate("MainWindow", "flare", None)
        )
        self.comboBox_color_pal_points.setItemText(
            11, QCoreApplication.translate("MainWindow", "crest", None)
        )
        self.comboBox_color_pal_points.setItemText(
            12, QCoreApplication.translate("MainWindow", "viridis", None)
        )
        self.comboBox_color_pal_points.setItemText(
            13, QCoreApplication.translate("MainWindow", "plasma", None)
        )
        self.comboBox_color_pal_points.setItemText(
            14, QCoreApplication.translate("MainWindow", "inferno", None)
        )
        self.comboBox_color_pal_points.setItemText(
            15, QCoreApplication.translate("MainWindow", "magma", None)
        )
        self.comboBox_color_pal_points.setItemText(
            16, QCoreApplication.translate("MainWindow", "cividis", None)
        )
        self.comboBox_color_pal_points.setItemText(
            17, QCoreApplication.translate("MainWindow", "Greys", None)
        )
        self.comboBox_color_pal_points.setItemText(
            18, QCoreApplication.translate("MainWindow", "Reds", None)
        )
        self.comboBox_color_pal_points.setItemText(
            19, QCoreApplication.translate("MainWindow", "Greens", None)
        )
        self.comboBox_color_pal_points.setItemText(
            20, QCoreApplication.translate("MainWindow", "Blues", None)
        )
        self.comboBox_color_pal_points.setItemText(
            21, QCoreApplication.translate("MainWindow", "Oranges", None)
        )
        self.comboBox_color_pal_points.setItemText(
            22, QCoreApplication.translate("MainWindow", "Purples", None)
        )
        self.comboBox_color_pal_points.setItemText(
            23, QCoreApplication.translate("MainWindow", "YlOrRd", None)
        )
        self.comboBox_color_pal_points.setItemText(
            24, QCoreApplication.translate("MainWindow", "tab10", None)
        )
        self.comboBox_color_pal_points.setItemText(
            25, QCoreApplication.translate("MainWindow", "deep", None)
        )
        self.comboBox_color_pal_points.setItemText(
            26, QCoreApplication.translate("MainWindow", "muted", None)
        )
        self.comboBox_color_pal_points.setItemText(
            27, QCoreApplication.translate("MainWindow", "pastel", None)
        )
        self.comboBox_color_pal_points.setItemText(
            28, QCoreApplication.translate("MainWindow", "bright", None)
        )
        self.comboBox_color_pal_points.setItemText(
            29, QCoreApplication.translate("MainWindow", "dark", None)
        )
        self.comboBox_color_pal_points.setItemText(
            30, QCoreApplication.translate("MainWindow", "colorblind", None)
        )
        self.comboBox_color_pal_points.setItemText(
            31, QCoreApplication.translate("MainWindow", "tab20", None)
        )
        self.comboBox_color_pal_points.setItemText(
            32, QCoreApplication.translate("MainWindow", "tab20b", None)
        )
        self.comboBox_color_pal_points.setItemText(
            33, QCoreApplication.translate("MainWindow", "tab20c", None)
        )
        self.comboBox_color_pal_points.setItemText(
            34, QCoreApplication.translate("MainWindow", "BuPu", None)
        )
        self.comboBox_color_pal_points.setItemText(
            35, QCoreApplication.translate("MainWindow", "BuPu_r", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_color_pal_points.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430 \u0434\u043b\u044f \u0442\u043e\u0447\u0435\u043a</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_color_for_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0426\u0432\u0435\u0442 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX. \u0415\u0441\u043b\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0446\u0432\u0435\u0442\u043e\u0432, \u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0437\u043d\u0430\u043a \u043c\u0435\u0436\u0434\u0443 \u043d\u0438\u043c\u0438: &quot;&amp;&quot;</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_color_for_box.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0426\u0432\u0435\u0442 \u0434\u043b\u044f box (HEX)", None
            )
        )
        # if QT_CONFIG(whatsthis)
        self.pushButton_HEX_box.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0434\u0435\u043b\u0430\u0442\u044c \u043a\u0430\u0441\u0442\u043e\u043c\u043d\u044b\u0435 \u0446\u0432\u0435\u0442\u0430 \u0434\u043b\u044f box.</p><p>\u0414\u043b\u044f \u044d\u0442\u043e\u0433\u043e \u0432\u044b\u0431\u0435\u0440\u0430\u0439\u0442\u0435 \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u043e \u0446\u0432\u0435\u0442\u0430 \u0432 \u043f\u0430\u043b\u0438\u0442\u0440\u0435.</p><p>\u0412 \u043f\u0430\u043d\u0435\u043b\u0435 \u0441\u043b\u0435\u0432\u0430 \u0431\u0443\u0434\u0435\u0442 \u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f \u0441\u0442\u0440\u043e\u043a\u0430, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0431\u0443\u0434\u0435\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0430 \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u044b.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.pushButton_HEX_box.setText(QCoreApplication.translate("MainWindow", "HEX", None))
        # if QT_CONFIG(tooltip)
        self.lb_color_forpoints.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0426\u0432\u0435\u0442 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX. \u0415\u0441\u043b\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0446\u0432\u0435\u0442\u043e\u0432, \u0442\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0437\u043d\u0430\u043a \u043c\u0435\u0436\u0434\u0443 \u043d\u0438\u043c\u0438: &quot;&amp;&quot;</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_color_forpoints.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u0442\u043e\u0447\u0435\u043a (HEX)",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.pushButton_HEX_points.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0434\u0435\u043b\u0430\u0442\u044c \u043a\u0430\u0441\u0442\u043e\u043c\u043d\u044b\u0435 \u0446\u0432\u0435\u0442\u0430 \u0434\u043b\u044f \u0442\u043e\u0447\u0435\u043a.</p><p>\u0414\u043b\u044f \u044d\u0442\u043e\u0433\u043e \u0432\u044b\u0431\u0435\u0440\u0430\u0439\u0442\u0435 \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u043e \u0446\u0432\u0435\u0442\u0430 \u0432 \u043f\u0430\u043b\u0438\u0442\u0440\u0435.</p><p>\u0412 \u043f\u0430\u043d\u0435\u043b\u0435 \u0441\u043b\u0435\u0432\u0430 \u0431\u0443\u0434\u0435\u0442 \u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f \u0441\u0442\u0440\u043e\u043a\u0430, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0431\u0443\u0434\u0435\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0430 \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u044b.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.pushButton_HEX_points.setText(QCoreApplication.translate("MainWindow", "HEX", None))
        self.lb_color_pal_box_19.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_color_pal_box_23.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c \u0442\u043e\u0447\u0435\u043a",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_color_pal_box_23.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c",
                None,
            )
        )
        self.lb_color_pal_box_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a \u0434\u043b\u044f \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f",
                None,
            )
        )
        self.lb_color_pal_box_6.setText(
            QCoreApplication.translate("MainWindow", "\u0428\u0440\u0438\u0444\u0442", None)
        )
        self.comboBox_fonts.setItemText(
            0, QCoreApplication.translate("MainWindow", "DejaVu Sans", None)
        )
        self.comboBox_fonts.setItemText(1, QCoreApplication.translate("MainWindow", "Tahoma", None))
        self.comboBox_fonts.setItemText(
            2, QCoreApplication.translate("MainWindow", "Verdana", None)
        )
        self.comboBox_fonts.setItemText(3, QCoreApplication.translate("MainWindow", "Arial", None))
        self.comboBox_fonts.setItemText(
            4, QCoreApplication.translate("MainWindow", "Trebuchet MS", None)
        )
        self.comboBox_fonts.setItemText(
            5, QCoreApplication.translate("MainWindow", "Times New Roman", None)
        )
        self.comboBox_fonts.setItemText(
            6, QCoreApplication.translate("MainWindow", "Georgia", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_fonts.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0428\u0440\u0438\u0444\u0442 \u0434\u043b\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0445",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 X",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_x_label.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 X",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 Y",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_y_label.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 Y",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 X",
                None,
            )
        )
        self.lb_color_pal_box_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 Y",
                None,
            )
        )
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_15),
            QCoreApplication.translate(
                "MainWindow",
                "\u0428\u0440\u0438\u0444\u0442, \u0446\u0432\u0435\u0442\u0430, \u0440\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.check_sort_or_not.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0411\u0435\u0437 \u0444\u043b\u0430\u0436\u043a\u0430 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0431\u0443\u0434\u0435\u0442 \u0442\u0430\u043a\u0438\u043c, \u043a\u0430\u043a\u043e\u0439 \u043e\u043d \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_sort_or_not.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0433\u0440\u0443\u043f\u043f\u0435? \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0431\u0430\u0437\u043e\u0432\u0430\u044f \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_sort_or_not.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0433\u0440\u0443\u043f\u043f\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_sort_or_not_ascending.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0433\u0440\u0443\u043f\u043f\u0435 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044e?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_sort_or_not_ascending.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044e",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_del_hue_6.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u0440\u043e\u043f\u0438\u0441\u0430\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b, \u043d\u0430\u0447\u0438\u043d\u0430\u044f \u0441 \u043f\u0435\u0440\u0432\u043e\u0433\u043e. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, '1 2 4 3'</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_del_hue_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.order_box_plot.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.order_box_plot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439. </p><p>\u0414\u043b\u044f \u044d\u0442\u043e\u0433\u043e \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b \u0446\u0438\u0444\u0440\u0430\u043c\u0438 \u0432\u0432\u0435\u0441\u0442\u0438 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u0439 \u043f\u043e\u0440\u044f\u0434\u043e\u043a.</p><p>\u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u043e\u0432\u0430\u043b\u043e \u043a\u043e\u043b-\u0432\u0443 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0432 \u0433\u0440\u0443\u043f\u043f\u0435.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u043c\u043e\u0436\u043d\u043e "
                "\u0432\u0432\u0435\u0441\u0442\u0438 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435:</p><p>1 2 4 3</p><p>\u0422\u043e\u0433\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u043f\u043e\u0440\u044f\u0434\u043e\u043a, \u043a\u0430\u043a \u043e\u043d \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u0432\u044b\u0448\u0435 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u043e\u0440\u044f\u0434\u043a\u0430 \u0431\u0435\u0437 \u0443\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0432\u0430\u043d\u0438\u044f</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_stattest_3.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043b-\u0432\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432 \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u0435 -- \u043f\u043e\u0434\u043f\u0438\u0441\u044c \u0441\u043d\u0438\u0437\u0443",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0434\u043f\u0438\u0441\u0438 N \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0432 \u0433\u0440\u0443\u043f\u043f\u0430\u0445",
                None,
            )
        )
        self.check_N_.setText("")
        # if QT_CONFIG(tooltip)
        self.lb__altern_heposisis_5.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "N - \u043a\u043e\u043b-\u0432\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432/\u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432 \u0432 \u0433\u0440\u0443\u043f\u043f\u0435",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb__altern_heposisis_5.setText(
            QCoreApplication.translate("MainWindow", "\u0420\u0430\u0437\u043c\u0435\u0440 N", None)
        )
        self.comboBox_box_check_N_.setItemText(
            0, QCoreApplication.translate("MainWindow", "x-small", None)
        )
        self.comboBox_box_check_N_.setItemText(
            1, QCoreApplication.translate("MainWindow", "small", None)
        )
        self.comboBox_box_check_N_.setItemText(
            2, QCoreApplication.translate("MainWindow", "medium", None)
        )
        self.comboBox_box_check_N_.setItemText(
            3, QCoreApplication.translate("MainWindow", "large", None)
        )
        self.comboBox_box_check_N_.setItemText(
            4, QCoreApplication.translate("MainWindow", "x-large", None)
        )
        self.comboBox_box_check_N_.setItemText(
            5, QCoreApplication.translate("MainWindow", "xx-large", None)
        )
        self.comboBox_box_check_N_.setItemText(
            6, QCoreApplication.translate("MainWindow", "xx-small", None)
        )

        self.label_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u0440\u0430\u0449\u0430\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u043d\u0430 \u0443\u0433\u043e\u043b",
                None,
            )
        )
        self.comboBox_spin_x_.setItemText(0, QCoreApplication.translate("MainWindow", "0", None))
        self.comboBox_spin_x_.setItemText(1, QCoreApplication.translate("MainWindow", "5", None))
        self.comboBox_spin_x_.setItemText(2, QCoreApplication.translate("MainWindow", "10", None))
        self.comboBox_spin_x_.setItemText(3, QCoreApplication.translate("MainWindow", "15", None))
        self.comboBox_spin_x_.setItemText(4, QCoreApplication.translate("MainWindow", "20", None))
        self.comboBox_spin_x_.setItemText(5, QCoreApplication.translate("MainWindow", "25", None))
        self.comboBox_spin_x_.setItemText(6, QCoreApplication.translate("MainWindow", "30", None))
        self.comboBox_spin_x_.setItemText(7, QCoreApplication.translate("MainWindow", "35", None))
        self.comboBox_spin_x_.setItemText(8, QCoreApplication.translate("MainWindow", "40", None))
        self.comboBox_spin_x_.setItemText(9, QCoreApplication.translate("MainWindow", "45", None))
        self.comboBox_spin_x_.setItemText(10, QCoreApplication.translate("MainWindow", "50", None))
        self.comboBox_spin_x_.setItemText(11, QCoreApplication.translate("MainWindow", "55", None))
        self.comboBox_spin_x_.setItemText(12, QCoreApplication.translate("MainWindow", "60", None))
        self.comboBox_spin_x_.setItemText(13, QCoreApplication.translate("MainWindow", "65", None))
        self.comboBox_spin_x_.setItemText(14, QCoreApplication.translate("MainWindow", "70", None))
        self.comboBox_spin_x_.setItemText(15, QCoreApplication.translate("MainWindow", "75", None))
        self.comboBox_spin_x_.setItemText(16, QCoreApplication.translate("MainWindow", "80", None))
        self.comboBox_spin_x_.setItemText(17, QCoreApplication.translate("MainWindow", "85", None))
        self.comboBox_spin_x_.setItemText(18, QCoreApplication.translate("MainWindow", "90", None))

        self.lb_stattest_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u0444\u043e\u043d \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u043c",
                None,
            )
        )
        self.check_background.setText("")
        # if QT_CONFIG(tooltip)
        self.lb_sd_or_minmax.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 \u0438\u043b\u0438 \u0440\u0430\u0437\u0431\u0440\u043e\u0441 \u043c\u0435\u0436\u0434\u0443 MIN-MAX",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_sd_or_minmax.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439",
                None,
            )
        )
        self.comboBox_sd_or_minmax.setItemText(
            0, QCoreApplication.translate("MainWindow", "SD", None)
        )
        self.comboBox_sd_or_minmax.setItemText(
            1, QCoreApplication.translate("MainWindow", "MIN-MAX", None)
        )

        # if QT_CONFIG(tooltip)
        self.lb_bottom_lim.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0435 \u0432\u0441\u0442\u0430\u0432\u043b\u044f\u0439\u0442\u0435 \u043b\u0438\u0448\u043d\u0438\u0435 \u043f\u0440\u043e\u0431\u0435\u043b\u044b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_bottom_lim.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0438\u0436\u043d\u044e\u044e \u0433\u0440\u0430\u043d\u0438\u0446\u0443",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.bottom_lim.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u0432\u0435\u0441\u0442\u0438 \u0447\u0438\u0441\u043b\u043e",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.lb_bottom_lim_2.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0435 \u0432\u0441\u0442\u0430\u0432\u043b\u044f\u0439\u0442\u0435 \u043b\u0438\u0448\u043d\u0438\u0435 \u043f\u0440\u043e\u0431\u0435\u043b\u044b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_bottom_lim_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0432\u0435\u0440\u0445\u043d\u044e\u044e \u0433\u0440\u0430\u043d\u0438\u0446\u0443",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.upper_lim.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u0432\u0435\u0441\u0442\u0438 \u0447\u0438\u0441\u043b\u043e",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_16),
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439 \u0438 \u0433\u0440\u0430\u043d\u0438\u0446",
                None,
            ),
        )
        self.lb_stattest_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c?",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_stat_znachimost.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_stat_znachimost.setText("")
        self.lb_color_pal_box_21.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0428\u0440\u0438\u0444\u0442 \u0437\u043d\u0430\u0447\u043a\u043e\u0432 \u0441\u0442\u0430\u0442.\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_size_stat_znachimost.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0428\u0440\u0438\u0444\u0442 \u0437\u043d\u0430\u0447\u043a\u043e\u0432 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb__altern_heposisis_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0417\u043d\u0430\u0447\u043e\u043a \u0441\u0442\u0430\u0442.\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438",
                None,
            )
        )
        self.comboBox_box_plot_sign_stat_znachimost.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow", "\u0437\u0432\u0435\u0437\u0434\u043e\u0447\u043a\u0430 (*)", None
            ),
        )
        self.comboBox_box_plot_sign_stat_znachimost.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\u043c\u0435\u043d\u044c\u0448\u0435 \u043a\u0430\u043a\u043e\u0433\u043e-\u0442\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f (p<)",
                None,
            ),
        )
        self.comboBox_box_plot_sign_stat_znachimost.setItemText(
            2,
            QCoreApplication.translate(
                "MainWindow",
                "\u0440\u0430\u0432\u043d\u043e \u043a\u0430\u043a\u043e\u043c\u0443-\u0442\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044e (p=)",
                None,
            ),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_box_plot_sign_stat_znachimost.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0417\u043d\u0430\u0447\u043e\u043a \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438.</p><p>\u041e\u0434\u0438\u043d \u0438\u0437 \u0442\u0440\u0435\u0445:</p><p>- \u0437\u0432\u0435\u0437\u0434\u043e\u0447\u043a\u0430 (*)</p><p>- \u0442\u043e\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 p (p=0.03)</p><p>- \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 p (p&lt;0.05)</p><p>\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u0434\u043b\u044f \u0437\u0434\u0435\u0437\u0434\u043e\u0447\u0435\u043a \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u0435\u0442\u0441\u044f \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c:</p><p>* p&lt;0.05, ** p&lt;0.01, *** p&lt;0.001, **** p&lt;0.0001</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_25.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041c\u0430\u043a\u0441.\u043a\u043e\u043b-\u0432\u043e *", None
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_max_n_stars.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b-\u0432\u043e \u0437\u043d\u0430\u043a\u043e\u0432 \u0434\u043b\u044f \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438.</p><p>\u0420\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u0434\u043b\u044f \u0437\u043d\u0430\u0447\u043a\u0430 \u0441\u0442\u0430\u0442.\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438 &quot;\u0437\u0432\u0435\u0437\u0434\u043e\u0447\u043a\u0430&quot; \u0438 &quot;\u0442\u043e\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 p&quot;.</p><p>\u0415\u0441\u043b\u0438 \u043c\u0430\u043a\u0441.\u043a\u043e\u043b-\u0432\u043e \u0437\u043d\u0430\u043a\u043e\u0432 = 1, \u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0432\u0435\u0434\u0435\u043d\u044b \u0442\u043e\u043b\u044c\u043a\u043e:</p><p>* \u0438\u043b\u0438 p&lt;0.05, \u0434\u0430\u0436\u0435"
                " \u0435\u0441\u043b\u0438 p=0.00001</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb__altern_heposisis.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0410\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u0433\u0438\u043f\u043e\u0442\u0435\u0437\u0430",
                None,
            )
        )
        self.comboBox_alter_hep.setItemText(
            0, QCoreApplication.translate("MainWindow", "two-sided", None)
        )
        self.comboBox_alter_hep.setItemText(
            1, QCoreApplication.translate("MainWindow", "less", None)
        )
        self.comboBox_alter_hep.setItemText(
            2, QCoreApplication.translate("MainWindow", "greater", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_alter_hep.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0410\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u0433\u0438\u043f\u043e\u0442\u0435\u0437\u0430 \u0434\u043b\u044f \u0442\u0435\u0441\u0442\u0430.</p><p>\u0415\u0441\u043b\u0438 \u043d\u0435 \u0437\u043d\u0430\u0435\u0442\u0435, \u0442\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0432\u0441\u0435\u0433\u0434\u0430 two-sided</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_stattest.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u043c. \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043f\u043e \u0440\u0430\u0437\u043d\u044b\u043c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u043c \u0442\u0435\u0441\u0442\u0430\u043c</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442",
                None,
            )
        )
        self.comboBox_stat_test.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow",
                "U-\u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041c\u0430\u043d\u043d\u0430 \u2014 \u0423\u0438\u0442\u043d\u0438",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422-\u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0421\u0442\u044c\u044e\u0434\u0435\u043d\u0442\u0430",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            2,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u0441\u0442 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            3,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u0441\u0442 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f (normal)",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            4,
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0423\u0438\u043b\u043a\u043e\u043a\u0441\u043e\u043d\u0430",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            5,
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041a\u0440\u0430\u0441\u043a\u0435\u043b\u0430 \u2014 \u0423\u043e\u043b\u043b\u0438\u0441\u0430",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            6,
            QCoreApplication.translate(
                "MainWindow",
                "\u041c\u0435\u0434\u0438\u0430\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            7,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u0441\u0442 \u0410\u043d\u0441\u0430\u0440\u0438-\u0411\u0440\u044d\u0434\u043b\u0438",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            8,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u0441\u0442 \u0424\u0438\u0448\u0435\u0440\u0430-\u041f\u0438\u0442\u043c\u0430\u043d\u0430",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            9,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            10,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041c\u0430\u043d\u043d\u0430 \u2014 \u0423\u0438\u0442\u043d\u0438",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            11,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0423\u0438\u043b\u043a\u043e\u043a\u0441\u043e\u043d\u0430",
                None,
            ),
        )
        self.comboBox_stat_test.setItemText(
            12,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0424\u0440\u0438\u0434\u043c\u0430\u043d\u0430",
                None,
            ),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_stat_test.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0441\u0442\u0430\u0442.\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438. </p><p>\u0412 \u0441\u043f\u0438\u0441\u043a\u0435 \u0435\u0441\u0442\u044c \u043a\u0430\u043a \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435, \u0442\u0430\u043a \u0438 \u043d\u0435\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0442\u0435\u0441\u0442\u044b.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_del_hue_7.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u044b\u0431\u0440\u0430\u0442\u044c, \u0435\u0441\u043b\u0438 \u043d\u0443\u0436\u043d\u043e \u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u0436\u0434\u0443 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u043c\u0438 \u0433\u0440\u0443\u043f\u043f\u0430\u043c\u0438. \u0412 \u0441\u0442\u0440\u043e\u043a\u0443 \u0432\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u043c\u0430\u0441\u0441\u0438\u0432 \u0438\u0437 \u043a\u043e\u0440\u0442\u0435\u0436\u0435\u0439 \u0433\u0440\u0443\u043f\u043f \u0441 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u043c \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u043c. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u0442\u044c 4 \u0433\u0440\u0443\u043f\u043f\u044b \u0438 \u0445\u043e\u0447\u0435\u0442\u0441\u044f \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435"
                "\u0442\u044c \u0441\u0442\u0430\u0442.\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u0436\u0434\u0443 1 \u0438 2, \u0430 \u0442\u0430\u043a\u0436\u0435 3 \u0438 4. \u0422\u043e\u0433\u0434\u0430 \u043d\u0430\u0434\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0441 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u043c '(1,2) (3,4)'</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_del_hue_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0447\u0451\u0442 \u0441\u0442\u0430\u0442.\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438 \u0442\u043e\u043b\u044c\u043a\u043e \u043c\u0435\u0436\u0434\u0443 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c\u0438 \u0433\u0440\u0443\u043f\u043f\u0430\u043c\u0438",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.STAT_znachimost_order_box_plot.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_17),
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0430\u0442.\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c",
                None,
            ),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "Box plot", None),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "Box plot", None),
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_sd_or_minmax_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043f\u043e",
                None,
            )
        )
        self.comboBox_correlation_figs_matrix.setItemText(
            0, QCoreApplication.translate("MainWindow", "pearson", None)
        )
        self.comboBox_correlation_figs_matrix.setItemText(
            1, QCoreApplication.translate("MainWindow", "kendall", None)
        )
        self.comboBox_correlation_figs_matrix.setItemText(
            2, QCoreApplication.translate("MainWindow", "spearman", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_correlation_figs_matrix.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041c\u0435\u0442\u043e\u0434 \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0439: \u041f\u0438\u0440\u0441\u043e\u043d, \u0421\u043f\u0438\u0440\u043c\u0435\u043d \u0438\u043b\u0438 \u041a\u0435\u043d\u0434\u0430\u043b.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_sd_or_minmax_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u0441\u0445\u0435\u043c\u0430",
                None,
            )
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            0, QCoreApplication.translate("MainWindow", "coolwarm", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            1, QCoreApplication.translate("MainWindow", "RdBu_r", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            2, QCoreApplication.translate("MainWindow", "YlGn", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            3, QCoreApplication.translate("MainWindow", "BuGn", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            4, QCoreApplication.translate("MainWindow", "GnBu", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            5, QCoreApplication.translate("MainWindow", "bwr", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            6, QCoreApplication.translate("MainWindow", "seismic", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            7, QCoreApplication.translate("MainWindow", "PiYG", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            8, QCoreApplication.translate("MainWindow", "RdGy", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            9, QCoreApplication.translate("MainWindow", "seismic", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            10, QCoreApplication.translate("MainWindow", "hot", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            11, QCoreApplication.translate("MainWindow", "inferno", None)
        )
        self.comboBox_correlation_color_map_for_figs.setItemText(
            12, QCoreApplication.translate("MainWindow", "gist_heat", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_correlation_color_map_for_figs.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u0441\u0445\u0435\u043c\u0430 \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u044b.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_size_corr_matrix.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0440\u0438\u0441\u0443\u043d\u043a\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.corr_mat_figsize.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0420\u0430\u0437\u043c\u0435\u0440 \u0440\u0438\u0441\u0443\u043d\u043a\u0430 \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u044b. </p><p>\u041f\u043e\u0434\u0431\u0438\u0440\u0430\u0435\u0442\u0441\u044f \u0432\u0440\u0443\u0447\u043d\u0443\u044e. \u0412\u043b\u0438\u044f\u0435\u0442 \u043d\u0430 \u0440\u0430\u0437\u043c\u0435\u0440 \u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_font_in.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041c\u0430\u0441\u0448\u0442\u0430\u0444 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.font_for_in.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041c\u0430\u0441\u0448\u0442\u0430\u0431 \u0448\u0440\u0438\u0444\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439 \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u043c\u0430\u0442\u0440\u0438\u0446.</p><p>\u041f\u043e\u0434\u0431\u0438\u0440\u0430\u0435\u0442\u0441\u044f \u0432\u0440\u0443\u0447\u043d\u0443\u044e.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_font_out.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.font_for_out.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430. \u041f\u043e\u0434\u0431\u0438\u0440\u0430\u0435\u0442\u0441\u044f \u0432\u0440\u0443\u0447\u043d\u0443\u044e.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_name_of_title.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_name_of_title.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.name_of_corr_matrix.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 &lt;title&gt;. </p><p>\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0440\u043c\u0443\u043b\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c:</p><p>&lt;title&gt; + \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435_\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 + (N=&lt;\u043a\u043e\u043b-\u0432\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432&gt;)</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_6),
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u0430",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_6),
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u0430",
                None,
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_corr_color_pallete_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430",
                None,
            )
        )
        self.comboBox_color_pal_corr.setItemText(
            0, QCoreApplication.translate("MainWindow", "Set1", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            1, QCoreApplication.translate("MainWindow", "Set2", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            2, QCoreApplication.translate("MainWindow", "Set3", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            3, QCoreApplication.translate("MainWindow", "Paired", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            4, QCoreApplication.translate("MainWindow", "Accent", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            5, QCoreApplication.translate("MainWindow", "Pastel1", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            6, QCoreApplication.translate("MainWindow", "Pastel2", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            7, QCoreApplication.translate("MainWindow", "Dark2", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            8, QCoreApplication.translate("MainWindow", "rocket", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            9, QCoreApplication.translate("MainWindow", "mako", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            10, QCoreApplication.translate("MainWindow", "flare", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            11, QCoreApplication.translate("MainWindow", "crest", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            12, QCoreApplication.translate("MainWindow", "viridis", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            13, QCoreApplication.translate("MainWindow", "plasma", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            14, QCoreApplication.translate("MainWindow", "inferno", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            15, QCoreApplication.translate("MainWindow", "magma", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            16, QCoreApplication.translate("MainWindow", "cividis", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            17, QCoreApplication.translate("MainWindow", "Greys", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            18, QCoreApplication.translate("MainWindow", "Reds", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            19, QCoreApplication.translate("MainWindow", "Greens", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            20, QCoreApplication.translate("MainWindow", "Blues", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            21, QCoreApplication.translate("MainWindow", "Oranges", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            22, QCoreApplication.translate("MainWindow", "Purples", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            23, QCoreApplication.translate("MainWindow", "YlOrRd", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            24, QCoreApplication.translate("MainWindow", "tab10", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            25, QCoreApplication.translate("MainWindow", "deep", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            26, QCoreApplication.translate("MainWindow", "muted", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            27, QCoreApplication.translate("MainWindow", "pastel", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            28, QCoreApplication.translate("MainWindow", "bright", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            29, QCoreApplication.translate("MainWindow", "dark", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            30, QCoreApplication.translate("MainWindow", "colorblind", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            31, QCoreApplication.translate("MainWindow", "tab20", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            32, QCoreApplication.translate("MainWindow", "tab20b", None)
        )
        self.comboBox_color_pal_corr.setItemText(
            33, QCoreApplication.translate("MainWindow", "tab20c", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_color_pal_corr.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430 \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u0433\u0440\u0430\u0444\u0438\u043a\u0430.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_del_hue_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0438\u0436\u043d\u044e\u044e \u0433\u0440\u0430\u043d\u0438\u0446\u0443",
                None,
            )
        )
        self.check_change_corr_fig_down_limit.setText("")
        # if QT_CONFIG(whatsthis)
        self.doubleSpinBox_corr_figs.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '\u041d\u0438\u0436\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u0433\u0440\u0430\u0444\u0438\u043a\u0430. \u0418\u043d\u043e\u0433\u0434\u0430 \u043f\u043e\u043b\u0435\u0437\u043d\u043e, \u0435\u0441\u043b\u0438 \u043d\u0443\u0436\u043d\u043e \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0447\u0435\u0442\u043a\u043e "0" \u0438\u043b\u0438 \u0434\u0440\u0443\u0433\u043e\u0435 \u0447\u0438\u0441\u043b\u043e.',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_del_hue_3.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u0430\u043b\u0435\u043a\u043e \u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440. </p><p>\u041c\u043e\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0442\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u043d\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_del_hue_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0438\u0437 \u0433\u0440\u0443\u043f\u043f\u044b",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.del_hue.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_del_hue_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_points_corrFIGS.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u0433\u0440\u0430\u0444\u0438\u043a\u0430.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_12.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.doubleSpinBox_corr_figs_fontscale.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0434\u043b\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.check_sort_or_not_corr_figs.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0411\u0435\u0437 \u0444\u043b\u0430\u0436\u043a\u0430 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0431\u0443\u0434\u0435\u0442 \u0442\u0430\u043a\u0438\u043c, \u043a\u0430\u043a\u043e\u0439 \u043e\u043d \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_sort_or_not_corr_figs.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0433\u0440\u0443\u043f\u043f\u0435?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_sort_or_not_corr_figs.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0433\u0440\u0443\u043f\u043f\u0435",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.check_setka.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_setka.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0441\u0435\u0442\u043a\u0443?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_setka.setText(
            QCoreApplication.translate("MainWindow", "\u0421\u0435\u0442\u043a\u0430", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a",
                None,
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0435 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_pairplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041d\u0435 \u0443\u0447\u0438\u0442\u0432\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443 \u0432 \u043c\u0430\u0442\u0440\u0438\u0446\u0435 \u0440\u0430\u0441\u0441\u0435\u044f\u043d\u0438\u044f? </p><p>\u0412 \u044d\u0442\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435 \u0432\u0441\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0431\u0443\u0434\u0443\u0442 \u043e\u0431\u044a\u0435\u0434\u0435\u043d\u0435\u043d\u044b.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_pairplot.setText("")
        self.lb_color_pal_box_24.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430",
                None,
            )
        )
        self.lb_color_pal_box_25.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430",
                None,
            )
        )
        self.comboBox_color_pairplot.setItemText(
            0, QCoreApplication.translate("MainWindow", "Set1", None)
        )
        self.comboBox_color_pairplot.setItemText(
            1, QCoreApplication.translate("MainWindow", "Set2", None)
        )
        self.comboBox_color_pairplot.setItemText(
            2, QCoreApplication.translate("MainWindow", "Set3", None)
        )
        self.comboBox_color_pairplot.setItemText(
            3, QCoreApplication.translate("MainWindow", "Pastel1", None)
        )
        self.comboBox_color_pairplot.setItemText(
            4, QCoreApplication.translate("MainWindow", "Pastel2", None)
        )
        self.comboBox_color_pairplot.setItemText(
            5, QCoreApplication.translate("MainWindow", "Paired", None)
        )
        self.comboBox_color_pairplot.setItemText(
            6, QCoreApplication.translate("MainWindow", "Accent", None)
        )
        self.comboBox_color_pairplot.setItemText(
            7, QCoreApplication.translate("MainWindow", "Dark2", None)
        )
        self.comboBox_color_pairplot.setItemText(
            8, QCoreApplication.translate("MainWindow", "rocket", None)
        )
        self.comboBox_color_pairplot.setItemText(
            9, QCoreApplication.translate("MainWindow", "mako", None)
        )
        self.comboBox_color_pairplot.setItemText(
            10, QCoreApplication.translate("MainWindow", "flare", None)
        )
        self.comboBox_color_pairplot.setItemText(
            11, QCoreApplication.translate("MainWindow", "crest", None)
        )
        self.comboBox_color_pairplot.setItemText(
            12, QCoreApplication.translate("MainWindow", "viridis", None)
        )
        self.comboBox_color_pairplot.setItemText(
            13, QCoreApplication.translate("MainWindow", "plasma", None)
        )
        self.comboBox_color_pairplot.setItemText(
            14, QCoreApplication.translate("MainWindow", "inferno", None)
        )
        self.comboBox_color_pairplot.setItemText(
            15, QCoreApplication.translate("MainWindow", "magma", None)
        )
        self.comboBox_color_pairplot.setItemText(
            16, QCoreApplication.translate("MainWindow", "cividis", None)
        )
        self.comboBox_color_pairplot.setItemText(
            17, QCoreApplication.translate("MainWindow", "Greys", None)
        )
        self.comboBox_color_pairplot.setItemText(
            18, QCoreApplication.translate("MainWindow", "Reds", None)
        )
        self.comboBox_color_pairplot.setItemText(
            19, QCoreApplication.translate("MainWindow", "Greens", None)
        )
        self.comboBox_color_pairplot.setItemText(
            20, QCoreApplication.translate("MainWindow", "Blues", None)
        )
        self.comboBox_color_pairplot.setItemText(
            21, QCoreApplication.translate("MainWindow", "Oranges", None)
        )
        self.comboBox_color_pairplot.setItemText(
            22, QCoreApplication.translate("MainWindow", "Purples", None)
        )
        self.comboBox_color_pairplot.setItemText(
            23, QCoreApplication.translate("MainWindow", "YlOrRd", None)
        )
        self.comboBox_color_pairplot.setItemText(
            24, QCoreApplication.translate("MainWindow", "tab10", None)
        )
        self.comboBox_color_pairplot.setItemText(
            25, QCoreApplication.translate("MainWindow", "deep", None)
        )
        self.comboBox_color_pairplot.setItemText(
            26, QCoreApplication.translate("MainWindow", "muted", None)
        )
        self.comboBox_color_pairplot.setItemText(
            27, QCoreApplication.translate("MainWindow", "pastel", None)
        )
        self.comboBox_color_pairplot.setItemText(
            28, QCoreApplication.translate("MainWindow", "bright", None)
        )
        self.comboBox_color_pairplot.setItemText(
            29, QCoreApplication.translate("MainWindow", "dark", None)
        )
        self.comboBox_color_pairplot.setItemText(
            30, QCoreApplication.translate("MainWindow", "colorblind", None)
        )
        self.comboBox_color_pairplot.setItemText(
            31, QCoreApplication.translate("MainWindow", "tab20", None)
        )
        self.comboBox_color_pairplot.setItemText(
            32, QCoreApplication.translate("MainWindow", "tab20b", None)
        )
        self.comboBox_color_pairplot.setItemText(
            33, QCoreApplication.translate("MainWindow", "tab20c", None)
        )

        # if QT_CONFIG(tooltip)
        self.lb_color_pal_box_28.setToolTip(
            QCoreApplication.translate("MainWindow", "\u0441\u043c. seaborn.pairplot", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_color_pal_box_28.setText(QCoreApplication.translate("MainWindow", "kind", None))
        self.comboBox_pairplot_kind.setItemText(
            0, QCoreApplication.translate("MainWindow", "scatter", None)
        )
        self.comboBox_pairplot_kind.setItemText(
            1, QCoreApplication.translate("MainWindow", "reg", None)
        )
        self.comboBox_pairplot_kind.setItemText(
            2, QCoreApplication.translate("MainWindow", "kde", None)
        )
        self.comboBox_pairplot_kind.setItemText(
            3, QCoreApplication.translate("MainWindow", "hist", None)
        )

        self.lb_color_pal_box_27.setText(
            QCoreApplication.translate("MainWindow", "\u0421\u0442\u0438\u043b\u044c", None)
        )
        self.comboBox_style_pairplot.setItemText(
            0, QCoreApplication.translate("MainWindow", "white", None)
        )
        self.comboBox_style_pairplot.setItemText(
            1, QCoreApplication.translate("MainWindow", "dark", None)
        )
        self.comboBox_style_pairplot.setItemText(
            2, QCoreApplication.translate("MainWindow", "whitegrid", None)
        )
        self.comboBox_style_pairplot.setItemText(
            3, QCoreApplication.translate("MainWindow", "darkgrid", None)
        )
        self.comboBox_style_pairplot.setItemText(
            4, QCoreApplication.translate("MainWindow", "ticks", None)
        )

        self.lb_color_pal_box_26.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_11),
            QCoreApplication.translate(
                "MainWindow",
                "\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0440\u0430\u0441\u0441\u0435\u044f\u043d\u0438\u044f",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_11),
            QCoreApplication.translate(
                "MainWindow",
                "\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0440\u0430\u0441\u0441\u0435\u044f\u043d\u0438\u044f",
                None,
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_color_pal_box_29.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430",
                None,
            )
        )
        self.lb_color_pal_box_30.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430",
                None,
            )
        )
        self.comboBox_color_jointplot.setItemText(
            0, QCoreApplication.translate("MainWindow", "Set1", None)
        )
        self.comboBox_color_jointplot.setItemText(
            1, QCoreApplication.translate("MainWindow", "Set2", None)
        )
        self.comboBox_color_jointplot.setItemText(
            2, QCoreApplication.translate("MainWindow", "Set3", None)
        )
        self.comboBox_color_jointplot.setItemText(
            3, QCoreApplication.translate("MainWindow", "Pastel1", None)
        )
        self.comboBox_color_jointplot.setItemText(
            4, QCoreApplication.translate("MainWindow", "Pastel2", None)
        )
        self.comboBox_color_jointplot.setItemText(
            5, QCoreApplication.translate("MainWindow", "Paired", None)
        )
        self.comboBox_color_jointplot.setItemText(
            6, QCoreApplication.translate("MainWindow", "Accent", None)
        )
        self.comboBox_color_jointplot.setItemText(
            7, QCoreApplication.translate("MainWindow", "Dark2", None)
        )
        self.comboBox_color_jointplot.setItemText(
            8, QCoreApplication.translate("MainWindow", "rocket", None)
        )
        self.comboBox_color_jointplot.setItemText(
            9, QCoreApplication.translate("MainWindow", "mako", None)
        )
        self.comboBox_color_jointplot.setItemText(
            10, QCoreApplication.translate("MainWindow", "flare", None)
        )
        self.comboBox_color_jointplot.setItemText(
            11, QCoreApplication.translate("MainWindow", "crest", None)
        )
        self.comboBox_color_jointplot.setItemText(
            12, QCoreApplication.translate("MainWindow", "viridis", None)
        )
        self.comboBox_color_jointplot.setItemText(
            13, QCoreApplication.translate("MainWindow", "plasma", None)
        )
        self.comboBox_color_jointplot.setItemText(
            14, QCoreApplication.translate("MainWindow", "inferno", None)
        )
        self.comboBox_color_jointplot.setItemText(
            15, QCoreApplication.translate("MainWindow", "magma", None)
        )
        self.comboBox_color_jointplot.setItemText(
            16, QCoreApplication.translate("MainWindow", "cividis", None)
        )
        self.comboBox_color_jointplot.setItemText(
            17, QCoreApplication.translate("MainWindow", "Greys", None)
        )
        self.comboBox_color_jointplot.setItemText(
            18, QCoreApplication.translate("MainWindow", "Reds", None)
        )
        self.comboBox_color_jointplot.setItemText(
            19, QCoreApplication.translate("MainWindow", "Greens", None)
        )
        self.comboBox_color_jointplot.setItemText(
            20, QCoreApplication.translate("MainWindow", "Blues", None)
        )
        self.comboBox_color_jointplot.setItemText(
            21, QCoreApplication.translate("MainWindow", "Oranges", None)
        )
        self.comboBox_color_jointplot.setItemText(
            22, QCoreApplication.translate("MainWindow", "Purples", None)
        )
        self.comboBox_color_jointplot.setItemText(
            23, QCoreApplication.translate("MainWindow", "YlOrRd", None)
        )
        self.comboBox_color_jointplot.setItemText(
            24, QCoreApplication.translate("MainWindow", "tab10", None)
        )
        self.comboBox_color_jointplot.setItemText(
            25, QCoreApplication.translate("MainWindow", "deep", None)
        )
        self.comboBox_color_jointplot.setItemText(
            26, QCoreApplication.translate("MainWindow", "muted", None)
        )
        self.comboBox_color_jointplot.setItemText(
            27, QCoreApplication.translate("MainWindow", "pastel", None)
        )
        self.comboBox_color_jointplot.setItemText(
            28, QCoreApplication.translate("MainWindow", "bright", None)
        )
        self.comboBox_color_jointplot.setItemText(
            29, QCoreApplication.translate("MainWindow", "dark", None)
        )
        self.comboBox_color_jointplot.setItemText(
            30, QCoreApplication.translate("MainWindow", "colorblind", None)
        )
        self.comboBox_color_jointplot.setItemText(
            31, QCoreApplication.translate("MainWindow", "tab20", None)
        )
        self.comboBox_color_jointplot.setItemText(
            32, QCoreApplication.translate("MainWindow", "tab20b", None)
        )
        self.comboBox_color_jointplot.setItemText(
            33, QCoreApplication.translate("MainWindow", "tab20c", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_color_jointplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430 \u0434\u043b\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043f\u043e \u0434\u0432\u0443\u043c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_color_pal_box_32.setToolTip(
            QCoreApplication.translate("MainWindow", "\u0441\u043c. seaborn.pairplot", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_color_pal_box_32.setText(QCoreApplication.translate("MainWindow", "kind", None))
        self.comboBox_pairplot_jointplot.setItemText(
            0, QCoreApplication.translate("MainWindow", "scatter", None)
        )
        self.comboBox_pairplot_jointplot.setItemText(
            1, QCoreApplication.translate("MainWindow", "kde", None)
        )
        self.comboBox_pairplot_jointplot.setItemText(
            2, QCoreApplication.translate("MainWindow", "hist", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_pairplot_jointplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044e \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0439.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_33.setText(
            QCoreApplication.translate("MainWindow", "\u0421\u0442\u0438\u043b\u044c", None)
        )
        self.comboBox_style_jointplot.setItemText(
            0, QCoreApplication.translate("MainWindow", "white", None)
        )
        self.comboBox_style_jointplot.setItemText(
            1, QCoreApplication.translate("MainWindow", "dark", None)
        )
        self.comboBox_style_jointplot.setItemText(
            2, QCoreApplication.translate("MainWindow", "whitegrid", None)
        )
        self.comboBox_style_jointplot.setItemText(
            3, QCoreApplication.translate("MainWindow", "darkgrid", None)
        )
        self.comboBox_style_jointplot.setItemText(
            4, QCoreApplication.translate("MainWindow", "ticks", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_style_jointplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0430. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0441\u0442\u0438\u043b\u0438 seaborn.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_31.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_point_size_for_jointplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u043e\u0447\u0435\u043a \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_13),
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043f\u043e \u0434\u0432\u0443\u043c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_13),
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043f\u043e \u0434\u0432\u0443\u043c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c",
                None,
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_sd_or_minmax_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043f\u043e",
                None,
            )
        )
        self.comboBox_correlation_one_parameter.setItemText(
            0, QCoreApplication.translate("MainWindow", "pearson", None)
        )
        self.comboBox_correlation_one_parameter.setItemText(
            1, QCoreApplication.translate("MainWindow", "kendall", None)
        )
        self.comboBox_correlation_one_parameter.setItemText(
            2, QCoreApplication.translate("MainWindow", "spearman", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_correlation_one_parameter.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041c\u0435\u0442\u043e\u0434 \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0439: \u041f\u0438\u0440\u0441\u043e\u043d, \u0421\u043f\u0438\u0440\u043c\u0435\u043d \u0438\u043b\u0438 \u041a\u0435\u043d\u0434\u0430\u043b.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_34.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.doubleSpinBox_size_for_one_correlation.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0438 \u043e\u0434\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_35.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0423\u0447\u0438\u0442\u044b\u0432\u0430\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0438, \u0433\u0434\u0435 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0438 \u0431\u043e\u043b\u044c\u0448\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.doubleSpinBox_one_correlation.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u0441\u0435\u0447\u043a\u0430 \u043f\u043e \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f\u043c. \u0412\u0441\u0435 \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0438\u0436\u0435 \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0447\u0438\u0441\u043b\u0430, \u043d\u0435 \u0431\u0443\u0434\u0443\u0442 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0442\u044c\u0441\u044f.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_corr_one_parameter_only_one.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0443 \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_corr_one_parameter_plot_sep_wind.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a \u0432 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u043c \u043e\u043a\u043d\u0435?</p><p>\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435, \u0442\u043e\u043b\u044c\u043a\u043e \u0435\u0441\u043b\u0438 \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0435\u0442\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043d\u0435 \u0447\u0435\u0440\u0435\u0437 \u0434\u0435\u0441\u043a\u0442\u043e\u043f\u043d\u0443\u044e \u0432\u0435\u0440\u0441\u0438\u044e.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_corr_one_parameter_plot_sep_wind.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a \u0432 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u043c \u043e\u043a\u043d\u0435",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_14),
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043e\u0434\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_14),
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043e\u0434\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430",
                None,
            ),
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.btn_plot_and_save_figs.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0432\u0441\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0445 \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u043f\u0430\u043f\u043a\u0430\u0445",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_plot_and_save_figs.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438",
                None,
            )
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab),
            QCoreApplication.translate(
                "MainWindow", "\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None
            ),
        )
        self.lb_path_for_profile.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.path_for_profile.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435, \u0432 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0431\u0443\u0434\u0443\u0442 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u044b \u043c\u0438\u043a\u0440\u043e\u0440\u0435\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u0440\u043e\u0444\u0438\u043b\u0438.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_profile.setText("")
        # if QT_CONFIG(tooltip)
        self.lb_patient_data.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0438\u0437 excel \u0442\u0430\u0431\u043b\u0438\u0446\u044b, \u0433\u0434\u0435 \u0435\u0441\u0442\u044c 3 \u0441\u0442\u043e\u043b\u0431\u0446\u0430: \u0438\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430, \u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c. \u0412\u0441\u0435 \u044f\u0447\u0435\u0439\u043a\u0438 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u043d\u0435 \u043f\u0443\u0441\u0442\u044b\u043c\u0438.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_patient_data.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.patient_data.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430.</p><p>\u0414\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0438\u0437 excel \u0438 \u0432\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u044b \u0432 \u0434\u0430\u043d\u043d\u0443\u044e \u044f\u0447\u0435\u0439\u043a\u0443.</p><p>\u0414\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u043e 3 \u0441\u0442\u043e\u043b\u0431\u0446\u0430, \u043a \u043f\u0440\u0438\u043c\u0435\u0440\u0443:</p><p><br/></p><table border="0" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; border-collapse:collapse;" cellspacing="2" cellpadding="0"><thead><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-style:solid;"><p><span style=" font-fa'
                "mily:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">\u0421\u0440\u0435\u0434\u043d\u0435\u0435</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Rob"
                "oto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">SD</span></p></td></tr></thead><tr><td style=\" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">CSS, \u043c\u041f\u0430</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">300</span></p></td><td style=\" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1p"
                "x; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">15</span></p></td></tr><tr><td style=\" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">AI, %</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0"
                "f1115;\">62</span></p></td><td style=\" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">5</span></p></td></tr><tr><td style=\" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">AMP</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemF"
                "ont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">0,06</span></p></td><td style=\" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">0.01</span></p></td></tr></table><p><br/></p><p><span style=\" font-family:'Helvetica';\">\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043e\u043b\u0436\u043d\u044b \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u043d\u0430\u0437\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e \u0434\u043b\u044f \u043d\u043e\u0440\u043c\u044b \u0438 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430.</span></p><p><span style=\" font-family:'"
                "Helvetica';\">\u041d\u0430\u0437\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043c\u043e\u0433\u0443\u0442 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u043e. Latex \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442\u0441\u044f.</span></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.patient_data.setText("")
        # if QT_CONFIG(tooltip)
        self.lb_norm_data.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0438\u0437 excel \u0442\u0430\u0431\u043b\u0438\u0446\u044b, \u0433\u0434\u0435 \u0435\u0441\u0442\u044c 3 \u0441\u0442\u043e\u043b\u0431\u0446\u0430: \u0438\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430, \u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c. \u0412\u0441\u0435 \u044f\u0447\u0435\u0439\u043a\u0438 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u043d\u0435 \u043f\u0443\u0441\u0442\u044b\u043c\u0438.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_norm_data.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0430\u043d\u043d\u044b\u0435 \u043d\u043e\u0440\u043c\u044b",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.norm_data.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u043d\u043e\u0440\u043c\u044b.</p><p>\u0414\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0438\u0437 excel \u0438 \u0432\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u044b \u0432 \u0434\u0430\u043d\u043d\u0443\u044e \u044f\u0447\u0435\u0439\u043a\u0443.</p><p>\u0414\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0441\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u043e 3 \u0441\u0442\u043e\u043b\u0431\u0446\u0430, \u043a \u043f\u0440\u0438\u043c\u0435\u0440\u0443:</p><p><br/></p><table border="0" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; border-collapse:collapse;" cellspacing="2" cellpadding="0"><thead><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style'
                "=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">\u0421\u0440\u0435\u0434\u043d\u0435\u0435</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','In"
                "ter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">SD</span></p></td></tr></thead><tr><td style=\" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">CSS, \u043c\u041f\u0430</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#"
                "0f1115;\">300</span></p></td><td style=\" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">15</span></p></td></tr><tr><td style=\" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">AI, %</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span"
                " style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">62</span></p></td><td style=\" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">5</span></p></td></tr><tr><td style=\" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:1"
                "6px; color:#0f1115;\">AMP</span></p></td><td style=\" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">0,06</span></p></td><td style=\" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;\"><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;\">0.01</span></p></td></tr></table><p><br/></p><p><span style=\" font-family:'Helvetica';\">\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043e\u043b\u0436\u043d\u044b \u043e"
                "\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u043d\u0430\u0437\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e \u0434\u043b\u044f \u043d\u043e\u0440\u043c\u044b \u0438 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430.</span></p><p><span style=\" font-family:'Helvetica';\">\u041d\u0430\u0437\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043c\u043e\u0433\u0443\u0442 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u043e. Latex \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442\u0441\u044f.</span></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.norm_data.setText("")
        self.lb_norm_data_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.profile_title_rad.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.profile_title_rad.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041c\u0438\u043a\u0440\u043e\u0440\u0435\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430 ",
                None,
            )
        )
        self.lb_norm_data_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043e\u0441\u0438 \u0434\u043b\u044f \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.profile_title_lin.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043e\u0441\u0438 \u0434\u043b\u044f \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.profile_title_lin.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 \u043e\u0442 \u043d\u043e\u0440\u043c\u044b, %",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.check_profile_legend.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u043d\u043e\u0433\u0434\u0430 \u043b\u0443\u0447\u0448\u0435 \u043e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c, \u0447\u0442\u043e\u0431\u044b \u043e\u043d\u0430 \u043d\u0435 \u043d\u0430\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u043b\u0430\u0441\u044c \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_profile_legend.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043b\u0435\u0433\u0435\u043d\u0434\u0443?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_profile_legend.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041b\u0435\u0433\u0435\u043d\u0434\u0430", None
            )
        )
        self.lb__altern_heposisis_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u0440\u0430\u0449\u0430\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u0434\u043b\u044f \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f",
                None,
            )
        )
        self.comboBox_profile_lin_spin.setItemText(
            0, QCoreApplication.translate("MainWindow", "90", None)
        )
        self.comboBox_profile_lin_spin.setItemText(
            1, QCoreApplication.translate("MainWindow", "0", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_profile_lin_spin.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u0440\u0430\u0449\u0430\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u0434\u043b\u044f \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_20.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.doubleSpinBoX_profile.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0445.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u043c\u044f \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_4.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0446\u0432\u0435\u0442 \u0431\u044b\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX (\u043f\u0440\u0438\u043c\u0435\u0440, &quot;#FFFFFF&quot;)</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430 (HEX)",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.patient_prof.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u043c\u044f \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430/\u043e\u0431\u0440\u0430\u0437\u0446\u0430.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.patient_prof.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041f\u0430\u0446\u0438\u0435\u043d\u0442", None
            )
        )
        # if QT_CONFIG(whatsthis)
        self.color_for_patient.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0446\u0432\u0435\u0442\u0430 HEX.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.color_for_patient.setText(QCoreApplication.translate("MainWindow", "#DB4900", None))
        # if QT_CONFIG(whatsthis)
        self.check_profile_pat_line.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0430\u0446\u0438\u0435\u043d\u0442 -- \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u0438\u043d\u0438\u044e \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_profile_pat_line.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041b\u0438\u043d\u0438\u044f \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_profile_pat_sd.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0430\u0446\u0438\u0435\u043d\u0442 -- \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u0441 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u043c \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435\u043c \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_profile_pat_sd.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435",
                None,
            )
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u043c\u044f \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u044b",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.label_7.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u0446\u0432\u0435\u0442 \u0431\u044b\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 HEX (\u043f\u0440\u0438\u043c\u0435\u0440, &quot;#FFFFFF&quot;)</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u043e\u0440\u043c\u044b (HEX)",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.norm_prof.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u043c\u044f \u0434\u043b\u044f \u043d\u043e\u0440\u043c\u044b.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.norm_prof.setText(
            QCoreApplication.translate("MainWindow", "\u041d\u043e\u0440\u043c\u0430", None)
        )
        # if QT_CONFIG(whatsthis)
        self.color_for_norm.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u043e\u0440\u043c\u044b. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0446\u0432\u0435\u0442\u0430 HEX.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.color_for_norm.setText(QCoreApplication.translate("MainWindow", "#2A968D", None))
        # if QT_CONFIG(whatsthis)
        self.check_profile_norm_line.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u043e\u0440\u043c\u0430 -- \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u0438\u043d\u0438\u044e \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_profile_norm_line.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041b\u0438\u043d\u0438\u044f \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_profile_norm_sd.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u043e\u0440\u043c\u0430 -- \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u0441 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u043c \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435\u043c \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_profile_norm_sd.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.btn_plot_and_save_profile.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0438 \u043b\u0438\u043d\u0435\u0439\u043d\u044b\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u0438.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_plot_and_save_profile.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0440\u043e\u0444\u0438\u043b\u0438",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.check_profile_relative.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0415\u0441\u043b\u0438 \u043e\u0442\u043b\u0438\u0447\u0438\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435, \u0442\u043e \u043d\u0430 \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u043c \u0433\u0440\u0430\u0444\u0438\u043a\u0435 \u0431\u0443\u0434\u0435\u0442 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u043e\u0442\u043b\u0438\u0447\u0438\u044f \u0432 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430\u0445 \u043e\u0442 \u043d\u043e\u0440\u043c\u044b; \u0432 \u043f\u0440\u043e\u0442\u0438\u0432\u043d\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435, \u0437\u0430 100% \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442\u0441\u044f \u043d\u043e\u0440\u043c\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.check_profile_relative.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0440\u0430\u0437\u043b\u0438\u0447\u0438\u0439 \u043d\u0430 \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u043c \u0433\u0440\u0430\u0444\u0438\u043a\u0435?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_profile_relative.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043e\u0442\u043b\u0438\u0447\u0438\u044f \u043d\u0430 \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u043c \u0433\u0440\u0430\u0444\u0438\u043a\u0435",
                None,
            )
        )
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "1 \u0433\u0440\u0443\u043f\u043f\u0430", None)
        )
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "2 \u0433\u0440\u0443\u043f\u043f\u0430", None)
        )
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "3 \u0433\u0440\u0443\u043f\u043f\u0430", None)
        )
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432",
                None,
            )
        )
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041f\u043e\u0434\u043f\u0438\u0441\u044c", None
            )
        )
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", "\u0426\u0432\u0435\u0442\u0430", None)
        )
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0421\u0442\u0438\u043b\u044c \u043b\u0438\u043d\u0438\u0438", None
            )
        )
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0410\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u044f \u044d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u043e\u0432",
                None,
            )
        )
        ___qtablewidgetitem8 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0435\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u043c\u043e\u0441\u0442\u044c \u044d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u043e\u0432",
                None,
            )
        )
        ___qtablewidgetitem9 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0410\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u044f \u0442\u0440\u043e\u043c\u0431\u043e\u0446\u0438\u0442\u043e\u0432",
                None,
            )
        )
        ___qtablewidgetitem10 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", "red", None))
        ___qtablewidgetitem11 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", "green", None))
        ___qtablewidgetitem12 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", "blue", None))
        ___qtablewidgetitem13 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", "solid", None))
        ___qtablewidgetitem14 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", "solid", None))
        ___qtablewidgetitem15 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", "solid", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        # if QT_CONFIG(whatsthis)
        self.tableWidget.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0443\u0436\u043d\u043e \u043f\u0438\u0441\u0430\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u0442\u0438\u0440\u0435. \u0418\u043d\u0434\u0435\u043a\u0441 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u0441 \u043d\u0443\u043b\u044f, \u0430 \u043d\u0435 \u0435\u0434\u0438\u043d\u0438\u0446\u044b.</p><p><span style=" font-style:italic;">\u041f\u0440\u0438\u043c\u0435\u0440</span>: \u0435\u0441\u043b\u0438 \u0432\u0441\u0435\u0433\u043e 8 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432, \u0442\u043e \u043c\u043e\u0436\u043d\u043e \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0442\u0430\u043a:</p><p>(1 \u0433\u0440\u0443\u043f\u043f\u0430) &quot;0-3&quot;</p><p>(2 \u0433\u0440\u0443\u043f\u043f\u0430) &quot;4-5&quot;</p><p>(3 \u0433\u0440\u0443\u043f\u043f\u0430) &quot;6-7&quot;</p><p>\u0426\u0432\u0435\u0442\u0430: matplotlib.colors</p><p>\u0421\u0442'
                "\u0438\u043b\u044c \u043b\u0438\u043d\u0438\u0438: \u0441\u043c. matplotlib </p><p><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#7a7e85;\">solid, dashed, dashdot, dotted</span><br/></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_norm_data_4.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0443\u0436\u043d\u043e \u043f\u0438\u0441\u0430\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u0442\u0438\u0440\u0435.</p><p>\u041f\u0440\u0438\u043c\u0435\u0440: 0-3</p><p>\u0426\u0432\u0435\u0442\u0430: matplotlib.colors</p><p>\u0421\u0442\u0438\u043b\u044c \u043b\u0438\u043d\u0438\u0438: \u0441\u043c. matplotlib </p><p><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#000000;\">solid, dashed, dashdot, dotted</span></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lb_norm_data_4.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.lb_norm_data_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0434\u043b\u044f \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u043d\u044b\u0445 \u0433\u0440\u0443\u043f\u043f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0430 \u0440\u0430\u0434\u0438\u0430\u043b\u044c\u043d\u043e\u043c \u0433\u0440\u0430\u0444\u0438\u043a\u0435",
                None,
            )
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.widget2),
            QCoreApplication.translate(
                "MainWindow",
                "\u041c\u0438\u043a\u0440\u043e\u0440\u0435\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_2.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.path_for_pivot_table.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435, \u0433\u0434\u0435 \u043b\u0435\u0436\u0438\u0442(\u0430\u0442) excel \u0444\u0430\u0439\u043b(\u044b) \u0434\u043b\u044f \u0441\u0432\u043e\u0434\u043d\u044b\u0445 \u0442\u0430\u0431\u043b\u0438\u0446.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_pivot_table.setText("")
        self.lb_exel_name_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_pivot_table.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_exel_name_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_pivot_table_excel_sheet.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 excel \u0444\u0430\u0439\u043b\u0435 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_2.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u043c\u0435\u043d\u043d\u043e \u043f\u043e\u0441\u043b\u0435 \u044d\u0442\u043e\u0433\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043e\u043b\u0436\u043d\u044b \u0438\u0434\u0442\u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_pivot_hue.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u0442\u043e\u043b\u0431\u0435\u0446 \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f. \u042d\u0442\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, "\u041f\u043e\u043b".',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_17.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_color_pal_box_8.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u043a\u0440\u0443\u0433\u043b\u044f\u044e\u0442\u0441\u044f \u0432\u0441\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lb_color_pal_box_8.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u043a\u0440\u0443\u0433\u043b\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0434\u043e \u0437\u043d\u0430\u043a\u0430 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_pivot_table.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u043a\u0440\u0443\u0433\u043b\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0434\u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u043a\u0430 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_sd_or_minmax_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439",
                None,
            )
        )
        self.comboBox_sd_or_se_pivot.setItemText(
            0, QCoreApplication.translate("MainWindow", "SD", None)
        )
        self.comboBox_sd_or_se_pivot.setItemText(
            1, QCoreApplication.translate("MainWindow", "SE", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_sd_or_se_pivot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u044c SD \u0438\u043b\u0438 SE.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.btn_plot_and_save_pivot_table.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0432\u043e\u0434\u043d\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_plot_and_save_pivot_table.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0432\u043e\u0434\u043d\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443",
                None,
            )
        )
        self.lb_color_pal_box_18.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u0430",
                None,
            )
        )
        self.lb_sd_or_minmax_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u043f\u043e",
                None,
            )
        )
        self.comboBox_correlation_person_or_not.setItemText(
            0, QCoreApplication.translate("MainWindow", "pearson", None)
        )
        self.comboBox_correlation_person_or_not.setItemText(
            1, QCoreApplication.translate("MainWindow", "kendall", None)
        )
        self.comboBox_correlation_person_or_not.setItemText(
            2, QCoreApplication.translate("MainWindow", "spearman", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_correlation_person_or_not.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041c\u0435\u0442\u043e\u0434 \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0439: \u041f\u0438\u0440\u0441\u043e\u043d, \u0421\u043f\u0438\u0440\u043c\u0435\u043d \u0438\u043b\u0438 \u041a\u0435\u043d\u0434\u0430\u043b.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_sd_or_minmax_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u044f\u0447\u0435\u0439\u043a\u0438 \u0446\u0432\u0435\u0442\u043e\u043c",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_color_for_corr_pivot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u044f\u0447\u0435\u0439\u043a\u0438 \u0446\u0432\u0435\u0442\u043e\u043c?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_color_for_corr_pivot.setText("")
        self.lb_sd_or_minmax_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u0441\u0445\u0435\u043c\u0430",
                None,
            )
        )
        self.comboBox_correlation_color_map.setItemText(
            0, QCoreApplication.translate("MainWindow", "coolwarm", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            1, QCoreApplication.translate("MainWindow", "RdBu_r", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            2, QCoreApplication.translate("MainWindow", "YlGn", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            3, QCoreApplication.translate("MainWindow", "BuGn", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            4, QCoreApplication.translate("MainWindow", "GnBu", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            5, QCoreApplication.translate("MainWindow", "bwr", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            6, QCoreApplication.translate("MainWindow", "seismic", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            7, QCoreApplication.translate("MainWindow", "PiYG", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            8, QCoreApplication.translate("MainWindow", "RdGy", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            9, QCoreApplication.translate("MainWindow", "seismic", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            10, QCoreApplication.translate("MainWindow", "hot", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            11, QCoreApplication.translate("MainWindow", "inferno", None)
        )
        self.comboBox_correlation_color_map.setItemText(
            12, QCoreApplication.translate("MainWindow", "gist_heat", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_correlation_color_map.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u0441\u0445\u0435\u043c\u0430 \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u044b?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.btn_plot_and_save_corr_table.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0443\u044e \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u043f\u043e \u0432\u0441\u0435\u043c \u0434\u0430\u043d\u043d\u044b\u043c.</p><p>\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0432\u0441\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_plot_and_save_corr_table.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u0443\u044e \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u043f\u043e \u0432\u0441\u0435\u043c \u0434\u0430\u043d\u043d\u044b\u043c",
                None,
            )
        )
        self.lb_color_pal_box_22.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u0438\u043d\u0434\u0435\u043a\u0441\u0438\u0440\u0443\u0435\u043c\u044b\u0435/\u043f\u043e \u0441\u0442\u043e\u043b\u0431\u0446\u0430\u043c",
                None,
            )
        )
        self.lb_sd_or_minmax_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435",
                None,
            )
        )
        self.comboBox_index_data_or_raw.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow",
                "\u0438\u0437 \u0438\u043d\u0434\u0435\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u0441\u044b\u0440\u044b\u0435",
                None,
            ),
        )
        self.comboBox_index_data_or_raw.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\u0438\u0437 \u0441\u044b\u0440\u044b\u0445 \u0432 \u0438\u043d\u0434\u0435\u043a\u0441\u0438\u0440\u0443\u0435\u043c\u044b\u0435",
                None,
            ),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_index_data_or_raw.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0438\u0437 \u0448\u0438\u0440\u043e\u043a\u043e\u0433\u043e \u043a \u0434\u043b\u0438\u043d\u043d\u043e\u043c\u0443 \u0444\u043e\u0440\u043c\u0430\u0442\u0443 \u0438\u043b\u0438 \u043d\u0430\u043e\u0431\u043e\u0440\u043e\u0442.</p><p>\u041f\u043e\u0434 <span style=" font-style:italic;">\u0438\u043d\u0434\u0435\u043a\u0441\u0438\u0440\u0443\u0435\u043c\u044b\u043c\u0438</span> \u043f\u043e\u043b\u0430\u0433\u0430\u0435\u0442\u0441\u044f -- \u0434\u043b\u0438\u043d\u043d\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442.</p><p>\u041f\u043e\u0434 <span style=" font-style:italic;">\u0441\u044b\u0440\u044b\u043c</span> -- \u0448\u0438\u0440\u043e\u043a\u0438\u0439 \u0444\u043e\u0440\u043c\u0430\u0442.</p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.btn_save_pivot_or_melt.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0448\u0438\u0440\u043e\u043a\u043e\u0433\u043e \u0432 \u0434\u043b\u0438\u043d\u043d\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 \u0438\u043b\u0438 \u043d\u0430\u043e\u0431\u043e\u0440\u043e\u0442 \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_save_pivot_or_melt.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_8),
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_3.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.path_for_catplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 excel \u0444\u0430\u0439\u043b\u043e\u043c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_catplot.setText("")
        self.lb_exel_name_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_excel_catplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_exel_name_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 \u0444\u0430\u0439\u043b\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_excel_sheet_catplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 excel \u0444\u0430\u0439\u043b\u0435 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_3.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0413\u0440\u0443\u043f\u043f\u0430 \u043f\u043e \u043e\u0441\u0438 x",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_catplot_x.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u044b \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0433\u0440\u0443\u043f\u043f\u0430 &quot;\u0414\u0438\u0430\u0433\u043d\u043e\u0437&quot;.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_7.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_7.setText(
            QCoreApplication.translate("MainWindow", "\u0424\u043e\u0440\u043c\u0430\u0442", None)
        )
        self.comboBox_catplot_form_x.setItemText(
            0, QCoreApplication.translate("MainWindow", "str", None)
        )
        self.comboBox_catplot_form_x.setItemText(
            1, QCoreApplication.translate("MainWindow", "int", None)
        )
        self.comboBox_catplot_form_x.setItemText(
            2, QCoreApplication.translate("MainWindow", "float", None)
        )
        self.comboBox_catplot_form_x.setItemText(
            3, QCoreApplication.translate("MainWindow", "bool", None)
        )
        self.comboBox_catplot_form_x.setItemText(
            4, QCoreApplication.translate("MainWindow", "default", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_catplot_form_x.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u042f\u0432\u043d\u043e \u043f\u0440\u0438\u0432\u0435\u0441\u0442\u0438 \u0442\u0438\u043f \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f\u044b \u043f\u043e \u043e\u0441\u0438 X \u0432 \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u0439 \u0442\u0438\u043f.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_4.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u043e \u043e\u0441\u0438 y",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_catplot_y.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0422\u0430\u0440\u0433\u0435\u0442\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u0432\u044b\u0432\u043e\u0434\u0430 \u043d\u0430 \u043e\u0441\u044c Y.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, &quot;\u0421\u0438\u043b\u0430 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438&quot;. </p><p>\u041e\u0431\u044b\u0447\u043d\u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0443\u043c\u0435\u0432\u0430\u0435\u0442\u0441\u044f, \u0447\u0442\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0434\u0430\u043d\u043d\u043e\u043c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0435:</p><p>- float</p><p>- int</p><p>\u00a0\u0422\u043e \u0435\u0441\u0442\u044c \u043d\u0435\u043f\u0440\u0435\u0440\u044b\u0432\u043d\u044b\u0435 \u0438\u043b\u0438 \u0434\u0438\u0441\u043a\u0440\u0435\u0442\u043d\u044b\u0435.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_6.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_6.setText(
            QCoreApplication.translate("MainWindow", "\u0424\u043e\u0440\u043c\u0430\u0442", None)
        )
        self.comboBox_catplot_form_y.setItemText(
            0, QCoreApplication.translate("MainWindow", "float", None)
        )
        self.comboBox_catplot_form_y.setItemText(
            1, QCoreApplication.translate("MainWindow", "int", None)
        )
        self.comboBox_catplot_form_y.setItemText(
            2, QCoreApplication.translate("MainWindow", "str", None)
        )
        self.comboBox_catplot_form_y.setItemText(
            3, QCoreApplication.translate("MainWindow", "bool", None)
        )
        self.comboBox_catplot_form_y.setItemText(
            4, QCoreApplication.translate("MainWindow", "default", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_catplot_form_y.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u042f\u0432\u043d\u043e \u043f\u0440\u0438\u0432\u0435\u0441\u0442\u0438 \u0442\u0438\u043f \u0434\u043b\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043f\u043e \u043e\u0441\u0438 Y \u0432 \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u0439 \u0442\u0438\u043f.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_5.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e - \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_5.setText(
            QCoreApplication.translate(
                "MainWindow", "\u041f\u043e\u0434\u0433\u0440\u0443\u043f\u043f\u0430", None
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_catplot_hue.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u043e\u0434\u0433\u0440\u0443\u043f\u043f\u0430 \u0432 \u0433\u0440\u0443\u043f\u043f\u0435.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0433\u0440\u0443\u043f\u043f\u0430 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c &quot;\u0414\u0438\u0430\u0433\u043d\u043e\u0437&quot;, \u0430 \u043f\u043e\u0434\u0433\u0440\u0443\u043f\u043f\u0430 &quot;\u041f\u043e\u043b&quot;.</p><p>\u041d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435 \u0431\u0443\u0434\u0443\u0442 \u0432\u0441\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0435 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0438\u0437 \u0434\u0432\u0443\u0445 \u0433\u0440\u0443\u043f\u043f.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_8.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_8.setText(
            QCoreApplication.translate("MainWindow", "\u0424\u043e\u0440\u043c\u0430\u0442", None)
        )
        self.comboBox_catplot_form_hue.setItemText(
            0, QCoreApplication.translate("MainWindow", "str", None)
        )
        self.comboBox_catplot_form_hue.setItemText(
            1, QCoreApplication.translate("MainWindow", "int", None)
        )
        self.comboBox_catplot_form_hue.setItemText(
            2, QCoreApplication.translate("MainWindow", "float", None)
        )
        self.comboBox_catplot_form_hue.setItemText(
            3, QCoreApplication.translate("MainWindow", "bool", None)
        )
        self.comboBox_catplot_form_hue.setItemText(
            4, QCoreApplication.translate("MainWindow", "default", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_catplot_form_hue.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u042f\u0432\u043d\u043e \u043f\u0440\u0438\u0432\u0435\u0441\u0442\u0438 \u0442\u0438\u043f \u0434\u043b\u044f \u043f\u043e\u0434\u0433\u0440\u0443\u043f\u043f\u044b \u0432 \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u0439 \u0442\u0438\u043f.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_14.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.doubleSpinBox_catplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_color_pal_box_16.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430",
                None,
            )
        )
        self.comboBox_color_catplot.setItemText(
            0, QCoreApplication.translate("MainWindow", "Pastel1", None)
        )
        self.comboBox_color_catplot.setItemText(
            1, QCoreApplication.translate("MainWindow", "Pastel2", None)
        )
        self.comboBox_color_catplot.setItemText(
            2, QCoreApplication.translate("MainWindow", "Set1", None)
        )
        self.comboBox_color_catplot.setItemText(
            3, QCoreApplication.translate("MainWindow", "Set2", None)
        )
        self.comboBox_color_catplot.setItemText(
            4, QCoreApplication.translate("MainWindow", "Set3", None)
        )
        self.comboBox_color_catplot.setItemText(
            5, QCoreApplication.translate("MainWindow", "Paired", None)
        )
        self.comboBox_color_catplot.setItemText(
            6, QCoreApplication.translate("MainWindow", "Accent", None)
        )
        self.comboBox_color_catplot.setItemText(
            7, QCoreApplication.translate("MainWindow", "Dark2", None)
        )
        self.comboBox_color_catplot.setItemText(
            8, QCoreApplication.translate("MainWindow", "rocket", None)
        )
        self.comboBox_color_catplot.setItemText(
            9, QCoreApplication.translate("MainWindow", "mako", None)
        )
        self.comboBox_color_catplot.setItemText(
            10, QCoreApplication.translate("MainWindow", "flare", None)
        )
        self.comboBox_color_catplot.setItemText(
            11, QCoreApplication.translate("MainWindow", "crest", None)
        )
        self.comboBox_color_catplot.setItemText(
            12, QCoreApplication.translate("MainWindow", "viridis", None)
        )
        self.comboBox_color_catplot.setItemText(
            13, QCoreApplication.translate("MainWindow", "plasma", None)
        )
        self.comboBox_color_catplot.setItemText(
            14, QCoreApplication.translate("MainWindow", "inferno", None)
        )
        self.comboBox_color_catplot.setItemText(
            15, QCoreApplication.translate("MainWindow", "magma", None)
        )
        self.comboBox_color_catplot.setItemText(
            16, QCoreApplication.translate("MainWindow", "cividis", None)
        )
        self.comboBox_color_catplot.setItemText(
            17, QCoreApplication.translate("MainWindow", "Greys", None)
        )
        self.comboBox_color_catplot.setItemText(
            18, QCoreApplication.translate("MainWindow", "Reds", None)
        )
        self.comboBox_color_catplot.setItemText(
            19, QCoreApplication.translate("MainWindow", "Greens", None)
        )
        self.comboBox_color_catplot.setItemText(
            20, QCoreApplication.translate("MainWindow", "Blues", None)
        )
        self.comboBox_color_catplot.setItemText(
            21, QCoreApplication.translate("MainWindow", "Oranges", None)
        )
        self.comboBox_color_catplot.setItemText(
            22, QCoreApplication.translate("MainWindow", "Purples", None)
        )
        self.comboBox_color_catplot.setItemText(
            23, QCoreApplication.translate("MainWindow", "YlOrRd", None)
        )
        self.comboBox_color_catplot.setItemText(
            24, QCoreApplication.translate("MainWindow", "tab10", None)
        )
        self.comboBox_color_catplot.setItemText(
            25, QCoreApplication.translate("MainWindow", "deep", None)
        )
        self.comboBox_color_catplot.setItemText(
            26, QCoreApplication.translate("MainWindow", "muted", None)
        )
        self.comboBox_color_catplot.setItemText(
            27, QCoreApplication.translate("MainWindow", "pastel", None)
        )
        self.comboBox_color_catplot.setItemText(
            28, QCoreApplication.translate("MainWindow", "bright", None)
        )
        self.comboBox_color_catplot.setItemText(
            29, QCoreApplication.translate("MainWindow", "dark", None)
        )
        self.comboBox_color_catplot.setItemText(
            30, QCoreApplication.translate("MainWindow", "colorblind", None)
        )
        self.comboBox_color_catplot.setItemText(
            31, QCoreApplication.translate("MainWindow", "tab20", None)
        )
        self.comboBox_color_catplot.setItemText(
            32, QCoreApplication.translate("MainWindow", "tab20b", None)
        )
        self.comboBox_color_catplot.setItemText(
            33, QCoreApplication.translate("MainWindow", "tab20c", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_color_catplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043b\u0438\u0442\u0440\u0430 \u0434\u043b\u044f catplot.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_stattest_7.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0441\u043c. seaborn catplot</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0428\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430",
                None,
            )
        )
        self.comboBox_template_catplot.setItemText(
            0, QCoreApplication.translate("MainWindow", "bar", None)
        )
        self.comboBox_template_catplot.setItemText(
            1, QCoreApplication.translate("MainWindow", "box", None)
        )
        self.comboBox_template_catplot.setItemText(
            2, QCoreApplication.translate("MainWindow", "strip", None)
        )
        self.comboBox_template_catplot.setItemText(
            3, QCoreApplication.translate("MainWindow", "swarm", None)
        )
        self.comboBox_template_catplot.setItemText(
            4, QCoreApplication.translate("MainWindow", "violin", None)
        )
        self.comboBox_template_catplot.setItemText(
            5, QCoreApplication.translate("MainWindow", "boxen", None)
        )
        self.comboBox_template_catplot.setItemText(
            6, QCoreApplication.translate("MainWindow", "point", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_template_catplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0428\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430:</p><p>1. strip - \u0442\u043e\u0447\u0435\u0447\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a, \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u0432\u0441\u0435 \u0442\u043e\u0447\u043a\u0438 \u0434\u0430\u043d\u043d\u044b\u0445 \u0441 \u043b\u0435\u0433\u043a\u0438\u043c \u0440\u0430\u0437\u0431\u0440\u043e\u0441\u043e\u043c \u043f\u043e \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u0438 \u0447\u0442\u043e\u0431\u044b \u0438\u0437\u0431\u0435\u0436\u0430\u0442\u044c \u043f\u0435\u0440\u0435\u043a\u0440\u044b\u0442\u0438\u044f</p><p>2. swarm - \u0442\u043e\u0447\u0435\u0447\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a \u0431\u0435\u0437 \u043f\u0435\u0440\u0435\u043a\u0440\u044b\u0442\u0438\u044f, \u0442\u043e\u0447\u043a\u0438 \u0440\u0430\u0441\u043f\u043e\u043b\u0430\u0433\u0430\u044e\u0442\u0441\u044f \u043f\u043b\u043e\u0442\u043d\u043e,"
                " \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u044f \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e \u043e\u0441\u0438 Y</p><p>3. box - \u0431\u043e\u043a\u0441\u043f\u043b\u043e\u0442, \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043c\u0435\u0434\u0438\u0430\u043d\u0443, \u043a\u0432\u0430\u0440\u0442\u0438\u043b\u0438, \u0432\u044b\u0431\u0440\u043e\u0441\u044b \u0438 \u0440\u0430\u0437\u0431\u0440\u043e\u0441 \u0434\u0430\u043d\u043d\u044b\u0445</p><p>4. violin - \u0433\u0440\u0430\u0444\u0438\u043a \u043f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u0438, \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438 \u0435\u0433\u043e \u0444\u043e\u0440\u043c\u0443</p><p>5. boxen - \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u043d\u044b\u0439 \u0431\u043e\u043a\u0441\u043f\u043b\u043e\u0442 \u0434\u043b\u044f \u0431\u043e\u043b\u044c\u0448\u0438\u0445 \u043d"
                "\u0430\u0431\u043e\u0440\u043e\u0432 \u0434\u0430\u043d\u043d\u044b\u0445, \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u0431\u043e\u043b\u044c\u0448\u0435 \u043a\u0432\u0430\u043d\u0442\u0438\u043b\u0435\u0439</p><p>6. point - \u0433\u0440\u0430\u0444\u0438\u043a \u0441\u043e \u0441\u0440\u0435\u0434\u043d\u0438\u043c\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\u043c\u0438 \u0438 \u0434\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u043c\u0438 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430\u043c\u0438, \u0441\u043e\u0435\u0434\u0438\u043d\u044f\u0435\u0442 \u0442\u043e\u0447\u043a\u0438 \u043b\u0438\u043d\u0438\u044f\u043c\u0438</p><p>7. bar - \u0441\u0442\u043e\u043b\u0431\u0447\u0430\u0442\u0430\u044f \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430 \u0441\u043e \u0441\u0440\u0435\u0434\u043d\u0438\u043c\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\u043c\u0438 \u0438 \u0434\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b"
                "\u043c\u0438 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430\u043c\u0438</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_color_pal_box_15.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0435\u0439 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_color_pal_box_15.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0438",
                None,
            )
        )
        self.comboBox_catplot_SD_or_not.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435",
                None,
            ),
        )
        self.comboBox_catplot_SD_or_not.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0440\u0435\u0434\u043d\u0435\u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0448\u0438\u0431\u043a\u0430",
                None,
            ),
        )
        self.comboBox_catplot_SD_or_not.setItemText(
            2,
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b",
                None,
            ),
        )
        self.comboBox_catplot_SD_or_not.setItemText(
            3,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u0446\u0435\u043d\u0442\u0438\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b",
                None,
            ),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_catplot_SD_or_not.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0433\u0440\u0435\u0448\u043d\u043e\u0441\u0442\u0438 \u0434\u043b\u044f \u0432\u044b\u0432\u043e\u0434\u0430: SD, SE, \u0434\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0438\u043b\u0438 \u043f\u0435\u0440\u0446\u0435\u043d\u0442\u0438\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u0440\u0430\u0449\u0430\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u043d\u0430 \u0443\u0433\u043e\u043b",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_catplot_angle.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u0440\u0430\u0449\u0430\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u043d\u0430 \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u0439 \u0443\u0433\u043e\u043b.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_stattest_6.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c?",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_stat_znachimost_catplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_stat_znachimost_catplot.setText("")
        # if QT_CONFIG(tooltip)
        self.lb_stattest_5.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442",
                None,
            )
        )
        self.comboBox_stat_test_catplot.setItemText(
            0, QCoreApplication.translate("MainWindow", "Brunner-Munzel", None)
        )
        self.comboBox_stat_test_catplot.setItemText(
            1, QCoreApplication.translate("MainWindow", "Levene", None)
        )
        self.comboBox_stat_test_catplot.setItemText(
            2, QCoreApplication.translate("MainWindow", "Mann-Whitney", None)
        )
        self.comboBox_stat_test_catplot.setItemText(
            3, QCoreApplication.translate("MainWindow", "Mann-Whitney-gt", None)
        )
        self.comboBox_stat_test_catplot.setItemText(
            4, QCoreApplication.translate("MainWindow", "Mann-Whitney-ls", None)
        )
        self.comboBox_stat_test_catplot.setItemText(
            5, QCoreApplication.translate("MainWindow", "t-test_ind", None)
        )
        self.comboBox_stat_test_catplot.setItemText(
            6, QCoreApplication.translate("MainWindow", "t-test_welch", None)
        )
        self.comboBox_stat_test_catplot.setItemText(
            7, QCoreApplication.translate("MainWindow", "t-test_paired", None)
        )
        self.comboBox_stat_test_catplot.setItemText(
            8, QCoreApplication.translate("MainWindow", "Wilcoxon", None)
        )
        self.comboBox_stat_test_catplot.setItemText(
            9, QCoreApplication.translate("MainWindow", "Kruskal", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_stat_test_catplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438 \u0434\u043b\u044f catplot.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_stattest_14.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_14.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u043d\u0443\u0442\u0440\u0438 \u043f\u043e\u0434\u0433\u0440\u0443\u043f\u043f\u044b",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.check_stat_znachimost_catplot_inside_subgroup.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u043d\u0443\u0442\u0440\u0438 \u043f\u043e\u0434\u0433\u0440\u0443\u043f\u043f\u044b?",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.check_stat_znachimost_catplot_inside_subgroup.setText("")
        # if QT_CONFIG(tooltip)
        self.lb_stattest_9.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0424\u043e\u0440\u043c\u0430\u0442 \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439 \u0434\u043b\u044f \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438",
                None,
            )
        )
        self.comboBox_catplot_stat_formatt.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow", "\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 p", None
            ),
        )
        self.comboBox_catplot_stat_formatt.setItemText(
            1, QCoreApplication.translate("MainWindow", "*", None)
        )
        self.comboBox_catplot_stat_formatt.setItemText(
            2,
            QCoreApplication.translate("MainWindow", "\u043f\u043e\u043b\u043d\u044b\u0439", None),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_catplot_stat_formatt.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0424\u043e\u0440\u043c\u0430\u0442 \u043f\u043e\u0434\u043f\u0438\u0441\u0435\u0439 \u0434\u043b\u044f \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438:</p><p>\u041e\u0434\u0438\u043d \u0438\u0437 \u0442\u0440\u0435\u0445:</p><p>- \u0437\u0432\u0435\u0437\u0434\u043e\u0447\u043a\u0430 (*)</p><p>- \u0442\u043e\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 p (p=0.03)</p><p>- \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 p (p&lt;0.05)</p><p>\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u0434\u043b\u044f \u0437\u0434\u0435\u0437\u0434\u043e\u0447\u0435\u043a \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u0435\u0442\u0441\u044f \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c:</p><p>* p&lt;0.05, ** p&lt;0.01, *** p&lt;0.001, **** p&lt;0.0001</p><p>\u0414\u0430\u043d\u043d\u0430\u044f \u0440"
                "\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0430 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0435\u0442\u0441\u044f \u0432 txt \u0444\u0430\u0439\u043b \u0440\u044f\u0434\u043e\u043c \u0441 \u0440\u0438\u0441\u0443\u043d\u043a\u043e\u043c.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_stattest_10.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "\u0441\u043c. \u043f\u0430\u043a\u0435\u0442 statannotations", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u043f\u0440\u0430\u0432\u043a\u0430 \u043d\u0430 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0443\u044e \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443 \u0433\u0438\u043f\u043e\u0442\u0435\u0437",
                None,
            )
        )
        self.comboBox_catplot_mult_stat.setItemText(
            0, QCoreApplication.translate("MainWindow", "None", None)
        )
        self.comboBox_catplot_mult_stat.setItemText(
            1, QCoreApplication.translate("MainWindow", "bonferroni", None)
        )
        self.comboBox_catplot_mult_stat.setItemText(
            2, QCoreApplication.translate("MainWindow", "holm-bonferroni", None)
        )
        self.comboBox_catplot_mult_stat.setItemText(
            3, QCoreApplication.translate("MainWindow", "benjamini-hochberg", None)
        )
        self.comboBox_catplot_mult_stat.setItemText(
            4, QCoreApplication.translate("MainWindow", "Benjamini-Yekutieli", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_catplot_mult_stat.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u043f\u0440\u0430\u0432\u043a\u0430 \u043d\u0430 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0443\u044e \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443 \u0433\u0438\u043f\u043e\u0442\u0435\u0437. \u0412\u0430\u0436\u043d\u043e \u043a\u043e\u0433\u0434\u0430 \u043c\u043d\u043e\u0433\u043e \u043f\u043e\u043f\u0430\u0440\u043d\u044b\u0445 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.btn_plot_and_save_catplot.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a catplot \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c png \u0444\u0430\u0439\u043b.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_plot_and_save_catplot.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a",
                None,
            )
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_10),
            QCoreApplication.translate("MainWindow", "Catplot", None),
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_7.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "RheoScan - \u0440\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0440\u0435\u0434\u043d\u0438\u0435 \u0438 SD \u043f\u043e \u0444\u0430\u0439\u043b\u0443 \u0438\u043b\u0438 \u0444\u0430\u0439\u043b\u0430\u043c",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_5.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f excel \u0444\u0430\u0439\u043b\u044b \u0438\u043b\u0438 \u0444\u0430\u0439\u043b. \u0415\u0441\u043b\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u043e\u0434\u043d\u043e\u043c \u0444\u0430\u0439\u043b\u0435, \u0442\u043e \u043d\u0443\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e. </p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443 \u0438\u043b\u0438 \u0444\u0430\u0439\u043b\u0430\u043c",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.path_for_RheoScan_describe.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u0443\u0442\u044c \u043f\u0430\u043f\u043a\u0435 \u043a excel \u0444\u0430\u0439\u043b\u0443 \u0438\u043b\u0438 \u0444\u0430\u0439\u043b\u0430\u043c, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0431\u044b\u043b\u0438 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u044b \u043f\u0443\u0442\u0435\u043c \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0438\u0437 \u043f\u0435\u0440\u0432\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0438.</p><p>\u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e \u0431\u0443\u0434\u0443\u0442 \u0440\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u044b \u0432\u0441\u0435 excel \u0444\u0430\u0439\u043b\u044b \u0438\u0437 \u043f\u0430\u043f\u043a\u0438.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_RheoScan_describe.setText("")
        # if QT_CONFIG(whatsthis)
        self.toolButton_RheoScan.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043b\u0435\u0436\u0430\u0442 excel \u0444\u0430\u0439\u043b\u044b \u0438\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u043e.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.toolButton_RheoScan.setText(QCoreApplication.translate("MainWindow", "...", None))
        # if QT_CONFIG(tooltip)
        self.lb_stattest_12.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>&quot;\u041e\u0434\u0438\u043d \u0444\u0430\u0439\u043b - \u043e\u0434\u0438\u043d \u043e\u0431\u0440\u0430\u0437\u0435\u0446&quot; - \u043f\u043e\u0434\u0440\u0430\u0437\u0443\u043c\u0435\u0432\u0430\u0435\u0442, \u0447\u0442\u043e \u0432\u0441\u0435 \u0432 \u0444\u0430\u0439\u043b\u0435 \u0431\u0443\u0434\u0435\u0442 \u0443\u0441\u0440\u0435\u0434\u043d\u044f\u0442\u044c\u0441\u044f</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_12.setText(
            QCoreApplication.translate("MainWindow", "\u0414\u0430\u043d\u043d\u044b\u0435", None)
        )
        self.comboBox_RheoScan_describe.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0434\u0438\u043d \u0444\u0430\u0439\u043b - \u043e\u0434\u0438\u043d \u043e\u0431\u0440\u0430\u0437\u0435\u0446",
                None,
            ),
        )
        self.comboBox_RheoScan_describe.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0434\u0438\u043d \u0444\u0430\u0439\u043b - \u043c\u043d\u043e\u0433\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u043e\u0432",
                None,
            ),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_RheoScan_describe.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>\u041c\u043e\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435: </p><p>1. \u041b\u0438\u0431\u043e \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u043c\u043d\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u043e\u0432, \u0433\u0434\u0435 \u043a\u0430\u0436\u0434\u044b\u0439 \u0444\u0430\u0439\u043b -- \u044d\u0442\u043e \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u043f\u043e \u043e\u0434\u043d\u043e\u043c\u0443 \u043e\u0431\u0440\u0430\u0437\u0446\u0443/\u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0443.</p><p>2. \u041b\u0438\u0431\u043e \u0443 \u0432\u0430\u0441 \u043e\u0434\u0438\u043d \u0444\u0430\u0439\u043b, <span style=" text-decoration: underline;">\u0433\u0434\u0435 \u043f\u0435\u0440\u0432\u0430\u044f \u043a\u043e\u043b\u043e\u043d\u043a\u0430 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u043e\u0431\u0440\u0430\u0437\u0446'
                "\u0430 \u0438\u043b\u0438 \u0424\u0418\u041e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430</span>. \u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u044d\u0442\u043e \u0431\u044b\u043b\u0430 \u043f\u0435\u0440\u0432\u0430\u044f \u043a\u043e\u043b\u043e\u043d\u043a\u0430.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_6.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041d\u0430\u0434\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b \u0441\u0442\u0440\u043e\u043a\u0443 \u0438\u0437 (0 \u0438 1) \u0438\u043b\u0438 (f \u0438 t) \u0438\u043b\u0438 (false \u0438 true) \u0438\u043b\u0438 (n \u0438 y) \u0432 \u043a\u0430\u043a\u0438\u0445 \u043b\u0438\u0441\u0442\u0430\u0445 \u0441\u0447\u0438\u0442\u0430\u0442\u044c SD, \u0430 \u0432 \u043a\u0430\u043a\u0438\u0445 \u043d\u0435 \u0441\u0447\u0438\u0442\u0430\u0442\u044c. \u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u0442\u044c 3 \u043b\u0438\u0441\u0442\u0430 (Agg, Stress, Deform) \u0438 \u043c\u044b \u0432\u0432\u0435\u043b\u0438 &quot;0 1 0&quot;, \u0442\u043e\u0433\u0434\u0430 SD \u043f\u043e\u0441\u0447\u0438\u0442\u0430\u0435\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u043d\u0430 \u043b\u0438\u0441\u0442\u0435 &quot;Stress&quot;.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.lb_path_for_plot_6.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b\u044b \u043d\u0430\u043f\u0438\u0441\u0430\u0442\u044c True \u0438\u043b\u0438 False, \u0438\u043b\u0438 \u0436\u0435 0, 1, \u0442\u0435\u043c \u0441\u0430\u043c\u044b\u043c \u043f\u043e\u043c\u0435\u0442\u0438\u0432 \u043b\u0438\u0441\u0442\u044b.",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.lb_path_for_plot_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0447\u0435\u0442 SD \u043d\u0430 \u0440\u0430\u0437\u043d\u044b\u0445 \u043b\u0438\u0441\u0442\u0430\u0445",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.RheoScan_describe_mask_sheets.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442\u0430/\u0438\u0433\u043d\u043e\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 SD \u043d\u0430 \u0440\u0430\u0437\u043d\u044b\u0445 \u043b\u0438\u0441\u0442\u0430\u0445.</p><p>\u041f\u043e \u0434\u0435\u0444\u043e\u043b\u0442\u0443 SD \u0440\u0430\u0441\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u043b\u0438\u0441\u0442\u043e\u0432 excel.</p><p>\u041f\u043e \u0441\u0443\u0442\u0438 \u044d\u0442\u043e \u043c\u0430\u0441\u043a\u0430, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0434\u043e\u043b\u0436\u043d\u0430 \u0441\u043e\u0441\u0442\u043e\u044f\u0442\u044c \u0438\u0437:</p><p><span style=\" font-weight:700;\">\u043f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445</span> -- \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c SD  -- <span style=\" font-family:'Menlo','Monaco','Courier New','monospace"
                "'; font-size:12px; color:#cccccc;\">(</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;y&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;yes&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;t&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;true&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'"
                "Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;on&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;1&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">)</span></p><p>\u0438\u043b\u0438</p><p><span style=\" font-weight:700;\">\u043e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0445</span> -- \u0443\u0431\u0440\u0430\u0442\u044c SD -- <span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">(</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;n&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menl"
                "o','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;no&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;f&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;false&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;off&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">, </span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\""
                ">&quot;0&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">)</span></p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0435\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 3 \u043b\u0438\u0441\u0442\u0430 \u0438 \u043d\u0443\u0436\u043d\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u043f\u0435\u0440\u0432\u044b\u0445 \u0434\u0432\u0443\u0445 \u043f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c SD, \u0430 \u0434\u043b\u044f \u0442\u0440\u0435\u0442\u044c\u0435\u0433\u043e -- \u041d\u0415\u0422, \u0442\u043e \u043d\u0443\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438:</p><p>&quot;1 1 0&quot; -- \u0432\u0432\u0435\u0441\u0442\u0438 \u0431\u0435\u0437 \u043a\u0430\u0432\u044b\u0447\u0435\u043a.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.RheoScan_describe_mask_sheets.setText("")
        # if QT_CONFIG(whatsthis)
        self.btn_RheoScan_describe_file_or_files.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0440\u0435\u0434\u043d\u0438\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0438 SD \u0434\u043b\u044f \u0444\u0430\u0439\u043b\u0430 \u0438\u043b\u0438 \u0444\u0430\u0439\u043b\u043e\u0432 \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 excel \u0444\u0430\u0439\u043b.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_RheoScan_describe_file_or_files.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u0441\u0432\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u0444\u0430\u0439\u043b\u0443 \u0438\u043b\u0438 \u0444\u0430\u0439\u043b\u0430\u043c",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_10.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                "RheoScan - \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_9.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.path_for_rheoscan_report.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 excel \u0444\u0430\u0439\u043b\u043e\u043c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_rheoscan_report.setText("")
        self.lb_exel_name_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_rheoscan_report.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.calendarWidget_rheoscan_report.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_22.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0430 (\u0424\u0418\u041e):",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.rheoscan_report_name_exp.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0424\u0418\u041e \u0442\u043e\u0433\u043e, \u043a\u0442\u043e \u043f\u0440\u043e\u0432\u043e\u0434\u0438\u043b \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_24.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0437\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443 \u0434\u0430\u043d\u043d\u044b\u0445:",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.rheoscan_report_name_process.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0424\u0418\u041e \u0442\u043e\u0433\u043e, \u043a\u0442\u043e \u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043b \u0434\u0430\u043d\u043d\u044b\u0435.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.toolBox.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.rheoscan_report_parameters_dict.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0417\u0434\u0435\u0441\u044c \u043d\u0443\u0436\u043d\u043e \u0432 \u0432\u0438\u0434\u0435 Python \u0441\u043b\u043e\u0432\u0430\u0440\u044f \u0432\u0432\u0435\u0441\u0442\u0438 \u043f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443, \u0432 excel \u0444\u0430\u0439\u043b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0438\u043d\u0434\u0435\u043a\u0441\u0430 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u043d\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f &quot;AI&quot;, \u0430 \u0432 \u043e\u0442\u0447\u0435\u0442\u0435 \u043c\u044b \u0445\u043e\u0442\u0438\u043c \u0432\u0438\u0434\u0435\u0442\u044c &quot;AI, %&quot;.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443:</p><p>{&quot;AI&quot;:&quot;AI, %&quot;, &quot;CSS&quot;:&quot;CSS, \u043c\u041f\u0430&quot;, &quot;T1/2&quot;: &quot;T1/2, \u0441\u0435\u043a"
                ".&quot;}</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.rheoscan_report_parameters_dict.setPlainText(
            QCoreApplication.translate(
                "MainWindow",
                '{"AI":"AI, %",\n'
                ' "CSS":"CSS, \u043c\u041f\u0430",\n'
                ' "T1/2": "T1/2, \u0441\u0435\u043a."}',
                None,
            )
        )
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.page),
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432",
                None,
            ),
        )
        # if QT_CONFIG(whatsthis)
        self.rheoscan_report_norm_dict.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0417\u0434\u0435\u0441\u044c \u043d\u0443\u0436\u043d\u043e \u0432 \u0432\u0438\u0434\u0435 Python \u0441\u043b\u043e\u0432\u0430\u0440\u044f \u0432\u0432\u0435\u0441\u0442\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u043d\u043e\u0440\u043c\u044b.<br/>\u0412\u0430\u0436\u043d\u043e, \u0447\u0442\u043e\u0431\u044b \u043a\u043b\u044e\u0447\u0438 - \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u043e\u0432\u0430\u043b\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\u043c \u0441\u043b\u043e\u0432\u0430\u0440\u044f \u0438\u0437 \u0440\u0430\u0437\u0434\u0435\u043b\u0435 &quot;\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432&quot;.</p><p>\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043d\u043e\u0440\u043c\u044b \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f, \u043a"
                "\u0430\u043a \u0441\u0440\u0435\u0434\u043d\u0435\u0435<span style=\" font-family:'Google Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0a0a0a; background-color:#ffffff;\">\u00b1</span>SD.</p><p>\u041a \u043f\u0440\u0438\u043c\u0435\u0440\u0443:</p><p>{&quot;AI, %&quot;: &quot;40\u00b110&quot;, &quot;CSS, \u043c\u041f\u0430&quot;: &quot;180\u00b150&quot;, &quot;T1/2, \u0441\u0435\u043a.&quot;: &quot;7\u00b12&quot;}</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.rheoscan_report_norm_dict.setPlainText(
            QCoreApplication.translate(
                "MainWindow",
                '{"AI, %": "40\u00b110",\n'
                ' "CSS, \u043c\u041f\u0430": "180\u00b150",\n'
                ' "T1/2, \u0441\u0435\u043a.": "7\u00b12"}',
                None,
            )
        )
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.page_2),
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u043d\u043e\u0440\u043c\u044b (\u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u00b1 SD)",
                None,
            ),
        )
        # if QT_CONFIG(whatsthis)
        self.rheoscan_report_comment.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u043e\u0442\u0447\u0435\u0442\u0443.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.rheoscan_report_comment.setPlainText(
            QCoreApplication.translate(
                "MainWindow",
                '- \u0418\u043d\u0434\u0435\u043a\u0441 \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 ("AI, %") \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u043f\u043e\u0432\u044b\u0448\u0435\u043d\n'
                '- \u0413\u0438\u0434\u0440\u043e\u0434\u0438\u043d\u0430\u043c\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043f\u0440\u043e\u0447\u043d\u043e\u0441\u0442\u044c \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0432 ("CSS, \u043c\u041f\u0430") \u0432 \u043d\u043e\u0440\u043c\u0435\n'
                '- \u0412\u0440\u0435\u043c\u044f \u0430\u0433\u0440\u0435\u0433\u0430\u0446\u0438\u0438 \u044d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u043e\u0432 ("T1/2, \u0441\u0435\u043a.") \u043f\u043e\u043d\u0438\u0436\u0435\u043d\u043e\n'
                "\n"
                "\u0412 \u0445\u043e\u0434\u0435 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0439 \u043d\u0435\u0448\u0442\u0430\u0442\u043d\u044b\u0445 \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u0439 \u043d\u0435 \u0432\u043e\u0437\u043d\u0438\u043a\u0430\u043b\u043e.",
                None,
            )
        )
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.page_3),
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u043f.\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439",
                None,
            ),
        )
        # if QT_CONFIG(whatsthis)
        self.btn_make_rheoscan_report.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442 \u043f\u043e \u043e\u0434\u043d\u043e\u043c\u0443 \u043e\u0431\u0440\u0430\u0437\u0446\u0443/\u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0443 \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0435\u0433\u043e \u0432 pdf.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_make_rheoscan_report.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442",
                None,
            )
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_4),
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 RheoScan",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_8.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u043c\u0435\u0436\u0434\u0443 2 \u0432\u044b\u0431\u043e\u0440\u043a\u0430\u043c\u0438 - \u0442\u043e\u043b\u044c\u043a\u043e p-value",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_4.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.path_for_dop_stat.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 excel \u0444\u0430\u0439\u043b\u043e\u043c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_dop_stat.setText("")
        self.lb_exel_name_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_excel_dop_stat.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_exel_name_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 \u0444\u0430\u0439\u043b\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_excel_sheet_dop_stat.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 excel \u0444\u0430\u0439\u043b\u0435 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_9.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_dop_stat_x.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u21161/2 \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u0430.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_10.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0412\u0442\u043e\u0440\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_dop_stat_y.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043b\u043e\u043d\u043a\u0430 \u21162/2 \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u0430.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_stattest_8.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043b\u044f \u043f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0442\u0435\u0441\u0442\u043e\u0432 \u0441\u0447\u0435\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0434\u043e\u043b\u0433\u0438\u043c.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_stattest_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442",
                None,
            )
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow",
                "U-\u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041c\u0430\u043d\u043d\u0430 \u2014 \u0423\u0438\u0442\u043d\u0438",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422-\u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0421\u0442\u044c\u044e\u0434\u0435\u043d\u0442\u0430",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            2,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u0441\u0442 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            3,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u0441\u0442 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f (normal)",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            4,
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0423\u0438\u043b\u043a\u043e\u043a\u0441\u043e\u043d\u0430",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            5,
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041a\u0440\u0430\u0441\u043a\u0435\u043b\u0430 \u2014 \u0423\u043e\u043b\u043b\u0438\u0441\u0430",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            6,
            QCoreApplication.translate(
                "MainWindow",
                "\u041c\u0435\u0434\u0438\u0430\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            7,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u0441\u0442 \u0410\u043d\u0441\u0430\u0440\u0438-\u0411\u0440\u044d\u0434\u043b\u0438",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            8,
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u0435\u0441\u0442 \u0424\u0438\u0448\u0435\u0440\u0430-\u041f\u0438\u0442\u043c\u0430\u043d\u0430",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            9,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0411\u0440\u0443\u043d\u043d\u0435\u0440\u0430 \u2014 \u041c\u044e\u043d\u0446\u0435\u043b\u044f",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            10,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u041c\u0430\u043d\u043d\u0430 \u2014 \u0423\u0438\u0442\u043d\u0438",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            11,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0423\u0438\u043b\u043a\u043e\u043a\u0441\u043e\u043d\u0430",
                None,
            ),
        )
        self.comboBox_stat_test_dop_stat.setItemText(
            12,
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0424\u0440\u0438\u0434\u043c\u0430\u043d\u0430",
                None,
            ),
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_stat_test_dop_stat.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0435\u0441\u0442 \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u0430.</p><p>\u041d\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043f\u0435\u0440\u043c\u0443\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0442\u0435\u0441\u0442\u044b, \u0435\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u043c\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0432 \u043a\u043e\u043b\u043e\u043d\u043a\u0430\u0445.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb__altern_heposisis_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0410\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u0433\u0438\u043f\u043e\u0442\u0435\u0437\u0430",
                None,
            )
        )
        self.comboBox_alter_hep_dop_stat.setItemText(
            0, QCoreApplication.translate("MainWindow", "two-sided", None)
        )
        self.comboBox_alter_hep_dop_stat.setItemText(
            1, QCoreApplication.translate("MainWindow", "less", None)
        )
        self.comboBox_alter_hep_dop_stat.setItemText(
            2, QCoreApplication.translate("MainWindow", "greater", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_alter_hep_dop_stat.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0410\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u0433\u0438\u043f\u043e\u0442\u0435\u0437\u0430.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_11.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_11.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 p:", None
            )
        )
        # if QT_CONFIG(whatsthis)
        self.p_value_dop_stat.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u0412\u044b\u0432\u043e\u0434\u0438\u043c\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 p.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.p_value_dop_stat.setText("")
        # if QT_CONFIG(whatsthis)
        self.btn_dop_stat_calc.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u043c\u0435\u0436\u0434\u0443 \u0434\u0432\u0443\u043c\u044f \u0441\u0442\u043e\u043b\u0431\u0446\u0430\u043c\u0438.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_dop_stat_calc.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c",
                None,
            )
        )
        self.tabWidget_4.setTabText(
            self.tabWidget_4.indexOf(self.tab_19),
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442. \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c \u043c\u0435\u0436\u0434\u0443 2 \u0432\u044b\u0431\u043e\u0440\u043a\u0430\u043c\u0438",
                None,
            ),
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_11.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u0440\u0438\u0437\u043d\u0430\u043a\u043e\u0432 - \u0440\u0438\u0441\u0443\u043d\u043e\u043a",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.lb_path_for_plot_12.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043d\u0430\u0439\u0434\u0435\u043d excel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lb_path_for_plot_12.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a excel \u0444\u0430\u0439\u043b\u0443",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.path_for_excel_cluster.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 excel \u0444\u0430\u0439\u043b\u043e\u043c \u0434\u043b\u044f \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u043a\u043e\u0432 \u043f\u043e \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0438.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.path_for_excel_cluster.setText("")
        self.lb_exel_name_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_cluster_file.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 excel \u0444\u0430\u0439\u043b\u0430 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lb_exel_name_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 \u0444\u0430\u0439\u043b\u0435",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.comboBox_cluster_excel_sheet.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0441\u0442\u0430 \u0432 excel \u0444\u0430\u0439\u043b\u0435 -- \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438. \u041d\u0430\u0434\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_12.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_12.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u043a\u043e\u043b-\u0432\u043e \u043a\u043b\u0430\u0441\u0441\u0442\u0435\u0440\u043e\u0432",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_cluster_n.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043b-\u0432\u043e \u043a\u043b\u0430\u0441\u0441\u0442\u0435\u0440\u043e\u0432 \u0434\u043b\u044f \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_13.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_13.setText(
            QCoreApplication.translate(
                "MainWindow", "\u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None
            )
        )
        self.comboBox_cluster_coord.setItemText(
            0, QCoreApplication.translate("MainWindow", "MDS", None)
        )
        self.comboBox_cluster_coord.setItemText(
            1, QCoreApplication.translate("MainWindow", "PCA", None)
        )

        # if QT_CONFIG(whatsthis)
        self.comboBox_cluster_coord.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u0430 \u0434\u043b\u044f 2D \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f: MDS \u0438\u043b\u0438 PSA.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.lb_hue_name_14.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.lb_hue_name_14.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0440\u0430\u0437\u043c\u0435\u0440 \u043f\u0443\u0437\u044b\u0440\u044c\u043a\u043e\u0432",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.spinBox_cluster_buble_size.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0443\u0437\u044b\u0440\u044c\u043a\u043e\u0432 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0435.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.btn_cluster_save_file.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044e \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_cluster_save_file.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044e \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a",
                None,
            )
        )
        self.tabWidget_4.setTabText(
            self.tabWidget_4.indexOf(self.tab_20),
            QCoreApplication.translate(
                "MainWindow",
                "\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u0440\u0438\u0437\u043d\u0430\u043a\u043e\u0432",
                None,
            ),
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_12),
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u043f. \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430",
                None,
            ),
        )
        self.Lab_stuff.setTabText(
            self.Lab_stuff.indexOf(self.tabWidgetPage4),
            QCoreApplication.translate(
                "MainWindow",
                "\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445",
                None,
            ),
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0434\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438\u0437 JSON \u0444\u0430\u0439\u043b\u0430",
                None,
            )
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u0443\u0442\u044c \u043a JSON \u0444\u0430\u0439\u043b\u0443:",
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        self.lineEdit_json_load.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u043b\u043d\u044b\u0439 \u043f\u0443\u0442\u044c \u043a JSON \u0444\u0430\u0439\u043b\u0443",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.btn_json_load.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u041f\u043e\u0434\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438\u0437 JSON \u0444\u0430\u0439\u043b\u0430. </p><p>\u042d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043f\u043e\u043b\u0435\u0437\u043d\u043e, \u0435\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u0433\u043e\u0442\u043e\u0432\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a \u0434\u043b\u044f \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432 \u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0438 \u0432\u0430\u043c \u043d\u0435 \u0445\u043e\u0447\u0435\u0442\u0441\u044f \u043a\u0430\u0436\u0434\u044b\u0439 \u0440\u0430\u0437 \u043f\u0440\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c"
                " \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438.</p><p>JSON \u0444\u0430\u0439\u043b \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c \u043f\u043e \u0442\u0438\u043f\u0443:</p><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">{</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">&quot;rheoscan_report_name_exp&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">:</span><span style=\" font-family:'Menlo','Monaco','Cou"
                "rier New','monospace'; font-size:12px; color:#ce9178;\">&quot;\u0424\u0418\u041e&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">,</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">&quot;rheoscan_report_parameters_dict&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">:{</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo"
                "','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">&quot;AAA&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">:</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;\">&quot;aaa&quot;</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">   },</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">&quot;check_approx_agg&quot;</span><span style=\" font-fami"
                "ly:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">:</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;\">true</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">,</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\"/><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;\">&quot;check_approx_deform&quot;</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">:</span><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;\">true</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-ri"
                "ght:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;\"><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;\">}</span></pre><p>\u0422\u043e \u0435\u0441\u0442\u044c \u043a\u043b\u044e\u0447 -- \u044d\u0442\u043e \u0438\u043c\u044f \u043e\u0431\u044a\u0435\u043a\u0442\u0430 (\u0432 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u0438 \u044f\u0432\u043d\u043e \u0443\u043a\u0430\u0437\u0430\u043d\u043e \u0432 \u043f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430\u0445), \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 -- \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0432 \u0434\u0430\u043d\u043d\u043e\u0435 \u043f\u043e\u043b\u0435 \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u044c.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.btn_json_load.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u041f\u043e\u0434\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438",
                None,
            )
        )
        self.Lab_stuff.setTabText(
            self.Lab_stuff.indexOf(self.tab_9),
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u043f.\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438",
                None,
            ),
        )

    # retranslateUi
