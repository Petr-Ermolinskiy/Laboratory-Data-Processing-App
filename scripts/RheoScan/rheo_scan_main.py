import math
import os
from glob import glob

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.optimize as opt
from pandas import to_numeric
from PySide6.QtWidgets import QMessageBox
from scipy.integrate import trapz
from sklearn.metrics import r2_score


def all_rheo_scan_level(self) -> None:
    # закроем все рисунки, если они открыты
    # если этого не сделать, то может быть такое, что рисунки наложатся друг на друга
    plt.close()

    # это на каком мы уровне находимся
    level = self.ui.spinBox_level.value()
    # какой путь был введен пользователем
    path = self.ui.main_path.text()

    # сюда будут сохраняться все данные
    all_and_all = pd.DataFrame()

    # проходимся по каждому пути
    for path_for_one in get_subfolder_files_paths(level, path):
        check = main_thingy(self, path_for_one)
        if check[0] != 0:
            break
        all_and_all = pd.concat([all_and_all, check[1]], axis=1, ignore_index=False)
    # сохраняем общий массив
    if check[0] == 0 and self.ui.check_save_RheoScan_overall.isChecked():
        with pd.ExcelWriter(
            path + "\\" + "overall_data_" + path.split("\\")[-1] + ".xlsx"
        ) as writer:
            all_and_all.T.reset_index().drop(columns=["index"]).to_excel(
                writer,
                sheet_name="All_data",
            )
    if check[0] == 0:
        dlg = QMessageBox(self)
        dlg.setWindowTitle("RheoScan")
        dlg.setText("Все данные успешно записаны в excel/csv файл(ы)")
        dlg.exec()


def get_subfolder_files_paths(level: int, path: str, s: set | None = None) -> set:
    if s is None:
        s = set()

    if level == 1:
        s.add(path)
        return s

    for i in os.scandir(path):
        if i.is_dir():
            if level != 1:
                get_subfolder_files_paths(level - 1, i.path, s)
            else:
                s.add(i.path)

    return s


