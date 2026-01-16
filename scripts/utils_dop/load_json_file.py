"""Загрузка значений из JSON файла."""  # noqa: INP001

import json

from loguru import logger
from PySide6.QtCore import QDate, QTime
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


def load_widgets_from_json(self) -> None:  # noqa: ANN001, C901
    """Загружает значения из JSON файла и устанавливает их в соответствующие виджеты."""
    dlg = QMessageBox(self)

    # параметры, которые нам понадобятся
    json_path = self.ui.lineEdit_json_load.text()

    if json_path == "":
        show_message(dlg, "Загрузка JSON файла", "Не введен путь к JSON файлу")
        return

    try:
        # Читаем JSON файл
        with open(json_path, encoding="utf-8") as f:
            settings = json.load(f)

        # Проходим по всем ключам (object names) в JSON
        for object_name, value in settings.items():
            # Находим виджет по имени - ИСПРАВЛЕННЫЙ ВАРИАНТ
            widget = None

            # Пробуем найти виджет по разным типам
            widget_types = [
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
                QWidget,
            ]

            for widget_type in widget_types:
                widget = self.findChild(widget_type, object_name)
                if widget is not None:
                    break

            # Если не нашли в основном окне, ищем в ui
            if widget is None and hasattr(self, "ui"):
                # Пробуем получить атрибут по имени
                widget = getattr(self.ui, object_name, None)
                if widget is None:
                    # Ищем в ui как дочерний элемент
                    for widget_type in widget_types:
                        widget = self.ui.findChild(widget_type, object_name)
                        if widget is not None:
                            break

            if widget is None:
                logger.info(f"Виджет с именем '{object_name}' не найден")
                continue

            # Устанавливаем значение в зависимости от типа виджета
            _set_widget_value(widget, value)

        logger.info(f"Настройки успешно загружены из {json_path}")

    except FileNotFoundError:
        msg = f"Файл {json_path} не найден"
        show_message(dlg, "Загрузка JSON файла", msg)
        logger.info(msg)
    except json.JSONDecodeError:
        msg = f"Ошибка чтения JSON файла {json_path}"
        show_message(dlg, "Загрузка JSON файла", msg)
        logger.info(msg)
    except Exception as e:
        msg = f"Ошибка при загрузке настроек: {e}"
        show_message(dlg, "Загрузка JSON файла", msg)
        logger.info(msg)


def _set_widget_value(widget, value) -> None:  # noqa: ANN001, C901, PLR0912, PLR0915
    """
    Устанавливает значение для виджета в зависимости от его типа.

    Args:
        widget: Виджет PySide6
        value: Значение для установки

    """
    widget_type = type(widget).__name__

    try:
        if widget_type == "QCheckBox":
            widget.setChecked(bool(value))

        elif widget_type == "QLineEdit":
            widget.setText(str(value))

        elif widget_type == "QComboBox":
            # Пытаемся найти текст в выпадающем списке
            index = widget.findText(str(value))
            if index >= 0:
                widget.setCurrentIndex(index)
            else:
                # Если текст не найден, пробуем установить по индексу
                try:
                    widget.setCurrentIndex(int(value))
                except (ValueError, IndexError):
                    logger.info(f"Не удалось установить значение для {widget.objectName()}")

        elif widget_type == "QCalendarWidget" and value:
            # Предполагаем, что value - строка даты в формате 'YYYY-MM-DD'
            date = QDate.fromString(str(value), "yyyy-MM-dd")
            if date.isValid():
                widget.setSelectedDate(date)
            else:
                # Попробуем другие форматы дат
                date_formats = ["dd.MM.yyyy", "MM/dd/yyyy", "dd-MM-yyyy"]
                for fmt in date_formats:
                    date = QDate.fromString(str(value), fmt)
                    if date.isValid():
                        widget.setSelectedDate(date)
                        break

        elif widget_type == "QSpinBox":
            widget.setValue(int(value))

        elif widget_type == "QDoubleSpinBox":
            widget.setValue(float(value))

        elif widget_type in {"QTextEdit", "QPlainTextEdit"}:
            widget.setPlainText(str(value))

        elif widget_type == "QRadioButton":
            widget.setChecked(bool(value))

        elif widget_type == "QSlider":
            widget.setValue(int(value))

        elif widget_type == "QDateEdit":
            date = QDate.fromString(str(value), "yyyy-MM-dd")
            if date.isValid():
                widget.setDate(date)

        elif widget_type == "QTimeEdit":
            time = QTime.fromString(str(value), "HH:mm:ss")
            if time.isValid():
                widget.setTime(time)
            else:
                # Попробуем другой формат
                time = QTime.fromString(str(value), "HH:mm")
                if time.isValid():
                    widget.setTime(time)

        else:
            logger.info(f"Тип виджета {widget_type} для {widget.objectName()} не поддерживается")

    except Exception as e:
        logger.info(f"Ошибка при установке значения для {widget.objectName()}: {e}")
