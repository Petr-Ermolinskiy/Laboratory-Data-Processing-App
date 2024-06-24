##############
import sys
############################
# библиотеки для создания приложения
from PySide6.QtWidgets import (QApplication)
from PySide6.QtGui import QIcon

import os
# главный класс Main_window
from main_ui_class import Main_window


def myapp_id_logo() -> None:
    # чтобы Лого показывалось:
    # https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
    import ctypes

    myapp_id = 'Petr_Ermolinskiy.GUI_app.processing.v_3'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)


###################
# запуск приложения
###################
if __name__ == '__main__':
    myapp_id_logo()

    app = QApplication(sys.argv)

    # важно обозначить для того, чтобы лого обозначалось правильно
    basedir = os.path.dirname(__file__)
    # добавляем иконку
    app.setWindowIcon(QIcon(os.path.join(basedir, 'logo.ico')))

    # выполняем всё
    window = Main_window()
    window.show()
    sys.exit(app.exec())
