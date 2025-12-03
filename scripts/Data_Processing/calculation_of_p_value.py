# нужно для Пермутационных тестов, даже если светит серым
from pathlib import Path

import numba  # noqa: F401
import numpy as np
import pandas as pd
from permutations_stats.permutations import permutation_test, repeated_permutation_test
from PySide6.QtWidgets import QMessageBox
from scipy import stats


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
    if path == "":
        dlg.setWindowTitle("Расчёт p-value")
        dlg.setText("Не введен путь к папкам")
        dlg.exec()
        return

    files = Path(path) / exel_name

    try:
        # читаем exel файл - index_col=0,
        df = pd.read_excel(str(files), sheet_name=sheet_name)
        df[x_name] = df[x_name].map(lambda x: float(x))
        df[y_name] = df[y_name].map(lambda x: float(x))
    except Exception as e:
        dlg.setWindowTitle("Расчёт p-value")
        dlg.setText("Ошибка: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    try:
        # Расчитываем стат. Тест.
        if stat_test == "U-критерий Манна — Уитни":
            _, p = stats.mannwhitneyu(
                df[x_name].dropna(),
                df[y_name].dropna(),
                alternative=alternative,
            )
        elif stat_test == "Т-критерий Стьюдента":
            _, p = stats.ttest_ind(
                df[x_name].dropna(),
                df[y_name].dropna(),
                alternative=alternative,
            )
        elif stat_test == "Критерий Уилкоксона":
            _, p = stats.wilcoxon(df[x_name].dropna(), df[y_name].dropna(), alternative=alternative)
        elif stat_test == "Критерий Краскела — Уоллиса":
            _, p = stats.kruskal(df[x_name].dropna(), df[y_name].dropna())
        elif stat_test == "Медианный критерий":
            _, p = stats.mood(df[x_name].dropna(), df[y_name].dropna(), alternative=alternative)
        elif stat_test == "Тест Ансари-Брэдли":
            _, p = stats.ansari(df[x_name].dropna(), df[y_name].dropna(), alternative=alternative)
        elif stat_test == "Тест Бруннера — Мюнцеля":
            _, p = stats.brunnermunzel(
                df[x_name].dropna(),
                df[y_name].dropna(),
                alternative=alternative,
            )
        elif stat_test == "Тест Бруннера — Мюнцеля (normal)":
            # distribution='normal' - если что-то не так или данные только одно значение, но в этом случае этот тест лучше не использовать
            _, p = stats.brunnermunzel(
                df[x_name].dropna(),
                df[y_name].dropna(),
                distribution="normal",
                alternative=alternative,
            )
        elif stat_test == "Тест Фишера-Питмана":

            def statistic(x, y, axis) -> float:
                return np.mean(x, axis=axis) - np.mean(y, axis=axis)

            # вычисляем
            all_data = stats.permutation_test(
                (df[x_name].dropna(), df[y_name].dropna()),
                statistic,
                permutation_type="independent",
                vectorized=True,
                alternative=alternative,
            )
            # само значение p
            p = all_data.pvalue
        elif stat_test == "Пермутационный критерий Бруннера — Мюнцеля":
            stat = permutation_test(
                df[x_name].dropna(),
                df[y_name].dropna(),
                test="brunner_munzel",
                alternative=alternative,
            )
            p = stat.pvalue
        elif stat_test == "Пермутационный критерий Манна — Уитни":
            stat = permutation_test(
                df[x_name].dropna(),
                df[y_name].dropna(),
                test="mann_whitney",
                alternative=alternative,
            )
            p = stat.pvalue
        elif stat_test == "Пермутационный критерий Уилкоксона":
            # изменим формат
            data = np.vstack([df[x_name].dropna(), df[y_name].dropna()]).T
            # сделаем расчет
            stat = repeated_permutation_test(data, test="wilcoxon", alternative=alternative)
            p = stat.pvalue
        elif stat_test == "Пермутационный критерий Фридмана":
            # изменим формат
            data = np.vstack([df[x_name].dropna(), df[y_name].dropna()]).T
            # сделаем расчет
            stat = repeated_permutation_test(data, test="friedman", alternative=alternative)
            p = stat.pvalue
        else:
            p = "Внутренняя ошибка - обратитесь в разработчику"

    except Exception as e:
        dlg.setWindowTitle("Расчёт p-value")
        dlg.setText("Ошибка при расчете: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    self.ui.p_value_dop_stat.setText(str(p))
    return
