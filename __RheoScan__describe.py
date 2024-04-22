#необходимые библиотеки
import pandas as pd
import glob
import os
# для вывода диалогового окна
from PySide6.QtWidgets import QMessageBox

def RheoScan_describe_file_or_files(self):
    dlg = QMessageBox(self)
    # путь
    path = self.ui.path_for_RheoScan_describe.text()
    if path == '':
        dlg.setWindowTitle("Обработка файлов RheoScan")
        dlg.setText("Не введен путь к excel файлу")
        dlg.exec()
        return None

    if self.ui.RheoScan_describe_mask_sheets.text() == '':
        mask = None
    else:
        try:
            mask = self.ui.RheoScan_describe_mask_sheets.text()
            mask = mask.split(' ')
            mask = [bool(strtobool(i)) for i in mask]
        except Exception as e:
            dlg.setWindowTitle("Обработка файлов RheoScan")
            dlg.setText("В поле <Расчет SD на разных листах> неправильный ввод.\n" + str(e))
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()
            return None

    try:
        if self.ui.comboBox_RheoScan_describe.currentText() == 'Один файл - один образец':
            _describe_all_multiple_files(path, mask)
        else:
            _describe_all_one_file(path, mask)
    except Exception as e:
        dlg.setWindowTitle("Обработка файлов RheoScan")
        dlg.setText("Ошибка в обработке: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return None

    dlg.setWindowTitle("Обработка файлов RheoScan")
    dlg.setText("Все данные успешно обработаны")
    dlg.exec()
    return None


# функция, когда файлов много и один файл == один образец
def _describe_all_multiple_files(path: str, mask_sheet=None) -> None:
    path = path + '\\'

    files_all = glob.glob(path + '*.xlsx')

    describe_all_files = pd.DataFrame()

    for file in files_all:
        sheets = pd.ExcelFile(file).sheet_names

        if mask_sheet == None:
            mask_sheet = [True] * len(sheets)
        elif type(mask_sheet) != list:
            return 0
        elif len(mask_sheet) > len(sheets):
            return 0
        elif len(mask_sheet) < len(sheets):
            mask_sheet = [*mask_sheet, *[False] * (len(sheets) - len(mask_sheet))]

        describe_data_frame = pd.DataFrame()
        # file name
        name_of_file = file.split('\\')[-1].split('.')[0]
        # file name
        for one_sheet, mask in zip(sheets, mask_sheet):
            # читаем exel файл
            df = pd.read_excel(file, one_sheet)

            mean_vals = df[df.columns[2:]].mean()

            if mask:
                std_vals = df[df.columns[2:]].std()
                std_vals.index = std_vals.index + '_SD'
                one_sheet = pd.DataFrame([pd.concat([mean_vals, std_vals])], index=[name_of_file])
                one_sheet = one_sheet[one_sheet.columns.sort_values()]
            else:
                one_sheet = pd.DataFrame([mean_vals], index=[name_of_file])
            describe_data_frame = pd.concat([describe_data_frame, one_sheet], axis=1)

        # сохраняем в основной DataFrame
        describe_all_files = pd.concat([describe_all_files, describe_data_frame], axis=0)

    # сохраняем в excel файл
    describe_all_files.to_excel(path + 'describe_' + 'ALL' + '.xlsx')

# функция, когда файл один и один файл == много образцов -- причем колонка с индексами -- первая
def _describe_all_one_file(path: str, mask_sheet=None) -> None:
    describe_file = pd.DataFrame()

    describe_data_frame = pd.DataFrame()

    sheets = pd.ExcelFile(path).sheet_names
    if mask_sheet == None:
        mask_sheet = [True] * len(sheets)
    elif type(mask_sheet) != list:
        return 0
    elif len(mask_sheet) > len(sheets):
        return 0
    elif len(mask_sheet) < len(sheets):
        mask_sheet = [*mask_sheet, *[False] * (len(sheets) - len(mask_sheet))]

    for one_sheet, mask in zip(sheets, mask_sheet):
        # читаем exel файл
        df = pd.read_excel(path, one_sheet)

        mean_df = df.groupby(df.columns[0]).mean()

        if mask:
            std_df = df.groupby(df.columns[0]).std()
            std_df.columns = std_df.columns + '_SD'
            df_describe_for_one_sheet = pd.concat([mean_df, std_df], axis=1)
            df_describe_for_one_sheet = df_describe_for_one_sheet[df_describe_for_one_sheet.columns.sort_values()]
        else:
            df_describe_for_one_sheet = mean_df

        # describe
        describe_file = pd.concat([describe_file, df_describe_for_one_sheet], axis=1)

    # save data to the excel file
    describe_file.to_excel('\\'.join(path.split('\\')[:-1]) + '\\' + 'file_describe.xlsx')

# функция для правильного интерпретирования введенных значений
def strtobool (val):
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return 1
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return 0
    else:
        return 1