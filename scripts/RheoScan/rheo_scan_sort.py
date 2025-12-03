import os
from pathlib import Path

from pandas import read_table
from PySide6.QtWidgets import QMessageBox


def replacetext(path_to_file) -> None:
    # Reading and storing the content of the file in
    file = Path(path_to_file)
    # a data variable
    data = file.read_text()

    # Replacing the text using the replace function
    data = data.replace(".", ",")

    # Writing the replaced data
    # in the text file
    file.write_text(data)


def subfold(path, level) -> None:
    global s
    if level == 1:
        s.add(path)
        return
    for i in os.scandir(path):
        if i.is_dir():
            if level != 1:
                subfold(i.path, level - 1)
            else:
                s.add(i.path)
    return


def sort_these_files(path, self) -> bool:
    path_obj = Path(path)
    ############
    # Изменим название папок на маленькие буквы, если такие папки есть
    for sub_folders in path_obj.iterdir():
        if sub_folders.is_dir():
            name = sub_folders.name
            if name == "Agg":
                (path_obj / "Agg").rename(path_obj / "agg")
            if name == "Stress":
                (path_obj / "Stress").rename(path_obj / "stress")
            if name == "Deform":
                (path_obj / "Deform").rename(path_obj / "deform")
    ############
    files_all = list(path_obj.glob("*.txt"))
    if files_all == []:
        dlg = QMessageBox(self)
        dlg.setWindowTitle("RheoScan")
        dlg.setText(f"По пути {path} нет txt файлов. Продолжить?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        return button == QMessageBox.No

    # создаем подпапки для файлов
    (path_obj / "agg").mkdir(parents=True, exist_ok=True)
    (path_obj / "stress").mkdir(parents=True, exist_ok=True)
    (path_obj / "deform").mkdir(parents=True, exist_ok=True)
    # прочитать все файлы и добавить данные в DataFrame
    for i in files_all:
        replacetext(str(i))
        # правильный срез данных
        all_lines_agg = sum(1 for line in open(i))
        # прочитать каждый файл и извлечь данные
        x = read_table(i, skipfooter=all_lines_agg - 13, engine="python", header=None, decimal=",")
        var = x.iloc[5][0][0:3]
        if var == "ATM":
            i.rename(path_obj / "stress" / i.name)
        elif var == "AI:":
            i.rename(path_obj / "agg" / i.name)
        elif var == "Def":
            i.rename(path_obj / "deform" / i.name)
    return False


def sort_rheo_scan_data(self) -> None:
    path, level = self.ui.main_path.text(), self.ui.spinBox_level.value()

    dlg = QMessageBox(self)
    if path == "":
        dlg.setWindowTitle("RheoScan")
        dlg.setText("Не введен путь к папкам")
        dlg.exec()
        return

    global s
    s = set()
    subfold(path, level)
    for path_for_one in s:
        if sort_these_files(path_for_one, self):
            break

    dlg.setWindowTitle("RheoScan")
    dlg.setText("Данные рассортированы по подпапкам")
    dlg.exec()
    return
