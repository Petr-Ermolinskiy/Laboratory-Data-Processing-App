#необходимые библиотеки
import math
from math import pi

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# для вывода диалогового окна
from PySide6.QtWidgets import QMessageBox

def prifile_plot(self) -> None:
    dlg = QMessageBox(self)
    #########################
    # параметры, которые нам понадобятся
    #########################
    #это цвета
    prifile_data__ = [self.ui.patient_prof.text(), self.ui.norm_prof.text(), self.ui.color_for_patient.text(), self.ui.color_for_norm.text()]
    # это всё остальное
    patient_d = self.ui.patient_data.text()
    norm_d = self.ui.norm_data.text()
    # путь к папке для сохранения файла
    path = self.ui.path_for_profile.text()
    # чертить линии или нет
    pat_line = self.ui.check_profile_pat_line.isChecked()
    pat_sd = self.ui.check_profile_pat_sd.isChecked()
    norm_line = self.ui.check_profile_norm_line.isChecked()
    norm_sd = self.ui.check_profile_norm_sd.isChecked()
    #########################


    sns.reset_orig()
    # какие группы? 1-ая группа -- пациент; 2-ая группа -- это контрольная группа
    I_index = [prifile_data__[0], prifile_data__[1]]

    if path == '':
        dlg.setWindowTitle("Микрореологический профиль")
        dlg.setText("Не введен путь к сохранению графиков")
        dlg.exec()
        return None

    path = path + '//'
    if len(prifile_data__[2]) != 7 or len(prifile_data__[3]) != 7 or prifile_data__[2][0] + prifile_data__[3][0] != '##':
        dlg.setWindowTitle("Микрореологический профиль - Ошибка")
        dlg.setText("Неправильные значения цветов HEX")
        dlg.exec()
        return None
    #######
    # Цвета для радиального графика
    #######
    # цвета для Пациента
    color_Patient = prifile_data__[2]
    # цвета для НОРМЫ
    color_NORM = prifile_data__[3]
    ###

    #######
    # Цвета для линейного графика
    #######
    # цвета для Пациента
    color_Patient_line = prifile_data__[2]  # вот ещё хороший цвет  #E3936D   #DB4900   #D98F6A
    # цвета для НОРМЫ
    color_NORM_line = prifile_data__[3]
    ###
    if patient_d == '' or norm_d == '':
        dlg.setWindowTitle("Микрореологический профиль - Ошибка")
        dlg.setText("Введите данные для профилей")
        dlg.exec()
        return None

    # получаем словарь для средних значениях и стандарного отклонения для ПАЦИЕНТА
    patient_data, SD_patient_data = get_data_from_clipboard(patient_d, self)
    # проверка
    if patient_data==None or SD_patient_data==None:
        return None
    # получаем словарь для средних значениях и стандарного отклонения для НОРМЫ
    norm_data, SD_norm_data = get_data_from_clipboard(norm_d, self)
    # проверка
    if norm_data==None or SD_norm_data==None:
        return None
    # создаём нормированные значения параметров пациента и нормы
    patient_data_norm = {}
    norm_data_norm = {}
    # создаём нормированные значения стандартных отклонений параметров пациента и нормы
    SD_patient_data_norm = {}
    SD_norm_data_norm = {}

    # для каждого параметра...
    for i in patient_data:
        # параметры микроциркуляции
        patient_data_norm[i] = patient_data[i] / norm_data[i]
        norm_data_norm[i] = norm_data[i] / norm_data[i]
        # стандартное отклонение
        SD_patient_data_norm[i] = SD_patient_data[i] / norm_data[i]
        SD_norm_data_norm[i] = SD_norm_data[i] / norm_data[i]
    # создаём DataFrame с нормированными значениями пациента и нормы
    df = pd.DataFrame(columns=list(patient_data_norm), index=I_index)
    df.loc[I_index[0]] = patient_data_norm
    df.loc[I_index[1]] = norm_data_norm
    # создаём DataFrame с стандартными отклонениями нормированных значений пациента и нормы
    SD_df = pd.DataFrame(columns=list(patient_data_norm), index=I_index)
    SD_df.loc[I_index[0]] = SD_patient_data_norm
    SD_df.loc[I_index[1]] = SD_norm_data_norm


    # максимальное значение для графика
    MAX_Y = math.ceil(find_max(patient_data_norm))

    # выделяем категории и кол-во категорий
    categories = list(patient_data_norm)
    N = len(patient_data_norm)
    # специально заменим некоторые параметры и части на нижнее подчеркивание
    categories_new = change_name_of_categories(categories)

    # Вычисляем угол отклонения для каждой категории
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    ########################
    #
    #
    # построение профиля в радиальном отображении
    #
    #
    ########################

    # инициализируем построение функции в полярных координатах
    fig = plt.figure()
    ax = plt.axes(polar=True)

    # для нижнего подчеркивания
    params = {'mathtext.default': 'regular'}
    plt.rcParams.update(params)

    # название профиля
    plt.title("Микрореологический профиль пациента " + I_index[0])

    # сетка
    plt.grid(True, linestyle='dotted', alpha=0.5)

    # чтобы первая категория была сверху, то делаем так
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # нарисуем ось X + добавим подписи
    plt.xticks(angles[:-1], categories_new)

    # определим ось Y + добавим границы
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4], color="grey", size=0)
    plt.ylim(0, MAX_Y)

    ########################

    # параметры ПАЦИЕНТА
    values = df.loc[I_index[0]].values.tolist()
    values += values[:1]
    # стандартные отклонения для параметров пациента
    SD_values = SD_df.loc[I_index[0]].values.tolist()
    SD_values += SD_values[:1]
    # построение
    if pat_line:
        ax.plot(angles, values, linewidth=1.5, linestyle='solid', label=I_index[0], color=color_Patient)
    if pat_sd:
        PATIENT_fill = ax.fill_between(angles, y1=mul_err_plus(values, SD_values), y2=mul_err_minus(values, SD_values),
                                   alpha=0.3, linewidth=0, color=color_Patient)
    # сделаем аннотацию в процентах -- также выделим в цвета значения, если они выходят за пределы нормы
    for i in range(len(categories)):
        name = categories[i]
        if patient_data[name] - SD_patient_data[name] > norm_data[name] + SD_norm_data[name]:
            what_color = 'red'
        elif patient_data[name] + SD_patient_data[name] < norm_data[name] - SD_norm_data[name]:
            what_color = 'blue'
        else:
            what_color = 'black'
        ax.annotate(to_percent(values)[i], xy=(angles[i], MAX_Y), textcoords='data', size=8, color=what_color, ha='center',
                    va='center', bbox=dict(boxstyle='round', facecolor='w', edgecolor='black'))
    ########################
    # парметры НОРМЫ
    values_N = df.loc[I_index[1]].values.tolist()
    values_N += values_N[:1]
    # стандартные отклонения для параметров нормы
    SD_values_N = SD_df.loc[I_index[1]].values.tolist()
    SD_values_N += SD_values_N[:1]
    # построение
    if norm_line:
        ax.plot(angles, values_N, linewidth=1.5, linestyle='solid', label=I_index[1],color=color_NORM)
    if norm_sd:
        NORM_fill = ax.fill_between(angles, y1=mul_err_plus(values_N, SD_values_N), y2=mul_err_minus(values_N, SD_values_N),
                                alpha=0.3, linewidth=0, label=I_index[1], color=color_NORM)
    ########################

    ########################
    # Код ниже нужен для правильного расположения подписей
    rstep = int(ax.get_theta_direction())
    if rstep > 0:
        rmin = 0
        rmax = len(angles)
    else:
        rmin = len(angles) - 1
        rmax = -1

    for label, i in zip(ax.get_xticklabels(), range(rmin, rmax, rstep)):
        angle_rad = angles[i] + ax.get_theta_offset()
        if 0 < angle_rad <= pi / 2:
            ha = 'center'
            va = "bottom"
        elif pi / 2 < angle_rad <= pi:
            ha = 'right'
            va = "baseline"
        elif pi < angle_rad < (3 * pi / 2):
            ha = 'right'
            va = "top"
        elif angle_rad == (3 * pi / 2):
            ha = 'center'
            va = "top"
        elif 2 * pi > angle_rad > (3 * pi / 2):
            ha = 'left'
            va = "top"
        else:
            ha = 'left'
            va = "baseline"
        label.set_verticalalignment(va)
        label.set_horizontalalignment(ha)
    ########################

    # добавим легенды
    # ...основная легенда
    ax.legend(bbox_to_anchor=(0.0, 0.0))

    # имена параметров
    names_for_line = list(df.columns)
    names_for_line = change_name_of_categories(names_for_line)
    # параметры ПАЦИЕНТА + стандарное отклонение
    patien_values_for_line = to_percent_for_line(df.loc[I_index[0]].values.tolist(), 'mean')
    SD_patien_values_for_line = to_percent_for_line(SD_df.loc[I_index[0]].values.tolist(), 'SD')
    # параметры -- стандарное отклонение
    norm_values_for_line = to_percent_for_line(df.loc[I_index[1]].values.tolist(), 'mean')
    SD_norm_values_for_line = to_percent_for_line(SD_df.loc[I_index[1]].values.tolist(), 'SD')

    ########################
    #
    #
    # построение профиля в линейном отображении
    #
    #
    ########################

    # строим линейный график
    fig2 = plt.figure()
    ax2 = plt.axes()
    # вращаем на 90 градусов подписи
    plt.xticks(rotation='vertical')
    # сетка
    plt.grid(True, axis='x', linestyle='dashed', alpha=0.5)

    # подписи к осям
    plt.ylabel('Отклонение от нормы, %')

    # строим кривую для ПАЦИЕНТА
    if pat_line:
        ax2.plot(names_for_line, patien_values_for_line, color=color_Patient_line, label=I_index[0])
    if pat_sd:
        ax2.fill_between(names_for_line, y1=mul_err_plus(patien_values_for_line, SD_patien_values_for_line),
                     y2=mul_err_minus(patien_values_for_line, SD_patien_values_for_line), alpha=0.3, linewidth=0,
                     color=color_Patient_line)
    # строим кривую для НОРМЫ
    if norm_line:
        ax2.plot(names_for_line,norm_values_for_line, color=color_NORM_line, label = I_index[1])
    if norm_sd:
        ax2.fill_between(names_for_line, y1=mul_err_plus(norm_values_for_line, SD_norm_values_for_line),
                     y2=mul_err_minus(norm_values_for_line, SD_norm_values_for_line), alpha=0.3, linewidth=0,
                     color=color_NORM_line, label=I_index[1])

    # удалим отсупы по оси X -- если это нужно, то надо добавить строчку ниже
    # ax2.set_xlim(left=0, right=len(names_for_line)-1)
    # добавим легенду
    ax2.legend()

    try:
        # сохранение графика в радиальных координатах
        fig.savefig(path + I_index[0] + '.png', dpi=600, bbox_inches='tight')
        # сохранение графика в линейных координатах
        fig2.savefig(path + I_index[0] + '_line' + '.png', dpi=600, bbox_inches='tight')
        # очистим графики -- у меня почему-то без этого иногда графики при повторном построении накладывались
        ax.cla()
        ax2.cla()
        plt.clf()

        dlg.setWindowTitle("Микрореологический профиль - Успешное сохранение")
        dlg.setText("Профили успешно сохранились")
        dlg.exec()
        return None
    except Exception as e:
        # очистим графики -- у меня почему-то без этого иногда графики при повторном построении накладывались
        ax.cla()
        ax2.cla()
        plt.clf()

        dlg.setWindowTitle("Микрореологический профиль - Ошибка")
        dlg.setText("Профили не сохранились.\n" + str(e))
        dlg.exec()
        return None

