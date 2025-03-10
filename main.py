import os
import sys
import ctypes

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

# главный класс MainWindowProcessingApp
from main_window_processing_app import MainWindowProcessingApp


def myapp_id_logo() -> None:
    """
    Функция для того, чтобы показывалось лого. См:
    https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
    """
    myapp_id = 'Petr_Ermolinskiy.GUI_app.processing.v_3'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
    return None


if __name__ == '__main__':
    myapp_id_logo()

    app = QApplication(sys.argv)

    # важно обозначить для того, чтобы лого выводилось на Windows правильно
    basedir = os.path.dirname(__file__)
    # добавляем иконку
    app.setWindowIcon(QIcon(os.path.join(basedir, 'style/logo.ico')))

    # запускаем код программы
    window = MainWindowProcessingApp()
    window.show()
    sys.exit(app.exec())
