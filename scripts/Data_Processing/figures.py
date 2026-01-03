import math
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numba  # noqa: F401
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import Normalize
from permutations_stats.permutations import permutation_test, repeated_permutation_test
from PySide6.QtWidgets import QMessageBox
from scipy import stats

from scripts.Data_Processing.utils.fig_val_separator import (
    apply_global_comma_patch,
    is_patched,
    restore_global_comma_patch,
)

warnings.filterwarnings("ignore", category=FutureWarning)


##############################################################
#
# главная функция
#
##############################################################
def figs_plot(self) -> None:
    dlg = QMessageBox(self)
    # закроем все рисунки, если они открыты
    # если этого не сделать, то может быть такое, что рисунки наложатся друг на друга
    plt.close("all")
    # В этот list будут записываться все доп. Функции для графиков -- см. определение ниже.
    global plot_feature_data__
    # Я решил все особенности и доп. функции для построения графиков перевести в массив "plot_feature_data__".
    # По большей части это связано с тем, что этот код я несколько раз переписывал.
    # И это удобно, если надо быстро что-то добавить.
    plot_feature_data__ = lets_add_all_parameters_for_figs_here(self)
    #########################
    # параметры, которые нам понадобятся
    path = self.ui.path_for_plot.text()
    exel_name = self.ui.comboBox.currentText()
    # от чего смотрится зависимость?
    hue_name = self.ui.comboBox_2.currentText()
    # стоим или не строим - box plot, корреляционные графики, матрицы и др.
    box_plot_or_not = self.ui.check_box_plot.isChecked()
    corr_is_need_matrix = self.ui.check_corr_matrix.isChecked()
    corr_is_need = self.ui.check_corr_figs.isChecked()
    pairplot_is_need = self.ui.check_box_pairplot.isChecked()
    jointplot_is_need = self.ui.check_jointplot.isChecked()
    # корреляции одного параметра
    corr_one_parameter_is_need = self.ui.check_corr_one_parameter.isChecked()
    # по всем листам проходимся или же только по одному?
    all_sheets_true = self.ui.check_box_figs_all_sheets.isChecked()
    one_sheet_name = self.ui.comboBox_figs_sheets.currentText()
    #########################
    # проверяем на ошибки
    checc = error_for_val_plot(plot_feature_data__, path, exel_name)

    if checc != "__":
        dlg.setWindowTitle("Графики")
        dlg.setText(checc)
        dlg.exec()
        return

    # делаем патч, если нужно заменить точки на запятые в качестве разделителя
    if self.ui.checkBox_point_comma_separator.isChecked() and not is_patched():
        apply_global_comma_patch()

    # основной путь
    path_obj = Path(path)
    # путь до файла
    files = path_obj / exel_name

    try:
        names = pd.ExcelFile(str(files)).sheet_names
    except Exception as e:
        dlg.setWindowTitle("Графики")
        dlg.setText("Нет такого файла/директории или файл испорчен.\n" + str(e))
        dlg.exec()
        return

    # если стоит галочка corr_one_parameter_is_need, то выполняем только корреляции по одному параметру, а на другие не обращаем
    if corr_one_parameter_is_need:
        try:
            corr_one_parameter(path_obj, files, one_sheet_name, hue_name)
            #############################
            # завершаем работу
            ############################
            dlg.setWindowTitle("Графики")
            dlg.setText("Все графики успешно сохранены")
            dlg.exec()
            return
        except Exception as e:
            dlg.setWindowTitle("Корреляция одного параметра")
            dlg.setText("Ошибка в обработке.\n" + str(e))
            dlg.exec()
            return

    # если стоит галочка, то проходимся по всем листам, но если же all_sheets_true == False,
    # то выбираем только один лист
    if not all_sheets_true:
        names = [one_sheet_name]

    # выполняем функцию do_for_one_sheet по всем листам (или же только по одному) в excel файле
    check_cykle = "__"
    for i in names:
        check_cykle = do_for_one_sheet(
            path_obj,
            files,
            i,
            box_plot_or_not,
            corr_is_need,
            corr_is_need_matrix,
            pairplot_is_need,
            jointplot_is_need,
            hue_name,
        )
        if check_cykle != "__":
            break

    # восстановим патч
    if is_patched():
        restore_global_comma_patch()

    if check_cykle == "__":
        dlg.setWindowTitle("Графики")
        dlg.setText("Все графики успешно сохранены")
        dlg.exec()
        return
    dlg.setWindowTitle("Графики - Ошибка")
    dlg.setText(check_cykle)
    dlg.setIcon(QMessageBox.Icon.Critical)
    dlg.exec()

    return


def reset_origin_sns() -> None:
    """Восстанавливает настройки."""
    sns.reset_orig()


##############################################################
#
# строим корреляции только одного параметра
#
##############################################################
def corr_one_parameter(path_obj, files, what_sheet, hue_name) -> None:
    # читаем exel файл - index_col=0,
    df = pd.read_excel(str(files), sheet_name=what_sheet)
    df.index.rename(None, inplace=True)
    # на всякий случай почистим
    df.columns = df.columns.str.replace("\\n", "\n", regex=False)
    # выделяем те колонки, которые нас будут интерисовать с точки зрения обработки!

    # будем смотреть один параметр если стоит галочка, иначе все параметры
    corr_list = [hue_name] if plot_feature_data__["corr_one_parameter_only_one"] else df.columns

    ###
    # корреляционная матрица
    ###
    correlation_matrix = df.corr(method=plot_feature_data__["correlation_one_parameter"])
    limit_ = plot_feature_data__["one_correlation"]
    correlation_matrix = correlation_matrix.map(
        lambda x: x if x > limit_ or x < -limit_ else 0,
    )
    for i in correlation_matrix.columns:
        correlation_matrix.loc[i, i] = 0
    for i in correlation_matrix.columns:
        if (correlation_matrix[i] == 0).all():
            correlation_matrix = correlation_matrix.drop(columns=i).drop(i)

    if correlation_matrix.empty:
        msg = "Нет корреляций для выставленных границ"
        raise ValueError(msg)

    # папка для сохранения результатов
    path_one_corr = path_obj / "one_corr"
    path_one_corr.mkdir(parents=True, exist_ok=True)

    # размер шрифта
    font_for_one_corr = int(15 * plot_feature_data__["size_for_one_correlation"])

    # строим корреляции для одного параметра или для многих
    for name_var in corr_list:
        target_variable = name_var

        target_correlations = correlation_matrix[target_variable][
            correlation_matrix[target_variable] != 0
        ]
        target_correlations = target_correlations.sort_values(ascending=False)

        # Нормализуем значения корреляции в диапазоне 0-1
        norm = Normalize(vmin=-1, vmax=1)
        colors = [plt.cm.coolwarm(norm(value)) for value in target_correlations.values]

        # построим график
        one_corr_plot = plt.figure(figsize=(12, 6))
        target_correlations.plot(kind="barh", color=colors)
        plt.title(f"Корреляции параметров с {target_variable}", size=font_for_one_corr)
        plt.xlabel(
            "Коэффициент корреляции "
            + {"pearson": "Пирсона", "kendall": "Кендалла", "spearman": "Спирмена"}[
                plot_feature_data__["correlation_one_parameter"]
            ],
            size=font_for_one_corr,
        )
        plt.ylabel("Параметры", size=font_for_one_corr)
        plt.xlim(-1, 1)
        plt.yticks(size=font_for_one_corr)
        plt.xticks(size=font_for_one_corr - 3)
        plt.xticks(np.arange(-1, +1.1, 0.1))
        plt.tight_layout()
        one_corr_plot.savefig(str(path_one_corr / f"{safe_name(target_variable)}.png"))
    # построим график в отдельном окне
    if (
        plot_feature_data__["corr_one_parameter_only_one"]
        and plot_feature_data__["corr_one_parameter_plot_sep_wind"]
    ):
        plt.show()


