import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# для вывода диалогового окна
from PySide6.QtWidgets import QMessageBox
# https://github.com/webermarcolivier/statannot
from statannotations.Annotator import Annotator


def for_save(Name_fiqure) -> str:
    Name_fiqure = Name_fiqure.replace('/', '')
    Name_fiqure = Name_fiqure.replace('\n', '')
    Name_fiqure = Name_fiqure.replace('\\frac', '')
    Name_fiqure = Name_fiqure.replace('\\', '')
    Name_fiqure = Name_fiqure.replace('$', '')
    Name_fiqure = Name_fiqure.replace('{', '')
    Name_fiqure = Name_fiqure.replace('}', '')
    Name_fiqure = Name_fiqure.replace('*', '')
    return Name_fiqure


def change_type(x, __type__):
    if __type__ == 'str':
        return str(x)
    elif __type__ == 'int':
        return int(round(float(str(x).replace(' ', '').replace(',', '.')), 0))
    elif __type__ == 'float':
        return float(str(x).replace(' ', '').replace(',', '.'))
    elif __type__ == 'bool':
        if x == '1' or x == float(1) or x == 1:
            return True
        elif x == '0' or x == float(0) or x == 0:
            return False
        else:
            return 'nan'
    else:
        return x


def plot_catplot(self) -> None:
    dlg = QMessageBox(self)
    # закроем все рисунки, если они открыты
    # если этого не сделать, то может быть такое, что рисунки наложатся друг на друга
    plt.close()
    #########################
    # параметры, которые нам понадобятся
    path = self.ui.path_for_catplot.text()
    exel_name = self.ui.comboBox_excel_catplot.currentText()
    sheet_name = self.ui.comboBox_excel_sheet_catplot.currentText()
    x_name = self.ui.comboBox_catplot_x.currentText()
    y_name = self.ui.comboBox_catplot_y.currentText()
    hue_name = self.ui.comboBox_catplot_hue.currentText()
    pallette_catplot = self.ui.comboBox_color_catplot.currentText()
    _error_ = self.ui.comboBox_catplot_SD_or_not.currentText()
    bar_or_not = self.ui.comboBox_template_catplot.currentText()
    type_x, type_y, type_hue = self.ui.comboBox_catplot_form_x.currentText(), self.ui.comboBox_catplot_form_y.currentText(), self.ui.comboBox_catplot_form_hue.currentText()
    ttest_stat = self.ui.comboBox_stat_test_catplot.currentText()
    stat_or_not = self.ui.check_stat_znachimost_catplot.isChecked()
    scale_ = self.ui.doubleSpinBox_catplot.value()
    mult_camparison = self.ui.comboBox_catplot_mult_stat.currentText()
    stat_formatter = self.ui.comboBox_catplot_stat_formatt.currentText()
    #########################
    if path == '':
        dlg.setWindowTitle("Catplot")
        dlg.setText("Не введен путь к папкам")
        dlg.exec()
        return None

    files = path + '//' + exel_name
    if hue_name == '--без подгруппы':
        hue_name = None

    # какие стат значимости чертить
    stat_formatter_dict = {'значение p': 'simple', '*': 'star', 'полный': 'full', 'None': None}
    stat_formatter = stat_formatter_dict[stat_formatter]

    if mult_camparison == 'None':
        mult_camparison = None

    # какие погррешности чертить
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
    # для стат значимости
    pop = list(df[args['x']].unique())
    combinations = [(pop[x], pop[x + y]) for y in range(len(pop), 0, -1) for x in range((len(pop) - y))]

    if args['hue'] != None:
        pop2 = list(df[args['hue']].unique())
        combinations = []
        # Getting all permutations of pop
        # with length of pop2
        combinations = [[(pop[i], pop2[j]), (pop[li], pop2[k])] for i in range(len(pop) - 1, 0, -1) for li in range(len(pop) - i) for j in range(len(pop2)) for k in
                        range(len(pop2))]
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
    # edgecolor="black",
    if args['hue'] == None:
        n_and_n = df.groupby(args['x'])[args['y']].count()

        for cat_ax in cat_plot.axes:
            for sm_cat_ax in cat_ax:
                # важно проходиться по xlabels, а не просто по n_and_n, иначе будет неправильный порядок. см. https://stackoverflow.com/questions/64783410/adding-number-of-observations-to-seaborn-catplot-stirpplot
                xlabels = [x.get_text() for x in sm_cat_ax.get_xticklabels()]
                for i, n in enumerate(xlabels):
                    sm_cat_ax.annotate(f'n={n_and_n[n]}', xy=(i, 0.01), xycoords=('data', 'axes fraction'), ha='center',
                                       size='small')

    if stat_or_not:
        for ax_n in cat_plot.axes:
            for ax in ax_n:
                annot = Annotator(ax, combinations, data=df, **args)
                annot.configure(test=ttest_stat, text_format=stat_formatter, loc='inside', verbose=2, comparisons_correction=mult_camparison, hide_non_significant=True)
                annot.apply_test().annotate()
                # Один из следующих:
                # - Brunner-Munzel, Levene, Mann-Whitney, Mann-Whitney-gt, Mann-Whitney-ls, t-test_ind, t-test_welch, t-test_paired, Wilcoxon, Kruskal
    try:
        cat_plot.savefig(path + '//' + for_save(str(x_name) + '_' + str(y_name) + '_' + str(hue_name)) + '.png', dpi=600)
    except Exception as e:
        dlg.setWindowTitle("Ошибка - Catplot")
        dlg.setText("График не сохранен.\n" + str(e))
        dlg.exec()
        return None

    try:
        file1 = open(path + '//' + for_save(str(x_name) + '_' + str(y_name) + '_' + str(hue_name)) + '.txt', "w")
        if stat_or_not:
            L0 = 'Был использован тест: ' + ttest_stat + '\n'
            L1 = 'Была использована поправка на множественную проверку гипотез: ' + str(mult_camparison) + '\n'
        else:
            L0 = 'Не было использовано стат. теста \n'
            L1 = '\n'

        L2 = '*: 1.00e-02 < p <= 5.00e-02 \n**: 1.00e-03 < p <= 1.00e-02 \n***: 1.00e-04 < p <= 1.00e-03 \n****: p <= 1.00e-04'

        file1.writelines(L0 + L1 + L2)
        file1.close()
    except Exception as e:
        dlg.setWindowTitle("Ошибка - Catplot")
        dlg.setText("TXT файл для графика.\n" + str(e))
        dlg.exec()
        return None

    try:
        if args['hue'] == None:
            jjj = df.groupby(args['x'])[args['y']].count()
        else:
            jjj = df.groupby([args['x'], args['hue']])[args['y']].count()
        jjj.rename("N").to_csv(path + '//' + for_save(str(x_name) + '_' + str(y_name) + '_' + str(hue_name)) + '_N_of_data.txt', sep='\t')
    except Exception as e:
        dlg.setWindowTitle("Ошибка - Catplot")
        dlg.setText("TXT файл для N в группах не сохранен.\n" + str(e))
        dlg.exec()
        return None

    dlg.setWindowTitle("Catplot")
    dlg.setText("График успешно сохранен")
    dlg.exec()
    return None
