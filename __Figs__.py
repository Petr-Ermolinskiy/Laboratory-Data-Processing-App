# необходимые библиотеки
# для работы с папками
import os
from tkinter import messagebox

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

##############################################################
'''
plot_feature_data__[0] - цвет для box - палитра
plot_feature_data__[1] - цвет для points - палитра
plot_feature_data__[2] - цвет для box
plot_feature_data__[3] - цвет для points
plot_feature_data__[4] - SD or MAX-MIN
plot_feature_data__[5] - bottom limit
plot_feature_data__[6] - цвет для corr
plot_feature_data__[7] - del hue
plot_feature_data__[8] - matrix corr fig size
plot_feature_data__[9] - matrix font corr for in
plot_feature_data__[10] - matrix font corr for out
plot_feature_data__[11] - matrix name of corr figure
plot_feature_data__[12] - stat test
plot_feature_data__[13] - alter heposisis
plot_feature_data__[14] - spin x_label
plot_feature_data__[15] - sort x_label or not
plot_feature_data__[16] - делать стат значимость или нет
plot_feature_data__[17] - размер шрифт для оси x -- подпись
plot_feature_data__[18] - размер шрифт для оси y -- подпись
plot_feature_data__[19] - размер шрифт для оси x -- значения
plot_feature_data__[20] - размер шрифт для оси y -- значения
plot_feature_data__[21] - какой шрифт - только для Box
plot_feature_data__[22] - размер точек для среднего значения
plot_feature_data__[23] - нужно ли внизу размечать N
plot_feature_data__[24] - сделать фон прозрачным или нет
plot_feature_data__[25] - корреляционные кривые - надо изменять нижнюю границу или нет
plot_feature_data__[26] - корреляционные кривые - нижняя граница
plot_feature_data__[27] - корреляционные кривые - размер точек
plot_feature_data__[28] - корреляционные кривые - размер шрифта на графике
plot_feature_data__[29] - корреляционные кривые - сортировать значения в группах или нет
plot_feature_data__[30] - корреляционные кривые - сетка
plot_feature_data__[31] - порядок подписей к box plot
plot_feature_data__[32] - изменить порядок стат. значимости
'''


##############################################################
def safe_name(name) -> str:
    name = name.replace('/', '').replace('\n', '').replace('\\frac', '').replace('\\', '').replace('$', '').replace('{', '').replace('}', '').replace('*', '').replace('%', '').replace(':', '')
    return name