#######
# доп. функции
#######

#функция превращения данных из буфера обмена в 2 словаря -- среднее и погрешность
def get_data_from_clipboard(just_DATA, self):

    if just_DATA=='norm':
        # словарь с значениями параметров нормы
        norm_data = {'CSS, мПа': 250, 'AI, %': 41, 'AMP': 0.0527, 'T1/2, сек.': 5.9, 'DI (3 Па)': 0.322,
                     'DI (20 Па)': 0.525, 'ВА, сек.': 6.6, 'СА, пН': 6.2, 'СД, пН': 3.36, 'СА/СД': 1.05, 'DA, %': 33,
                     'VA, %/мин': 30}
        # словарь с значениями стандартных отклонений параметров  нормы
        SD_norm_data = {'CSS, мПа': 20, 'AI, %': 2, 'AMP': 0.001, 'T1/2, сек.': 1, 'DI (3 Па)': 0.03,
                        'DI (20 Па)': 0.05, 'ВА, сек.': 1, 'СА, пН': 0.5, 'СД, пН': 0.2, 'СА/СД': 0.1, 'DA, %': 5,
                        'VA, %/мин': 5}
        return norm_data, SD_norm_data
    #данные, скопированные из exel -- 3 столбца: (1) параметры; (2) среднее; (3) погрешность
    #разделим данные по \t
    just_DATA=just_DATA.split("\t")
    #сделаем подготовку данных
    for i in range(1,len(just_DATA)):
        if i%2==0 and i != len(just_DATA)-1:
            just_DATA[i]=just_DATA[i].split("\n", 1)
            just_DATA[i][0]=just_DATA[i][0].replace(',','.')
        else:
            just_DATA[i]=just_DATA[i].replace(',','.')
            just_DATA[i] = just_DATA[i].replace('\n', '')
    #массив чтобы flatten данные
    clear_DATA = []
    #необходимый цикл, чтобы избавится от list of list
    for i in just_DATA:
        if type(i)==list and len(i)==2:
            clear_DATA.append(i[0])
            clear_DATA.append(i[1])
        elif type(i)==list and len(i)==1:
            clear_DATA.append(i[0])
        else:
            clear_DATA.append(i)
    if len(clear_DATA)%3!=0:
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Микрореологический профиль - Ошибка")
        dlg.setText("Введенными данные для микрореологического профиля не подходят. Данные должны представлять собой 3 столбца - параметр, среднее и стандартное отклонение")
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return None, None

    #сделаем 2 словаря (среднее и погрешность) на основе списка clear_DATA

    #словарь с значениями параметров пациентов
    patient_data = {}
    #словарь с значениями стандартных отклонений параметров  пациентов
    SD_patient_data = {}

    #заполним данные словари значениями
    k = 0
    while k < len(clear_DATA) - 1:
        patient_data[clear_DATA[k]] = float(clear_DATA[k+1])
        SD_patient_data[clear_DATA[k]] = float(clear_DATA[k+2])
        k=k+3
    return patient_data, SD_patient_data


