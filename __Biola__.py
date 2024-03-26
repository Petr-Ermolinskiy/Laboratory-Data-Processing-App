#необходимые библиотеки
import pandas as pd
import scipy as sc
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from scipy.signal import savgol_filter
from tkinter import messagebox
#библиотека дополнительная для графиков
import seaborn as sns

def biola_result(plot_fiture, path, name_of_file, number_of_these_windows_born, number_of_these_windows_fluc, windows_born, windows_fluc):
    path = path + '//'
    # изначальный DataFrame - читаем файл
    try:
        #для кодировки на английском
        dff = pd.read_csv(path + name_of_file, sep=' ', engine='python', error_bad_lines=False, index_col=False, header=None)
        # добавляем индексы для того, чтобы в дальнейшем разделить данные
        name = dff.iat[1, 0] + ' ' + dff.iat[2, 0] + 'мкМ' + ' ' + dff.iat[0, 0]
    except:
        #для кодировки на русском
        dff = pd.read_csv(path + name_of_file, sep=' ', engine='python', on_bad_lines='skip', index_col=False, encoding='cp1251')
        # добавляем индексы для того, чтобы в дальнейшем разделить данные
        name = dff.iat[0, 0] + ' ' + dff.iat[1, 0] + ' мкМ' + ' ' + dff.columns[0]
    #для более новых библиотек:
    # добавляем дополнительный столбец
    dff['индекс для split'] = ""

    for i in range(len(dff)):
        if type(dff.iat[i, 1]) != float:
            if ':' in dff.iat[i, 1] and i + 1 < len(dff):
                name = dff.iat[i + 1, 0] + ' ' + dff.iat[i + 2, 0] + ' мкМ' + ' ' + dff.iat[i, 0]
                dff.at[i, 'индекс для split'] = 'del'
                continue
        dff.at[i, 'индекс для split'] = name

    # удаляем ненужные строки
    dff.drop([0, 1, 2, 3, 4], inplace=True)
    # создаем массив, чтобы найти ненужные строки...
    massive_for_del = dff[dff['индекс для split'] == 'del'].index.values
    # ...и удалить их
    for i in massive_for_del:
        dff.drop([i, i + 1, i + 2, i + 3, i + 4], inplace=True)
    # переобозначим индекс
    dff = dff.reset_index(drop=True)
    # уберем все запятые
    dff = dff.replace(',', '', regex=True)
    # переименуем колонки
    hh = dff.columns.values.tolist()
    dff.rename(columns={hh[0]: 'по Борну', hh[1]: 'по флуктациям', hh[2]: 'Index'}, inplace=True)
    # чтобы не было ошибок
    dff['по флуктациям'] = dff['по флуктациям'].replace('-1.#IO', '-1.0')
    # изменим формат
    dff['по Борну'] = dff['по Борну'].astype(float)
    dff['по флуктациям'] = dff['по флуктациям'].astype(float)
    # разделяем для разных пациентов
    newf_BORN = dff.pivot(columns='Index', values='по Борну')
    newf_FLUC = dff.pivot(columns='Index', values='по флуктациям')
    ###########
    # выбрасываем все NaN там, где они есть для каждого столбца и сохраняем значения в новый DataFrame
    BORN = pd.DataFrame()
    for i in newf_BORN.columns:
        ignore_nan = newf_BORN[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True)
        BORN.insert(loc=0, column=i, value=ignore_nan)
    BORN = BORN[BORN.columns[::-1]]
    ###########
    # выбрасываем все NaN там, где они есть для каждого столбца и сохраняем значения в новый DataFrame
    FLUC = pd.DataFrame()
    for i in newf_FLUC.columns:
        ignore_nan = newf_FLUC[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True)
        FLUC.insert(loc=0, column=i, value=ignore_nan)
    FLUC = FLUC[FLUC.columns[::-1]]
    # создадим DataFrame для времени - 4 Гц
    Time = pd.DataFrame()
    Time['время'] = range(0, max(len(BORN), len(FLUC)), 1)
    Time['время'] = Time['время'] * 0.25
    # создадим DataFrame для производной по Борну
    diff_BORN = pd.DataFrame()
    # для каждой колонки для измерений по Борну находим производную, умножаем её на 4 (4 Гц - с такой чистатой идут измерения), добавляем в конец значение 0, чтобы совпала длина массива
    for i in BORN.columns:
        for_born_diff = np.diff(BORN[i], n=1)
        for_born_diff = for_born_diff * 4
        for_born_diff = np.insert(for_born_diff, len(for_born_diff), 0.0)
        diff_BORN.insert(loc=0, column=i, value=for_born_diff)
    # создадим DataFrame для производной по Флуктациям
    diff_FLUC = pd.DataFrame()
    # для каждой колонки для измерений по Флуктациям находим производную, умножаем её на 4 (4 Гц - с такой чистатой идут измерения), добавляем в конец значение 0, чтобы совпала длина массива
    for i in FLUC.columns:
        for_fluc_diff = np.diff(FLUC[i], n=1)
        for_fluc_diff = for_fluc_diff * 4
        for_fluc_diff = np.insert(for_fluc_diff, len(for_fluc_diff), 0.0)
        diff_FLUC.insert(loc=0, column=i, value=for_fluc_diff)
    # избавимся от плохих значений, если они есть
    diff_BORN.dropna(inplace=True)
    diff_FLUC.dropna(inplace=True)
    # создадим DataFrame для сглаженной производной по Борну
    smooth_diff_BORN = pd.DataFrame()
    # для каждой колонки для измерений по Борну производим сглаживание
    if number_of_these_windows_born>1:
        for i in diff_BORN.columns:
            born_dif_smoth = sc.signal.savgol_filter(x=diff_BORN[i], window_length=number_of_these_windows_born,
                                                     polyorder=1)
            smooth_diff_BORN.insert(loc=0, column=i, value=born_dif_smoth)
    else:
        smooth_diff_BORN=diff_BORN
    # создадим DataFrame для сглаженной производной по Флуктациям
    smooth_diff_FLUC = pd.DataFrame()
    # для каждой колонки для измерений по Флуктациям производим сглаживание
    if number_of_these_windows_fluc>1:
        for i in diff_FLUC.columns:
            fluc_dif_smoth = sc.signal.savgol_filter(x=diff_FLUC[i], window_length=number_of_these_windows_fluc,
                                                     polyorder=1)
            smooth_diff_FLUC.insert(loc=0, column=i, value=fluc_dif_smoth)
    else:
        smooth_diff_FLUC=diff_FLUC
    # умножим все значения на 60, чтобы получить размерность */мин, а не */сек.
    smooth_diff_BORN = smooth_diff_BORN * 60
    smooth_diff_FLUC = smooth_diff_FLUC * 60
    # избавимся от плохих значений, если они есть
    BORN.dropna(inplace=True)
    FLUC.dropna(inplace=True)
    # создадим DataFrame для сглаженной кривой Борну
    smooth_BORN = pd.DataFrame()
    # для каждой колонки для измерений по Борну производим сглаживание
    if windows_born>1:
        for i in BORN.columns:
            born__smoth = sc.signal.savgol_filter(x=BORN[i], window_length=windows_born, polyorder=1)
            smooth_BORN.insert(loc=0, column=i, value=born__smoth)
    else:
        smooth_BORN=BORN
    # создадим DataFrame для сглаженной кривой Флуктациям
    smooth_FLUC = pd.DataFrame()
    # для каждой колонки для измерений по Борну производим сглаживание
    if windows_fluc>1:
        for i in FLUC.columns:
            fluc__smoth = sc.signal.savgol_filter(x=FLUC[i], window_length=windows_fluc, polyorder=1)
            smooth_FLUC.insert(loc=0, column=i, value=fluc__smoth)
    else:
        smooth_FLUC=FLUC
    '''
    Конечный DataFrame для данных 
    '''
    # создание результирующего DataFrame данных
    result_main = pd.DataFrame()
    # добавить максимальные значения в наш DataFrame
    result_main.insert(loc=0, column='Max произв. по флуктациям, отн.ед.', value=smooth_diff_FLUC.loc[50:, :].max())
    result_main.insert(loc=0, column='Max по флуктациям, отн.ед.', value=smooth_FLUC.loc[50:, :].max())
    result_main.insert(loc=0, column='Max произв. по Борну, %', value=smooth_diff_BORN.loc[50:, :].max())
    result_main.insert(loc=0, column='Max по Борну, %', value=smooth_BORN.loc[50:, :].max())

    # добавить столбец с концентрацией для последующего анализа
    for_conc_stuff = result_main.index.to_series().str.split(" ", expand=True)
    # теперь просто записываем for_conc_stuff в наш конечный DataFrame
    result_main.insert(loc=0, column='Дата', value=for_conc_stuff.iloc[:, -1])
    result_main.insert(loc=0, column='Концентрация АДФ, мкм', value=for_conc_stuff.iloc[:, -3])
    result_main.insert(loc=0, column='Пациент/донор/образец', value=for_conc_stuff.iloc[:, 0])
    # Все отрицательные значения заменим на 0
    for i in result_main.columns[3:]:
        result_main.loc[result_main[i] < 0, i] = 0
    '''
    Усредненный DataFrame
    '''
    combined_data_frame = pd.DataFrame()
    # ошибка и среднее
    combined_data_frame.insert(loc=0, column='SD(произв.ср.разм.агр.), отн.ед.', value=smooth_diff_FLUC.std(axis=1))
    combined_data_frame.insert(loc=0, column='Производная среднего размера агрегата, отн.ед.',
                               value=smooth_diff_FLUC.mean(axis=1))
    # ошибка и среднее
    combined_data_frame.insert(loc=0, column='SD(ср.разм.агр.), отн.ед.', value=smooth_FLUC.std(axis=1))
    combined_data_frame.insert(loc=0, column='Средний размер агрегата, отн.ед.', value=smooth_FLUC.mean(axis=1))
    # ошибка и среднее
    combined_data_frame.insert(loc=0, column='SD(произв.борн.), %/мин.', value=smooth_diff_BORN.std(axis=1))
    combined_data_frame.insert(loc=0, column='Производная по Борну, %/мин.', value=smooth_diff_BORN.mean(axis=1))
    # ошибка и среднее
    combined_data_frame.insert(loc=0, column='SD(борн.), %', value=smooth_BORN.std(axis=1))
    combined_data_frame.insert(loc=0, column='По Борну, %', value=smooth_BORN.mean(axis=1))
    # столбец времени
    combined_data_frame.insert(loc=0, column='Время, с.', value=Time['время'])
    '''
    Построение графиков
    '''
    #какие погррешности чертить
    error_set = {'Среднеквадратическое отклонение': 'sd', 'Среднеквадратическая ошибка': 'se',
                 'Доверительный интервал': 'ci', 'Перцентильный интервал': 'pi'}
    error_ = error_set[plot_fiture[1]]

    #подпись наверху графика
    if plot_fiture[2] == 'Eng':
        title1 = 'Averaged curve for '
        title2 = ' patients'
    else:
        title1 = 'Усредненная кривая по '
        title2 = ' пациентам'

    sns.reset_orig()
    #насколько шрифт изменяем
    sns.set(font_scale=plot_fiture[0])
    ##################################
    just_for_plot = pd.melt(smooth_BORN.join(Time), id_vars=['время'])
    just_for_plot.columns = ['Время, с', 'Пациент', 'Светопропускание,%']
    if plot_fiture[2] == 'Eng':
        just_for_plot.columns = ['Time, s', 'Пациент', 'Light transmission,%']

    #стили
    sns.set_style("ticks")
    if plot_fiture[3]:
        sns.set_style("whitegrid")

    fig, ax = plt.subplots()
    sns.lineplot(data=just_for_plot, x=just_for_plot.columns[0], y=just_for_plot.columns[2], errorbar=error_, ax=ax).set(
        title=title1 + str(len(result_main)) + title2)
    ax.set_xlim(0, 300)
    plt.tight_layout()

    just_for_plot2 = pd.melt(smooth_diff_BORN.join(Time), id_vars=['время'])
    just_for_plot2.columns = ['Время, с', 'Пациент', 'Производная светопропускания,%/мин.']
    if plot_fiture[2] == 'Eng':
        just_for_plot2.columns = ['Time, s', 'Пациент', 'Light transmission derivative, %/min']

    #sns.set_style("whitegrid")
    fig2, ax2 = plt.subplots()
    sns.lineplot(data=just_for_plot2, x=just_for_plot2.columns[0], y=just_for_plot2.columns[2], errorbar=error_, ax=ax2).set(
        title=title1 + str(len(result_main)) + title2)
    ax2.set_xlim(0, 300)
    plt.tight_layout()

    just_for_plot3 = pd.melt(smooth_FLUC.join(Time), id_vars=['время'])
    just_for_plot3.columns = ['Время, с', 'Пациент', 'Средний размер агрегата, отн.ед.']
    if plot_fiture[2] == 'Eng':
        just_for_plot3.columns = ['Time, s', 'Пациент', 'Average aggregate size, a.u.']

    #sns.set_style("whitegrid")
    fig3, ax3 = plt.subplots()
    sns.lineplot(data=just_for_plot3, x=just_for_plot3.columns[0], y=just_for_plot3.columns[2], errorbar=error_, ax=ax3).set(
        title=title1 + str(len(result_main)) + title2)
    ax3.set_xlim(0, 300)
    plt.tight_layout()

    just_for_plot4 = pd.melt(smooth_diff_FLUC.join(Time), id_vars=['время'])
    just_for_plot4.columns = ['Время, с', 'Пациент', 'Производная среднего размера агрегата, отн.ед.']
    if plot_fiture[2] == 'Eng':
        just_for_plot4.columns = ['Time, s', 'Пациент', 'Average aggregate size derivative, a.u.']

    #sns.set_style("whitegrid")
    fig4, ax4 = plt.subplots()
    sns.lineplot(data=just_for_plot4, x=just_for_plot4.columns[0], y=just_for_plot4.columns[2], errorbar=error_,
                 ax=ax4).set(title=title1 + str(len(result_main)) + title2)
    ax4.set_xlim(0, 300)
    plt.tight_layout()

    with pd.ExcelWriter(path + name_of_file.replace('.txt', '') +'_agg'+ ".xlsx") as writer:
        result_main.to_excel(writer, sheet_name='полученные данные')
        Time.to_excel(writer, sheet_name='время')
        smooth_BORN.to_excel(writer, sheet_name='Светопропускание, %')
        smooth_diff_BORN.to_excel(writer, sheet_name='Произв. от светопроп., % сек')
        smooth_FLUC.to_excel(writer, sheet_name='Ср. разм. агр., отн.ед.')
        smooth_diff_FLUC.to_excel(writer, sheet_name='Произв. от ср. разм. агр.')
        combined_data_frame.to_excel(writer, sheet_name='Усредненные данные по строкам')
    # сохраняем усредненные графики
    fig.savefig(path + 'Светопропускание.png', dpi=600)
    fig2.savefig(path + 'Производная_светопропускания.png', dpi=600)
    fig3.savefig(path + 'Средний_радиус.png', dpi=600)
    fig4.savefig(path + 'Производная_среднего_радиуса.png', dpi=600)

    return messagebox.showinfo('Biola', f'Excel файл и все графики успешно сохранены')