# функцию эту я не всю придумал сам, а взял часть с сайта https://rowannicholls.github.io/python/graphs/ax_based/boxplots_significance.html#test-for-statistical-significance
# также см. ссылку: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html
def box_and_whisker(data, title, xlabel, ylabel, xticklabels, Name_fiqure, bottom_lim='', make_an_SD=True):
    global stat_znachimost
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

    ###изменить цвета! если введен агрумент цвета, то цвет будет один; есть такие цвета хорошие 'Pastel1' 'Blues' 'Greens' 'Purples' или такие https://r02b.github.io/seaborn_palettes/
    if plot_feature_data__[2] == '' or plot_feature_data__[3] == '':
        # для точек измерений
        take_a_color_point = plot_feature_data__[1]
        # для box-ов
        take_a_color = plot_feature_data__[0]
        # специальный массив для box-ов
        colors = sns.color_palette(take_a_color)
    else:
        # для точек измерений
        take_a_color_point = [plot_feature_data__[3]] * len(bp['boxes'])
        # специальный массив для box-ов
        colors = [plot_feature_data__[2]] * len(bp['boxes'])

    # стандартное отклонение - добавить вместо разброса между min-max
    if make_an_SD:
        sns.set(style="ticks", rc={"lines.linewidth": 0.7})
        sns.pointplot(data=data, palette=['black'] * len(bp['boxes']), ax=ax, errorbar="sd", capsize=0.2)

    # добавить точки! важный параметр palette=take_a_color_point
    try:
        sns.stripplot(data=data, alpha=0.6, palette=take_a_color_point, ax=ax, linewidth=1, size=6)
    except:
        return messagebox.showerror('Ошибка', 'Скорее всего вы ввели неправильный цвет HEX')

    ####################################

    # вот тут добавляются цвета к нашим box-ам
    ##############
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # Colour of the median lines
    plt.setp(bp['medians'], color='k')

    if stat_znachimost:
        # Check for statistical significance
        significant_combinations = []
        # Check from the outside pairs of boxes inwards
        if plot_feature_data__[32] != '':
            try:
                combinations = plot_feature_data__[32].split()
                combinations = [item.replace('(', '').replace(')', '') for item in combinations]
                combinations = [tuple(map(int, item.split(','))) for item in combinations]
            except:
                return messagebox.showerror('Ошибка', 'Графики - box plot - неправильное значение в поле <Расчёт стат.значимости только между следующими группами>')
        else:
            ls = list(range(1, len(data) + 1))
            combinations = [(ls[x], ls[x + y]) for y in reversed(ls) for x in range((len(ls) - y))]
        for c in combinations:
            data1 = data[c[0] - 1]
            data2 = data[c[1] - 1]

            # Significance
            if plot_feature_data__[12] == 'U-критерий Манна — Уитни':
                U, p = stats.mannwhitneyu(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Т-критерий Стьюдента':
                U, p = stats.ttest_ind(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Критерий Уилкоксона':
                U, p = stats.wilcoxon(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Критерий Краскела — Уоллиса':
                U, p = stats.kruskal(data1, data2)
            elif plot_feature_data__[12] == 'Медианный критерий':
                U, p = stats.mood(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Тест Ансари-Брэдли':
                U, p = stats.ansari(data1, data2, alternative=plot_feature_data__[13])
            elif plot_feature_data__[12] == 'Тест Бруннера — Мюнцеля':
                U, p = stats.brunnermunzel(data1, data2, alternative=plot_feature_data__[13])
            else:
                #distribution='normal' - если что-то не так или данные только одно значение
                U, p = stats.brunnermunzel(data1, data2, distribution='normal', alternative=plot_feature_data__[13])

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
            # Significance level
            p = significant_combination[1]
            if p < 0.0001:
                sig_symbol = '****'
            elif p < 0.001:
                sig_symbol = '***'
            elif p < 0.01:
                sig_symbol = '**'
            elif p < 0.05:
                sig_symbol = '*'
            text_height = bar_height + (yrange * 0.01)
            plt.text((x1 - 1 + x2 - 1) * 0.5, text_height, sig_symbol, ha='center', c='k')

    # Adjust y-axis
    bottom, top = ax.get_ylim()
    yrange = top - bottom
    if bottom_lim == '':
        ax.set_ylim(bottom - 0.02 * yrange, top)
    else:
        bottom = float(bottom_lim.replace(",", "."))
        ax.set_ylim(bottom, top)
        bottom = bottom + 0.02 * yrange

    # Annotate sample size below each box
    # ''' внизу чтобы было кол-во данных
    if plot_feature_data__[23]:
        for i, dataset in enumerate(data):
            sample_size = len(dataset)
            ax.text(i, bottom, fr'n = {sample_size}', ha='center', size='x-small')
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
    # сохранение рисунка
    plt.savefig(path_name_fiqure_folder + '//' + safe_name(Name_fiqure) + '.png', dpi=600, format='png', transparent=plot_feature_data__[24])
    plt.close()
    ax.cla()
    plt.clf()
    return 0


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
def just_plot_it_(big_G, dict_for_future, df_list, name_of_X_axis):
    for parameter_ in dict_for_future:
        global plot_feature_data__
        global do_SD
        ylabel = parameter_
        check=box_and_whisker(big_G[dict_for_future[parameter_]], '', name_of_X_axis, ylabel,
                        df_list[dict_for_future[parameter_]].columns, parameter_, plot_feature_data__[5],
                        make_an_SD=do_SD)
        if check != 0:
            break


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
                # рассчитаем стат.значимости
                if plot_feature_data__[12] == 'U-критерий Манна — Уитни':
                    statistic, p_value = stats.mannwhitneyu(df_list[dict_for_future[i]][col1].dropna(),
                                                            df_list[dict_for_future[i]][col2].dropna(),
                                                            alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Т-критерий Стьюдента':
                    statistic, p_value = stats.ttest_ind(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna(),
                                                         alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Критерий Уилкоксона':
                    statistic, p_value = stats.wilcoxon(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna(),
                                                         alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Критерий Краскела — Уоллиса':
                    statistic, p_value = stats.kruskal(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna())
                elif plot_feature_data__[12] == 'Медианный критерий':
                    statistic, p_value = stats.mood(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna(),
                                                         alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Тест Ансари-Брэдли':
                    statistic, p_value = stats.ansari(df_list[dict_for_future[i]][col1].dropna(),
                                                         df_list[dict_for_future[i]][col2].dropna(),
                                                         alternative=plot_feature_data__[13])
                elif plot_feature_data__[12] == 'Тест Бруннера — Мюнцеля':
                    statistic, p_value = stats.brunnermunzel(df_list[dict_for_future[i]][col1].dropna(),
                                                             df_list[dict_for_future[i]][col2].dropna(),
                                                             alternative=plot_feature_data__[13])
                else:
                    statistic, p_value = stats.brunnermunzel(df_list[dict_for_future[i]][col1].dropna(),
                                                             df_list[dict_for_future[i]][col2].dropna(),
                                                             distribution='normal',
                                                             alternative=plot_feature_data__[13])
                # добавим в наш DataFrame
                dop_DF.loc[col1, col2] = round(p_value, 4)
        df_list_stat.append(dop_DF)
        df_list_stat[dict_for_future[i]] = df_list_stat[dict_for_future[i]].style.applymap(
            lambda x: 'color:red' if x < 0.05 else 'color:black')
    return df_list_stat


# Функция для построения графика корреляций #1
def only_regplot(df, x_, y_, what_is_hue, color_palette=None, not_in_hue=[], _lim_='', sort_or_not=False):
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


# Функция для построения корреляционных матриц
def corr_matrix_for_all_indexes(new_df):
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
        corr = df_for_corr.corr(method='spearman')
        # изменить параметр font_scale, если много значений: по дефолту -- font_scale=0.8 figsize=(16,8) fontsize=20
        # sns.set(font_scale=0.9)
        # plt.figure(figsize=(6,6))
        # plt.title(title_, fontsize=12)

        sns.set(font_scale=float(plot_feature_data__[9]))
        plt.figure(figsize=(float(plot_feature_data__[8]), float(plot_feature_data__[8])))
        plt.title(title_, fontsize=float(plot_feature_data__[10]))
        sns.heatmap(corr,
                    cmap='RdBu_r',  # задаёт цветовую схему
                    annot=True,  # рисует значения внутри ячеек
                    linewidth=.9,
                    vmin=-1, vmax=1)  # указывает начало цветовых кодов от -1 до 1.
        plt.tight_layout()
        name_of_file_ = str(i).replace('<', 'less')
        name_of_file_ = name_of_file_.replace('>=', 'more')
        plt.savefig(path_name_fiqure_folder_corr_matrix + '//' + safe_name(name_of_file_) + '.png', dpi=600, format='png')
        #также экспортируем в excel
        corr.to_excel(path_name_fiqure_folder_corr_matrix + '//' + safe_name(name_of_file_) + ".xlsx", engine="openpyxl")
        plt.close()
        plt.clf()


def do_for_one_sheet(what_sheet):
    global hue_name
    global path_name_fiqure_folder_corr_matrix
    global path_name_fiqure_folder_corr
    global path_name_fiqure_folder
    global plot_feature_data__
    global name_of_X_axis
    global stat_znachimost

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
            return messagebox.showerror('Ошибка', 'В таблице нет такого столбца:' + str(hue_name_for_sheet))
        index_for_col_interest = list(columns_of_interest).index(hue_name_for_sheet)
        columns_of_interest = columns_of_interest[index_for_col_interest + 1:]

    # все столбцы с данными приводим к численному виду

    for dd in columns_of_interest:
        try:
            df[dd] = df[dd].apply(pd.to_numeric)
        except:
            message_ = 'В колонке ' + str(dd) + ' представлены значения, \nкоторые нельзя конвертировать в числа'
            return messagebox.showerror('Ошибка', message_)

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
        corr_matrix_for_all_indexes(new_df)

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
            only_regplot(df, x_, y_, what_is_hue=hue_name_for_sheet, not_in_hue=plot_feature_data__[7],
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
                    just_all_we_need2 = just_all_we_need2[just_all_we_need2.columns.sort_values()]
                elif plot_feature_data__[31]!='':
                    columns__temp = plot_feature_data__[31].replace(',', '').replace(';', ' ').split()

                    if len(just_all_we_need2.columns) != len(columns__temp):
                        return messagebox.showerror('Ошибка', 'Графики - box plot - кол-во подписей в поле <Изменить порядок подписей> не верно')
                    try:
                        columns__temp = list(map(int, columns__temp))
                        columns__temp = [x - 1 for x in columns__temp]
                        columns__ = [just_all_we_need2.columns[x] for x in columns__temp]
                        just_all_we_need2 = just_all_we_need2.reindex(columns=columns__)
                    except:
                        return messagebox.showerror('Ошибка', 'Графики - box plot - что-то не так в поле <Изменить порядок подписей>')

                # сохраняем в список DataFrame-ов
                df_list.append(just_all_we_need2)
        if stat_znachimost:
            # вот и массив с таблицами p-values
            df_list_stat = calculate_table_for_p_val(df_list, dict_for_future)
        # вот и массив для графиков
        big_G = just_to_numpy_for_plot(df_list, dict_for_future)
        # построение графиков
        just_plot_it_(big_G, dict_for_future, df_list, name_of_X_axis)
        if stat_znachimost:
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
# главная функция
#
##############################################################
def figs_plot(plot_feature_data__from_ui, path_from_ui, exel_name, hue_name_from_ui, check_box_plot, check_matrix,
              check_corr_figs):
    global path
    global files
    global corr_is_need
    global plot_feature_data__
    global corr_is_need_matrix
    global box_plot_or_not
    global hue_name
    global do_SD
    global stat_znachimost

    checc = error_for_val_plot(plot_feature_data__from_ui, path_from_ui, exel_name)
    if checc != '':
        return messagebox.showerror('Ошибка', checc)

    # записываем в другую переменную
    plot_feature_data__ = plot_feature_data__from_ui

    # stat значимость делаем или нет?
    stat_znachimost = plot_feature_data__[16]

    # погрешности на графиках -- SD or MIN-MAX
    do_SD = True if plot_feature_data__[4] == 'SD' else False

    path = path_from_ui + '//'
    # путь до файла
    files = path + exel_name
    # от чего смотрится зависимость?
    hue_name = hue_name_from_ui

    # нужно ли считать корреляции?
    corr_is_need = check_corr_figs
    corr_is_need_matrix = check_matrix

    # строить ли обычные графики
    box_plot_or_not = check_box_plot

    try:
        names = pd.ExcelFile(files).sheet_names
    except:
        return messagebox.showerror('Ошибка', 'Нет такого файла или директории')

    # выполяем основной цикл по всем листам в excel файле
    check_cykle = '__'
    for i in names:
        check_cykle = do_for_one_sheet(i)
        if check_cykle != '__':
            break
    if check_cykle == '__':
        return messagebox.showinfo('Построение графиков', f'Все графики успешно сохранены')


##############################################################
#
# функция для ошибок
#
##############################################################

def error_for_val_plot(plot_feature_data__from_ui, path_from_ui, exel_name):
    if path_from_ui == '':
        return 'Путь для файла отсутствует'
    if exel_name == '':
        return 'Имя файла отсутствует'
    if exel_name == '':
        return 'Имя файла отсутствует'
    if plot_feature_data__from_ui[5].replace(".", "").replace(",", "").isdigit() is False and plot_feature_data__from_ui[5] != '':
        return 'Параметр нижней границы содержит буквы'
    if plot_feature_data__from_ui[8].replace(".", "").replace(",", "").isdigit() is False and plot_feature_data__from_ui[8] != '':
        print(plot_feature_data__from_ui[8])
        return 'Параметр для корреляционной матрицы содержит буквы'
    if plot_feature_data__from_ui[10].replace(".", "").replace(",", "").isdigit() is False and plot_feature_data__from_ui[10] != '':
        print(plot_feature_data__from_ui[10])
        return 'Параметр для корреляционной матрицы содержит буквы'
    return ''
