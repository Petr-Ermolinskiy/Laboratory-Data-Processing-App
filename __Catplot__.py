import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#https://github.com/webermarcolivier/statannot
#pip install statannot -- from statannot import add_stat_annotation
from statannotations.Annotator import Annotator
import math
from itertools import permutations
from tkinter import messagebox
import statsmodels

def for_save(Name_fiqure):
    Name_fiqure = Name_fiqure.replace('/', '')
    Name_fiqure = Name_fiqure.replace('\n', '')
    Name_fiqure = Name_fiqure.replace('\\frac', '')
    Name_fiqure = Name_fiqure.replace('\\', '')
    Name_fiqure = Name_fiqure.replace('$', '')
    Name_fiqure = Name_fiqure.replace('{', '')
    Name_fiqure = Name_fiqure.replace('}', '')
    return Name_fiqure

def change_type(x, __type__):
    if __type__ == 'str':
        return str(x)
    elif __type__ == 'int':
        return int(round(float(str(x).replace(' ','').replace(',','.')),0))
    elif __type__ == 'float':
        return float(str(x).replace(' ','').replace(',','.'))
    elif __type__ == 'bool':
        if x == '1' or x == float(1) or x == 1:
            return True
        elif x == '0' or x == float(0) or x == 0:
            return False
        else:
            return 'nan'
    else:
        return x

def plot_catplot(path, exel_name, sheet_name, x_name, y_name, hue_name, pallette_catplot, _error_, bar_or_not, type_x, type_y, type_hue, ttest_stat, stat_or_not, scale_, mult_camparison, stat_formatter):
    files = path + '//' + exel_name
    if hue_name == '--без подгруппы':
        hue_name = None

    # какие стат значимости чертить
    stat_formatter_dict = {'значение p': 'simple', '*': 'star', 'полный': 'full', 'None': None}
    stat_formatter = stat_formatter_dict[stat_formatter]

    if mult_camparison == 'None':
        mult_camparison = None

    #какие погррешности чертить
    error_set = {'Среднеквадратическое отклонение': 'sd', 'Среднеквадратическая ошибка': 'se', 'Доверительный интервал': 'ci', 'Перцентильный интервал': 'pi'}
    _error_ = error_set[_error_]

    ############
    args = dict(x=x_name, y=y_name, hue=hue_name, palette=pallette_catplot, errorbar=_error_, kind=bar_or_not)
    # errorbar either “ci”, “pi”, “se”, or “sd”

    # читаем exel файл - index_col=0,
    df = pd.read_excel(files, sheet_name=sheet_name)
    df.index.rename(None, inplace=True)

    if args['hue'] != None:
        df = df.dropna(subset=[args['x'], args['y'], args['hue']])
        df[args['hue']] = df[args['hue']].map(lambda x: change_type(x, type_hue))
    else:
        df = df.dropna(subset=[args['x'], args['y']])

    df[args['x']] = df[args['x']].map(lambda x: change_type(x, type_x))
    df[args['y']] = df[args['y']].map(lambda x: change_type(x, type_y))
    #для стат значимости
    pop = list(df[args['x']].unique())
    combinations = [(pop[x], pop[x + y]) for y in range(len(pop),0,-1) for x in range((len(pop) - y))]

    if args['hue'] != None:
        pop2 = list(df[args['hue']].unique())
        combinations = []
        # Getting all permutations of pop
        # with length of pop2
        combinations = [[(pop[i], pop2[j]), (pop[li], pop2[k])] for i in range(len(pop) - 1, 0, -1) for li in range(len(pop) - i) for j in range(len(pop2)) for k in range(len(pop2))]
        combinations2 = [[(pop[i], pop2[j]), (pop[i], pop2[k])] for i in range(len(pop)) for j in range(len(pop2) - 1, 0, -1) for k in range(len(pop2) - j)]
        for val in combinations2:
            if val[0] == val[1]:
                combinations2.remove(val)
        combinations = combinations + combinations2

    sns.reset_orig()
    sns.set(font_scale=scale_)
    sns.set_style("ticks")

    try:
        cat_plot = sns.catplot(edgecolor="black", data=df, **args)
    except:
        cat_plot = sns.catplot(data=df, **args)
    #edgecolor="black",
    if args['hue'] == None:
        n_and_n = df.groupby(args['x'])[args['y']].count()
        for cat_ax in cat_plot.axes:
            for sm_cat_ax in cat_ax:
                for i, n in enumerate(n_and_n):
                    sm_cat_ax.annotate(f'n={n}', xy=(i, 0.01), xycoords=('data', 'axes fraction'), ha='center',
                                       size='small')

    if stat_or_not:
        for ax_n in cat_plot.axes:
            for ax in ax_n:
                annot = Annotator(ax, combinations, data=df, **args)
                annot.configure(test=ttest_stat, text_format=stat_formatter, loc='inside', verbose=2, comparisons_correction=mult_camparison, hide_non_significant=True)
                annot.apply_test().annotate()
                ###
                # test – Union[StatTest, str]: Statistical test to run.
                # Either a StatTest instance or one of:
                # - Brunner-Munzel
                # - Levene
                # - Mann-Whitney
                # - Mann-Whitney-gt
                # - Mann-Whitney-ls
                # - t-test_ind
                # - t-test_welch
                # - t-test_paired
                # - Wilcoxon
                # - Kruskal
                ###

    try:
        cat_plot.savefig(path + '//' + for_save(str(x_name) +'_'+ str(y_name) +'_'+ str(hue_name)) + '.png', dpi=600)
    except:
        return messagebox.showerror('Ошибка - Catplot', 'График не сохранен')

    try:
        file1 = open(path + '//' + for_save(str(x_name) +'_'+ str(y_name) +'_'+ str(hue_name)) + '.txt', "w")
        if stat_or_not:
            L0 = 'Был использован тест: ' + ttest_stat + '\n'
            L1 = 'Была использована поправка на множественную проверку гипотез: ' + str(mult_camparison) + '\n'
        else:
            L0 = 'Не было использовано стат. теста \n'
            L1 = '\n'

        L2 = '*: 1.00e-02 < p <= 5.00e-02 \n**: 1.00e-03 < p <= 1.00e-02 \n***: 1.00e-04 < p <= 1.00e-03 \n****: p <= 1.00e-04'

        # \n is placed to indicate EOL (End of Line)
        file1.writelines(L0 + L1 + L2)
        file1.close()  # to change file access modes
    except:
        return messagebox.showerror('Ошибка - Catplot', 'txt файл для графика не сохранен')

    try:
        if args['hue'] == None:
            jjj = df.groupby(args['x'])[args['y']].count()
        else:
            jjj = df.groupby([args['x'], args['hue']])[args['y']].count()
        jjj.rename("N").to_csv(path + '//' + for_save(str(x_name) +'_'+ str(y_name) +'_'+ str(hue_name)) + '_N_of_data.txt', sep='\t')
    except:
        return messagebox.showerror('Ошибка - Catplot', 'txt файл для N в группах не сохранен')

    return messagebox.showinfo('Catplot', f'График успешно сохранен')