#функция для вычисления положительного отклонения
def mul_err_plus(values, SD_values):
    dop=values.copy()
    SD_dop = SD_values.copy()
    for i in range(len(dop)):
        dop[i]=dop[i]+SD_dop[i]
    return dop


#функция для вычисления отрицательного отклонения
def mul_err_minus(values, SD_values):
    dop=values.copy()
    SD_dop = SD_values.copy()
    for i in range(len(dop)):
        dop[i]=dop[i]-SD_dop[i]
    return dop


#функция нахождения максимального значения
def find_max(dict_):
    max_=0.0
    for i in dict_:
        if max_<dict_[i]:
            max_= dict_[i]
    return max_


#функция перевода значения в %
def to_percent(list_):
    list_percent = []
    for i in list_:
        list_percent.append(str(int(round(i*100,0)))+'%')
    return list_percent


#функция перевода значения в относительные % для построения профиля в линейных координатах
def to_percent_for_line(list_,mean_or_SD):
    list_percent = []
    for i in list_:
        if mean_or_SD=='mean':
            list_percent.append((i-1)*100)
        if mean_or_SD=='SD':
            list_percent.append(i*100)
    return list_percent


#функция получения массива для построения гладкой линии
def smooth_curve(start, finish, up_limit):
    xxx=[]
    yyy=[]
    i=start
    while i<=finish:
        xxx.append(i)
        yyy.append(up_limit-0.1)
        i=i+0.05
    return xxx, yyy


#функция для переименования категорий для красоты некоторых параметров
def change_name_of_categories(categories):
    new = categories.copy()
    for i in range(len(new)):
        new[i]=new[i].replace('T1/2, сек.', '$T_{1/2}, сек.$')
    return new

