import pandas as pd
from PySide6.QtWidgets import QMessageBox


# функция, конвертирующая данные либо в индексированные, либо по столбцам
def pivot_or_melt_excel_file(self) -> None:
    dlg = QMessageBox(self)
    #########################
    # параметры, которые нам понадобятся
    path = self.ui.path_for_pivot_table.text()
    exel_name = self.ui.comboBox_pivot_table.currentText()
    sheet_we_need = self.ui.comboBox_pivot_table_excel_sheet.currentText()
    hue_name = str(self.ui.comboBox_pivot_hue.currentText())
    # как конвертировать данные - индексированные или сырые
    convert_type = self.ui.comboBox_index_data_or_raw.currentText()
    #########################
    if path == "":
        dlg.setWindowTitle("Сводная таблица")
        dlg.setText("Не введен путь к excel файлу")
        dlg.exec()
        return
    file = path + "//" + exel_name
    try:
        names = pd.ExcelFile(file).sheet_names
    except Exception as e:
        dlg.setWindowTitle("Сводная таблица")
        dlg.setText("Нет такого файла или директории.\n" + str(e))
        dlg.exec()
        return

    df = pd.read_excel(file, sheet_name=sheet_we_need)
    df.columns = [str(i) for i in df.columns]
    # отсекаем всё то, что не нужно
    index_col = df.columns.get_loc(hue_name)
    df = df[df.columns[index_col:]]

    if convert_type == "из индексированных в сырые":
        pivot_df_with_nan = pd.pivot(df, columns=hue_name)
        # следующая сточка очень важна, чтобы не потерять какие-то значения, если есть ряд пропусков
        pivot_df = pd.DataFrame(
            index=list(range(max(pivot_df_with_nan.count()))),
            columns=pivot_df_with_nan.columns,
        )
        # убираем NaN
        for j in pivot_df_with_nan.columns:
            ignore_nan = pivot_df_with_nan[j]
            ignore_nan = ignore_nan.dropna().reset_index(drop=True)
            pivot_df[j] = ignore_nan.copy()
        # сохраняем датафрейм
        pivot_df.to_excel(path + "//" + "pivot_" + exel_name)
    elif convert_type == "из сырых в индексируемые":
        # сохраняем датафрейм - тут всё намного легче
        df.melt().dropna().to_excel(path + "//" + "unpivot_" + exel_name)
    else:
        pass

    dlg.setWindowTitle("Сводная таблица")
    dlg.setText("Данные успешно переведены " + convert_type)
    dlg.exec()
    return


# сводная таблица
def pivot_do_for_sheet(self) -> None:
    dlg = QMessageBox(self)
    #########################
    # параметры, которые нам понадобятся
    path = self.ui.path_for_pivot_table.text()
    exel_name = self.ui.comboBox_pivot_table.currentText()
    sheet_we_need = self.ui.comboBox_pivot_table_excel_sheet.currentText()
    hue_name = self.ui.comboBox_pivot_hue.currentText()
    __round__ = self.ui.spinBox_pivot_table.value()
    error = self.ui.comboBox_sd_or_se_pivot.currentText()
    #########################
    if path == "":
        dlg.setWindowTitle("Сводная таблица")
        dlg.setText("Не введен путь к excel файлу")
        dlg.exec()
        return

    files = path + "//" + exel_name
    try:
        names = pd.ExcelFile(files).sheet_names
    except Exception as e:
        dlg.setWindowTitle("Сводная таблица")
        dlg.setText("Нет такого файла или директории.\n" + str(e))
        dlg.exec()
        return

    # выполяем основной цикл по всем листам в excel файле - тогда нужно указать "names" вместо "[sheet_we_need]"
    check_cykle = "__"
    for i in [sheet_we_need]:
        check_cykle = do_pivot(path, exel_name, i, hue_name, __round__, error, self)
        if check_cykle != "__":
            break
    if check_cykle == "__":
        dlg.setWindowTitle("Сводная таблица")
        dlg.setText("Сводная таблица сохранена в excel файл")
        dlg.exec()
        return
    dlg.setWindowTitle("Сводная таблица")
    dlg.setText("Сводная таблица не сохранена в excel файл или какие-то проблемы с таблицей")
    dlg.exec()
    return


