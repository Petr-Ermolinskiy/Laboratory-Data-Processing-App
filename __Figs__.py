# необходимые библиотеки
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import numpy as np
import math
# для Пермутационных тестов
from permutations_stats.permutations import permutation_test, repeated_permutation_test
import numba

# для вывода диалогового окна
from PySide6.QtWidgets import QMessageBox

##############################################################
#
# главная функция
#
##############################################################
def figs_plot(self) -> None:
    dlg = QMessageBox(self)
    # закроем все рисунки, если они открыты
    # если этого не сделать, то может быть такое, что рисунки наложатся друг на друга
    plt.close()
    # в этот list будут записываться все доп. функции для графиков -- см. определение ниже
    global plot_feature_data__
    # я решил все особенности и кастомизацию графиков перевести в массив "plot_feature_data__" -- по большей части это связано с тем, что этот код я несколько раз переписывал
    plot_feature_data__ = lets_add_all_parameters_for_figs_here(self)
    #########################
    # параметры, которые нам понадобятся
    path = self.ui.path_for_plot.text()
    exel_name = self.ui.comboBox.currentText()
    # от чего смотрится зависимость?
    hue_name = self.ui.comboBox_2.currentText()
    # стоим или не строим - box plot, корреляционные графики или матрицы
    box_plot_or_not = self.ui.check_box_plot.isChecked()
    corr_is_need_matrix = self.ui.check_corr_matrix.isChecked()
    corr_is_need = self.ui.check_corr_figs.isChecked()
    # по всем листам проходимся или же только по одному?
    all_sheets_true = self.ui.check_box_figs_all_sheets.isChecked()
    one_sheet_name = self.ui.comboBox_figs_sheets.currentText()
    #########################
    # проверяем на ошибки
    checc = error_for_val_plot(plot_feature_data__, path, exel_name)

    if checc != '__':
        dlg.setWindowTitle("Графики")
        dlg.setText(checc)
        dlg.exec()
        return None

    # основной путь
    path = path + '//'
    # путь до файла
    files = path + exel_name

    try:
        names = pd.ExcelFile(files).sheet_names
    except Exception as e:
        dlg.setWindowTitle("Графики")
        dlg.setText('Нет такого файла/директории или файл испорчен.\n' + str(e))
        dlg.exec()
        return None

    # если стоит галочка, то проходимся по всем листам, но если же all_sheets_true == False
    # то выбираем только один лист
    if all_sheets_true == False:
        names = [one_sheet_name]

    # выполяем функцию do_for_one_sheet по всем листам (или же только по одному) в excel файле
    check_cykle = '__'
    for i in names:
        check_cykle = do_for_one_sheet(path, files, i, box_plot_or_not, corr_is_need, corr_is_need_matrix, hue_name)
        if check_cykle != '__':
            break
    if check_cykle == '__':
        dlg.setWindowTitle("Графики")
        dlg.setText('Все графики успешно сохранены')
        dlg.exec()
        return None
    else:
        dlg.setWindowTitle("Графики - Ошибка")
        dlg.setText(check_cykle)
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return None


