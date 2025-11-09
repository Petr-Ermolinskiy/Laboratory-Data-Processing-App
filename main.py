import ctypes
import json
import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from main_window_processing_app import MainWindowProcessingApp, resource_path


def myapp_id_logo(_version_app: str) -> None:
    """Функция для того, чтобы показывалось лого.

    См: https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105.
    """
    myapp_id = f"Petr_Ermolinskiy.GUI_app.processing.{_version_app}"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)


if __name__ == "__main__":
    with open(resource_path("config.json")) as f:
        data = json.load(f)
        version_app = data["version"]

    # для иконки лого в Windows
    myapp_id_logo(version_app)

    # приложение
    app = QApplication(sys.argv)

    # важно обозначить для того, чтобы лого выводилось на Windows правильно
    basedir = os.path.dirname(__file__)
    # добавляем иконку
    app.setWindowIcon(QIcon(os.path.join(basedir, "app/style/logo.ico")))

    # запускаем код программы
    window = MainWindowProcessingApp(version_app)
    window.show()
    sys.exit(app.exec())