# основная функция для извлечения данных
def main_thingy(self, path_for_one) -> [int, pd.DataFrame]:
    dlg = QMessageBox(self)
    #########################
    # параметры, которые нам понадобятся
    #########################
    # данные для аппроксимации
    agg_approx_data__ = [
        self.ui.tua_1_agg.value(),
        self.ui.tua_2_agg.value(),
        self.ui.r2_def.value(),
        self.ui.spinBox_n_max_deform.value(),
    ]
    # изначальный путь
    path_r = self.ui.main_path.text()
    # проверка на флажки
    var_agg = self.ui.check_agg.isChecked()
    var_stress = self.ui.check_stress.isChecked()
    var_deform = self.ui.check_deform.isChecked()
    exel_ = self.ui.check_save_exel.isChecked()
    csv_ = self.ui.check_save_csv.isChecked()
    var_stat = self.ui.check_stat_for_column.isChecked()
    fiting_aggreg = self.ui.check_figs_for_agg.isChecked()
    var_fit = self.ui.check_approx_agg.isChecked()
    var_fit_deform = self.ui.check_approx_deform.isChecked()
    fiting_deform = self.ui.check_for_deform.isChecked()
    vibros_check = self.ui.vibros_delete.isChecked()
    save_only_one_name = self.ui.check_name_rheoscan.isChecked()
    save_raw_deform_data = self.ui.check_approx_deform_raw_data.isChecked()
    dop_css_parameter = self.ui.check_dop_CSS_parameter.isChecked()
    # позиция имени, которое будет сохранено
    name_position = self.ui.spinBox_check_name_rheoscan.value()
    # разделитель данных
    sep_r = self.ui.separator_for_data.text()
    # отклонение на сколько интерквартильных размаха считать выбором
    iqr_val = self.ui.iqr_vibros.value()
    #########################

    # для того чтобы избежать ошибок
    all_def_des, all_CSS_des, fit_res_des, all_agg_des, fit_res_deform_des = (
        pd.DataFrame(index=["mean"]),
        pd.DataFrame(index=["mean"]),
        pd.DataFrame(index=["mean"]),
        pd.DataFrame(index=["mean"]),
        pd.DataFrame(index=["mean"]),
    )

    # это путь к папке, в которой должны быть следующие подпапки: agg, stress, deform.
    path = path_for_one
    if path == "":
        dlg.setWindowTitle("RheoScan")
        dlg.setText("Не введен путь к подпапкам")
        dlg.exec()
        return [1, pd.DataFrame()]
    path = path + "\\"
    # имя файла
    name_of_patient = path.split("\\")[-2]
    # подпапки
    path_agg = path + "agg//"
    path_css = path + "stress//"
    path_def = path + "deform//"
    # массив всех txt файлов во всех подпапках
    files_agg = glob(path_agg + "*.txt")
    files_css = glob(path_css + "*.txt")
    files_def = glob(path_def + "*.txt")
    if files_agg == [] and files_css == [] and files_def == []:
        dlg.setWindowTitle("RheoScan - Ошибка")
        dlg.setText(f"По пути {path} либо нет подпапок, либо в этих подпапках нет txt файлов")
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return [1, pd.DataFrame()]

    # сохраняем файл в какой-то из двух форматов exel или csv
    saving_s_exel = exel_
    saving_s_csv = csv_
    # как разделить имя для последующей обработки - оставить пустым, если не нужно
    how_to_split = sep_r
    # нужна ли статистика по столбцам? 0 - нет, 1 - да
    stat_need = var_stat

    """
    Маленькая кювета - AI, T1/2, AMP
    """
    if var_agg and files_agg != []:
        # Data Frame для маленькой кюветы (AI, T1/2, AMP)
        all_agg = pd.DataFrame()
        # прочитать все файлы и добавить данные в DataFrame
        for i in files_agg:
            # правильный срез данных
            try:
                all_lines_agg = sum(1 for line in open(i))
            except Exception as e:
                dlg.setWindowTitle("RheoScan")
                dlg.setText("Ошибка в чтении файла:\n" + i + "\n" + str(e))
                dlg.exec()
                return [1, pd.DataFrame()]
            # прочитать каждый файл и извлечь данные
            x = pd.read_table(
                i,
                skipfooter=all_lines_agg - 13,
                engine="python",
                header=None,
                decimal=",",
            )
            yy = x.drop([0, 2, 3, 4, 9, 10])
            jj = yy[0].apply(lambda x: pd.Series(x.split(":"))).T
            all_agg = all_agg.append(jj.loc[1], ignore_index=True)
        all_agg.columns = ["Patient", "AI", "T1/2", "AMP", "M"]
        # изменить ',' на '.'
        all_agg = all_agg.replace(",", ".", regex=True)
        # преобразовать тип данных для всех параметров за исключением 'Patient'
        all_agg["AI"] = all_agg["AI"].astype(float)
        all_agg["T1/2"] = all_agg["T1/2"].astype(float)
        all_agg["AMP"] = all_agg["AMP"].astype(float)
        all_agg["M"] = all_agg["M"].astype(float)

        # обновить индекс
        all_agg = all_agg.reset_index(drop=True)

    """
    Аппроксимировать полученные кривые - t1, t2
    """

    if fiting_aggreg:
        # создаем подпапку для графиков аппроксимации
        name_of_agg_fit_folder = "!Fit agg fiqures"
        path_for_agg_fit = path + name_of_agg_fit_folder
        os.makedirs(path_for_agg_fit, exist_ok=True)

    if var_fit and files_agg != []:
        # Data Frame для апроксимации
        fit_res = pd.DataFrame(
            columns=[
                "Patient",
                "y0",
                "A1",
                "A2",
                "A1+A2",
                "t1",
                "t2",
                "assim",
                "R^2",
                "AI (2.5 sec.), %",
                "AI (5 sec.), %",
                "AI (10 sec.), %",
                "AI (50 sec.), %",
                "AI (100 sec.), %",
                "AI (max), %",
            ],
        )
        # индекс для сохранения
        jkd = 1

        # функция, которой аппроксимируется кривая
        def f(x, y0, A1, A2, t1, t2):
            return y0 + A1 * np.exp(-(x / t1)) + A2 * np.exp(-(x / t2))

        # код, который позволяет аппроксимировать кривые и сохраняет результат аппроксимации в файл
        for i in files_agg:
            ############
            # правильный срез данных для имени
            all_lines_agg = sum(1 for line in open(i))
            # прочтатать каждый файл и извлечь данные имени
            x_agg_name = pd.read_table(
                i,
                skipfooter=all_lines_agg - 3,
                engine="python",
                header=None,
                decimal=",",
            )
            Name_fit_agg = x_agg_name.iloc[1, 0].split(":")[1]
            ############
            x = pd.read_table(i, skiprows=22, header=None, decimal=",")
            try:
                x.columns = ["Time, s", "Raw data, a.u.", "Approx. data, a.u."]
                x = x.replace({",": "."}, regex=True)
                for col_name in x.columns:
                    x[col_name] = pd.to_numeric(x[col_name], errors="coerce")
            except Exception as e:
                dlg.setWindowTitle("RheoScan - ошибка аппроксимации")
                dlg.setText("Ошибка чтения данных из файла:\n" + str(i) + "\n" + str(e))
                dlg.setIcon(QMessageBox.Icon.Critical)
                dlg.exec()
                return [1, pd.DataFrame()]
            # находим assim
            Up = x["Raw data, a.u."][0]
            Bottom = x["Raw data, a.u."].min()
            Bottom_index = x["Raw data, a.u."].idxmin()
            # assim -- это скорее ассиметрия эритроцитов
            assim = Up - Bottom
            # Непосредственно сама аппроксимация (функция opt.curve_fit). Если вдруг не удается хорошо аппроксимировать ф-ию, надо изменить bounds
            # среда может жаловаться, что Too many values to unpack, но тут всё хорошо
            (y0_, A1_, A2_, t1_, t2_), _ = opt.curve_fit(
                f,
                x["Time, s"][Bottom_index + 3 :],
                x["Raw data, a.u."][Bottom_index + 3 :],
                bounds=(
                    (0, -10, -10, 0, 0),
                    (10, 10, 10, float(agg_approx_data__[0]), float(agg_approx_data__[1])),
                ),
            )
            # расчет r^2
            r2 = r2_score(f(x["Time, s"], *[y0_, A1_, A2_, t1_, t2_]), x["Raw data, a.u."])

            # далее вычислим AI по сырым данным -- если выходим за пределы дата фрейма, то просто возвращаем None
            def calc_ai_index_in_percent(data_frame, time, bottom_index):
                try:
                    integral_raw = trapz(
                        data_frame.iloc[bottom_index : bottom_index + int(time * 10), 1]
                        - data_frame.iloc[:, 1].min(),
                        data_frame.iloc[bottom_index : bottom_index + int(time * 10), 0],
                    )
                    # индекс агрегации определяется, не просто как отношение: площадь под кривой к площади прямоугольника,
                    # а как к площади прямоугольника, верхняя сторона которого лежит на линии MAX значений
                    # для просто прямоугольника надо раскомментировать строчку ниже
                    integral_rect = (
                        data_frame.iloc[:, 1].max() - data_frame.iloc[:, 1].min()
                    ) * time
                    return integral_raw / integral_rect * 100
                except:  # noqa: E722
                    return None

            # Индексы агрегации для 5 сек., 10 сек., 50 сек., 100 сек.
            ai_index_2_5 = calc_ai_index_in_percent(x, 2.5, Bottom_index)
            ai_index_5 = calc_ai_index_in_percent(x, 5, Bottom_index)
            ai_index_10 = calc_ai_index_in_percent(x, 10, Bottom_index)
            ai_index_50 = calc_ai_index_in_percent(x, 50, Bottom_index)
            ai_index_100 = calc_ai_index_in_percent(x, 100, Bottom_index)
            ai_index_max = calc_ai_index_in_percent(x, math.floor(len(x) / 10) - 1, Bottom_index)

            # сохранение значений аппроксимации в строку и далее в Data Frame
            fit_res.loc[jkd] = (
                Name_fit_agg,
                y0_,
                abs(A1_),
                abs(A2_),
                abs(A1_) + abs(A2_),
                t1_,
                t2_,
                assim,
                r2,
                ai_index_2_5,
                ai_index_5,
                ai_index_10,
                ai_index_50,
                ai_index_100,
                ai_index_max,
            )
            jkd += 1
            if fiting_aggreg:
                #####################################
                # графики делаем по аппроксимации
                fig, ax = plt.subplots()
                fig.patch.set_facecolor("white")
                plt.plot(x["Time, s"], x["Raw data, a.u."], "b-")
                plt.plot(x["Time, s"], f(x["Time, s"], y0_, A1_, A2_, t1_, t2_), "r-")
                plt.legend(("Raw Data", "Fit Data"))
                plt.title(Name_fit_agg + " (r2=" + str(round(r2, 3)) + ")")
                plt.xlabel("Время, с")
                plt.ylabel("Светопропускание, отн.ед.")
                # сохраняем все рисунки в отдельную папку
                fig.savefig(path_for_agg_fit + "\\" + Name_fit_agg + ".png", dpi=600, format="png")

                # закрываем и всё очищаем
                plt.close()
                ax.cla()
                plt.clf()
                #####################################
        fit_res = fit_res.reset_index(drop=True)
        #####################################
    """
    Большая кювета - CSS
    """
    if var_stress and files_css != []:
        # Data Frame для большой кюветы (CSS)
        all_CSS = pd.DataFrame()
        # прочитать все файлы и добавить данные в DataFrame
        for i in files_css:
            # правильный срез данных
            try:
                all_lines_CSS = sum(1 for line in open(i))
            except Exception as e:
                dlg.setWindowTitle("RheoScan")
                dlg.setText("Ошибка в чтении файла:\n" + i + "\n" + str(e))
                dlg.exec()
                return [1, pd.DataFrame()]
            # прочитать каждый файл и извлечь данные
            x = pd.read_table(
                i,
                skipfooter=all_lines_CSS - 15,
                header=None,
                decimal=",",
                index_col=False,
                engine="python",
            )
            data_css = x.drop([0, 2, 3, 4, 5, 6, 7, 8, 11])
            data_css = data_css[0].apply(lambda x: pd.Series(x.split(":"))).T
            if dop_css_parameter:
                ############
                # читаем все остальные данные - новый параметр
                ############
                new_css_parameter = pd.read_table(
                    i,
                    skiprows=17,
                    decimal=",",
                    engine="python",
                    header=None,
                )
                # индекс максимальная интенсивность
                max_int_css_index = new_css_parameter.iloc[:, 2].idxmax()
                max_int_css_index -= 5
                # индекс, когда shear stress был порядка 2 Па
                index_min = new_css_parameter[new_css_parameter[3] < 2].index.min()
                try:
                    # аппроксимация - среда может жаловаться, что "Too many values to unpack", но тут всё хорошо
                    (_, _, new_parameter), _ = opt.curve_fit(
                        lambda t, a, b, c: a + b * np.exp(-t / c),
                        new_css_parameter[3][index_min:max_int_css_index],
                        new_css_parameter[2][index_min:max_int_css_index],
                    )
                except Exception as e:
                    dlg.setWindowTitle("RheoScan - Ошибка")
                    dlg.setText(
                        f"Проблема при аппроксимации данных CSS в файле по пути:\n{i}\n"
                        + str(e)
                        + "\nПродолжить обсчет?",
                    )
                    dlg.setIcon(QMessageBox.Icon.Critical)
                    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    ret = dlg.exec()

                    if ret == QMessageBox.Yes:
                        new_parameter = 0
                    else:
                        return [1, pd.DataFrame()]

                # добавляем всё в датафрейм
                all_CSS = all_CSS.append(
                    pd.concat([data_css.loc[1], pd.Series(data=str(new_parameter))], axis=0),
                    ignore_index=True,
                )
            else:
                # добавляем всё в датафрейм
                all_CSS = all_CSS.append(data_css.loc[1])

        if dop_css_parameter:
            all_CSS.columns = ["Patient", "Critical time, s", "CSS", "New parameter, Pa"]
        else:
            all_CSS.columns = ["Patient", "Critical time, s", "CSS"]
        # делаем всё то же самое, что и для обработки для маленькой кюветы
        all_CSS = all_CSS.applymap(lambda x: str(x.replace(",", ".")))
        # преобразовать тип данных для всех параметров за исключением 'Patient'
        all_CSS["Critical time, s"] = all_CSS["Critical time, s"].astype(float)
        all_CSS["CSS"] = all_CSS["CSS"].astype(float)
        if dop_css_parameter:
            all_CSS["New parameter, Pa"] = all_CSS["New parameter, Pa"].astype(float)
            # изменить порядок -- для простоты
            all_CSS = all_CSS[["Patient", "CSS", "Critical time, s", "New parameter, Pa"]]
        else:
            # изменить порядок -- для простоты
            all_CSS = all_CSS[["Patient", "CSS", "Critical time, s"]]
        # обновить индекс
        all_CSS = all_CSS.reset_index(drop=True)

    """
    Большая кювета - деформируемость
    """
    if var_deform and files_def != []:
        # Data Frame для значений сдвиговых напряжений (в Па)
        xxx = pd.DataFrame({"Pa": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20]})
        xxx = xxx.T
        # Data Frame для значений деформируемости
        all_def = pd.DataFrame()
        # Data Frame для только для имен (для дальнейшего объединения) -- нельзя их сразу объединить, потому что имя находится в другом месте и одновременно не прочитать
        all_def_name = pd.DataFrame(columns=["Patient"])
        # прочитать все файлы и добавить данные в DataFrame
        for i in files_def:
            # правильный срез данных
            try:
                all_lines_def = sum(1 for line in open(i))
            except Exception as e:
                dlg.setWindowTitle("RheoScan")
                dlg.setText("Ошибка в чтении файла:\n" + i + "\n" + str(e))
                dlg.exec()
                return [1, pd.DataFrame()]
            # прочитать каждый файл и извлечь данные
            x = pd.read_table(
                i,
                skiprows=all_lines_def - 14,
                header=None,
                decimal=",",
                index_col=False,
                engine="python",
            )
            # всё для того, чтобы не было Inf
            x[1] = x[1].astype(float)
            # убираем повторяющееся значение
            data_def = x.drop([1])
            all_def = all_def.append(data_def[1])
            # Data Frame для имени
            newx = pd.read_table(
                i,
                skipfooter=50,
                header=None,
                decimal=",",
                index_col=False,
                engine="python",
            )
            newx_x = newx.loc[1]
            s_x = "".join(newx_x)
            new_str_x = s_x.replace("Patient name:", "")
            all_def_name = all_def_name.append({"Patient": new_str_x}, ignore_index=True)
        # меняем подписи по колонкам
        all_def.columns = [
            "1 Pa",
            "2 Pa",
            "3 Pa",
            "4 Pa",
            "5 Pa",
            "6 Pa",
            "7 Pa",
            "8 Pa",
            "10 Pa",
            "12 Pa",
            "15 Pa",
            "17 Pa",
            "20 Pa",
        ]
        all_def = all_def.reset_index(drop=True)
        all_def.insert(loc=0, column="Patient", value=all_def_name["Patient"])

        ################################################
        # выбрасываем все колонки, где есть Inf и/или Nan
        i_o = 0
        i_end = len(all_def)
        while i_o < i_end:
            count_inf = np.isinf(all_def.iloc[i_o].to_numpy()[1:].astype(float)).any()
            count_nan = np.isnan(all_def.iloc[i_o].to_numpy()[1:].astype(float)).any()
            if count_inf + count_nan:
                all_def = all_def.drop(labels=i_o, axis=0)
                all_def = all_def.reset_index(drop=True)
                i_end = i_end - 1
            i_o += 1
    """
    Апроксимировать полученные кривые - вязкость внутриклеточного содержимого и предел текучести
    """
    if fiting_deform:
        # создаем подпапка для графиков аппроксимации
        name_of_def_fit_folder = "!Fit def fiqures"
        path_for_def_fit = path + name_of_def_fit_folder
        os.makedirs(path_for_def_fit, exist_ok=True)

    if var_fit_deform and files_def != []:
        # Data Frame для аппроксимации
        fit_res_deform = pd.DataFrame(
            {
                "Patient": [],
                "r^2": [],
                "nn": [],
                "Yield strength": [],
                "Viscosity": [],
                "Extrapol": [],
                "Slope": [],
            },
        )

        # функция, которой будем аппроксимировать - линейная функция от логарифма напряжений сдвига!
        def f(x: float, a: float, b: float):
            """Линейная функция."""
            return a * x + b

        # дополнительный Data Frame для сдвиговых напряжений
        one1 = pd.DataFrame(
            {1: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0, 15.0, 17.0, 20.0]},
        )
        one1 = one1.T
        # дополнительный Data Frame для сдвиговых напряжений в логарифме
        one2 = one1.applymap(lambda x: str(math.log10(x))).T
        one2 = one2.apply(to_numeric)
        # Data Frame для всех полученных данных
        # r_sq - для накопления всех данных
        r_sq = pd.DataFrame(
            {
                "Patient": [],
                "r^2": [],
                "nn": [],
                "Yield strength": [],
                "Viscosity": [],
                "Extrapol": [],
                "Slope": [],
                "r^2-dop": [],
            },
        )
        # r_sq_seq - для накопления значений аппроксимаций только для одного файла, через которое происходит выделения только тех значений аппроксимации, для которых R^2 максимален
        r_sq_seq = pd.DataFrame(
            {
                "Patient": [],
                "r^2": [],
                "nn": [],
                "Yield strength": [],
                "Viscosity": [],
                "Extrapol": [],
                "Slope": [],
                "r^2-dop": [],
            },
        )
        # количество плохих файлов
        sum_bad_files = 0

        for i in files_def:
            # правильный срез данных
            all_lines_def_dop = sum(1 for line in open(i))
            # прочитать каждый файл и извлечь данные
            x = pd.read_table(
                i,
                skiprows=all_lines_def_dop - 14,
                header=None,
                decimal=",",
                index_col=False,
                engine="python",
            )
            # всё для того, чтобы не было Inf
            x[1] = x[1].astype(float)
            # убираем повторяющееся значение
            data_def_approx = x.drop([1])
            # проверка, что файл не поврежден
            count_inf = np.isinf(data_def_approx[1]).values.any()
            count_nan = np.isnan(data_def_approx[1]).values.any()
            sum_count = count_inf + count_nan
            if sum_count:
                sum_bad_files += 1
                continue
            # дополнительно делаем Data Frame для того, чтобы сохранить имя
            xip = pd.read_table(
                i,
                skipfooter=50,
                header=None,
                decimal=",",
                index_col=False,
                engine="python",
            )
            iopp = xip.loc[1]
            sss = "".join(iopp)
            ttt = sss.replace("Patient name:", "")
            # df2 - непосредственно значения индекса элонгации для последующей аппроксимации
            df2 = data_def_approx[1]
            # one3 - непосредственно значения сдвиговых напряжений для последующей аппроксимации
            one3 = one2[1]
            # количество значений индекса элонгации -- всего 13
            n = len(df2)
            # обновить индексы для перестаховки
            df2 = df2.reset_index(drop=True)
            one3 = one3.reset_index(drop=True)
            # обнулить r_sq_seq, чтобы потом в него записать значение с max R^2
            r_sq_seq = r_sq_seq.iloc[0:0]
            # далее цикл, в котором апроксимируются значения индекса элонгации, и если R^2 <0.95, то ищется точка с максимальной ошибкой, она выбрасывается, и заново проводится аппроксимация
            while True:
                # непосредственно сама аппроксимация
                popt, pcov = opt.curve_fit(f, one3, df2)
                # расчет r^2 -- именно этот r^2 используется
                residuals = df2 - f(one3, *popt)
                ss_res = np.sum(residuals**2)
                ss_tot = np.sum((df2 - np.mean(df2)) ** 2)
                r_squared = 1 - (ss_res / ss_tot)
                # дополнительный расчет r^2 -- более простой в воплощении, но немного не верный,
                # т.к. шкала у нас нелинейная и точки расположены относительно друг от друга на разном расстоянии
                r222 = r2_score(f(one3, *popt), df2)
                # Найти точку с максимальной ошибкой среди всех
                dop_val = residuals**2
                max_ind = dop_val.idxmax()
                # получить из данных аппроксимации значения вязкости внутриклеточного содержимого и предела текучести
                viscosity = 1 / popt[0]
                yieldd = pow(10, -popt[1] / popt[0])
                # также в отдельные переменные поместим сами значения аппроксимации
                extra = popt[1]
                sslope = popt[0]
                # добавим полученные данные в наши Data Frame
                r_sq = r_sq.append(
                    {
                        "Patient": ttt,
                        "r^2": r_squared,
                        "nn": n,
                        "Yield strength": yieldd,
                        "Viscosity": viscosity,
                        "Extrapol": extra,
                        "Slope": sslope,
                        "r^2-dop": r222,
                    },
                    ignore_index=True,
                )
                r_sq_seq = r_sq_seq.append(
                    {
                        "Patient": ttt,
                        "r^2": r_squared,
                        "nn": n,
                        "Yield strength": yieldd,
                        "Viscosity": viscosity,
                        "Extrapol": extra,
                        "Slope": sslope,
                        "r^2-dop": r222,
                    },
                    ignore_index=True,
                )

                if n < agg_approx_data__[3] or r_squared > float(agg_approx_data__[2]):
                    if fiting_deform:
                        #####################################
                        # графики делаем по аппроксимации
                        fig, ax = plt.subplots()
                        fig.patch.set_facecolor("white")
                        plt.plot(
                            one3,
                            df2,
                            linestyle="-",
                            marker="o",
                            color="k",
                            markerfacecolor="#0f1569",
                        )
                        plt.plot(one3, f(one3, sslope, extra), "r-")
                        plt.legend(("Raw Data", "Fit Data"))
                        plt.title(ttt + " (r2=" + str(round(r_squared, 3)) + ")")
                        plt.xlabel("Сдвиговое напряжение, Log10(Па)")
                        plt.ylabel("Индекс деформируемости, отн.ед.")
                        # сохраняем все рисунки в отдельную папку
                        fig.savefig(path_for_def_fit + "\\" + ttt + ".png", dpi=600, format="png")
                        # закрываем и всё очищаем
                        plt.close()
                        ax.cla()
                        plt.clf()
                        #####################################
                    break
                # уберем точку с максимальной ошибкой по индексу элонгации
                df2.pop(max_ind)
                # уберем точку с максимальной ошибкой по сдвиговому напряжению
                one3.pop(max_ind)
                # обновляем индексы! это очень важно, иначе просто у вас неправильно всё посчитается
                df2 = df2.reset_index(drop=True)
                one3 = one3.reset_index(drop=True)
                # уменьшаем на 1 количество точек и если убрано больше 3 точек или R^2 больше 0.95, то останавливаемся и выходим из цикла
                n -= 1
            # выбираем только значение с максимальным R^2 - находим индекс с максимальным R^2
            max_value_index = r_sq_seq["r^2"].idxmax()
            # по индексу максимального значения находим само значения и записываем всю строку в наш изначальный Data Frame
            fit_res_deform = fit_res_deform.append(r_sq_seq.loc[max_value_index])
        # обновляем индексы
        fit_res_deform = fit_res_deform.reset_index(drop=True)
        # сохранить только те значения, для которых R^2>0.95
        fit_res_deform = fit_res_deform[fit_res_deform["r^2"] >= 0.95]
        # и ещё раз обновляем индексы (нужно чтобы после выбрашенных значений был четкий порядок)
        fit_res_deform = fit_res_deform.reset_index(drop=True)
        # изменить порядкок -- красоты, чтобы R^2 был справа
        fit_res_deform = fit_res_deform[
            ["Patient", "nn", "Yield strength", "Viscosity", "Extrapol", "Slope", "r^2", "r^2-dop"]
        ]
        # изменить порядкок -- красоты, чтобы R^2 был справа
        r_sq = r_sq[
            ["Patient", "nn", "Yield strength", "Viscosity", "Extrapol", "Slope", "r^2", "r^2-dop"]
        ]

    """
    Удаляем выбросы, если их нужно удалить дополнительные массивы для статистики
    """
    if vibros_check:
        if var_agg and files_agg != []:
            out_lets_quartile(all_agg, iqr_val)
        if var_fit and files_agg != []:
            out_lets_quartile(fit_res, iqr_val)
        if var_stress and files_css != []:
            out_lets_quartile(all_CSS, iqr_val)
        if var_deform and files_def != []:
            out_lets_quartile(all_def, iqr_val)
        if var_fit_deform and files_def != []:
            out_lets_quartile(fit_res_deform, iqr_val)
    """
    Дополнительные массивы для статистики
    """
    if var_agg and files_agg != []:
        all_agg_des = all_agg.describe()
    if var_fit and files_agg != []:
        fit_res_des = fit_res.describe()
    if var_stress and files_css != []:
        all_CSS_des = all_CSS.describe()
    if var_deform and files_def != []:
        all_def_des = all_def.describe()
    if var_fit_deform and files_def != []:
        fit_res_deform_des = fit_res_deform.describe()

    """
    Разделение имен (для индекса при построении)
    """

    # функция для того, чтобы разделить столбец 'Patient'

    """
            if how_to_split != '' and how_to_split.split('=')[0] == 'symbols':
                if type(how_to_split.split('=')[1]) == int:
                    jj.loc[1][1] = jj.loc[1][1][0:int(how_to_split.split('=')[1])]
                else:
                    pass
    """

    def splitting(all_split, self):
        # также можно оставить только определенное количество символов
        if how_to_split.split("=")[0] == "symbols":
            if how_to_split.split("=")[1].isdigit():
                all_split["Patient"] = all_split["Patient"].map(
                    lambda x: x[0 : 1 + int(how_to_split.split("=")[1])],
                )
            else:
                pass
        try:
            for_index_stuff = all_split["Patient"].str.split(how_to_split, expand=True)
            if save_only_one_name:
                all_split["Patient"] = for_index_stuff[name_position - 1]
            else:
                # лучше не использовать следующее, а то значения поплывут (могут поплыть): for_index_stuff=for_index_stuff.reset_index(drop=True)
                # если можно разделить на больше столбцов, то делим!
                if len(for_index_stuff.columns) > 2:
                    all_split.insert(loc=1, column="Name_3", value=for_index_stuff[2])
                if len(for_index_stuff.columns) > 1:
                    all_split.insert(loc=1, column="Name_2", value=for_index_stuff[1])
                all_split.insert(loc=1, column="Name_1", value=for_index_stuff[0])
        except Exception as e:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("RheoScan - Ошибка")
            dlg.setText(
                "Не удалось разделить имена по разделителю.\nПуть "
                + str(path)
                + "\n Ошибка: "
                + str(e),
            )
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()

    # применяем эту функцию ко всем Data Frame, которые нас интересуют
    if how_to_split != "":
        if var_agg and files_agg != []:
            splitting(all_agg, self)
        if var_stress and files_css != []:
            splitting(all_CSS, self)
        if var_deform and files_def != []:
            splitting(all_def, self)
        if var_fit and files_agg != []:
            splitting(fit_res, self)
        if var_fit_deform and files_def != []:
            splitting(fit_res_deform, self)
    """
    Обновление индексов
    """
    # сделаем так, чтобы индекс начинался с 1, а не с 0
    if var_agg and files_agg != []:
        all_agg.index += 1
    if var_fit and files_agg != []:
        fit_res.index += 1
    if var_stress and files_css != []:
        all_CSS.index += 1
    if var_deform and files_def != []:
        all_def.index += 1
    if var_fit_deform and files_def != []:
        fit_res_deform.index += 1
        r_sq.index += 1

    """
    Выделение ячеек цветом -- только для аппроксимации agg
    """
    # выделим ячейки с R^2 < 0.99 для дальнейшей проверки по графикам -- сначала идёт функция для выделения, а в дальнейшем применяем эту функцию к DataFrame
    if var_fit and files_agg != []:

        def highlight(df, col2highlite="R^2"):
            ret = pd.DataFrame("", index=df.index, columns=df.columns)
            ret.loc[df["R^2"] < 0.99, col2highlite] = "background-color: red"
            return ret

        # применяем функцию к DataFrame 'fit_res'
        fit_res_without = fit_res.copy()
        fit_res = fit_res.style.apply(highlight, col2highlite="R^2", axis=None)
    """
    Сохранение
    """
    # если нужно, то сохраняем файлы не по подпапкам, а в одном месте
    path_of_the_folder = path
    if (
        self.ui.comboBox_RheoScan_path_save.currentText()
        == "Сохранить excel/cvs файлы в одном месте"
    ):
        path = path_r + "\\"
    # сохраняем все полученные данные
    try:
        if saving_s_exel:
            with pd.ExcelWriter(path + name_of_patient + ".xlsx") as writer:
                if var_agg and files_agg != []:
                    all_agg.to_excel(writer, index_label="Номер", sheet_name="Agg")
                    if stat_need:
                        all_agg_des.to_excel(writer, index_label="Номер", sheet_name="Agg-Stat")
                if var_fit and files_agg != []:
                    fit_res.to_excel(writer, index_label="Номер", sheet_name="Agg-Fit")
                    if stat_need:
                        fit_res_des.to_excel(writer, index_label="Номер", sheet_name="Agg-Fit-Stat")
                if var_stress and files_css != []:
                    all_CSS.to_excel(writer, index_label="Номер", sheet_name="CSS")
                    if stat_need:
                        all_CSS_des.to_excel(writer, index_label="Номер", sheet_name="CSS-Stat")
                if var_deform and files_def != []:
                    all_def.to_excel(writer, index_label="Номер", sheet_name="Deform")
                    if stat_need:
                        all_def_des.to_excel(writer, index_label="Номер", sheet_name="Deform-Stat")
                if var_fit_deform and files_def != []:
                    fit_res_deform.to_excel(writer, index_label="Номер", sheet_name="Deform-Fit")
                    if stat_need:
                        fit_res_deform_des.to_excel(
                            writer,
                            index_label="Номер",
                            sheet_name="Deform-Fit-Stat",
                        )
                    if save_raw_deform_data:
                        r_sq.to_excel(writer, index_label="Номер", sheet_name="Deform-Fit-Raw")
        if saving_s_csv:
            if var_agg and files_agg != []:
                all_agg.to_csv(path + "Agg" + "__" + name_of_patient + ".csv")
            if var_fit and files_agg != []:
                fit_res_without.to_csv(path + "Agg-Fit" + "__" + name_of_patient + ".csv")
            if var_stress and files_css != []:
                all_CSS.to_csv(path + "CSS" + "__" + name_of_patient + ".csv")
            if var_deform and files_def != []:
                all_def.to_csv(path + "Deform" + "__" + name_of_patient + ".csv")
            if var_fit_deform and files_def != []:
                fit_res_deform.to_csv(path + "Deform-Fit" + "__" + name_of_patient + ".csv")
    except Exception as e:
        dlg.setWindowTitle("RheoScan - Ошибка сохранения")
        dlg.setText(
            "Скорее всего у вас сейчас открыт файл, который программа хочет перезаписать, или неправильно указан уровень подпапок.\n"
            + str(e),
        )
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return [1, pd.DataFrame()]
    return [
        0,
        pd.concat(
            [
                pd.Series(
                    [path_of_the_folder.split("\\")[-2], path_of_the_folder.split("\\")[-3]],
                    index=["Patient", "Date or smth"],
                ),
                all_agg_des.loc["mean"],
                all_CSS_des.loc["mean"],
                all_def_des.loc["mean"],
                fit_res_des.loc["mean"],
                fit_res_deform_des.loc["mean"],
            ],
            axis=0,
            ignore_index=False,
        ),
    ]


# Функция для вычисления выбросов - ничего не возвращает и очищает 1 Data Frame от выбросов - определение выбросов стандартное
def out_lets_quartile(all_Data_Frame: pd.DataFrame, factor: int):
    for i in all_Data_Frame.columns:
        if i == "Patient" or len(all_Data_Frame[i]) <= 3:
            continue
        q1 = all_Data_Frame.loc[:, i].quantile(0.25)
        q3 = all_Data_Frame.loc[:, i].quantile(0.75)
        for j in range(len(all_Data_Frame[i])):
            if (
                all_Data_Frame.loc[j, i] < q1 - (q3 - q1) * factor
                or all_Data_Frame.loc[j, i] > q3 + (q3 - q1) * factor
            ):
                all_Data_Frame.loc[j, i] = np.nan
