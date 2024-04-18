import pandas as pd
from tkinter import messagebox

def describe_this_dataframe(path, _df, __round__, error, what_sheet, _int=False, index='index'):
    final = pd.DataFrame()

    for i in _df['index'].unique():
        final_res = _df[_df[index] == i].dropna()
        column_name = str(i) + ' (N=' + str(len(final_res)) + ')'
        gg = final_res.mean(numeric_only=True).round(__round__)
        if error == 'SD':
            gg_error = final_res.std(numeric_only=True).round(__round__)
        elif error == 'SE':
            gg_error = final_res.sem(numeric_only=True).round(__round__)
        if _int:
            gg = gg.astype(int)
            gg_error = gg_error.astype(int)
        final[column_name] = gg.apply(str) + '±' + gg_error.apply(str)
        final.to_excel(path + '//' + str(what_sheet) + "_pivot_table.xlsx", engine="openpyxl")
    return 0

def do_pivot(path, exel_name, what_sheet, hue_name, __round__, error):
    files = path + '//' + exel_name

    # читаем exel файл - index_col=0,
    df = pd.read_excel(files, sheet_name=what_sheet)
    df.index.rename(None, inplace=True)
    # на всякий случай почистим
    df.columns = df.columns.str.replace('\\n', '\n', regex=False)
    # выделяем те колонки, которые нас будут интерисовать с точки зрения обработки!
    columns_of_interest = df.columns[:]
    # если ничего не введено, то тогда первый столбец будет hue
    if hue_name == '':
        hue_name_for_sheet = columns_of_interest[0]
        columns_of_interest = columns_of_interest[1:]
    else:
        hue_name_for_sheet = hue_name.replace('\\n', '\n')
        if hue_name_for_sheet not in columns_of_interest:
            return messagebox.showerror('Ошибка', 'В таблице нет такого столбца:' + str(hue_name_for_sheet))
        index_for_col_interest = list(columns_of_interest).index(hue_name_for_sheet)
        columns_of_interest = columns_of_interest[index_for_col_interest + 1:]

    # все столбцы с данными приводим к численному виду

    for dd in columns_of_interest:
        try:
            df[dd] = df[dd].apply(pd.to_numeric)
        except:
            message_ = 'В колонке ' + str(dd) + ' представлены значения, \nкоторые нельзя конвертировать в числа'
            return messagebox.showerror('Ошибка', message_)

    # название оси X
    name_of_X_axis = hue_name_for_sheet
    # создаем новый DataFrame только с колонками для обработки
    new_df = df[columns_of_interest].copy()
    # и добавляем в него только колонку для значений индекса/концентрации/образца!
    new_df.insert(loc=0, column='index', value=df[hue_name_for_sheet])  # Диагноз или группа

    if __round__ == 0:
        __int__ = True
    else:
        __int__ = False

    describe_this_dataframe(path, new_df, __round__, error, what_sheet, _int=__int__, index='index')

    return '__'


def do_for_each_sheet(path, exel_name, hue_name, __round__, error):
    files = path + '//' + exel_name
    try:
        names = pd.ExcelFile(files).sheet_names
    except:
        return messagebox.showerror('Ошибка', 'Нет такого файла или директории')

    # выполяем основной цикл по всем листам в excel файле
    check_cykle = '__'
    for i in names:
        check_cykle = do_pivot(path, exel_name, i, hue_name, __round__, error)
        if check_cykle != '__':
            break
    if check_cykle == '__':
        return messagebox.showinfo('Сводная таблица', 'Сводная таблица сохранена в excel файл')
    else:
        return messagebox.showerror('Ошибка - Сводная таблица', 'Сводная таблица не сохранена в excel файл или какие-то проблемы с таблицей')


def corr_for_each_sheeeeeeet(path, exel_name, hue_name, pierson_or_not, color_or_not, __color_map__):
    files = path + '//' + exel_name
    try:
        names = pd.ExcelFile(files).sheet_names
    except:
        return messagebox.showerror('Ошибка', 'Нет такого файла или директории')

    # выполяем основной цикл по всем листам в excel файле
    check_cykle = '__'
    for i in names:
        check_cykle = corr_sheeeeeeet(path, exel_name, hue_name, i, pierson_or_not, color_or_not, __color_map__)
        if check_cykle != '__':
            break
    if check_cykle == '__':
        return messagebox.showinfo('Сводная таблица', 'Корреляционная матрица сохранена в excel файл')
    else:
        return messagebox.showerror('Ошибка - Сводная таблица', 'Корреляционная матрица не сохранена в excel файл или какие-то проблемы с таблицей')

def corr_sheeeeeeet(path, exel_name, hue_name, what_sheet, pierson_or_not, color_or_not, __color_map__):
    files = path + '//' + exel_name

    # читаем exel файл - index_col=0,
    df = pd.read_excel(files, sheet_name=what_sheet)
    df.index.rename(None, inplace=True)
    # на всякий случай почистим
    df.columns = df.columns.str.replace('\\n', '\n', regex=False)
    # выделяем те колонки, которые нас будут интерисовать с точки зрения обработки!
    columns_of_interest = df.columns[:]
    # если ничего не введено, то тогда первый столбец будет hue
    if hue_name == '':
        hue_name_for_sheet = columns_of_interest[0]
        columns_of_interest = columns_of_interest[1:]
    else:
        hue_name_for_sheet = hue_name.replace('\\n', '\n')
        if hue_name_for_sheet not in columns_of_interest:
            return messagebox.showerror('Ошибка', 'В таблице нет такого столбца:' + str(hue_name_for_sheet))
        index_for_col_interest = list(columns_of_interest).index(hue_name_for_sheet)
        columns_of_interest = columns_of_interest[index_for_col_interest + 1:]

    # все столбцы с данными приводим к численному виду

    for dd in columns_of_interest:
        try:
            df[dd] = df[dd].apply(pd.to_numeric)
        except:
            message_ = 'В колонке ' + str(dd) + ' представлены значения, \nкоторые нельзя конвертировать в числа'
            return messagebox.showerror('Ошибка', message_)

    # название оси X
    name_of_X_axis = hue_name_for_sheet
    # создаем новый DataFrame только с колонками для обработки
    new_df = df[columns_of_interest].copy()
    # и добавляем в него только колонку для значений индекса/концентрации/образца!
    new_df.insert(loc=0, column='index', value=df[hue_name_for_sheet])  # Диагноз или группа

    ##тут уже идёт корреляции
    new_df = new_df[new_df.columns[1:]]
    corr = new_df.corr(method=pierson_or_not)

    if color_or_not:
        (corr.style.background_gradient(cmap=__color_map__).to_excel(path + '//' + what_sheet + "_corr_matrix.xlsx", engine="openpyxl"))
    else:
        corr.to_excel(path + '//' + what_sheet + "_corr_matrix.xlsx", engine="openpyxl")
    return '__'