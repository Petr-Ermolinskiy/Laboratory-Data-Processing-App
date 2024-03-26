from PyPDF2 import PdfReader
import pandas as pd
import re
from tkinter import messagebox
####################################
import sys

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO
####################################
def conentration_to_excel(path, file):

    final_dataframe = pd.DataFrame()

    path += '//'

    reader = PdfReader(path + file)

    # читаем каждую страницу файла
    for i in range(len(reader.pages)):
        try:
            page = reader.pages[i]
            gg = page.extract_text()

            # уберем двойные пробелы, чтобы в случае, когда фамилии разделены двойными пробелами не было ошибок
            gg = gg.replace('  ', ' ')

            # обязательно ставим после \n 3 пробела, чтобы их не убрал r'string'. потом убираем пробелы, если они есть для имён
            gg = gg.replace('\n', '\n   ')
            gg = re.sub(r'(\S)\s(\S)', r'\1\2', gg)
            gg = re.sub(r'(\S)\s(\S)', r'\1\2', gg)
            gg = gg.replace(' -', '-')
            gg = gg.replace('- ', '-')

            # оставляем только одинарные пробелы
            while '  ' in gg:
                gg = gg.replace('  ', ' ')
            # убираем пробел после \n
            gg = gg.replace('\n ', '\n')

            # убираем первые 2 строчки
            gg = re.sub(r"^[^\n]+\n", "", gg)
            gg = re.sub(r"^[^\n]+\n", "", gg)

            # просто так строку в pd.read_csv не передать, поэтому поступаем так
            TESTDATA = StringIO(gg)

            df = pd.read_csv(TESTDATA, header=None, delim_whitespace=True)

            # записываем всё в основной DataFrame
            final_dataframe = pd.concat([df, final_dataframe], ignore_index=True)
        except:
            return messagebox.showerror('Ошибка', f'На странице {i} есть проблемы. Обратитесь в поддержку, или же измените pdf')

    try:
        final_dataframe.columns = ['Фамилия', 'Концентрация тромбоцитов,тыс/мкл', 'Контроль']
    except:
        return messagebox.showerror('Ошибка','В данных есть проблемы -- выделилось не 3 столбца, а больше. Обратитесь в поддержку, или же измените pdf')
    try:
        final_dataframe.to_excel(path + "platelets_concentration.xlsx")
    except:
        return messagebox.showerror('Ошибка','Excel файл с концентрациями не сохранился')
    return messagebox.showinfo('Biola', f'Excel файл и все графики успешно сохранены')