##############################################################
#
# проходимся по одному листу и стоим всё, что надо
#
##############################################################
def do_for_one_sheet(path, files, what_sheet, box_plot_or_not, corr_is_need, corr_is_need_matrix, hue_name):
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
            return 'В таблице нет такого столбца:' + str(hue_name_for_sheet)
        index_for_col_interest = list(columns_of_interest).index(hue_name_for_sheet)
        columns_of_interest = columns_of_interest[index_for_col_interest + 1:]

    # все столбцы с данными приводим к численному виду

    for dd in columns_of_interest:
        try:
            df[dd] = df[dd].apply(pd.to_numeric)
        except Exception as e:
            message = 'В колонке ' + str(dd) + ' представлены значения, которые нельзя конвертировать в числа.\n' + str(e)
            return message

    # название оси X
    name_of_X_axis = hue_name_for_sheet
    # создаем новый DataFrame только с колонками для обработки
    new_df = df[columns_of_interest].copy()
    # и добавляем в него только колонку для значений индекса/концентрации/образца!
    new_df.insert(loc=0, column='index', value=df[hue_name_for_sheet])  # Диагноз
    if corr_is_need_matrix:
        # создаем подпапку для графиков корреляции
        name_fiqure_folder_corr_matrix = 'correlation_matrix' + '//' + what_sheet
        path_name_fiqure_folder_corr_matrix = path + name_fiqure_folder_corr_matrix
        os.makedirs(path_name_fiqure_folder_corr_matrix, exist_ok=True)
        # создаём корреляционные матрицы и сохраняем
        corr_matrix_for_all_indexes(new_df, path_name_fiqure_folder_corr_matrix)

    if corr_is_need:
        # создаем подпапку для графиков корреляции
        name_fiqure_folder_corr = 'correlation'
        path_name_fiqure_folder_corr = path + name_fiqure_folder_corr
        os.makedirs(path_name_fiqure_folder_corr, exist_ok=True)
        # what_is_hue = 'index'

        # найдет все уникальные комбинации признаков
        ls = list(range(1, len(new_df.columns[1:]) + 1))
        combinations__ = [(ls[x], ls[x + y]) for y in reversed(ls) for x in range((len(ls) - y))]
        ###################
        # пройдемся по всем колонкам из combinations__
        for i in combinations__:
            x_, y_ = new_df.columns[i[0]], new_df.columns[i[1]]
            only_regplot(df, x_, y_, path_name_fiqure_folder_corr, what_is_hue=hue_name_for_sheet, not_in_hue=plot_feature_data__[7],
                         color_palette=plot_feature_data__[6], _lim_=plot_feature_data__[5], sort_or_not=plot_feature_data__[15])

    if box_plot_or_not:
        # создаем подпапку для графиков аппроксимации
        name_fiqure_folder = 'fiqures'
        path_name_fiqure_folder = path + name_fiqure_folder
        os.makedirs(path_name_fiqure_folder, exist_ok=True)
        # создаем словарь значений параметров
        dict_for_future = {}
        # и создаем массив для DataFrame-ов
        df_list = []
        index_index = 0
        for i in new_df.columns:
            if i != 'index':
                # делаем словарь для индексов
                dict_for_future[i] = index_index
                index_index += 1
                # разделяем по индексу
                just_all_we_need = new_df.pivot(columns='index', values=i)
                # оставляем изначальный порядок значений
                just_all_we_need = just_all_we_need.reindex(columns=new_df['index'].unique()[::-1])
                # следующая сточка очень важна, чтобы не потерять какие-то значения, если есть ряд пропусков
                just_all_we_need2 = pd.DataFrame(index=list(range(0, max(just_all_we_need.count()))))
                # убираем NaN
                for j in just_all_we_need.columns:
                    ignore_nan = just_all_we_need[j]
                    ignore_nan = ignore_nan.dropna()
                    ignore_nan = ignore_nan.reset_index(drop=True)
                    just_all_we_need2.insert(loc=0, column=j, value=ignore_nan)
                # изменяем порядок колонок - сортируем, если это надо
                if plot_feature_data__[15]:
                    just_all_we_need2 = just_all_we_need2[just_all_we_need2.columns.sort_values(ascending=plot_feature_data__[39])]
                elif plot_feature_data__[31]!='':
                    columns__temp = plot_feature_data__[31].replace(',', '').replace(';', ' ').split()

                    if len(just_all_we_need2.columns) != len(columns__temp):
                        return f'Кол-во подписей в поле <Изменить порядок подписей> не верно.\n Должно быть {len(just_all_we_need2.columns)}, а введено {len(columns__temp)}.'
                    try:
                        columns__temp = list(map(int, columns__temp))
                        columns__temp = [x - 1 for x in columns__temp]
                        columns__ = [just_all_we_need2.columns[x] for x in columns__temp]
                        just_all_we_need2 = just_all_we_need2.reindex(columns=columns__)
                    except Exception as e:
                        return 'Поле <Изменить порядок подписей> заполнено не верно.\n' + str(e)

                # сохраняем в список DataFrame-ов
                df_list.append(just_all_we_need2)
        if plot_feature_data__[16]:
            # вот и массив с таблицами p-values
            try:
                df_list_stat = calculate_table_for_p_val(df_list, dict_for_future)
            except Exception as e:
                return 'Скорее всего проблема с данными: в одной из групп отсутствуют данные для обработки.\n' + str(e)
        # вот и массив для графиков
        big_G = just_to_numpy_for_plot(df_list, dict_for_future)
        # построение графиков
        check = just_plot_it_(big_G, dict_for_future, df_list, name_of_X_axis, path_name_fiqure_folder)
        if check != '__':
            return check

        if plot_feature_data__[16]:
            # создаем подпапку для exel файлов
            os.makedirs(path + 'stat', exist_ok=True)
            #############
            with pd.ExcelWriter(path + 'stat' + '//' + what_sheet + ".xlsx") as writer:
                for i in dict_for_future:
                    name_of_sheet = i
                    name_of_sheet = safe_name(name_of_sheet)

                    if len(name_of_sheet) > 31:
                        name_of_sheet = name_of_sheet[0:30]
                    df_list[dict_for_future[i]].to_excel(writer, sheet_name=name_of_sheet)
            #############
            with pd.ExcelWriter(
                    path + 'stat' + '//' + what_sheet + '_' + plot_feature_data__[12] + "_p-values.xlsx") as writer:
                for i in dict_for_future:
                    name_of_sheet = i
                    name_of_sheet = safe_name(name_of_sheet)

                    if len(name_of_sheet) > 31:
                        name_of_sheet = name_of_sheet[0:30]
                    df_list_stat[dict_for_future[i]].to_excel(writer, sheet_name=name_of_sheet)
    return '__'



