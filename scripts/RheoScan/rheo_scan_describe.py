import glob

import pandas as pd
from PySide6.QtWidgets import QMessageBox


def rheo_scan_describe_file_or_files(self):
    dlg = QMessageBox(self)
    # путь
    path = self.ui.path_for_RheoScan_describe.text()
    if path == "":
        dlg.setWindowTitle("Обработка файлов RheoScan")
        dlg.setText("Не введен путь к excel файлу")
        dlg.exec()
        return

    if self.ui.RheoScan_describe_mask_sheets.text() == "":
        mask = None
    else:
        try:
            mask = self.ui.RheoScan_describe_mask_sheets.text()
            mask = mask.split(" ")
            mask = [bool(strtobool(i)) for i in mask]
        except Exception as e:
            dlg.setWindowTitle("Обработка файлов RheoScan")
            dlg.setText("В поле <Расчет SD на разных листах> неправильный ввод.\n" + str(e))
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()
            return

    try:
        if self.ui.comboBox_RheoScan_describe.currentText() == "Один файл - один образец":
            _describe_all_multiple_files(path, mask)
        else:
            _describe_all_one_file(path, mask)
    except Exception as e:
        dlg.setWindowTitle("Обработка файлов RheoScan")
        dlg.setText("Ошибка в обработке: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    dlg.setWindowTitle("Обработка файлов RheoScan")
    dlg.setText("Все данные успешно обработаны")
    dlg.exec()
    return


# функция, когда файлов много и один файл == один образец
def _describe_all_multiple_files(path: str, mask_sheet_main=None) -> None:
    path = path + "\\"

    files_all = glob.glob(path + "*.xlsx")
    if path + "RheoScan_summary.xlsx" in files_all:
        files_all.remove(path + "RheoScan_summary.xlsx")

    describe_all_files = pd.DataFrame()

    for file in files_all:
        sheets = pd.ExcelFile(file).sheet_names

        if mask_sheet_main is None:
            mask_sheet = [True] * len(sheets)
        elif isinstance(mask_sheet_main, list) or len(mask_sheet_main) > len(sheets):
            return 0
        elif len(mask_sheet_main) < len(sheets):
            mask_sheet = [*mask_sheet_main, *[False] * (len(sheets) - len(mask_sheet_main))]
        else:
            mask_sheet = [False] * len(sheets)
        describe_data_frame = pd.DataFrame()
        # file name
        name_of_file = "".join(file.split("\\")[-1].split(".")[:-1])
        for one_sheet, mask in zip(sheets, mask_sheet, strict=False):
            # читаем exel файл
            df = pd.read_excel(file, one_sheet)
            mean_vals = df[df.columns[2:]].mean()
            if mask:
                std_vals = df[df.columns[2:]].std()
                std_vals.index = std_vals.index + "_SD"
                one_sheet = pd.DataFrame([pd.concat([mean_vals, std_vals])], index=[name_of_file])
                one_sheet = one_sheet[one_sheet.columns.sort_values()]
            else:
                one_sheet = pd.DataFrame([mean_vals], index=[name_of_file])
            describe_data_frame = pd.concat([describe_data_frame, one_sheet], axis=1)
        # сохраняем в основной DataFrame
        describe_all_files = pd.concat([describe_all_files, describe_data_frame], axis=0)

    # сохраняем в excel файл
    describe_all_files.to_excel(path + "RheoScan_summary.xlsx")
    return None


# функция, когда файл один и один файл == много образцов -- причем колонка с индексами -- первая
def _describe_all_one_file(path: str, mask_sheet: list | None = None) -> None:
    describe_file = pd.DataFrame()
    sheets = pd.ExcelFile(path).sheet_names
    if mask_sheet is None:
        mask_sheet = [True] * len(sheets)
    elif isinstance(mask_sheet, list) or len(mask_sheet) > len(sheets):
        return
    elif len(mask_sheet) < len(sheets):
        mask_sheet = [*mask_sheet, *[False] * (len(sheets) - len(mask_sheet))]

    for one_sheet, mask in zip(sheets, mask_sheet, strict=False):
        # читаем exel файл
        df = pd.read_excel(path, one_sheet)

        mean_df = df.groupby(df.columns[0]).mean()

        if mask:
            std_df = df.groupby(df.columns[0]).std()
            std_df.columns = std_df.columns + "_SD"
            df_describe_for_one_sheet = pd.concat([mean_df, std_df], axis=1)
            df_describe_for_one_sheet = df_describe_for_one_sheet[
                df_describe_for_one_sheet.columns.sort_values()
            ]
        else:
            df_describe_for_one_sheet = mean_df

        # статистика
        describe_file = pd.concat([describe_file, df_describe_for_one_sheet], axis=1)
    # сохраняем
    describe_file.to_excel("\\".join(path.split("\\")[:-1]) + "\\" + "RheoScan_summary.xlsx")


def strtobool(val: str) -> int:
    """Функция для правильной интерпретации введенных значений -- 0 или 1 на выходе."""
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return 1
    if val in ("n", "no", "f", "false", "off", "0"):
        return 0
    return 1
