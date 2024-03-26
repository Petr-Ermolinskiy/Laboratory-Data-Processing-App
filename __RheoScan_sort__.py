import glob
import os
from tkinter import messagebox
from pandas import read_table
from pathlib2 import Path


def replacetext(path_to_file):
    # Reading and storing the content of the file in
    file = Path(path_to_file)
    # a data variable
    data = file.read_text()

    # Replacing the text using the replace function
    data = data.replace('.', ',')

    # Writing the replaced data
    # in the text file
    file.write_text(data)
    return 0

def subfold(path, level):
    global s
    if level == 1:
        s.add(path)
        return
    for i in os.scandir(path):
        if i.is_dir():
            if level !=1:
                subfold(i.path, level-1)
            else:
                s.add(i.path)


def sort_these_files(path):
    path = path + '\\'
    ############
    #Изменим название папок на маленькие буквы, если такие папки есть
    for sub_folders in os.scandir(path):
        if sub_folders.is_dir():
            name = sub_folders.path.split('\\')[-1]
            if name == 'Agg':
                os.rename(path + "Agg", path + "agg")
            if name == 'Stress':
                os.rename(path + "Stress", path + "stress")
            if name == 'Deform':
                os.rename(path + "Deform", path + "deform")
    ############
    files_all = glob.glob(path+'*.txt')
    if files_all == []:
        return messagebox.showerror('Ошибка', f'По пути {path} нет txt файлов')
    # создаем подпапки для файлов
    os.makedirs(path + 'agg', exist_ok=True)
    os.makedirs(path + 'stress', exist_ok=True)
    os.makedirs(path + 'deform', exist_ok=True)
    # прочитать все файлы и добавить данные в DataFrame
    for i in files_all:
        replacetext(i)
        # правильный срез данных
        all_lines_agg = sum(1 for line in open(i))
        # прочтатать каждый файл и извлечь данные
        x = read_table(i, skipfooter=all_lines_agg - 13, engine='python', header=None, decimal=',')
        var = x.iloc[5][0][0:3]
        if var == 'ATM':
            os.rename(i, path + 'stress//' + i.split('\\')[-1])
        elif var == 'AI:':
            os.rename(i, path + 'agg//' + i.split('\\')[-1])
        elif var == 'Def':
            os.rename(i, path + 'deform//' + i.split('\\')[-1])
    return 0

def sort_RheoScan_data(path, level):
    if path == '':
        return messagebox.showerror('Ошибка', f'В поле <путь к папке с подпапками> ничего не введено')
    global s
    s = set()
    subfold(path, level)
    for path_for_one in s:
        sort_these_files(path_for_one)
    messagebox.showinfo('RheoScan', f'Данные рассортированы по подпапкам')