##############################################################
#
# BOX PLOT
#
##############################################################
# функцию эту я не всю придумал сам, а взял часть с сайта https://rowannicholls.github.io/python/graphs/ax_based/boxplots_significance.html#test-for-statistical-significance
# также см. ссылку: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html
def box_and_whisker(data, title, xlabel, ylabel, xticklabels, Name_fiqure, path_name_fiqure_folder, make_an_SD=True):
    sns.reset_orig()
    """
    Create a box-and-whisker plot with significance bars.
    """
    # если будем строить со стандарным отклоением, то укажем дополнительный аргумент
    if make_an_SD:
        whisk_MIN_MAX = 0
    else:
        whisk_MIN_MAX = 1.5

    # аргумент positions -- очень важен -- без него всё поедет! positions=range(len(data)) !
    ax = plt.axes()
    ax.cla()
    bp = ax.boxplot(data, widths=0.6, whis=whisk_MIN_MAX, patch_artist=True, positions=range(len(data)), showmeans=True,
                    showfliers=False, meanprops={"marker": "D", "markerfacecolor": "white", "markeredgecolor": "black",
                                                 "markersize": str(plot_feature_data__[22])})

    ###изменить цвета! если введен агрумент цвета, то цвет будет один;
    # есть такие цвета хорошие 'Pastel1' 'Blues' 'Greens' 'Purples' или такие https://r02b.github.io/seaborn_palettes/
    if plot_feature_data__[2] == '' and plot_feature_data__[3] == '':
        # для точек измерений
        take_a_color_point = plot_feature_data__[1]
        # специальный массив для box-ов
        colors = sns.color_palette(plot_feature_data__[0])
    elif plot_feature_data__[2] == '' and plot_feature_data__[3] != '':
        # для точек измерений
        if '&' in plot_feature_data__[3]:
            take_a_color_point = filter(None, plot_feature_data__[3].split('&'))
        else:
            take_a_color_point = [plot_feature_data__[3]] * len(bp['boxes'])
        # специальный массив для box-ов
        colors = sns.color_palette(plot_feature_data__[0])
    elif plot_feature_data__[2] != '' and plot_feature_data__[3] == '':
        # для точек измерений
        take_a_color_point = plot_feature_data__[1]
        # специальный массив для box-ов
        if '&' in plot_feature_data__[2]:
            colors = filter(None, plot_feature_data__[2].split('&'))
        else:
            colors = [plot_feature_data__[2]] * len(bp['boxes'])
    else:
        # для точек измерений
        if '&' in plot_feature_data__[3]:
            take_a_color_point = filter(None, plot_feature_data__[3].split('&'))
        else:
            take_a_color_point = [plot_feature_data__[3]] * len(bp['boxes'])
        # специальный массив для box-ов
        if '&' in plot_feature_data__[2]:
            colors = plot_feature_data__[2].split('&')
        else:
            colors = [plot_feature_data__[2]] * len(bp['boxes'])

    # стандартное отклонение - добавить вместо разброса между min-max
    if make_an_SD:
        sns.set(style="ticks", rc={"lines.linewidth": 0.7})
        sns.pointplot(data=data, palette=['black'] * len(bp['boxes']), ax=ax, errorbar="sd", capsize=0.2)

    # добавить точки! цвет: palette=take_a_color_point
    try:
        sns.stripplot(data=data, alpha=plot_feature_data__[41], palette=take_a_color_point, ax=ax, linewidth=1, size=plot_feature_data__[33])
    except Exception as e:
        return 'Box plot: скорее всего вы ввели неправильный(е) цвет(а) HEX.\nЦвет для HEX должен быть в формате <#XXXXXX>.\nДля нескольких цветов используйте разделительный знак: &.\n' + str(e)

    ####################################

    # вот тут добавляются цвета к нашим box-ам
    ##############
    try:
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
    except Exception as e:
        return 'Box plot: скорее всего вы ввели неправильный(е) цвет(а) HEX.\nЦвет для HEX должен быть в формате <#XXXXXX>.\nДля нескольких цветов используйте разделительный знак: &.\n' + str(e)

    # Colour of the median lines
    plt.setp(bp['medians'], color='k')

    if plot_feature_data__[16]:
        # Check for statistical significance
        significant_combinations = []
        # Check from the outside pairs of boxes inwards
        if plot_feature_data__[32] != '':
            try:
                combinations = plot_feature_data__[32].split()
                combinations = [item.replace('(', '').replace(')', '') for item in combinations]
                combinations = [tuple(map(int, item.split(','))) for item in combinations]
            except Exception as e:
                return 'Box plot: неправильное значение в поле <Расчёт стат.значимости только между следующими группами>:\n' + str(e)
        else:
            ls = list(range(1, len(data) + 1))
            combinations = [(ls[x], ls[x + y]) for y in reversed(ls) for x in range((len(ls) - y))]
        for c in combinations:
            data1 = data[c[0] - 1]
            data2 = data[c[1] - 1]

            # Significance
            if plot_feature_data__[12] == 'U-критерий Манна — Уитни':
                _, p = stats.mannwhitneyu(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Т-критерий Стьюдента':
                _, p = stats.ttest_ind(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Критерий Уилкоксона':
                _, p = stats.wilcoxon(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Критерий Краскела — Уоллиса':
                _, p = stats.kruskal(data1, data2)
            elif plot_feature_data__[12] == 'Медианный критерий':
                _, p = stats.mood(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Тест Ансари-Брэдли':
                _, p = stats.ansari(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Тест Бруннера — Мюнцеля':
                _, p = stats.brunnermunzel(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Тест Бруннера — Мюнцеля (normal)':
                #distribution='normal' - если что-то не так или данные только одно значение, но в этом случае этот тест лучше не использовать
                _, p = stats.brunnermunzel(data1, data2, distribution='normal', alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Тест Фишера-Питмана':
                def statistic(x, y, axis):
                    return np.mean(x, axis=axis) - np.mean(y, axis=axis)

                # вычисляем
                all_data = stats.permutation_test((data1, data2), statistic, permutation_type='independent', vectorized=True, alternative=plot_feature_data__[13])
                # само значение p
                p = all_data.pvalue
            elif plot_feature_data__[12] == 'Пермутационный критерий Бруннера — Мюнцеля':
                stat = permutation_test(data1, data2, test="brunner_munzel",
                                        alternative=plot_feature_data__[13])
                p = stat.pvalue
            elif plot_feature_data__[12] == 'Пермутационный критерий Манна — Уитни':
                stat = permutation_test(data1, data2, test="mann_whitney",
                                        alternative=plot_feature_data__[13])
                p = stat.pvalue
            elif plot_feature_data__[12] == 'Пермутационный критерий Уилкоксона':
                # изменим формат
                data_for_paired_permutations = np.vstack([data1, data2]).T
                # сделаем расчет
                stat = repeated_permutation_test(data_for_paired_permutations, test="wilcoxon", alternative=plot_feature_data__[13])
                p = stat.pvalue
            elif plot_feature_data__[12] == 'Пермутационный критерий Фридмана':
                # изменим формат
                data_for_paired_permutations = np.vstack([data1, data2]).T
                # сделаем расчет
                stat = repeated_permutation_test(data_for_paired_permutations, test="friedman", alternative=plot_feature_data__[13])
                p = stat.pvalue
            else:
                pass

            if p < 0.05:
                significant_combinations.append([c, p])

        # Get info about y-axis
        bottom, top = ax.get_ylim()
        yrange = top - bottom

        # Significance bars
        for i, significant_combination in enumerate(significant_combinations):
            # Columns corresponding to the datasets of interest
            x1 = significant_combination[0][0]
            x2 = significant_combination[0][1]
            # What level is this bar among the bars above the plot?
            level = len(significant_combinations) - i
            # Plot the bar
            bar_height = (yrange * 0.08 * level) + top
            bar_tips = bar_height - (yrange * 0.02)
            plt.plot(
                [x1 - 1, x1 - 1, x2 - 1, x2 - 1],
                [bar_tips, bar_height, bar_height, bar_tips], lw=1, c='k')
            ##############
            # эта функция нужна, если нужно точное значение p
            def round_to(num, digits=2):
                if num == 0: return 0
                scale = int(-math.floor(math.log10(abs(num - int(num))))) + digits - 1
                if scale < digits: scale = digits
                return round(num, scale)
            ##############
            # Significance level
            p = significant_combination[1]
            if p < 0.0001:
                sig_symbol = '****'
                if plot_feature_data__[38] == 'меньше какого-то значения (p<)':
                    sig_symbol = 'p < 0.0001'
                elif plot_feature_data__[38] == 'равно какому-то значению (p=)':
                    sig_symbol = 'p = ' + str(round_to(p))
            elif p < 0.001:
                sig_symbol = '***'
                if plot_feature_data__[38] == 'меньше какого-то значения (p<)':
                    sig_symbol = 'p < 0.001'
                elif plot_feature_data__[38] == 'равно какому-то значению (p=)':
                    sig_symbol = 'p = ' + str(round_to(p))
            elif p < 0.01:
                sig_symbol = '**'
                if plot_feature_data__[38] == 'меньше какого-то значения (p<)':
                    sig_symbol = 'p < 0.01'
                elif plot_feature_data__[38] == 'равно какому-то значению (p=)':
                    sig_symbol = 'p = ' + str(round_to(p))
            elif p < 0.05:
                sig_symbol = '*'
                if plot_feature_data__[38] == 'меньше какого-то значения (p<)':
                    sig_symbol = 'p < 0.05'
                elif plot_feature_data__[38] == 'равно какому-то значению (p=)':
                    sig_symbol = 'p = ' + str(round_to(p))
            text_height = bar_height + (yrange * 0.01)
            plt.text((x1 - 1 + x2 - 1) * 0.5, text_height, sig_symbol, ha='center', c='k', fontsize = plot_feature_data__[37])
    ###############
    # Изменим границы оси Y
    ###############
    bottom, top = ax.get_ylim()
    yrange = top - bottom
    # <0.02 * yrange> нужно, чтобы смотрелось всё хорошо, если не введена нижняя/верхняя граница
    ax.set_ylim(bottom - 0.02 * yrange, top + 0.02 * yrange)

    if plot_feature_data__[5] != '':
        bottom = float(plot_feature_data__[5].replace(",", "."))
        ax.set_ylim(bottom, top)
    if plot_feature_data__[36] != '':
        top = float(plot_feature_data__[36].replace(",", "."))
        ax.set_ylim(bottom, top)

    if plot_feature_data__[5] != '':
        # это нужно, чтобы N - количество данных отображалось корректно
        bottom = bottom + 0.02 * yrange

    # Annotate sample size below each box
    # ''' внизу чтобы было кол-во данных
    if plot_feature_data__[23]:
        for i, dataset in enumerate(data):
            sample_size = len(dataset)
            ax.text(i, bottom, fr'n = {sample_size}', ha='center', size=plot_feature_data__[40])
    # '''

    ######### Шрифт воставляем в самом конце, т.к. из-за изменения осей могут быть ошибки
    # Label y-axis
    ax.set_ylabel(ylabel, fontsize=plot_feature_data__[18], fontname=plot_feature_data__[21])
    # Label x-axis
    ax.set_xlabel(xlabel, fontsize=plot_feature_data__[17], fontname=plot_feature_data__[21])
    # Label x-axis ticks -- если нужно, можно добавить "rotation=40"
    new_x_tick_label = [item.replace('\\n', '\n') for item in map(str, list(xticklabels))]
    ax.set_xticklabels(new_x_tick_label, rotation=int(plot_feature_data__[14]))
    #################################### размер шрифта подписи
    plt.yticks(fontsize=plot_feature_data__[20], fontname=plot_feature_data__[21])
    plt.xticks(fontsize=plot_feature_data__[19], fontname=plot_feature_data__[21])

    # Hide x-axis major ticks
    ax.tick_params(axis='x', which='major', length=0)
    # Show x-axis minor ticks
    xticks = [0.5] + [x + 0.5 for x in ax.get_xticks()]
    ax.set_xticks(xticks, minor=True)
    # Clean up the appearance
    ax.tick_params(axis='x', which='minor', length=3, width=1)

    # очень важно, чтобы не обрезалось
    plt.tight_layout()
    try:
        # сохранение рисунка
        plt.savefig(path_name_fiqure_folder + '//' + safe_name(Name_fiqure) + '.png', dpi=600, format='png', transparent=plot_feature_data__[24])
    except Exception as e:
        return 'Box plot: ' + str(e)
    plt.close()
    ax.cla()
    plt.clf()
    return '__'


# Функция для преобразования данных для построения
def just_to_numpy_for_plot(df_list, dict_for_future):
    big_G = []
    small_G = []
    for parameter_ in dict_for_future:
        for i in df_list[dict_for_future[parameter_]].columns:
            small_G.append(df_list[dict_for_future[parameter_]][i].dropna().to_numpy())
        big_G.append(small_G)
        small_G = []
    return big_G


# Функция для построения графиков по входному массиву
def just_plot_it_(big_G, dict_for_future, df_list, name_of_X_axis, path_name_fiqure_folder):
    for parameter_ in dict_for_future:
        do_SD = True if plot_feature_data__[4] == 'SD' else False
        ylabel = parameter_
        check=box_and_whisker(big_G[dict_for_future[parameter_]], '', name_of_X_axis, ylabel,
                        df_list[dict_for_future[parameter_]].columns, parameter_, path_name_fiqure_folder,
                        make_an_SD=do_SD)
        if check != '__':
            return check
    return '__'


# Функция для получения массива датафреймов с таблицами p-values
def calculate_table_for_p_val(df_list, dict_for_future):
    df_list_stat = []
    for i in dict_for_future:
        dop_DF = pd.DataFrame(index=df_list[dict_for_future[i]].columns, columns=df_list[dict_for_future[i]].columns)
        # пройдемся по всем парам столбцов
        for col1 in dop_DF.columns:
            for col2 in dop_DF.columns:
                if col1 == col2:
                    dop_DF.loc[col1, col2] = 1.0
                    continue
                # рассчитаем стат. значимости
                if plot_feature_data__[12] == 'U-критерий Манна — Уитни':
                    _, p_value = stats.mannwhitneyu(df_list[dict_for_future[i]][col1].dropna(),
                                                            df_list[dict_for_future[i]][col2].dropna(),
                                                            alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Т-критерий Стьюдента':
                    _, p_value = stats.ttest_ind(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna(),
                                                         alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Критерий Уилкоксона':
                    _, p_value = stats.wilcoxon(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna(),
                                                         alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Критерий Краскела — Уоллиса':
                    _, p_value = stats.kruskal(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna())
                elif plot_feature_data__[12] == 'Медианный критерий':
                    _, p_value = stats.mood(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna(),
                                                         alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Тест Ансари-Брэдли':
                    _, p_value = stats.ansari(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna(),
                                                         alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Тест Бруннера — Мюнцеля':
                    _, p_value = stats.brunnermunzel(df_list[dict_for_future[i]][col1].dropna(),
                                                             df_list[dict_for_future[i]][col2].dropna(),
                                                             alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Тест Бруннера — Мюнцеля (normal)':
                    _, p_value = stats.brunnermunzel(df_list[dict_for_future[i]][col1].dropna(),
                                                             df_list[dict_for_future[i]][col2].dropna(),
                                                             distribution='normal',
                                                             alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Тест Фишера-Питмана':
                    def statistic(x, y, axis):
                        return np.mean(x, axis=axis) - np.mean(y, axis=axis)
                    # вычисляем
                    all_data = stats.permutation_test((df_list[dict_for_future[i]][col1].dropna(), df_list[dict_for_future[i]][col2].dropna()), statistic, permutation_type='independent',
                                          vectorized=True, alternative=plot_feature_data__[13])
                    # само значение p
                    p_value = all_data.pvalue

                elif plot_feature_data__[12] == 'Пермутационный критерий Бруннера — Мюнцеля':
                    stat = permutation_test(df_list[dict_for_future[i]][col1].dropna(), df_list[dict_for_future[i]][col2].dropna(), test="brunner_munzel",
                                            alternative=plot_feature_data__[13])
                    p_value = stat.pvalue
                elif plot_feature_data__[12] == 'Пермутационный критерий Манна — Уитни':
                    stat = permutation_test(df_list[dict_for_future[i]][col1].dropna(), df_list[dict_for_future[i]][col2].dropna(), test="mann_whitney",
                                            alternative=plot_feature_data__[13])
                    p_value = stat.pvalue
                elif plot_feature_data__[12] == 'Пермутационный критерий Уилкоксона':
                    # изменим формат
                    data_for_paired_permutations = np.vstack([df_list[dict_for_future[i]][col1].dropna(), df_list[dict_for_future[i]][col2].dropna()]).T
                    # сделаем расчет
                    stat = repeated_permutation_test(data_for_paired_permutations, test="wilcoxon", alternative=plot_feature_data__[13])
                    p_value = stat.pvalue
                elif plot_feature_data__[12] == 'Пермутационный критерий Фридмана':
                    # изменим формат
                    data_for_paired_permutations = np.vstack([df_list[dict_for_future[i]][col1].dropna(), df_list[dict_for_future[i]][col2].dropna()]).T
                    # сделаем расчет
                    stat = repeated_permutation_test(data_for_paired_permutations, test="friedman", alternative=plot_feature_data__[13])
                    p_value = stat.pvalue
                else:
                    pass
                # добавим в наш DataFrame
                dop_DF.loc[col1, col2] = round(p_value, 4)
        df_list_stat.append(dop_DF)
        df_list_stat[dict_for_future[i]] = df_list_stat[dict_for_future[i]].style.applymap(
            lambda x: 'color:red' if x < 0.05 else 'color:black')
    return df_list_stat


##############################################################
#
# Функция для построения графиков корреляций
#
##############################################################
def only_regplot(df, x_, y_, path_name_fiqure_folder_corr, what_is_hue, color_palette=None, not_in_hue=[], _lim_='', sort_or_not=False):
    sns.reset_orig()
    sns.set(font_scale=plot_feature_data__[28])
    #стиль
    sns.set_style("ticks")
    if plot_feature_data__[30]:
        sns.set_style("whitegrid", {'axes.grid': True, "grid.color": ".9", "grid.linestyle": "--"})

    # узнаем в каком цвете нам строить задний фон под аннотацией к коэффициенту Пирсона
    current_color = sns.color_palette(color_palette)
    # создаём лист по интерисующим группам
    hue_what = df[what_is_hue].unique()
    hue_what = list(hue_what)
    if plot_feature_data__[29]:
        hue_what.sort()
    # удаляем элемент_ы hue, если это нужно
    try:
        if type(not_in_hue) == str and not_in_hue!='':
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
    for i, color__ in zip(hue_what, current_color):
        sns.regplot(data=df[df[what_is_hue] == i], x=x_, y=y_, ax=ax, color=color__, label=i, scatter_kws={'s': plot_feature_data__[27]})
        _, top = ax.get_ylim()
        max_ylim = max(max_ylim, top)
    # поменяем пределы значений на оси y
    if plot_feature_data__[25]:
        ax.set_ylim(plot_feature_data__[26], max_ylim)

    # и для каждой группы находим коэффициент Пирсона и добавляем его на график
    for val, color__ in zip(hue_what, current_color):
        new_massive = df[(df[what_is_hue] == val)][[x_, y_]].dropna()
        r, _ = stats.pearsonr(x=new_massive[x_], y=new_massive[y_])
        m = plt.text(.65, .93 - .1 * hue_what.index(val),
                     "{} (n={}): r = {:.2f}".format(val, len(df[(df[what_is_hue] == val)][x_]), r),
                     transform=ax.transAxes)
        # сделаем красивую рамку под аннотацией
        m.set_bbox(dict(color=color__, alpha=0.3))

    # переименовываем название графика
    name_of_g = (x_ + '_vs_' + y_).replace('\n', '')
    name_of_g = safe_name(name_of_g)

    # сохраняем рисунок
    fig.savefig(path_name_fiqure_folder_corr + '//' + name_of_g + '.png', dpi=600, format='png', bbox_inches='tight')
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
    all_things = set(new_df['index'])
    all_things = list(all_things)
    # делаем матрицы для всех
    for i in all_things:
        # создаем DataFrame по выделенному параметру
        df_for_corr = new_df[new_df['index'] == i]
        df_for_corr = df_for_corr[df_for_corr.columns[1:]]
        # какое будет название?
        # title_ = "Correlation matrix of the capillary blood flow characteristics\n for the " + i +' group (n=' + str(int(len(df_for_corr))) + ')'
        title_ = plot_feature_data__[11] + str(i) + ' (n=' + str(int(len(df_for_corr))) + ')'
        # корреляции делаем
        corr = df_for_corr.corr(method=plot_feature_data__[34])
        sns.set(font_scale=plot_feature_data__[9])
        plt.figure(figsize=(plot_feature_data__[8], plot_feature_data__[8]))
        plt.title(title_, fontsize=plot_feature_data__[10])
        sns.heatmap(corr,
                    cmap=plot_feature_data__[35],  # задаёт цветовую схему
                    annot=True,  # рисует значения внутри ячеек
                    linewidth=.9,
                    vmin=-1, vmax=1)  # указывает начало цветовых кодов от -1 до 1.
        plt.tight_layout()
        name_of_file_ = str(i).replace('<', 'less')
        name_of_file_ = name_of_file_.replace('>=', 'more')
        plt.savefig(path_name_fiqure_folder_corr_matrix + '//' + safe_name(name_of_file_) + '.png', dpi=600, format='png')
        #также экспортируем в excel
        corr.to_excel(path_name_fiqure_folder_corr_matrix + '//' + safe_name(name_of_file_) + '_' + plot_feature_data__[34] + ".xlsx", engine="openpyxl")
        plt.close()
        plt.clf()



##############################################################
#
# функция для ошибок
#
##############################################################

def error_for_val_plot(plot_feature_data__, path, exel_name):
    if path == '':
        return 'Путь для файла отсутствует'
    if exel_name == '':
        return 'Имя файла отсутствует'
    if plot_feature_data__[5].replace(".", "").replace(",", "").isdigit() is False and plot_feature_data__[5] != '':
        return 'Box plot: параметр нижней границы содержит буквы'
    if plot_feature_data__[36].replace(".", "").replace(",", "").isdigit() is False and plot_feature_data__[5] != '':
        return 'Box plot: параметр верхней границы содержит буквы'
    return '__'

# функция для безопасного имени при сохранении
def safe_name(name) -> str:
    name = name.replace('/', '').replace('\n', '').replace('\\frac', '').replace('\\', '').replace('$', '').replace('{', '').replace('}', '').replace('*', '').replace('%', '').replace(':', '')
    return name


# добавляем в массив plot_feature_data__ всё, что мы хотим -- я его так отдельно выделил в качестве безопасности при объявлении его global
def lets_add_all_parameters_for_figs_here(self):
    # так, конечно, не очень хорошо делать, но я не думаю, что это прям очень неудобный кастыль
    # я так всё пишу, потому что я всё это переписывал и данная запись наиболее читаема
    plot_feature_data__ = [0] * 100

    # цвет для box - палитра
    plot_feature_data__[0] = self.ui.comboBox_color_pal_box.currentText()
    # цвет для points - палитра
    plot_feature_data__[1] = self.ui.comboBox_color_pal_points.currentText()
    # цвет для box
    plot_feature_data__[2] = self.ui.color_box.text()
    # цвет для points
    plot_feature_data__[3] = self.ui.color_points.text()
    # SD or MAX-MIN
    plot_feature_data__[4] = self.ui.comboBox_sd_or_minmax.currentText()
    # bottom limit
    plot_feature_data__[5] = self.ui.bottom_lim.text()
    # цвет для corr
    plot_feature_data__[6] = self.ui.comboBox_color_pal_corr.currentText()
    # del hue для корреляционных графиков
    plot_feature_data__[7] = self.ui.del_hue.text()
    # matrix corr fig size
    plot_feature_data__[8] = self.ui.corr_mat_figsize.value()
    # matrix font corr for in
    plot_feature_data__[9] = self.ui.font_for_in.value()
    # matrix font corr for out
    plot_feature_data__[10] = self.ui.font_for_out.value()
    # matrix name of corr figure
    plot_feature_data__[11] = self.ui.name_of_corr_matrix.text()
    # stat test
    plot_feature_data__[12] = self.ui.comboBox_stat_test.currentText()
    # alter heposisis
    plot_feature_data__[13] = self.ui.comboBox_alter_hep.currentText()
    # spin x_label
    plot_feature_data__[14] = self.ui.comboBox_spin_x_.currentText()
    # sort x_label or not
    plot_feature_data__[15] = self.ui.check_sort_or_not.isChecked()
    # делать стат значимость или нет
    plot_feature_data__[16] = self.ui.check_stat_znachimost.isChecked()
    # размер шрифт для оси x -- подпись
    plot_feature_data__[17] = self.ui.spinBox_x_label.value()
    # размер шрифт для оси y -- подпись
    plot_feature_data__[18] = self.ui.spinBox_y_label.value()
    # размер шрифт для оси x -- значения
    plot_feature_data__[19] = self.ui.spinBox_x_val.value()
    # размер шрифт для оси y -- значения
    plot_feature_data__[20] = self.ui.spinBox_y_vals.value()
    # какой шрифт - только для Box
    plot_feature_data__[21] = self.ui.comboBox_fonts.currentText()
    # размер точек для среднего значения
    plot_feature_data__[22] = self.ui.spinBox_mean_val_size.value()
    # нужно ли внизу размечать N
    plot_feature_data__[23] = self.ui.check_N_.isChecked()
    # сделать фон прозрачным или нет
    plot_feature_data__[24] = self.ui.check_background.isChecked()
    # корреляционные кривые - надо изменять нижнюю границу или нет
    plot_feature_data__[25] = self.ui.check_change_corr_fig_down_limit.isChecked()
    # корреляционные кривые - нижняя граница
    plot_feature_data__[26] = self.ui.doubleSpinBox_corr_figs.value()
    # корреляционные кривые - размер точек
    plot_feature_data__[27] = self.ui.spinBox_points_corrFIGS.value()
    # корреляционные кривые - размер шрифта на графике
    plot_feature_data__[28] = self.ui.doubleSpinBox_corr_figs_fontscale.value()
    # корреляционные кривые - сортировать значения в группах или нет
    plot_feature_data__[29] = self.ui.check_sort_or_not_corr_figs.isChecked()
    # корреляционные кривые - сетка
    plot_feature_data__[30] = self.ui.check_setka.isChecked()
    # порядок подписей к box plot
    plot_feature_data__[31] = self.ui.order_box_plot.text()
    # изменить порядок стат. значимости
    plot_feature_data__[32] = self.ui.STAT_znachimost_order_box_plot.text()
    # размер точек на графике box plot
    plot_feature_data__[33] = self.ui.spinBox_point_size.value()
    # корреляционная матрица -- по чему считать корреляции -- по пирсону или др
    plot_feature_data__[34] = self.ui.comboBox_correlation_figs_matrix.currentText()
    # корреляционная матрица -- цветовая палитра
    plot_feature_data__[35] = self.ui.comboBox_correlation_color_map_for_figs.currentText()
    # box-plot -- верхняя граница
    plot_feature_data__[36] = self.ui.upper_lim.text()
    # box-plot -- шрифт значка стат. значимости
    plot_feature_data__[37] = self.ui.spinBox_size_stat_znachimost.value()
    # box-plot -- значок стат. значимости (*, p< или p=)
    plot_feature_data__[38] = self.ui.comboBox_box_plot_sign_stat_znachimost.currentText()
    # box-plot -- возрастание или убывание -- сортировки
    plot_feature_data__[39] = self.ui.check_sort_or_not_ascending.isChecked()
    # box-plot -- размер подписей N
    plot_feature_data__[40] = self.ui.comboBox_box_check_N_.currentText()
    # box-plot -- прозрачность точек
    plot_feature_data__[41] = self.ui.doubleSpinBox_points_opasity.value()

    return plot_feature_data__