# корреляционная матрица
def corr_for_sheet(self) -> None:
    dlg = QMessageBox(self)
    #########################
    # параметры, которые нам понадобятся
    path = self.ui.path_for_pivot_table.text()
    exel_name = self.ui.comboBox_pivot_table.currentText()
    sheet_we_need = self.ui.comboBox_pivot_table_excel_sheet.currentText()
    hue_name = self.ui.comboBox_pivot_hue.currentText()
    pierson_or_not = self.ui.comboBox_correlation_person_or_not.currentText()
    color_or_not = self.ui.check_color_for_corr_pivot.isChecked()
    __color_map__ = self.ui.comboBox_correlation_color_map.currentText()
    #########################

    if path == "":
        dlg.setWindowTitle("Корреляционная матрица")
        dlg.setText("Не введен путь к excel файлу")
        dlg.exec()
        return

    files = path + "//" + exel_name
    try:
        names = pd.ExcelFile(files).sheet_names
    except Exception as e:
        dlg.setWindowTitle("Корреляционная матрица")
        dlg.setText("Нет такого файла или директории.\n" + str(e))
        dlg.exec()
        return

    # если хотим выполнить основной цикл по всем листам в excel файле, тогда нужно указать "names" вместо "[sheet_we_need]"
    check_cykle = "__"
    for i in [sheet_we_need]:
        check_cykle = corr_sheet(
            path,
            exel_name,
            hue_name,
            i,
            pierson_or_not,
            color_or_not,
            __color_map__,
            self,
        )
        if check_cykle != "__":
            break
    if check_cykle == "__":
        dlg.setWindowTitle("Корреляционная матрица")
        dlg.setText("Корреляционная матрица сохранена в excel файл")
        dlg.exec()
        return
    dlg.setWindowTitle("Корреляционная матрица")
    dlg.setText("Корреляционная матрица не сохранена в excel файл или какие-то проблемы с таблицей")
    dlg.exec()
    return


############
# доп. функции
############
def describe_this_dataframe(
    path,
    _df,
    __round__,
    error,
    what_sheet,
    _int=False,
    index="index",
) -> None:
    final = pd.DataFrame()

    for i in _df["index"].unique():
        final_res = _df[_df[index] == i].dropna()
        final_res = final_res[final_res.columns[1:]]

        column_name = str(i) + " (N=" + str(len(final_res)) + ")"
        gg = final_res.mean(numeric_only=True).round(__round__)
        if error == "SD":
            gg_error = final_res.std(numeric_only=True).round(__round__)
        elif error == "SE":
            gg_error = final_res.sem(numeric_only=True).round(__round__)
        if _int:
            gg = gg.astype(int)
            gg_error = gg_error.astype(int)
        final[column_name] = gg.apply(str) + "±" + gg_error.apply(str)
        final.to_excel(path + "//" + str(what_sheet) + "_pivot_table.xlsx", engine="openpyxl")


