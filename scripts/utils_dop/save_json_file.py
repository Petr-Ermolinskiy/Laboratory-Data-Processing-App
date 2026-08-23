"""Выгрузка значений в JSON файл."""  # noqa: INP001

import json

from loguru import logger
from PySide6.QtWidgets import (
    QCalendarWidget,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDoubleSpinBox,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTextEdit,
    QTimeEdit,
    QWidget,
)


def show_message(dlg, title: str, text: str) -> None:  # noqa: ANN001
    """Показ сообщения в UI."""
    dlg.setWindowTitle(title)
    dlg.setText(text)
    dlg.exec()


def save_widgets_to_json(self) -> None:
    """Сохраняет текущие значения всех виджетов в JSON файл."""
    dlg = QMessageBox(self)

    # параметры, которые нам понадобятся
    json_path = self.ui.lineEdit_json_save.text()

    if json_path == "":
        show_message(dlg, "Сохранение JSON файла", "Не введен путь для сохранения JSON файла")
        return

    try:
        settings = {}

        # Получаем главное окно (self) и ищем виджеты в нем
        # В PySide6 findChildren доступен у QWidget и его наследников

        # Вариант 1: Ищем все виджеты в главном окне
        all_widgets = self.findChildren(QWidget)

        # Типы виджетов, которые поддерживаются
        supported_types = [
            QCheckBox,
            QLineEdit,
            QComboBox,
            QCalendarWidget,
            QSpinBox,
            QDoubleSpinBox,
            QTextEdit,
            QPlainTextEdit,
            QRadioButton,
            QSlider,
            QDateEdit,
            QTimeEdit,
        ]

        for widget in all_widgets:
            # Проверяем, что виджет имеет objectName и поддерживаемый тип
            if not widget.objectName():
                continue

            # Проверяем, является ли виджет одним из поддерживаемых типов
            is_supported = False
            for widget_type in supported_types:
                if isinstance(widget, widget_type):
                    is_supported = True
                    break

            if not is_supported:
                continue

            value = _get_widget_value(widget)
            if value is not None:
                settings[widget.objectName()] = value

        # Сохраняем в JSON файл
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)

        logger.info(f"Настройки успешно сохранены в {json_path}")
        show_message(dlg, "Сохранение JSON файла", f"Настройки успешно сохранены в {json_path}")

    except Exception as e:
        msg = f"Ошибка при сохранении настроек: {e}"
        show_message(dlg, "Сохранение JSON файла", msg)
        logger.info(msg)


def _get_widget_value(widget):
    """
    Получает значение из виджета в зависимости от его типа.

    Args:
        widget: Виджет PySide6

    Returns:
        Значение виджета в формате, подходящем для JSON

    """
    widget_type = type(widget).__name__

    try:
        if widget_type == "QCheckBox":
            return widget.isChecked()

        if widget_type == "QLineEdit":
            return widget.text()

        if widget_type == "QComboBox":
            return widget.currentText()

        if widget_type == "QCalendarWidget":
            return widget.selectedDate().toString("yyyy-MM-dd")

        if widget_type == "QSpinBox" or widget_type == "QDoubleSpinBox":
            return widget.value()

        if widget_type in {"QTextEdit", "QPlainTextEdit"}:
            return widget.toPlainText()

        if widget_type == "QRadioButton":
            return widget.isChecked()

        if widget_type == "QSlider":
            return widget.value()

        if widget_type == "QDateEdit":
            return widget.date().toString("yyyy-MM-dd")

        if widget_type == "QTimeEdit":
            return widget.time().toString("HH:mm:ss")

        logger.info(f"Тип виджета {widget_type} для {widget.objectName()} не поддерживается")
        return None

    except Exception as e:
        logger.info(f"Ошибка при получении значения для {widget.objectName()}: {e}")
        return None
