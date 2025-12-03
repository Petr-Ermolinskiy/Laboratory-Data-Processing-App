import math
from math import pi
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from PySide6.QtWidgets import QMessageBox


def prifile_plot(self) -> None:
    dlg = QMessageBox(self)
    # закроем все рисунки, если они открыты
    # если этого не сделать, то может быть такое, что рисунки наложатся друг на друга
    plt.close()
    #########################
    # параметры, которые нам понадобятся
    #########################
    # это цвета
    prifile_data__ = [
        self.ui.patient_prof.text(),
        self.ui.norm_prof.text(),
        self.ui.color_for_patient.text(),
        self.ui.color_for_norm.text(),
    ]
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
    # название для профилей
    title_rad = self.ui.profile_title_rad.text()
    y_line_title = self.ui.profile_title_lin.text()
    # название для профилей
    spin_x_for_lin_profile = self.ui.comboBox_profile_lin_spin.currentText()
    # легенда
    add_legend = self.ui.check_profile_legend.isChecked()
    # scale рисунка
    fond_scale_profile = self.ui.doubleSpinBoX_profile.value()
    #########################

    sns.reset_orig()
    # насколько шрифт изменяем
    sns.set(font_scale=fond_scale_profile)
    # это будет лучшим
    sns.set_style("ticks")

    # Первая группа -- пациент; Вторая группа -- это контрольная группа
    I_index = [prifile_data__[0], prifile_data__[1]]

    if path == "":
        dlg.setWindowTitle("Микрореологический профиль")
        dlg.setText("Не введен путь к сохранению графиков")
        dlg.exec()
        return

    path_obj = Path(path)
    if (
        len(prifile_data__[2]) != 7
        or len(prifile_data__[3]) != 7
        or prifile_data__[2][0] + prifile_data__[3][0] != "##"
    ):
        dlg.setWindowTitle("Микрореологический профиль - Ошибка")
        dlg.setText("Неправильные значения цветов HEX")
        dlg.exec()
        return
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
    if patient_d == "" or norm_d == "":
        dlg.setWindowTitle("Микрореологический профиль - Ошибка")
        dlg.setText("Введите данные для профилей")
        dlg.exec()
        return

    # получаем словарь для средних значений и стандартного отклонения для ПАЦИЕНТА
    patient_data, SD_patient_data = get_data_from_clipboard(patient_d, self)
    # проверка
    if patient_data == None or SD_patient_data == None:
        return
    # получаем словарь для средних значений и стандартного отклонения для НОРМЫ
    norm_data, SD_norm_data = get_data_from_clipboard(norm_d, self)
    # проверка
    if norm_data == None or SD_norm_data == None:
        return
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
    # создаём DataFrame со стандартными отклонениями нормированных значений пациента и нормы
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
    params = {"mathtext.default": "regular"}
    plt.rcParams.update(params)

    # название профиля
    if title_rad != "":
        plt.title(str(title_rad) + I_index[0])

    # сетка
    plt.grid(True, linestyle="dotted", alpha=0.5)

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
        ax.plot(
            angles,
            values,
            linewidth=1.5,
            linestyle="solid",
            label=I_index[0],
            color=color_Patient,
        )
    if pat_sd:
        label_line_sd_pat = I_index[0]
        if pat_line:
            label_line_sd_pat = None
        PATIENT_fill = ax.fill_between(
            angles,
            y1=mul_err_plus(values, SD_values),
            y2=mul_err_minus(values, SD_values),
            alpha=0.3,
            linewidth=0,
            label=label_line_sd_pat,
            color=color_Patient,
        )
    # сделаем аннотацию в процентах -- также выделим в цвета значения, если они выходят за пределы нормы
    for i in range(len(categories)):
        name = categories[i]
        if patient_data[name] - SD_patient_data[name] > norm_data[name] + SD_norm_data[name]:
            what_color = "red"
        elif patient_data[name] + SD_patient_data[name] < norm_data[name] - SD_norm_data[name]:
            what_color = "blue"
        else:
            what_color = "black"
        ax.annotate(
            to_percent(values, self.ui.check_profile_relative.isChecked())[i],
            xy=(angles[i], MAX_Y),
            textcoords="data",
            size=int(8 * fond_scale_profile),
            color=what_color,
            ha="center",
            va="center",
            bbox=dict(boxstyle="round", facecolor="w", edgecolor="black"),
        )
    ########################
    # параметры НОРМЫ
    values_N = df.loc[I_index[1]].values.tolist()
    values_N += values_N[:1]
    # стандартные отклонения для параметров нормы
    SD_values_N = SD_df.loc[I_index[1]].values.tolist()
    SD_values_N += SD_values_N[:1]
    # построение
    if norm_line:
        ax.plot(
            angles,
            values_N,
            linewidth=1.5,
            linestyle="solid",
            label=I_index[1],
            color=color_NORM,
        )
    if norm_sd:
        label_line_sd = I_index[1]
        if norm_line:
            label_line_sd = None
        NORM_fill = ax.fill_between(
            angles,
            y1=mul_err_plus(values_N, SD_values_N),
            y2=mul_err_minus(values_N, SD_values_N),
            alpha=0.3,
            linewidth=0,
            label=label_line_sd,
            color=color_NORM,
        )
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

    for label, i in zip(ax.get_xticklabels(), range(rmin, rmax, rstep), strict=False):
        angle_rad = angles[i] + ax.get_theta_offset()
        if 0 < angle_rad <= pi / 2:
            ha = "center"
            va = "bottom"
        elif pi / 2 < angle_rad <= pi:
            ha = "right"
            va = "baseline"
        elif pi < angle_rad < (3 * pi / 2):
            ha = "right"
            va = "top"
        elif angle_rad == (3 * pi / 2):
            ha = "center"
            va = "top"
        elif 2 * pi > angle_rad > (3 * pi / 2):
            ha = "left"
            va = "top"
        else:
            ha = "left"
            va = "baseline"
        label.set_verticalalignment(va)
        label.set_horizontalalignment(ha)
    ########################

    # добавим легенды
    # ...основная легенда
    if add_legend:
        ax.legend(bbox_to_anchor=(0.0, 0.0))

    ########################
    #
    #
    # добавим кастомное обозначение параметров, если это нужно
    #
    #
    ########################
    try:
        if self.ui.tableWidget.item(0, 0).text() != "":
            # Добавим информацию для типа измеряемых о параметрах (агрегация эритроцитов, деформируемость эритроцитов, и др.)
            # сортируем по категориям, где параметры агрегации или деформируемости или др. изменить индексы у angles по категориям
            # linestyle=dashed dashdot dotted
            EA_Rheo = self.ui.tableWidget.item(0, 0).text()
            EA_Rheo = EA_Rheo.split("-")
            EA_Rheo = list(map(int, EA_Rheo))
            # здесь агрегация эритроцитов или что-то другое
            name_n_1 = self.ui.tableWidget.item(1, 0).text()
            x, y = smooth_curve(angles[EA_Rheo[0]], angles[EA_Rheo[1]], MAX_Y)
            (line_EA_Rheo,) = ax.plot(
                x,
                y,
                linewidth=4,
                linestyle=self.ui.tableWidget.item(3, 0).text(),
                color=self.ui.tableWidget.item(2, 0).text(),
                label=name_n_1,
                alpha=0.4,
            )

            if self.ui.tableWidget.item(0, 1) != None:
                ED_Rheo = self.ui.tableWidget.item(0, 1).text()
                ED_Rheo = ED_Rheo.split("-")
                ED_Rheo = list(map(int, ED_Rheo))
                # здесь деформируемость эритроцитов или что-то другое
                name_n_2 = self.ui.tableWidget.item(1, 1).text()
                x, y = smooth_curve(angles[ED_Rheo[0]], angles[ED_Rheo[1]], MAX_Y)
                (line_ED_Rheo,) = ax.plot(
                    x,
                    y,
                    linewidth=4,
                    linestyle=self.ui.tableWidget.item(3, 1).text(),
                    color=self.ui.tableWidget.item(2, 1).text(),
                    label=name_n_2,
                    alpha=0.4,
                )

            if self.ui.tableWidget.item(0, 2) != None:
                PA_Biola = self.ui.tableWidget.item(0, 2).text()
                PA_Biola = PA_Biola.split("-")
                PA_Biola = list(map(int, PA_Biola))
                # здесь агрегация тромбоцитов или что-то другое
                name_n_3 = self.ui.tableWidget.item(1, 2).text()
                x, y = smooth_curve(angles[PA_Biola[0]], angles[PA_Biola[1]], MAX_Y)
                (line_PA_Biola,) = ax.plot(
                    x,
                    y,
                    linewidth=4,
                    linestyle=self.ui.tableWidget.item(3, 2).text(),
                    color=self.ui.tableWidget.item(2, 2).text(),
                    label=name_n_3,
                    alpha=0.4,
                )
            # добавим легенду
            if add_legend:
                ax.legend(bbox_to_anchor=(1.25, 0.95))
    except Exception as e:
        dlg.setWindowTitle("Микрореологический профиль")
        dlg.setText("Проблема с вводом данных в таблицу.\n" + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    # на всякий случай
    plt.tight_layout()

    # имена параметров
    names_for_line = list(df.columns)
    names_for_line = change_name_of_categories(names_for_line)
    # параметры ПАЦИЕНТА + стандартное отклонение
    patien_values_for_line = to_percent_for_line(df.loc[I_index[0]].values.tolist(), "mean")
    SD_patien_values_for_line = to_percent_for_line(SD_df.loc[I_index[0]].values.tolist(), "SD")
    # параметры -- стандартное отклонение
    norm_values_for_line = to_percent_for_line(df.loc[I_index[1]].values.tolist(), "mean")
    SD_norm_values_for_line = to_percent_for_line(SD_df.loc[I_index[1]].values.tolist(), "SD")

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
    plt.xticks(rotation=int(spin_x_for_lin_profile))
    # сетка
    plt.grid(True, axis="x", linestyle="dashed", alpha=0.5)

    # подписи к осям
    plt.ylabel(str(y_line_title))

    # строим кривую для ПАЦИЕНТА
    if pat_line:
        ax2.plot(names_for_line, patien_values_for_line, color=color_Patient_line, label=I_index[0])
    if pat_sd:
        label_line_sd_lin_pat = I_index[0]
        if pat_line:
            label_line_sd_lin_pat = None
        ax2.fill_between(
            names_for_line,
            y1=mul_err_plus(patien_values_for_line, SD_patien_values_for_line),
            y2=mul_err_minus(patien_values_for_line, SD_patien_values_for_line),
            alpha=0.3,
            linewidth=0,
            color=color_Patient_line,
            label=label_line_sd_lin_pat,
        )
    # строим кривую для НОРМЫ
    if norm_line:
        ax2.plot(names_for_line, norm_values_for_line, color=color_NORM_line, label=I_index[1])
    if norm_sd:
        label_line_sd_lin = I_index[1]
        if norm_line:
            label_line_sd_lin = None
        ax2.fill_between(
            names_for_line,
            y1=mul_err_plus(norm_values_for_line, SD_norm_values_for_line),
            y2=mul_err_minus(norm_values_for_line, SD_norm_values_for_line),
            alpha=0.3,
            linewidth=0,
            color=color_NORM_line,
            label=label_line_sd_lin,
        )

    # удалим отступы по оси X -- если это нужно, то надо добавить строчку ниже
    # ax2.set_xlim(left=0, right=len(names_for_line)-1)
    # добавим легенду
    if add_legend:
        ax2.legend()

    plt.tight_layout()

    try:
        # сохранение графика в радиальных координатах
        fig.savefig(str(path_obj / f"{I_index[0]}.png"), dpi=600, bbox_inches="tight")
        # сохранение графика в линейных координатах
        fig2.savefig(str(path_obj / f"{I_index[0]}_line.png"), dpi=600, bbox_inches="tight")
        # очистим графики -- у меня почему-то без этого иногда графики при повторном построении накладывались
        ax.cla()
        ax2.cla()
        plt.clf()

        dlg.setWindowTitle("Микрореологический профиль - Успешное сохранение")
        dlg.setText("Профили успешно сохранились")
        dlg.exec()
        return
    except Exception as e:
        # очистим графики -- у меня почему-то без этого иногда графики при повторном построении накладывались
        ax.cla()
        ax2.cla()
        plt.clf()

        dlg.setWindowTitle("Микрореологический профиль - Ошибка")
        dlg.setText("Профили не сохранились.\n" + str(e))
        dlg.exec()
        return


#######
# доп. функции
#######


# функция превращения данных из буфера обмена в 2 словаря -- среднее и погрешность
def get_data_from_clipboard(just_DATA, self) -> (dict, dict):
    if just_DATA == "norm":
        # словарь со значениями параметров нормы
        norm_data = {
            "CSS, мПа": 250,
            "AI, %": 41,
            "AMP": 0.0527,
            "T1/2, сек.": 5.9,
            "DI (3 Па)": 0.322,
            "DI (20 Па)": 0.525,
            "ВА, сек.": 6.6,
            "СА, пН": 6.2,
            "СД, пН": 3.36,
            "СА/СД": 1.05,
            "DA, %": 33,
            "VA, %/мин": 30,
        }
        # словарь со значениями стандартных отклонений параметров  нормы
        SD_norm_data = {
            "CSS, мПа": 20,
            "AI, %": 2,
            "AMP": 0.001,
            "T1/2, сек.": 1,
            "DI (3 Па)": 0.03,
            "DI (20 Па)": 0.05,
            "ВА, сек.": 1,
            "СА, пН": 0.5,
            "СД, пН": 0.2,
            "СА/СД": 0.1,
            "DA, %": 5,
            "VA, %/мин": 5,
        }
        return norm_data, SD_norm_data
    # данные, скопированные из exel -- 3 столбца: (1) параметры; (2) среднее; (3) погрешность
    # разделим данные по \t
    just_DATA = just_DATA.split("\t")
    # сделаем подготовку данных
    for i in range(1, len(just_DATA)):
        if i % 2 == 0 and i != len(just_DATA) - 1:
            just_DATA[i] = just_DATA[i].split("\n", 1)
            just_DATA[i][0] = just_DATA[i][0].replace(",", ".")
        else:
            just_DATA[i] = just_DATA[i].replace(",", ".")
            just_DATA[i] = just_DATA[i].replace("\n", "")
    # массив чтобы flatten данные
    clear_DATA = []
    # необходимый цикл, чтобы избавится от list of list
    for i in just_DATA:
        if type(i) == list and len(i) == 2:
            clear_DATA.append(i[0])
            clear_DATA.append(i[1])
        elif type(i) == list and len(i) == 1:
            clear_DATA.append(i[0])
        else:
            clear_DATA.append(i)
    if len(clear_DATA) % 3 != 0:
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Микрореологический профиль - Ошибка")
        dlg.setText(
            "Введенными данные для микрореологического профиля не подходят. Данные должны представлять собой 3 столбца - параметр, среднее и стандартное отклонение",
        )
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return None, None

    # сделаем 2 словаря (среднее и погрешность) на основе списка clear_DATA

    # словарь со значениями параметров пациентов
    patient_data = {}
    # словарь со значениями стандартных отклонений параметров  пациентов
    SD_patient_data = {}

    # заполним данные словари значениями
    k = 0
    while k < len(clear_DATA) - 1:
        patient_data[clear_DATA[k]] = float(clear_DATA[k + 1])
        SD_patient_data[clear_DATA[k]] = float(clear_DATA[k + 2])
        k = k + 3
    return patient_data, SD_patient_data


# функция для вычисления положительного отклонения
def mul_err_plus(values, SD_values):
    dop = values.copy()
    SD_dop = SD_values.copy()
    for i in range(len(dop)):
        dop[i] = dop[i] + SD_dop[i]
    return dop


# функция для вычисления отрицательного отклонения
def mul_err_minus(values, SD_values):
    dop = values.copy()
    SD_dop = SD_values.copy()
    for i in range(len(dop)):
        dop[i] = dop[i] - SD_dop[i]
    return dop


# функция нахождения максимального значения
def find_max(dict_):
    max_ = 0.0
    for i in dict_:
        max_ = max(max_, dict_[i])
    return max_


# функция перевода значения в %
def to_percent(list_, relative: bool):
    rel = 0
    if relative:
        rel = 100
    list_percent = []
    for i in list_:
        list_percent.append(str(int(round(i * 100 - rel, 0))) + "%")
    return list_percent


# функция перевода значения в относительные % для построения профиля в линейных координатах
def to_percent_for_line(list_, mean_or_SD):
    list_percent = []
    for i in list_:
        if mean_or_SD == "mean":
            list_percent.append((i - 1) * 100)
        if mean_or_SD == "SD":
            list_percent.append(i * 100)
    return list_percent


# функция получения массива для построения гладкой линии
def smooth_curve(start, finish, up_limit):
    xxx = []
    yyy = []
    i = start
    while i <= finish:
        xxx.append(i)
        yyy.append(up_limit - 0.1)
        i = i + 0.05
    return xxx, yyy


# функция для переименования категорий для красоты некоторых параметров
def change_name_of_categories(categories):
    new = categories.copy()
    for i in range(len(new)):
        new[i] = new[i].replace("T1/2, сек.", "$T_{1/2}, сек.$")
        new[i] = new[i].replace("\\n", "\n")
    return new
