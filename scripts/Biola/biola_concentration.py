import re
from io import StringIO

import pandas as pd
from PyPDF2 import PdfReader
from PySide6.QtWidgets import QMessageBox


def conentration_to_excel(self, path, file) -> None:
    dlg = QMessageBox(self)
    # DataFrame основной
    final_dataframe = pd.DataFrame()

    if path == "":
        dlg.setWindowTitle("Biola - PDF")
        dlg.setText("Не введен путь к файлу PDF")
        dlg.exec()
        return

    path += "//"
    # читаем PDF файл
    reader = PdfReader(path + file)

    # читаем каждую страницу файла
    for i in range(len(reader.pages)):
        try:
            page = reader.pages[i]
            gg = page.extract_text()

            # уберем двойные пробелы, чтобы в случае, когда фамилии разделены двойными пробелами не было ошибок
            gg = gg.replace("  ", " ")

            # обязательно ставим после \n 3 пробела, чтобы их не убрал r'string'. Потом убираем пробелы, если они есть для имён
            gg = gg.replace("\n", "\n   ")
            gg = re.sub(r"(\S)\s(\S)", r"\1\2", gg)
            gg = re.sub(r"(\S)\s(\S)", r"\1\2", gg)
            gg = gg.replace(" -", "-")
            gg = gg.replace("- ", "-")

            # оставляем только одинарные пробелы
            while "  " in gg:
                gg = gg.replace("  ", " ")
            # убираем пробел после \n
            gg = gg.replace("\n ", "\n")

            # убираем первые 2 строчки
            gg = re.sub(r"^[^\n]+\n", "", gg)
            gg = re.sub(r"^[^\n]+\n", "", gg)

            # просто так строку в pd.read_csv не передать, поэтому поступаем так
            testdata = StringIO(gg)

            df = pd.read_csv(testdata, header=None, delim_whitespace=True)

            # записываем всё в основной DataFrame
            final_dataframe = pd.concat([df, final_dataframe], ignore_index=True)
        except Exception as e:
            dlg.setWindowTitle("Biola - PDF")
            dlg.setText(f"На странице {i} есть проблемы. Измените pdf.\n" + str(e))
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()
            return

    try:
        final_dataframe.columns = ["Фамилия", "Концентрация тромбоцитов,тыс/мкл", "Контроль"]
    except Exception as e:
        dlg.setWindowTitle("Biola - PDF")
        dlg.setText(
            "В данных есть проблемы -- выделилось не 3 столбца, а больше. Измените pdf.\n" + str(e),
        )
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return
    try:
        final_dataframe.to_excel(path + "platelets_concentration.xlsx")
    except Exception as e:
        dlg.setWindowTitle("Biola - PDF")
        dlg.setText("Excel файл с концентрациями не сохранился.\n" + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    dlg.setWindowTitle("Biola - PDF")
    dlg.setText("Excel файл и все графики успешно сохранены")
    dlg.exec()
    return