##############################################################
#
# проходимся по одному листу и стоим всё, что надо
#
##############################################################
def do_for_one_sheet(
    path_obj,
    files,
    what_sheet,
    box_plot_or_not,
    corr_is_need,
    corr_is_need_matrix,
    pairplot_is_need,
    jointplot_is_need,
    hue_name,
):
    # читаем exel файл - index_col=0,
    df = pd.read_excel(str(files), sheet_name=what_sheet)
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
            return "В таблице нет такого столбца:" + str(hue_name_for_sheet)
        index_for_col_interest = list(columns_of_interest).index(hue_name_for_sheet)
        columns_of_interest = columns_of_interest[index_for_col_interest + 1 :]

    # все столбцы с данными приводим к численному виду
    for dd in columns_of_interest:
        try:
            df[dd] = df[dd].apply(pd.to_numeric)
        except Exception as e:
            message = (
                "В колонке "
                + str(dd)
                + " представлены значения, которые нельзя конвертировать в числа.\n"
                + str(e)
            )
            return message

    # название оси X
    name_of_X_axis = hue_name_for_sheet
    # создаем новый DataFrame только с колонками для обработки
    new_df = df[columns_of_interest].copy()
    # и добавляем в него только колонку для значений индекса/концентрации/образца!
    new_df.insert(loc=0, column="index", value=df[hue_name_for_sheet])  # Диагноз
    if corr_is_need_matrix:
        # создаем подпапку для графиков корреляции
        path_name_fiqure_folder_corr_matrix = path_obj / "correlation_matrix" / what_sheet
        path_name_fiqure_folder_corr_matrix.mkdir(parents=True, exist_ok=True)
        # создаём корреляционные матрицы и сохраняем
        corr_matrix_for_all_indexes(new_df, path_name_fiqure_folder_corr_matrix)

    if corr_is_need:
        # создаем подпапку для графиков корреляции
        path_name_fiqure_folder_corr = path_obj / "correlation"
        path_name_fiqure_folder_corr.mkdir(parents=True, exist_ok=True)

        # найдет все уникальные комбинации признаков
        ls = list(range(1, len(new_df.columns[1:]) + 1))
        combinations__ = [(ls[x], ls[x + y]) for y in reversed(ls) for x in range(len(ls) - y)]
        ###################
        # пройдемся по всем колонкам из combinations__
        for i in combinations__:
            x_, y_ = new_df.columns[i[0]], new_df.columns[i[1]]
            only_regplot(
                df,
                x_,
                y_,
                path_name_fiqure_folder_corr,
                what_is_hue=hue_name_for_sheet,
                not_in_hue=plot_feature_data__["del_hue"],
                color_palette=plot_feature_data__["color_pal_corr"],
                _lim_=plot_feature_data__["bottom_lim"],
                sort_or_not=plot_feature_data__["check_sort_or_not"],
            )

    if pairplot_is_need:
        # создаем подпапку для графиков корреляции
        path_name_fiqure_folder_pairplot = path_obj / "pairplot"
        path_name_fiqure_folder_pairplot.mkdir(parents=True, exist_ok=True)
        # создаём корреляционные матрицы и сохраняем
        pairplot(new_df, hue_name_for_sheet, what_sheet, path_name_fiqure_folder_pairplot)

    if jointplot_is_need:
        # создаем подпапку для графиков корреляции
        path_name_fiqure_folder_jointplot = path_obj / "jointplot"
        path_name_fiqure_folder_jointplot.mkdir(parents=True, exist_ok=True)
        # создаём графики jointplot
        jointplot(new_df, hue_name_for_sheet, what_sheet, path_name_fiqure_folder_jointplot)

    if box_plot_or_not:
        # создаем подпапку для графиков аппроксимации
        path_name_fiqure_folder = path_obj / "fiqures"
        path_name_fiqure_folder.mkdir(parents=True, exist_ok=True)
        # создаем словарь значений параметров
        dict_for_future = {}
        # и создаем массив для DataFrame-ов
        df_list = []
        index_index = 0
        for i in new_df.columns:
            if i != "index":
                # делаем словарь для индексов
                dict_for_future[i] = index_index
                index_index += 1
                # разделяем по индексу
                just_all_we_need = new_df.pivot(columns="index", values=i)
                # оставляем изначальный порядок значений
                just_all_we_need = just_all_we_need.reindex(columns=new_df["index"].unique()[::-1])
                # следующая сточка очень важна, чтобы не потерять какие-то значения, если есть ряд пропусков
                just_all_we_need2 = pd.DataFrame(index=list(range(max(just_all_we_need.count()))))
                # убираем NaN
                for j in just_all_we_need.columns:
                    ignore_nan = just_all_we_need[j]
                    ignore_nan = ignore_nan.dropna()
                    ignore_nan = ignore_nan.reset_index(drop=True)
                    just_all_we_need2.insert(loc=0, column=j, value=ignore_nan)
                # изменяем порядок колонок - сортируем, если это надо
                if plot_feature_data__["check_sort_or_not"]:
                    just_all_we_need2 = just_all_we_need2[
                        just_all_we_need2.columns.sort_values(
                            ascending=plot_feature_data__["check_sort_or_not_ascending"],
                        )
                    ]
                elif plot_feature_data__["order_box_plot"] != "":
                    columns__temp = (
                        plot_feature_data__["order_box_plot"]
                        .replace(",", "")
                        .replace(";", " ")
                        .split()
                    )

                    if len(just_all_we_need2.columns) != len(columns__temp):
                        return f"Кол-во подписей в поле <Изменить порядок подписей> не верно.\n Должно быть {len(just_all_we_need2.columns)}, а введено {len(columns__temp)}."
                    try:
                        columns__temp = list(map(int, columns__temp))
                        columns__temp = [x - 1 for x in columns__temp]
                        columns__ = [just_all_we_need2.columns[x] for x in columns__temp]
                        just_all_we_need2 = just_all_we_need2.reindex(columns=columns__)
                    except Exception as e:
                        return "Поле <Изменить порядок подписей> заполнено не верно.\n" + str(e)

                # сохраняем в список DataFrame-ов
                df_list.append(just_all_we_need2)
        if plot_feature_data__["check_stat_znachimost"]:
            # вот и массив с таблицами p-values
            try:
                df_list_stat = calculate_table_for_p_val(df_list, dict_for_future)
            except Exception as e:
                return (
                    "Скорее всего проблема с данными: в одной из групп отсутствуют данные для обработки.\n"
                    + str(e)
                )
        # вот и массив для графиков
        big_G = just_to_numpy_for_plot(df_list, dict_for_future)
        # построение графиков
        check = just_plot_it_(
            big_G,
            dict_for_future,
            df_list,
            name_of_X_axis,
            path_name_fiqure_folder,
        )
        if check != "__":
            return check

        if plot_feature_data__["check_stat_znachimost"]:
            # создаем подпапку для exel файлов
            stat_path = path_obj / "stat"
            stat_path.mkdir(parents=True, exist_ok=True)
            #############
            with pd.ExcelWriter(str(stat_path / f"{what_sheet}.xlsx")) as writer:
                for i in dict_for_future:
                    name_of_sheet = i
                    name_of_sheet = safe_name(name_of_sheet)

                    if len(name_of_sheet) > 31:
                        name_of_sheet = name_of_sheet[0:30]
                    df_list[dict_for_future[i]].to_excel(writer, sheet_name=name_of_sheet)
            #############
            with pd.ExcelWriter(
                str(
                    stat_path
                    / f"{what_sheet}_{plot_feature_data__['comboBox_stat_test']}_p-values.xlsx"
                ),
            ) as writer:
                for i in dict_for_future:
                    name_of_sheet = i
                    name_of_sheet = safe_name(name_of_sheet)

                    if len(name_of_sheet) > 31:
                        name_of_sheet = name_of_sheet[0:30]
                    df_list_stat[dict_for_future[i]].to_excel(writer, sheet_name=name_of_sheet)
    return "__"


