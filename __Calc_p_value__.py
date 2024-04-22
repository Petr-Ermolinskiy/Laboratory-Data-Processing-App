import pandas as pd
from scipy import stats
import numpy as np

# для вывода диалогового окна
from PySide6.QtWidgets import QMessageBox

# надо будет добавить pip install permutations-stats
# https://pypi.org/project/permutations-stats/

def p_value_calc_for_two_columns(self) -> None:
    dlg = QMessageBox(self)

    # параметры, которые нам понадобятся
    path = self.ui.path_for_dop_stat.text()
    exel_name = self.ui.comboBox_excel_dop_stat.currentText()
    sheet_name = self.ui.comboBox_excel_sheet_dop_stat.currentText()
    x_name = self.ui.comboBox_dop_stat_x.currentText()
    y_name = self.ui.comboBox_dop_stat_y.currentText()
    # статистика
    stat_test = self.ui.comboBox_stat_test_dop_stat.currentText()
    alternative = self.ui.comboBox_alter_hep_dop_stat.currentText()
    #
    if path == '':
        dlg.setWindowTitle("Расчёт p-value")
        dlg.setText("Не введен путь к папкам")
        dlg.exec()
        return None

    files = path + '//' + exel_name

    try:
        # читаем exel файл - index_col=0,
        df = pd.read_excel(files, sheet_name=sheet_name)
        df[x_name] = df[x_name].map(lambda x: float(x))
        df[y_name] = df[y_name].map(lambda x: float(x))
    except Exception as e:
        dlg.setWindowTitle("Расчёт p-value")
        dlg.setText("Ошибка: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return None

    try:
        # расчитываем стат. тест.
        if stat_test == 'U-критерий Манна — Уитни':
            _, p = stats.mannwhitneyu(df[x_name].dropna(), df[y_name].dropna(), alternative=alternative)
        elif stat_test == 'Т-критерий Стьюдента':
            _, p = stats.ttest_ind(df[x_name].dropna(), df[y_name].dropna(), alternative=alternative)
        elif stat_test == 'Критерий Уилкоксона':
            _, p = stats.wilcoxon(df[x_name].dropna(), df[y_name].dropna(), alternative=alternative)
        elif stat_test == 'Критерий Краскела — Уоллиса':
            _, p = stats.kruskal(df[x_name].dropna(), df[y_name].dropna())
        elif stat_test == 'Медианный критерий':
            _, p = stats.mood(df[x_name].dropna(), df[y_name].dropna(), alternative=alternative)
        elif stat_test == 'Тест Ансари-Брэдли':
            _, p = stats.ansari(df[x_name].dropna(), df[y_name].dropna(), alternative=alternative)
        elif stat_test == 'Тест Бруннера — Мюнцеля':
            _, p = stats.brunnermunzel(df[x_name].dropna(), df[y_name].dropna(), alternative=alternative)
        elif stat_test == 'Тест Бруннера — Мюнцеля (normal)':
            # distribution='normal' - если что-то не так или данные только одно значение, но в этом случае этот тест лучше не использовать
            _, p = stats.brunnermunzel(df[x_name].dropna(), df[y_name].dropna(), distribution='normal', alternative=alternative)
        elif stat_test == 'Тест Фишера-Питмана':
            def statistic(x, y, axis):
                return np.mean(x, axis=axis) - np.mean(y, axis=axis)

            # вычисляем
            all_data = stats.permutation_test((df[x_name].dropna(), df[y_name].dropna()), statistic, permutation_type='independent',
                                              vectorized=True,
                                              alternative=alternative)
            # само значение p
            p = all_data.pvalue
        else:
            p='Внутренняя ошибка'

    except Exception as e:
        dlg.setWindowTitle("Расчёт p-value")
        dlg.setText("Ошибка при расчете: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return None

    self.ui.p_value_dop_stat.setText(str(p))

    return None