def do_pivot(path, exel_name, what_sheet, hue_name, __round__, error, self):
    dlg = QMessageBox(self)

    files = path + "//" + exel_name

    # читаем exel файл - index_col=0,
    df = pd.read_excel(files, sheet_name=what_sheet)
    df.index.rename(None, inplace=True)
    # на всякий случай почистим
    df.columns = df.columns.str.replace("\\n", "\n", regex=False)
    # выделяем те колонки, которые нас будут интерисовать с точки зрения обработки!
    columns_of_interest = df.columns[:]
    # если ничего не введено, то тогда первый столбец будет hue
    if hue_name == "":
        hue_name_for_sheet = columns_of_interest[0]
        columns_of_interest = columns_of_interest[1:]
    else:
        hue_name_for_sheet = hue_name.replace("\\n", "\n")
        if hue_name_for_sheet not in columns_of_interest:
            dlg.setWindowTitle("Сводная таблица - Ошибка")
            dlg.setText("В таблице нет такого столбца:" + str(hue_name_for_sheet))
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()
            return 0
        index_for_col_interest = list(columns_of_interest).index(hue_name_for_sheet)
        columns_of_interest = columns_of_interest[index_for_col_interest + 1 :]

    # все столбцы с данными приводим к численному виду
    for dd in columns_of_interest:
        try:
            df[dd] = df[dd].apply(pd.to_numeric)
        except Exception as e:
            dlg.setWindowTitle("Сводная таблица - Ошибка")
            dlg.setText(
                "В колонке "
                + str(dd)
                + " представлены значения, \nкоторые нельзя конвертировать в числа.\n"
                + str(e),
            )
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()
            return 0

    # название оси X
    name_of_X_axis = hue_name_for_sheet
    # создаем новый DataFrame только с колонками для обработки
    new_df = df[columns_of_interest].copy()
    # и добавляем в него только колонку для значений индекса/концентрации/образца!
    new_df.insert(loc=0, column="index", value=df[hue_name_for_sheet])  # Диагноз или группа

    __int__ = __round__ == 0

    describe_this_dataframe(path, new_df, __round__, error, what_sheet, _int=__int__, index="index")

    return "__"


def corr_sheet(
    path,
    exel_name,
    hue_name,
    what_sheet,
    pierson_or_not,
    color_or_not,
    __color_map__,
    self,
):
    dlg = QMessageBox(self)

    files = path + "//" + exel_name

    # читаем exel файл - index_col=0,
    df = pd.read_excel(files, sheet_name=what_sheet)
    df.index = df.index.rename(None)
    # на всякий случай почистим
    df.columns = df.columns.str.replace("\\n", "\n", regex=False)
    # выделяем те колонки, которые нас будут интерисовать с точки зрения обработки!
    columns_of_interest = df.columns[:]
    # если ничего не введено, то тогда первый столбец будет hue
    if hue_name == "":
        hue_name_for_sheet = columns_of_interest[0]
        columns_of_interest = columns_of_interest[1:]
    else:
        hue_name_for_sheet = hue_name.replace("\\n", "\n")
        if hue_name_for_sheet not in columns_of_interest:
            dlg.setWindowTitle("Корреляционная матрица - Ошибка")
            dlg.setText("В таблице нет такого столбца:" + str(hue_name_for_sheet))
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()
            return 0

        index_for_col_interest = list(columns_of_interest).index(hue_name_for_sheet)
        columns_of_interest = columns_of_interest[index_for_col_interest + 1 :]

    # все столбцы с данными приводим к численному виду
    for dd in columns_of_interest:
        try:
            df[dd] = df[dd].apply(pd.to_numeric)
        except Exception as e:
            dlg.setWindowTitle("Корреляционная матрица - Ошибка")
            dlg.setText(
                "В колонке "
                + str(dd)
                + " представлены значения, \nкоторые нельзя конвертировать в числа.\n"
                + str(e),
            )
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()
            return 0

    # название оси X
    name_of_X_axis = hue_name_for_sheet
    # создаем новый DataFrame только с колонками для обработки
    new_df = df[columns_of_interest].copy()
    # и добавляем в него только колонку для значений индекса/концентрации/образца!
    new_df.insert(loc=0, column="index", value=df[hue_name_for_sheet])  # Диагноз или группа

    # тут уже идёт корреляции
    new_df = new_df[new_df.columns[1:]]
    corr = new_df.corr(method=pierson_or_not)

    if color_or_not:
        (
            corr.style.background_gradient(cmap=__color_map__).to_excel(
                path + "//" + what_sheet + "_corr_matrix.xlsx",
                engine="openpyxl",
            )
        )
    else:
        corr.to_excel(path + "//" + what_sheet + "_corr_matrix.xlsx", engine="openpyxl")
    return "__"