##############################################################
#
# BOX PLOT
#
##############################################################
# функцию эту я не всю придумал сам, а взял небольшую часть с сайта:
# https://rowannicholls.github.io/python/graphs/ax_based/boxplots_significance.html#test-for-statistical-significance
# также см. ссылку: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html
def box_and_whisker(
    data,
    title,
    xlabel,
    ylabel,
    xticklabels,
    Name_fiqure,
    path_name_fiqure_folder,
    make_an_SD=True,
) -> str:
    """Построим BOX plot с стат. значимостью."""
    sns.reset_orig()
    # если будем строить со стандартным отклонением, то укажем дополнительный аргумент
    whisk_MIN_MAX = 0 if make_an_SD else 1.5

    # аргумент positions -- очень важен -- без него всё не поедет!
    # positions=range(len(data)) !
    fig, ax = plt.subplots()
    ax.cla()
    bp = ax.boxplot(
        data,
        widths=0.6,
        whis=whisk_MIN_MAX,
        patch_artist=True,
        positions=range(len(data)),
        showmeans=True,
        showfliers=False,
        meanprops={
            "marker": "D",
            "markerfacecolor": "white",
            "markeredgecolor": "black",
            "markersize": str(plot_feature_data__["spinBox_mean_val_size"]),
        },
    )

    # Изменим цвета. Если введен аргумент цвета, то цвет будет один или несколько;
    # есть такие цвета хорошие 'Pastel1' 'Blues' 'Greens' 'Purples' или такие https://r02b.github.io/seaborn_palettes/
    if plot_feature_data__["color_box"] == "" and plot_feature_data__["color_points"] == "":
        # для точек измерений
        take_a_color_point = plot_feature_data__["color_pal_points"]
        # специальный массив для box-ов
        colors = sns.color_palette(plot_feature_data__["color_pal_box"])
    elif plot_feature_data__["color_box"] == "" and plot_feature_data__["color_points"] != "":
        # для точек измерений
        if "&" in plot_feature_data__["color_points"]:
            take_a_color_point = filter(None, plot_feature_data__["color_points"].split("&"))
        else:
            take_a_color_point = [plot_feature_data__["color_points"]] * len(bp["boxes"])
        # специальный массив для box-ов
        colors = sns.color_palette(plot_feature_data__["color_pal_box"])
    elif plot_feature_data__["color_box"] != "" and plot_feature_data__["color_points"] == "":
        # для точек измерений
        take_a_color_point = plot_feature_data__["color_pal_points"]
        # специальный массив для box-ов
        if "&" in plot_feature_data__["color_box"]:
            colors = filter(None, plot_feature_data__["color_box"].split("&"))
        else:
            colors = [plot_feature_data__["color_box"]] * len(bp["boxes"])
    else:
        # для точек измерений
        if "&" in plot_feature_data__["color_points"]:
            take_a_color_point = filter(None, plot_feature_data__["color_points"].split("&"))
        else:
            take_a_color_point = [plot_feature_data__["color_points"]] * len(bp["boxes"])
        # специальный массив для box-ов
        if "&" in plot_feature_data__["color_box"]:
            colors = plot_feature_data__["color_box"].split("&")
        else:
            colors = [plot_feature_data__["color_box"]] * len(bp["boxes"])

    # стандартное отклонение - добавить вместо разброса между min-max
    if make_an_SD:
        sns.set_theme(style="ticks", rc={"lines.linewidth": 0.7})
        sns.pointplot(
            data=data,
            palette=["black"] * len(bp["boxes"]),
            ax=ax,
            errorbar="sd",
            capsize=0.2,
        )

    # добавить точки! цвет: palette=take_a_color_point
    try:
        sns.stripplot(
            data=data,
            alpha=plot_feature_data__["points_opasity"],
            palette=take_a_color_point,
            ax=ax,
            linewidth=1,
            size=plot_feature_data__["point_size"],
        )
    except Exception as e:
        return (
            "Box plot: скорее всего вы ввели неправильный(е) цвет(а) HEX.\nЦвет для HEX должен быть в формате <#XXXXXX>.\nДля нескольких цветов используйте разделительный знак: &.\n"
            + str(e)
        )

    ##############
    # вот тут добавляются цвета к нашим box-ам
    ##############
    try:
        for patch, color in zip(bp["boxes"], colors, strict=False):
            patch.set_facecolor(color)
    except Exception as e:
        return (
            "Box plot: скорее всего вы ввели неправильный(е) цвет(а) HEX.\nЦвет для HEX должен быть в формате <#XXXXXX>.\nДля нескольких цветов используйте разделительный знак: &.\n"
            + str(e)
        )

    # цвет медианы
    plt.setp(bp["medians"], color="k")

    if plot_feature_data__["check_stat_znachimost"]:
        # Стат. Значимость.
        significant_combinations = []
        if plot_feature_data__["STAT_znachimost_order_box_plot"] != "":
            try:
                combinations = plot_feature_data__["STAT_znachimost_order_box_plot"].split()
                combinations = [item.replace("(", "").replace(")", "") for item in combinations]
                combinations = [tuple(map(int, item.split(","))) for item in combinations]
            except Exception as e:
                return (
                    "Box plot: неправильное значение в поле <Расчёт стат.значимости только между следующими группами>:\n"
                    + str(e)
                )
        else:
            ls = list(range(1, len(data) + 1))
            combinations = [(ls[x], ls[x + y]) for y in reversed(ls) for x in range(len(ls) - y)]
        for c in combinations:
            data1 = data[c[0] - 1]
            data2 = data[c[1] - 1]

            # Significance
            if plot_feature_data__["comboBox_stat_test"] == "U-критерий Манна — Уитни":
                _, p = stats.mannwhitneyu(
                    data1,
                    data2,
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
            elif plot_feature_data__["comboBox_stat_test"] == "Т-критерий Стьюдента":
                _, p = stats.ttest_ind(
                    data1,
                    data2,
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
            elif plot_feature_data__["comboBox_stat_test"] == "Критерий Уилкоксона":
                _, p = stats.wilcoxon(
                    data1,
                    data2,
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
            elif plot_feature_data__["comboBox_stat_test"] == "Критерий Краскела — Уоллиса":
                _, p = stats.kruskal(data1, data2)
            elif plot_feature_data__["comboBox_stat_test"] == "Медианный критерий":
                _, p = stats.mood(
                    data1,
                    data2,
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
            elif plot_feature_data__["comboBox_stat_test"] == "Тест Ансари-Брэдли":
                _, p = stats.ansari(
                    data1,
                    data2,
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
            elif plot_feature_data__["comboBox_stat_test"] == "Тест Бруннера — Мюнцеля":
                _, p = stats.brunnermunzel(
                    data1,
                    data2,
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
            elif plot_feature_data__["comboBox_stat_test"] == "Тест Бруннера — Мюнцеля (normal)":
                # distribution='normal' - если что-то не так или данные только одно значение, но в этом случае этот тест лучше не использовать
                _, p = stats.brunnermunzel(
                    data1,
                    data2,
                    distribution="normal",
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
            elif plot_feature_data__["comboBox_stat_test"] == "Тест Фишера-Питмана":

                def statistic(x, y, axis) -> float:
                    return np.mean(x, axis=axis) - np.mean(y, axis=axis)

                # вычисляем
                all_data = stats.permutation_test(
                    (data1, data2),
                    statistic,
                    permutation_type="independent",
                    vectorized=True,
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
                # само значение p
                p = all_data.pvalue
            elif (
                plot_feature_data__["comboBox_stat_test"]
                == "Пермутационный критерий Бруннера — Мюнцеля"
            ):
                stat = permutation_test(
                    data1,
                    data2,
                    test="brunner_munzel",
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
                p = stat.pvalue
            elif (
                plot_feature_data__["comboBox_stat_test"] == "Пермутационный критерий Манна — Уитни"
            ):
                stat = permutation_test(
                    data1,
                    data2,
                    test="mann_whitney",
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
                p = stat.pvalue
            elif plot_feature_data__["comboBox_stat_test"] == "Пермутационный критерий Уилкоксона":
                # изменим формат
                data_for_paired_permutations = np.vstack([data1, data2]).T
                # сделаем расчет
                stat = repeated_permutation_test(
                    data_for_paired_permutations,
                    test="wilcoxon",
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
                p = stat.pvalue
            elif plot_feature_data__["comboBox_stat_test"] == "Пермутационный критерий Фридмана":
                # изменим формат
                data_for_paired_permutations = np.vstack([data1, data2]).T
                # сделаем расчет
                stat = repeated_permutation_test(
                    data_for_paired_permutations,
                    test="friedman",
                    alternative=plot_feature_data__["comboBox_alter_hep"],
                )
                p = stat.pvalue
            else:
                pass

            if p < 0.05:
                significant_combinations.append([c, p])

        # МИН-МАКС оси Y
        bottom, top = ax.get_ylim()
        yrange = top - bottom

        # Бары статистической значимости
        for i, significant_combination in enumerate(significant_combinations):
            # Столбцы, соответствующие интересующим наборам данных
            x1 = significant_combination[0][0]
            x2 = significant_combination[0][1]
            # На каком уровне находится этот бар среди других?
            level = len(significant_combinations) - i
            # построим бары
            bar_height = (
                yrange * 0.08 * level * plot_feature_data__["size_stat_znachimost"] / 10
            ) + top
            bar_tips = bar_height - (yrange * 0.02)
            plt.plot(
                [x1 - 1, x1 - 1, x2 - 1, x2 - 1],
                [bar_tips, bar_height, bar_height, bar_tips],
                lw=1,
                c="k",
            )

            ##############
            # эта функция нужна, если нужно точное значение p
            def round_to(num, digits=2):
                if num == 0:
                    return 0
                scale = int(-math.floor(math.log10(abs(num - int(num))))) + digits - 1
                scale = max(scale, digits)
                return round(num, scale)

            ##############
            # Уровень значимости
            p = significant_combination[1]
            if p < 0.0001:
                sig_symbol = "****"
                if (
                    plot_feature_data__["box_plot_sign_stat_znachimost"]
                    == "меньше какого-то значения (p<)"
                ):
                    sig_symbol = "p < 0.0001"
                elif (
                    plot_feature_data__["box_plot_sign_stat_znachimost"]
                    == "равно какому-то значению (p=)"
                ):
                    sig_symbol = "p = " + str(round_to(p))
            elif p < 0.001:
                sig_symbol = "***"
                if (
                    plot_feature_data__["box_plot_sign_stat_znachimost"]
                    == "меньше какого-то значения (p<)"
                ):
                    sig_symbol = "p < 0.001"
                elif (
                    plot_feature_data__["box_plot_sign_stat_znachimost"]
                    == "равно какому-то значению (p=)"
                ):
                    sig_symbol = "p = " + str(round_to(p))
            elif p < 0.01:
                sig_symbol = "**"
                if (
                    plot_feature_data__["box_plot_sign_stat_znachimost"]
                    == "меньше какого-то значения (p<)"
                ):
                    sig_symbol = "p < 0.01"
                elif (
                    plot_feature_data__["box_plot_sign_stat_znachimost"]
                    == "равно какому-то значению (p=)"
                ):
                    sig_symbol = "p = " + str(round_to(p))
            elif p < 0.05:
                sig_symbol = "*"
                if (
                    plot_feature_data__["box_plot_sign_stat_znachimost"]
                    == "меньше какого-то значения (p<)"
                ):
                    sig_symbol = "p < 0.05"
                elif (
                    plot_feature_data__["box_plot_sign_stat_znachimost"]
                    == "равно какому-то значению (p=)"
                ):
                    sig_symbol = "p = " + str(round_to(p))
            text_height = bar_height + (yrange * 0.01)
            plt.text(
                (x1 - 1 + x2 - 1) * 0.5,
                text_height,
                sig_symbol,
                ha="center",
                c="k",
                fontsize=plot_feature_data__["size_stat_znachimost"],
            )
    ###############
    # Изменим границы оси Y
    ###############
    bottom, top = ax.get_ylim()
    yrange = top - bottom
    # <0.02 * yrange> нужно, чтобы смотрелось всё хорошо, если не введена нижняя/верхняя граница
    ax.set_ylim(bottom - 0.02 * yrange, top + 0.02 * yrange)

    if plot_feature_data__["bottom_lim"] != "":
        bottom = float(plot_feature_data__["bottom_lim"].replace(",", "."))
        ax.set_ylim(bottom, top)
    if plot_feature_data__["upper_lim"] != "":
        top = float(plot_feature_data__["upper_lim"].replace(",", "."))
        ax.set_ylim(bottom, top)

    if plot_feature_data__["bottom_lim"] != "" or plot_feature_data__["upper_lim"] != "":
        bottom, top = ax.get_ylim()
        yrange = top - bottom
        # это нужно, чтобы N - количество данных отображалось корректно
        bottom = bottom + 0.02 * yrange

    # Укажем размер выборки под каждым полем.
    # ''' внизу чтобы было кол-во данных
    if plot_feature_data__["check_N_"]:
        for i, dataset in enumerate(data):
            sample_size = len(dataset)
            ax.text(
                i,
                bottom,
                rf"n = {sample_size}",
                ha="center",
                size=plot_feature_data__["box_check_N_"],
            )
    # '''

    # Шрифт устанавливаем в самом конце, т.к. из-за изменения осей могут быть ошибки
    # Label y-axis
    ax.set_ylabel(
        ylabel,
        fontsize=plot_feature_data__["spinBox_y_label"],
        fontname=plot_feature_data__["comboBox_fonts"],
    )
    # Label x-axis
    ax.set_xlabel(
        xlabel,
        fontsize=plot_feature_data__["spinBox_x_label"],
        fontname=plot_feature_data__["comboBox_fonts"],
    )
    # Label x-axis ticks -- если нужно, можно добавить "rotation=40"
    new_x_tick_label = [item.replace("\\n", "\n") for item in map(str, list(xticklabels))]
    ax.set_xticklabels(new_x_tick_label, rotation=int(plot_feature_data__["comboBox_spin_x_"]))
    # размер шрифта подписи
    plt.yticks(
        fontsize=plot_feature_data__["spinBox_y_vals"],
        fontname=plot_feature_data__["comboBox_fonts"],
    )
    plt.xticks(
        fontsize=plot_feature_data__["spinBox_x_val"],
        fontname=plot_feature_data__["comboBox_fonts"],
    )

    # Скроем основные деления оси X
    ax.tick_params(axis="x", which="major", length=0)
    # Покажем мелкие деления оси X
    xticks = [0.5] + [x + 0.5 for x in ax.get_xticks()]
    ax.set_xticks(xticks, minor=True)
    ax.tick_params(axis="x", which="minor", length=3, width=1)

    # очень важно, чтобы не обрезалось
    plt.tight_layout()
    try:
        # сохранение рисунка
        plt.savefig(
            str(path_name_fiqure_folder / f"{safe_name(Name_fiqure)}.png"),
            dpi=600,
            format="png",
            transparent=plot_feature_data__["check_background"],
        )
    except Exception as e:
        return "Box plot: " + str(e)
    plt.close()
    ax.cla()
    plt.clf()
    return "__"


# Функция для преобразования данных для построения
def just_to_numpy_for_plot(df_list, dict_for_future) -> list:
    big_G = []
    small_G = []
    for parameter_ in dict_for_future:
        for i in df_list[dict_for_future[parameter_]].columns:
            small_G.append(df_list[dict_for_future[parameter_]][i].dropna().to_numpy())
        big_G.append(small_G)
        small_G = []
    return big_G


# Функция для построения графиков по входному массиву
def just_plot_it_(big_G, dict_for_future, df_list, name_of_X_axis, path_name_fiqure_folder) -> str:
    for parameter_ in dict_for_future:
        do_SD = True if plot_feature_data__["comboBox_sd_or_minmax"] == "SD" else False
        ylabel = parameter_
        check = box_and_whisker(
            big_G[dict_for_future[parameter_]],
            "",
            name_of_X_axis,
            ylabel,
            df_list[dict_for_future[parameter_]].columns,
            parameter_,
            path_name_fiqure_folder,
            make_an_SD=do_SD,
        )
        if check != "__":
            return check
    return "__"


# Функция для получения массива дата фреймов с таблицами p-values
def calculate_table_for_p_val(df_list, dict_for_future):
    df_list_stat = []
    for i in dict_for_future:
        dop_DF = pd.DataFrame(
            index=df_list[dict_for_future[i]].columns,
            columns=df_list[dict_for_future[i]].columns,
        )
        # пройдемся по всем парам столбцов
        for col1 in dop_DF.columns:
            for col2 in dop_DF.columns:
                if col1 == col2:
                    dop_DF.loc[col1, col2] = 1.0
                    continue
                # Рассчитаем стат. Значимости.
                if plot_feature_data__["comboBox_stat_test"] == "U-критерий Манна — Уитни":
                    _, p_value = stats.mannwhitneyu(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                elif plot_feature_data__["comboBox_stat_test"] == "Т-критерий Стьюдента":
                    _, p_value = stats.ttest_ind(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                elif plot_feature_data__["comboBox_stat_test"] == "Критерий Уилкоксона":
                    _, p_value = stats.wilcoxon(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                elif plot_feature_data__["comboBox_stat_test"] == "Критерий Краскела — Уоллиса":
                    _, p_value = stats.kruskal(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                    )
                elif plot_feature_data__["comboBox_stat_test"] == "Медианный критерий":
                    _, p_value = stats.mood(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                elif plot_feature_data__["comboBox_stat_test"] == "Тест Ансари-Брэдли":
                    _, p_value = stats.ansari(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                elif plot_feature_data__["comboBox_stat_test"] == "Тест Бруннера — Мюнцеля":
                    _, p_value = stats.brunnermunzel(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                elif (
                    plot_feature_data__["comboBox_stat_test"] == "Тест Бруннера — Мюнцеля (normal)"
                ):
                    _, p_value = stats.brunnermunzel(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                        distribution="normal",
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                elif plot_feature_data__["comboBox_stat_test"] == "Тест Фишера-Питмана":

                    def statistic(x, y, axis):
                        return np.mean(x, axis=axis) - np.mean(y, axis=axis)

                    # вычисляем
                    all_data = stats.permutation_test(
                        (
                            df_list[dict_for_future[i]][col1].dropna(),
                            df_list[dict_for_future[i]][col2].dropna(),
                        ),
                        statistic,
                        permutation_type="independent",
                        vectorized=True,
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                    # само значение p
                    p_value = all_data.pvalue

                elif (
                    plot_feature_data__["comboBox_stat_test"]
                    == "Пермутационный критерий Бруннера — Мюнцеля"
                ):
                    stat = permutation_test(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                        test="brunner_munzel",
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                    p_value = stat.pvalue
                elif (
                    plot_feature_data__["comboBox_stat_test"]
                    == "Пермутационный критерий Манна — Уитни"
                ):
                    stat = permutation_test(
                        df_list[dict_for_future[i]][col1].dropna(),
                        df_list[dict_for_future[i]][col2].dropna(),
                        test="mann_whitney",
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                    p_value = stat.pvalue
                elif (
                    plot_feature_data__["comboBox_stat_test"]
                    == "Пермутационный критерий Уилкоксона"
                ):
                    # изменим формат
                    data_for_paired_permutations = np.vstack(
                        [
                            df_list[dict_for_future[i]][col1].dropna(),
                            df_list[dict_for_future[i]][col2].dropna(),
                        ],
                    ).T
                    # сделаем расчет
                    stat = repeated_permutation_test(
                        data_for_paired_permutations,
                        test="wilcoxon",
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                    p_value = stat.pvalue
                elif (
                    plot_feature_data__["comboBox_stat_test"] == "Пермутационный критерий Фридмана"
                ):
                    # изменим формат
                    data_for_paired_permutations = np.vstack(
                        [
                            df_list[dict_for_future[i]][col1].dropna(),
                            df_list[dict_for_future[i]][col2].dropna(),
                        ],
                    ).T
                    # сделаем расчет
                    stat = repeated_permutation_test(
                        data_for_paired_permutations,
                        test="friedman",
                        alternative=plot_feature_data__["comboBox_alter_hep"],
                    )
                    p_value = stat.pvalue
                else:
                    pass
                # добавим в наш DataFrame
                dop_DF.loc[col1, col2] = round(p_value, 4)
        df_list_stat.append(dop_DF)
        df_list_stat[dict_for_future[i]] = df_list_stat[dict_for_future[i]].style.map(
            lambda x: "color:red" if x < 0.05 else "color:black",
        )
    return df_list_stat


##############################################################
#
# Функция для построения графиков корреляций
#
##############################################################
def only_regplot(
    df,
    x_,
    y_,
    path_name_fiqure_folder_corr,
    what_is_hue,
    color_palette=None,
    not_in_hue=[],
    _lim_="",
    sort_or_not=False,
):
    sns.reset_orig()
    sns.set_theme(font_scale=plot_feature_data__["doubleSpinBox_corr_figs_fontscale"])
    # стиль
    sns.set_style("ticks")
    if plot_feature_data__["check_setka"]:
        sns.set_style("whitegrid", {"axes.grid": True, "grid.color": ".9", "grid.linestyle": "--"})

    # узнаем в каком цвете нам строить задний фон под аннотацией к коэффициенту Пирсона
    current_color = sns.color_palette(color_palette)
    # создаём лист по интерисующим группам
    hue_what = df[what_is_hue].unique()
    hue_what = list(hue_what)
    if plot_feature_data__["check_sort_or_not_corr_figs"]:
        hue_what.sort()
    # удаляем элемент_ы hue, если это нужно
    try:
        if type(not_in_hue) == str and not_in_hue != "":
            hue_what.remove(not_in_hue)
        elif type(not_in_hue) == int or type(not_in_hue) == float:
            hue_what.remove(str(not_in_hue))
        else:
            for jj in not_in_hue:
                hue_what.remove(jj)
    except ValueError:
        pass
    if sort_or_not:
        hue_what.sort()
    # строим график
    fig = plt.figure()
    ax = plt.axes()

    # максимальное значение на оси y
    max_ylim = 0
    # с линиями это regplot
    for i, color__ in zip(hue_what, current_color, strict=False):
        sns.regplot(
            data=df[df[what_is_hue] == i],
            x=x_,
            y=y_,
            ax=ax,
            color=color__,
            label=i,
            scatter_kws={"s": plot_feature_data__["spinBox_points_corrFIGS"]},
        )
        _, top = ax.get_ylim()
        max_ylim = max(max_ylim, top)
    # поменяем пределы значений на оси y
    if plot_feature_data__["check_change_corr_fig_down_limit"]:
        ax.set_ylim(plot_feature_data__["doubleSpinBox_corr_figs"], max_ylim)

    # и для каждой группы находим коэффициент Пирсона и добавляем его на график
    for val, color__ in zip(hue_what, current_color, strict=False):
        new_massive = df[(df[what_is_hue] == val)][[x_, y_]].dropna()
        r, _ = stats.pearsonr(x=new_massive[x_], y=new_massive[y_])
        r = round(r, 2)
        if is_patched():
            r = str(r).replace(".", ",")
        m = plt.text(
            0.65,
            0.93 - 0.1 * hue_what.index(val),
            f"{val} (n={len(df[(df[what_is_hue] == val)][x_])}): r = {r}",
            transform=ax.transAxes,
        )
        # сделаем красивую рамку под аннотацией
        m.set_bbox({"color": color__, "alpha": 0.3})

    # переименовываем название графика
    name_of_g = (x_ + "_vs_" + y_).replace("\n", "")
    name_of_g = safe_name(name_of_g)

    # сохраняем рисунок
    fig.savefig(
        str(path_name_fiqure_folder_corr / f"{name_of_g}.png"),
        dpi=600,
        format="png",
        bbox_inches="tight",
    )
    plt.close(fig)
    ax.cla()
    plt.clf()


##############################################################
#
# Функция для построения корреляционных матриц
#
##############################################################
def corr_matrix_for_all_indexes(new_df, path_name_fiqure_folder_corr_matrix):
    sns.reset_orig()
    # определим, по каким параметрам будут корреляции
    all_things = set(new_df["index"])
    all_things = list(all_things)
    # делаем матрицы для всех
    for i in all_things:
        # создаем DataFrame по выделенному параметру
        df_for_corr = new_df[new_df["index"] == i]
        df_for_corr = df_for_corr[df_for_corr.columns[1:]]
        # какое будет название?
        title_ = (
            plot_feature_data__["name_of_corr_matrix"]
            + str(i)
            + " (n="
            + str(len(df_for_corr))
            + ")"
        )
        # корреляции делаем
        corr = df_for_corr.corr(method=plot_feature_data__["comboBox_correlation_figs_matrix"])
        corr = corr.apply(lambda x: round(x, 2))
        sns.set_theme(font_scale=plot_feature_data__["font_for_in"])
        plt.figure(
            figsize=(
                plot_feature_data__["corr_mat_figsize"],
                plot_feature_data__["corr_mat_figsize"],
            ),
        )
        plt.title(title_, fontsize=plot_feature_data__["font_for_out"])
        corr_matrix = sns.heatmap(
            corr,
            cmap=plot_feature_data__[
                "comboBox_correlation_color_map_for_figs"
            ],  # задаёт цветовую схему
            annot=True,  # рисует значения внутри ячеек
            linewidth=0.9,
            vmin=-1,
            vmax=1,
        )  # указывает начало цветовых кодов от -1 до 1.
        # Если нужно вращать подписи
        corr_matrix.set_xticklabels(corr_matrix.get_xticklabels(), rotation=90)
        corr_matrix.set_yticklabels(corr_matrix.get_yticklabels(), rotation=0)

        plt.tight_layout()
        name_of_file_ = str(i).replace("<", "less")
        name_of_file_ = name_of_file_.replace(">=", "more")
        plt.savefig(
            str(path_name_fiqure_folder_corr_matrix / f"{safe_name(name_of_file_)}.png"),
            dpi=600,
            format="png",
        )
        # также экспортируем в excel
        corr.to_excel(
            str(
                path_name_fiqure_folder_corr_matrix
                / f"{safe_name(name_of_file_)}_{plot_feature_data__['comboBox_correlation_figs_matrix']}.xlsx"
            ),
            engine="openpyxl",
        )
        plt.close()
        plt.clf()


##############################################################
#
# Функция для парных графиков - диаграмм рассеяния
#
##############################################################
def pairplot(new_df, hue_name_for_sheet, what_sheet, path):
    sns.reset_orig()
    sns.set_theme(font_scale=plot_feature_data__["doubleSpinBox_pairplot"])
    sns.set_style(plot_feature_data__["comboBox_style_pairplot"])

    if plot_feature_data__["comboBox_pairplot_kind"] == "reg":
        plot_kws = {"scatter_kws": {"s": plot_feature_data__["spinBox_point_size_for_pairplot"]}}
    elif plot_feature_data__["comboBox_pairplot_kind"] == "hist":
        plot_kws = None
    else:
        plot_kws = {"s": plot_feature_data__["spinBox_point_size_for_pairplot"]}

    # раньше я об этом не думал, но лучше было бы оставить самый первый столбец с изначальным именем
    if plot_feature_data__["check_pairplot"]:
        figure_pairplot = sns.pairplot(
            data=new_df,
            kind=plot_feature_data__["comboBox_pairplot_kind"],
            hue=None,
            plot_kws=plot_kws,
        )
    else:
        new_df = new_df.rename(columns={"index": hue_name_for_sheet})
        figure_pairplot = sns.pairplot(
            data=new_df,
            kind=plot_feature_data__["comboBox_pairplot_kind"],
            hue=hue_name_for_sheet,
            plot_kws=plot_kws,
            palette=plot_feature_data__["comboBox_color_pairplot"],
        )
        # раскомментировать ниже, если нужно выставить нижний предел
        """
        for ax in figure_pairplot.axes.flatten():
            ax.set_ylim(bottom=-10)
        """
        new_df = new_df.rename(columns={hue_name_for_sheet: "index"})

    figure_pairplot.savefig(str(path / f"{safe_name(what_sheet)}.png"), dpi=600, format="png")


##############################################################
#
# Функция для построения распределения по двум переменным
#
##############################################################
def jointplot(new_df, hue_name_for_sheet, what_sheet, path):
    sns.reset_orig()
    sns.set_theme(font_scale=plot_feature_data__["doubleSpinBox_jointplot"])
    sns.set_style(plot_feature_data__["comboBox_style_jointplot"])

    if plot_feature_data__["comboBox_pairplot_jointplot"] == "reg":
        plot_kws = {"scatter_kws": {"s": plot_feature_data__["spinBox_point_size_for_jointplot"]}}
    elif plot_feature_data__["comboBox_pairplot_jointplot"] == "hist":
        plot_kws = {}
    else:
        plot_kws = {"s": plot_feature_data__["spinBox_point_size_for_jointplot"]}

    # переименуем колонку для удобства
    new_df = new_df.rename(columns={"index": hue_name_for_sheet})

    # найдем все уникальные комбинации колонок
    ls = list(range(1, len(new_df.columns[1:]) + 1))
    combinations__ = [(ls[x], ls[x + y]) for y in reversed(ls) for x in range(len(ls) - y)]
    ###################
    # пройдемся по всем колонкам из combinations__
    for i in combinations__:
        x_, y_ = new_df.columns[i[0]], new_df.columns[i[1]]
        figure_jointplot = sns.jointplot(
            data=new_df,
            x=x_,
            y=y_,
            kind=plot_feature_data__["comboBox_pairplot_jointplot"],
            hue=hue_name_for_sheet,
            palette=plot_feature_data__["comboBox_color_jointplot"],
            **plot_kws,
        )
        figure_jointplot.savefig(
            str(path / f"{safe_name(what_sheet)}__{safe_name(x_)}__{safe_name(y_)}.png"),
            dpi=600,
            format="png",
        )

    # на всякий случай вернем, как всё было
    new_df = new_df.rename(columns={hue_name_for_sheet: "index"})


##############################################################
#
# функция для ошибок
#
##############################################################


def error_for_val_plot(plot_feature_data__, path, exel_name) -> str:
    if path == "":
        return "Путь для файла отсутствует"
    if exel_name == "":
        return "Имя файла отсутствует"
    if (
        plot_feature_data__["bottom_lim"]
        .replace(".", "")
        .replace(",", "")
        .replace("-", "")
        .isdigit()
        is False
        and plot_feature_data__["bottom_lim"] != ""
    ):
        return "Box plot: параметр нижней границы содержит буквы или неподдерживаемые символы"
    if (
        plot_feature_data__["upper_lim"]
        .replace(".", "")
        .replace(",", "")
        .replace("-", "")
        .isdigit()
        is False
        and plot_feature_data__["upper_lim"] != ""
    ):
        return "Box plot: параметр верхней границы содержит буквы или неподдерживаемые символы"
    return "__"


# функция для безопасного имени при сохранении
def safe_name(name: str) -> str:
    return (
        str(name)
        .replace("/", "")
        .replace("\n", "")
        .replace("\\frac", "")
        .replace("\\", "")
        .replace("$", "")
        .replace("{", "")
        .replace("}", "")
        .replace("*", "")
        .replace("%", "")
        .replace(":", "")
    )


# добавляем в массив plot_feature_data__ всё, что мы хотим -- я его так отдельно выделил в качестве безопасности при объявлении его global
def lets_add_all_parameters_for_figs_here(self):
    # так, конечно, не очень хорошо делать,
    # но я это очень удобный костыль
    # лучше было бы сделать словарь
    plot_feature_data__ = {}

    # цвет для box - палитра
    plot_feature_data__["color_pal_box"] = self.ui.comboBox_color_pal_box.currentText()
    # цвет для points - палитра
    plot_feature_data__["color_pal_points"] = self.ui.comboBox_color_pal_points.currentText()
    # цвет для box
    plot_feature_data__["color_box"] = self.ui.color_box.text()
    # цвет для points
    plot_feature_data__["color_points"] = self.ui.color_points.text()
    # SD or MAX-MIN
    plot_feature_data__["comboBox_sd_or_minmax"] = self.ui.comboBox_sd_or_minmax.currentText()
    # bottom limit
    plot_feature_data__["bottom_lim"] = self.ui.bottom_lim.text()
    # цвет для corr
    plot_feature_data__["color_pal_corr"] = self.ui.comboBox_color_pal_corr.currentText()
    # del hue для корреляционных графиков
    plot_feature_data__["del_hue"] = self.ui.del_hue.text()
    # matrix corr fig size
    plot_feature_data__["corr_mat_figsize"] = self.ui.corr_mat_figsize.value()
    # matrix font corr for in
    plot_feature_data__["font_for_in"] = self.ui.font_for_in.value()
    # matrix font corr for out
    plot_feature_data__["font_for_out"] = self.ui.font_for_out.value()
    # matrix name of corr figure
    plot_feature_data__["name_of_corr_matrix"] = self.ui.name_of_corr_matrix.text()
    # stat test
    plot_feature_data__["comboBox_stat_test"] = self.ui.comboBox_stat_test.currentText()
    # альтернативная гипотеза
    plot_feature_data__["comboBox_alter_hep"] = self.ui.comboBox_alter_hep.currentText()
    # spin x_label
    plot_feature_data__["comboBox_spin_x_"] = self.ui.comboBox_spin_x_.currentText()
    # sort x_label or not
    plot_feature_data__["check_sort_or_not"] = self.ui.check_sort_or_not.isChecked()
    # делать стат значимость или нет
    plot_feature_data__["check_stat_znachimost"] = self.ui.check_stat_znachimost.isChecked()
    # размер шрифт для оси x -- подпись
    plot_feature_data__["spinBox_x_label"] = self.ui.spinBox_x_label.value()
    # размер шрифт для оси y -- подпись
    plot_feature_data__["spinBox_y_label"] = self.ui.spinBox_y_label.value()
    # размер шрифт для оси x -- значения
    plot_feature_data__["spinBox_x_val"] = self.ui.spinBox_x_val.value()
    # размер шрифт для оси y -- значения
    plot_feature_data__["spinBox_y_vals"] = self.ui.spinBox_y_vals.value()
    # какой шрифт - только для Box
    plot_feature_data__["comboBox_fonts"] = self.ui.comboBox_fonts.currentText()
    # размер точек для среднего значения
    plot_feature_data__["spinBox_mean_val_size"] = self.ui.spinBox_mean_val_size.value()
    # нужно ли внизу размечать N
    plot_feature_data__["check_N_"] = self.ui.check_N_.isChecked()
    # сделать фон прозрачным или нет
    plot_feature_data__["check_background"] = self.ui.check_background.isChecked()
    # корреляционные кривые - надо изменять нижнюю границу или нет
    plot_feature_data__["check_change_corr_fig_down_limit"] = (
        self.ui.check_change_corr_fig_down_limit.isChecked()
    )
    # корреляционные кривые - нижняя граница
    plot_feature_data__["doubleSpinBox_corr_figs"] = self.ui.doubleSpinBox_corr_figs.value()
    # корреляционные кривые - размер точек
    plot_feature_data__["spinBox_points_corrFIGS"] = self.ui.spinBox_points_corrFIGS.value()
    # корреляционные кривые - размер шрифта на графике
    plot_feature_data__["doubleSpinBox_corr_figs_fontscale"] = (
        self.ui.doubleSpinBox_corr_figs_fontscale.value()
    )
    # корреляционные кривые - сортировать значения в группах или нет
    plot_feature_data__["check_sort_or_not_corr_figs"] = (
        self.ui.check_sort_or_not_corr_figs.isChecked()
    )
    # корреляционные кривые - сетка
    plot_feature_data__["check_setka"] = self.ui.check_setka.isChecked()
    # порядок подписей к box plot
    plot_feature_data__["order_box_plot"] = self.ui.order_box_plot.text()
    # изменить порядок стат. значимости
    plot_feature_data__["STAT_znachimost_order_box_plot"] = (
        self.ui.STAT_znachimost_order_box_plot.text()
    )
    # размер точек на графике box plot
    plot_feature_data__["point_size"] = self.ui.spinBox_point_size.value()
    # корреляционная матрица -- по чему считать корреляции -- по Пирсону или др
    plot_feature_data__["comboBox_correlation_figs_matrix"] = (
        self.ui.comboBox_correlation_figs_matrix.currentText()
    )
    # корреляционная матрица -- цветовая палитра
    plot_feature_data__["comboBox_correlation_color_map_for_figs"] = (
        self.ui.comboBox_correlation_color_map_for_figs.currentText()
    )
    # box-plot -- верхняя граница
    plot_feature_data__["upper_lim"] = self.ui.upper_lim.text()
    # box-plot -- шрифт значка стат. значимости
    plot_feature_data__["size_stat_znachimost"] = self.ui.spinBox_size_stat_znachimost.value()
    # box-plot -- значок стат. значимости (*, p< или p=)
    plot_feature_data__["box_plot_sign_stat_znachimost"] = (
        self.ui.comboBox_box_plot_sign_stat_znachimost.currentText()
    )
    # box-plot -- возрастание или убывание -- сортировки
    plot_feature_data__["check_sort_or_not_ascending"] = (
        self.ui.check_sort_or_not_ascending.isChecked()
    )
    # box-plot -- размер подписей N
    plot_feature_data__["box_check_N_"] = self.ui.comboBox_box_check_N_.currentText()
    # box-plot -- прозрачность точек
    plot_feature_data__["points_opasity"] = self.ui.doubleSpinBox_points_opasity.value()
    # pairplot: Не учитывать группу
    plot_feature_data__["check_pairplot"] = self.ui.check_pairplot.isChecked()
    # pairplot: Относительный размер шрифта
    plot_feature_data__["doubleSpinBox_pairplot"] = self.ui.doubleSpinBox_pairplot.value()
    # pairplot: Цветовая палитра
    plot_feature_data__["comboBox_color_pairplot"] = self.ui.comboBox_color_pairplot.currentText()
    # pairplot: Стиль
    plot_feature_data__["comboBox_style_pairplot"] = self.ui.comboBox_style_pairplot.currentText()
    # pairplot: Размер точек на графике
    plot_feature_data__["spinBox_point_size_for_pairplot"] = (
        self.ui.spinBox_point_size_for_pairplot.value()
    )
    # pairplot: kind
    plot_feature_data__["comboBox_pairplot_kind"] = self.ui.comboBox_pairplot_kind.currentText()
    ######
    # jointplot
    ######
    # jointplot: Относительный размер шрифта
    plot_feature_data__["doubleSpinBox_jointplot"] = self.ui.doubleSpinBox_jointplot.value()
    # jointplot: Цветовая палитра
    plot_feature_data__["comboBox_color_jointplot"] = self.ui.comboBox_color_jointplot.currentText()
    # jointplot: kind
    plot_feature_data__["comboBox_pairplot_jointplot"] = (
        self.ui.comboBox_pairplot_jointplot.currentText()
    )
    # jointplot: стиль
    plot_feature_data__["comboBox_style_jointplot"] = self.ui.comboBox_style_jointplot.currentText()
    # jointplot: Размер точек на графике
    plot_feature_data__["spinBox_point_size_for_jointplot"] = (
        self.ui.spinBox_point_size_for_jointplot.value()
    )
    ######
    # корреляции по одному параметру
    ######
    # корреляции по одному параметру: Пирсон или др.
    plot_feature_data__["correlation_one_parameter"] = (
        self.ui.comboBox_correlation_one_parameter.currentText()
    )
    # Корреляции по одному параметру: мин.знач. для корреляции
    plot_feature_data__["one_correlation"] = self.ui.doubleSpinBox_one_correlation.value()
    # корреляции по одному параметру: относительный шрифт
    plot_feature_data__["size_for_one_correlation"] = (
        self.ui.doubleSpinBox_size_for_one_correlation.value()
    )
    # корреляции по одному параметру: построить по всем параметрам
    plot_feature_data__["corr_one_parameter_only_one"] = (
        self.ui.check_corr_one_parameter_only_one.isChecked()
    )
    # корреляции по одному параметру: Построить график в отдельном окне
    plot_feature_data__["corr_one_parameter_plot_sep_wind"] = (
        self.ui.check_corr_one_parameter_plot_sep_wind.isChecked()
    )

    return plot_feature_data__
