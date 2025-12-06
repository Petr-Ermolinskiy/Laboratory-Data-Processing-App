import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sc
import seaborn as sns
from loguru import logger
from PySide6.QtWidgets import QMessageBox

# ----------------------------------------------- #
logger.remove()

logger.add(sys.stderr, format="<green>{time:HH:mm:ss}</green> | {level} | {message}", level="INFO")
# ----------------------------------------------- #


def biola_result(self) -> None:
    dlg = QMessageBox(self)
    # закроем все рисунки, если они открыты
    # если этого не сделать, то может быть такое, что рисунки наложатся друг на друга
    plt.close()
    #########################
    # параметры, которые нам понадобятся
    plot_figure = (
        self.ui.doubleSpinBox_Biola.value(),
        self.ui.comboBox_Biola_SD_or.currentText(),
        self.ui.comboBox_Biola_language.currentText(),
        self.ui.check_setka_biola.isChecked(),
    )
    path = self.ui.path_for_biola.text()
    name_of_file = self.ui.comboBox_biola.currentText()
    number_of_these_windows_born = self.ui.spinBox_biola_born.value()
    number_of_these_windows_fluc = self.ui.spinBox_biola_fluc.value()
    windows_born = self.ui.spinBox_biola_born_odd.value()
    windows_fluc = self.ui.spinBox_biola_fluc_odd.value()
    plot_figs = self.ui.check_biola_plot_figs.isChecked()
    #########################

    if path == "":
        dlg.setWindowTitle("Biola")
        dlg.setText("Не введен путь к папкам")
        dlg.exec()
        return

    path_obj = Path(path)
    # изначальный DataFrame - читаем файл
    try:
        # для кодировки на английском
        dff = pd.read_csv(
            str(path_obj / name_of_file),
            sep=" ",
            engine="python",
            on_bad_lines="skip",
            index_col=False,
            header=None,
        )
        # добавляем индексы для того, чтобы в дальнейшем разделить данные
        name = dff.iat[1, 0] + " " + dff.iat[2, 0] + "мкМ" + " " + dff.iat[0, 0]
    except Exception:
        logger.info("Biola: кодировка на русском")
        # для кодировки на русском
        dff = pd.read_csv(
            str(path_obj / name_of_file),
            sep=" ",
            engine="python",
            on_bad_lines="skip",
            index_col=False,
            header=None,
            encoding="cp1251",
        )
        # добавляем индексы для того, чтобы в дальнейшем разделить данные
        name = dff.iat[0, 0] + " " + dff.iat[1, 0] + " мкМ" + " " + dff.columns[0]

    # добавляем дополнительный столбец
    dff["индекс для split"] = ""

    # Используем at вместо loc, т.к. это сделает большой выигрыш в скорости
    for i in range(len(dff)):
        if type(dff.iat[i, 1]) != float and ":" in dff.iat[i, 1] and i + 1 < len(dff):
            name = dff.iat[i + 1, 0] + " " + dff.iat[i + 2, 0] + " мкМ" + " " + dff.iat[i, 0]
            dff.at[i, "индекс для split"] = "del"
            continue
        dff.at[i, "индекс для split"] = name

    # удаляем ненужные строки
    dff = dff.drop([0, 1, 2, 3, 4])
    # создаем массив, чтобы найти ненужные строки...
    massive_for_del = dff[dff["индекс для split"] == "del"].index.to_numpy()
    # ...и удалить их
    for i in massive_for_del:
        dff = dff.drop([i, i + 1, i + 2, i + 3, i + 4])
    # переобозначим индекс
    dff = dff.reset_index(drop=True)
    # уберем все запятые
    dff = dff.replace(",", "", regex=True)
    # переименуем колонки
    hh = dff.columns.values.tolist()
    dff = dff.rename(columns={hh[0]: "по Борну", hh[1]: "по флуктуациям", hh[2]: "Index"})
    # чтобы не было ошибок
    dff["по флуктуациям"] = dff["по флуктуациям"].replace("-1.#IO", "-1.0")
    # изменим формат
    dff["по Борну"] = dff["по Борну"].astype(float)
    dff["по флуктуациям"] = dff["по флуктуациям"].astype(float)
    # разделяем для разных пациентов
    new_f_born = dff.pivot(columns="Index", values="по Борну")
    new_f_fluc = dff.pivot(columns="Index", values="по флуктуациям")
    ###########
    # выбрасываем все NaN там, где они есть для каждого столбца и сохраняем значения в новый DataFrame
    born = pd.DataFrame()
    for i in new_f_born.columns:
        ignore_nan = new_f_born[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True)
        born.insert(loc=0, column=i, value=ignore_nan)
    born = born[born.columns[::-1]]
    ###########
    # выбрасываем все NaN там, где они есть для каждого столбца и сохраняем значения в новый DataFrame
    fluc = pd.DataFrame()
    for i in new_f_fluc.columns:
        ignore_nan = new_f_fluc[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True)
        fluc.insert(loc=0, column=i, value=ignore_nan)
    fluc = fluc[fluc.columns[::-1]]
    # создадим DataFrame для времени - 4 Гц
    time = pd.DataFrame()
    time["время"] = range(0, max(len(born), len(fluc)), 1)
    time["время"] = time["время"] * 0.25
    # создадим DataFrame для производной по Борну
    diff_born = pd.DataFrame()
    # для каждой колонки для измерений по Борну находим производную, умножаем её на 4 (4 Гц - с такой чистатой идут измерения),
    # добавляем в конец значение 0, чтобы совпала длина массива
    for i in born.columns:
        for_born_diff = np.diff(born[i], n=1)
        for_born_diff = for_born_diff * 4
        for_born_diff = np.insert(for_born_diff, len(for_born_diff), 0.0)
        diff_born.insert(loc=0, column=i, value=for_born_diff)
    # создадим DataFrame для производной по флуктуациям
    diff_fluc = pd.DataFrame()
    # для каждой колонки для измерений по флуктуациям находим производную, умножаем её на 4 (4 Гц - с такой чистатой идут измерения),
    # добавляем в конец значение 0, чтобы совпала длина массива
    for i in fluc.columns:
        for_fluc_diff = np.diff(fluc[i], n=1)
        for_fluc_diff = for_fluc_diff * 4
        for_fluc_diff = np.insert(for_fluc_diff, len(for_fluc_diff), 0.0)
        diff_fluc.insert(loc=0, column=i, value=for_fluc_diff)
    # избавимся от плохих значений, если они есть
    diff_born = diff_born.dropna()
    diff_fluc = diff_fluc.dropna()
    # создадим DataFrame для сглаженной производной по Борну
    smooth_diff_born = pd.DataFrame()
    # для каждой колонки для измерений по Борну производим сглаживание
    if number_of_these_windows_born > 1:
        for i in diff_born.columns:
            born_dif_smoth = sc.signal.savgol_filter(
                x=diff_born[i],
                window_length=number_of_these_windows_born,
                polyorder=1,
            )
            smooth_diff_born.insert(loc=0, column=i, value=born_dif_smoth)
    else:
        smooth_diff_born = diff_born
    # создадим DataFrame для сглаженной производной по Флуктуациям
    smooth_diff_fluc = pd.DataFrame()
    # для каждой колонки для измерений по Флуктуациям производим сглаживание
    if number_of_these_windows_fluc > 1:
        for i in diff_fluc.columns:
            fluc_dif_smoth = sc.signal.savgol_filter(
                x=diff_fluc[i],
                window_length=number_of_these_windows_fluc,
                polyorder=1,
            )
            smooth_diff_fluc.insert(loc=0, column=i, value=fluc_dif_smoth)
    else:
        smooth_diff_fluc = diff_fluc
    # умножим все значения на 60, чтобы получить размерность */мин, а не */сек.
    smooth_diff_born = smooth_diff_born * 60
    smooth_diff_fluc = smooth_diff_fluc * 60
    # избавимся от плохих значений, если они есть
    born = born.dropna()
    fluc = fluc.dropna()
    # создадим DataFrame для сглаженной кривой Борну
    smooth_born = pd.DataFrame()
    # для каждой колонки для измерений по Борну производим сглаживание
    if windows_born > 1:
        for i in born.columns:
            born_smooth = sc.signal.savgol_filter(
                x=born[i],
                window_length=windows_born,
                polyorder=1,
            )
            smooth_born.insert(loc=0, column=i, value=born_smooth)
    else:
        smooth_born = born
    # создадим DataFrame для сглаженной кривой флуктуациям
    smooth_fluc = pd.DataFrame()
    # для каждой колонки для измерений по Борну производим сглаживание
    if windows_fluc > 1:
        for i in fluc.columns:
            fluc__smoth = sc.signal.savgol_filter(
                x=fluc[i],
                window_length=windows_fluc,
                polyorder=1,
            )
            smooth_fluc.insert(loc=0, column=i, value=fluc__smoth)
    else:
        smooth_fluc = fluc
    """
    Конечный DataFrame для данных
    """
    # создание результирующего DataFrame данных
    result_main = pd.DataFrame()
    # добавить максимальные значения в наш DataFrame
    result_main.insert(
        loc=0,
        column="Max произв. по флуктуациям, отн.ед.",
        value=smooth_diff_fluc.loc[50:, :].max(),
    )
    result_main.insert(
        loc=0,
        column="Max по флуктуациям, отн.ед.",
        value=smooth_fluc.loc[50:, :].max(),
    )
    result_main.insert(
        loc=0,
        column="Max произв. по Борну, %",
        value=smooth_diff_born.loc[50:, :].max(),
    )
    result_main.insert(loc=0, column="Max по Борну, %", value=smooth_born.loc[50:, :].max())

    # добавить столбец с концентрацией для последующего анализа
    for_conc_stuff = result_main.index.to_series().str.split(" ", expand=True)
    # теперь просто записываем for_conc_stuff в наш конечный DataFrame
    result_main.insert(loc=0, column="Дата", value=for_conc_stuff.iloc[:, -1])
    result_main.insert(loc=0, column="Концентрация АДФ, мкм", value=for_conc_stuff.iloc[:, -3])
    result_main.insert(loc=0, column="Пациент/донор/образец", value=for_conc_stuff.iloc[:, 0])
    # Все отрицательные значения заменим на 0
    for i in result_main.columns[3:]:
        result_main.loc[result_main[i] < 0, i] = 0
    """
    Усредненный DataFrame
    """
    combined_data_frame = pd.DataFrame()
    # ошибка и среднее
    combined_data_frame.insert(
        loc=0,
        column="SD(произв.ср.разм.агр.), отн.ед.",
        value=smooth_diff_fluc.std(axis=1),
    )
    combined_data_frame.insert(
        loc=0,
        column="Производная среднего размера агрегата, отн.ед.",
        value=smooth_diff_fluc.mean(axis=1),
    )
    # ошибка и среднее
    combined_data_frame.insert(
        loc=0,
        column="SD(ср.разм.агр.), отн.ед.",
        value=smooth_fluc.std(axis=1),
    )
    combined_data_frame.insert(
        loc=0,
        column="Средний размер агрегата, отн.ед.",
        value=smooth_fluc.mean(axis=1),
    )
    # ошибка и среднее
    combined_data_frame.insert(
        loc=0,
        column="SD(произв.борн.), %/мин.",
        value=smooth_diff_born.std(axis=1),
    )
    combined_data_frame.insert(
        loc=0,
        column="Производная по Борну, %/мин.",
        value=smooth_diff_born.mean(axis=1),
    )
    # ошибка и среднее
    combined_data_frame.insert(loc=0, column="SD(борн.), %", value=smooth_born.std(axis=1))
    combined_data_frame.insert(loc=0, column="По Борну, %", value=smooth_born.mean(axis=1))
    # столбец времени
    combined_data_frame.insert(loc=0, column="Время, с.", value=time["время"])
    """
    Построение графиков
    """
    # какие погррешности чертить
    error_set = {
        "Среднеквадратическое отклонение": "sd",
        "Среднеквадратическая ошибка": "se",
        "Доверительный интервал": "ci",
        "Перцентильный интервал": "pi",
    }
    error_ = error_set[plot_figure[1]]

    # подпись наверху графика
    if plot_figure[2] == "Eng":
        title1 = "Averaged curve for "
        title2 = " patients"
    else:
        title1 = "Усредненная кривая по "
        title2 = " пациентам"
    if plot_figs:
        sns.reset_orig()
        # насколько шрифт изменяем
        sns.set(font_scale=plot_figure[0])
        ##################################
        just_for_plot = pd.melt(smooth_born.join(time), id_vars=["время"])
        just_for_plot.columns = ["Время, с", "Пациент", "Светопропускание,%"]
        if plot_figure[2] == "Eng":
            just_for_plot.columns = ["Time, s", "Пациент", "Light transmission,%"]

        # стили
        sns.set_style("ticks")
        if plot_figure[3]:
            sns.set_style("whitegrid")

        fig, ax = plt.subplots()
        sns.lineplot(
            data=just_for_plot,
            x=just_for_plot.columns[0],
            y=just_for_plot.columns[2],
            errorbar=error_,
            ax=ax,
        ).set(title=title1 + str(len(result_main)) + title2)
        ax.set_xlim(0, 300)
        plt.tight_layout()

        just_for_plot2 = pd.melt(smooth_diff_born.join(time), id_vars=["время"])
        just_for_plot2.columns = ["Время, с", "Пациент", "Производная светопропускания,%/мин."]
        if plot_figure[2] == "Eng":
            just_for_plot2.columns = ["Time, s", "Пациент", "Light transmission derivative, %/min"]

        # sns.set_style("whitegrid")  # noqa: ERA001
        fig2, ax2 = plt.subplots()
        sns.lineplot(
            data=just_for_plot2,
            x=just_for_plot2.columns[0],
            y=just_for_plot2.columns[2],
            errorbar=error_,
            ax=ax2,
        ).set(title=title1 + str(len(result_main)) + title2)
        ax2.set_xlim(0, 300)
        plt.tight_layout()

        just_for_plot3 = pd.melt(smooth_fluc.join(time), id_vars=["время"])
        just_for_plot3.columns = ["Время, с", "Пациент", "Средний размер агрегата, отн.ед."]
        if plot_figure[2] == "Eng":
            just_for_plot3.columns = ["Time, s", "Пациент", "Average aggregate size, a.u."]

        # sns.set_style("whitegrid")  # noqa: ERA001
        fig3, ax3 = plt.subplots()
        sns.lineplot(
            data=just_for_plot3,
            x=just_for_plot3.columns[0],
            y=just_for_plot3.columns[2],
            errorbar=error_,
            ax=ax3,
        ).set(title=title1 + str(len(result_main)) + title2)
        ax3.set_xlim(0, 300)
        plt.tight_layout()

        just_for_plot4 = pd.melt(smooth_diff_fluc.join(time), id_vars=["время"])
        just_for_plot4.columns = [
            "Время, с",
            "Пациент",
            "Производная среднего размера агрегата, отн.ед.",
        ]
        if plot_figure[2] == "Eng":
            just_for_plot4.columns = [
                "Time, s",
                "Пациент",
                "Average aggregate size derivative, a.u.",
            ]

        # sns.set_style("whitegrid")  # noqa: ERA001
        fig4, ax4 = plt.subplots()
        sns.lineplot(
            data=just_for_plot4,
            x=just_for_plot4.columns[0],
            y=just_for_plot4.columns[2],
            errorbar=error_,
            ax=ax4,
        ).set(title=title1 + str(len(result_main)) + title2)
        ax4.set_xlim(0, 300)
        plt.tight_layout()

        # сохраняем усредненные графики
        fig.savefig(str(path_obj / "Светопропускание.png"), dpi=600)
        fig2.savefig(str(path_obj / "Производная_светопропускания.png"), dpi=600)
        fig3.savefig(str(path_obj / "Средний_радиус.png"), dpi=600)
        fig4.savefig(str(path_obj / "Производная_среднего_радиуса.png"), dpi=600)

    with pd.ExcelWriter(str(path_obj / f"{name_of_file.replace('.txt', '')}_agg.xlsx")) as writer:
        result_main.to_excel(writer, sheet_name="полученные данные")
        time.to_excel(writer, sheet_name="время")
        smooth_born.to_excel(writer, sheet_name="Светопропускание, %")
        smooth_diff_born.to_excel(writer, sheet_name="Произв. от светопроп., % сек")
        smooth_fluc.to_excel(writer, sheet_name="Ср. разм. агр., отн.ед.")
        smooth_diff_fluc.to_excel(writer, sheet_name="Произв. от ср. разм. агр.")
        combined_data_frame.to_excel(writer, sheet_name="Усредненные данные по строкам")

    # завершаем работу
    dlg.setWindowTitle("Biola")
    dlg.setText("Excel файл и все графики успешно сохранены")
    dlg.exec()
    return
