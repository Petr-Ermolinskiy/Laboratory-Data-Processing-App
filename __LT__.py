#необходимые библиотеки
import pandas as pd
import os
import glob
import math
from tkinter import messagebox

def laser_tweezers(path, split_subfold, a, b, date_of_cal, a_end, b_end, date_of_cal_end, split, position):
    path = path + '\\'
    # имя файла
    name_of_exp = path.split('\\')[-2]
    # считываем все данные и сохраняем их в 2 DataFrame. Считываются все имена подпапок, и в каждой подпапке считываются имена файлов, в которых есть значения сил агрегации и дезагрегации
    all_FA = pd.DataFrame({'Concentration': [], 'Force, pN': []})
    all_FD = pd.DataFrame({'Concentration': [], 'Force, pN': []})
    all_end = pd.DataFrame({'Concentration': [], 'Force, pN': []})
    all_glass = pd.DataFrame({'Concentration': [], 'Force, pN': []})
    for sub_folders in os.scandir(path):
        if sub_folders.is_dir():
            name = sub_folders.path.split('\\')[-1]
            files = glob.glob(path + name + '\\' + '*.avi')
            # разделить имя подпапки, если это нужно
            if split_subfold != '':
                name_dop = name.split(split_subfold)
                try:
                    name = name_dop[position - 1]
                except:
                    continue
            for i in files:
                m = i.split('\\')[-1]
                m = m.replace('.avi', '')
                # разделитель между FA или FD или др и разделителем "-"! Указать другой, если он другой.
                m = m.split(split)
                if len(m) < 2:
                    continue
                kk = m[0]
                # по условию просто записывает в DataFrames всё, что есть -- тут у m нужно поставить -1
                add__add = pd.DataFrame({'Concentration': name, 'Force, pN': m[-1]}, index=[0])
                if len(kk) > 1 and len(m) > 0:
                    if kk[0:2] == 'FA' or kk[0:2] == 'fa' or kk[0:2] == 'Fa':
                        all_FA = pd.concat([all_FA, add__add], ignore_index=True)
                    if kk[0:2] == 'En' or kk[0:2] == 'en' or kk[0:2] == 'EN':
                        all_end = pd.concat([all_end, add__add], ignore_index=True)
                    if kk[0:2] == 'FD' or kk[0:2] == 'fd' or kk[0:2] == 'Fd':
                        all_FD = pd.concat([all_FD, add__add], ignore_index=True)
                    if kk[0:2] == 'Gl' or kk[0:2] == 'gl' or kk[0:2] == 'Gl':
                        all_glass = pd.concat([all_glass, add__add], ignore_index=True)
    # не обязательная вещь! не всегда нужна! привести имена папок к цифровому виду -- если имена содержат буквы, то надо изменить!
    try:
        all_FA['Concentration'] = all_FA['Concentration'].astype(int)
        all_FD['Concentration'] = all_FD['Concentration'].astype(int)
        all_end['Concentration'] = all_end['Concentration'].astype(int)
        all_glass['Concentration'] = all_glass['Concentration'].astype(int)
    except Exception:
        print('Нельзя перевести имена папок в формат int')
    # приводим значения к float
    all_FA['Force, pN'] = all_FA['Force, pN'].astype(float)
    all_FD['Force, pN'] = all_FD['Force, pN'].astype(float)
    all_end['Force, pN'] = all_end['Force, pN'].astype(float)
    all_glass['Force, pN'] = all_glass['Force, pN'].astype(float)
    # переводим значения в силы
    all_FA['Force, pN'] = all_FA['Force, pN'] * a + b
    all_FD['Force, pN'] = all_FD['Force, pN'] * a + b
    all_end['Force, pN'] = all_end['Force, pN'] * a_end + b_end
    all_glass['Force, pN'] = all_glass['Force, pN'] * a_end + b_end

    # сортируем по концентрации
    all_FA = all_FA.sort_values(by=['Concentration'])
    all_FD = all_FD.sort_values(by=['Concentration'])
    all_end = all_end.sort_values(by=['Concentration'])
    all_glass = all_glass.sort_values(by=['Concentration'])

    # сортируем по индексу столбца
    newf_FA = all_FA.pivot(columns='Concentration', values='Force, pN')
    newf_FD = all_FD.pivot(columns='Concentration', values='Force, pN')
    newf_END = all_end.pivot(columns='Concentration', values='Force, pN')
    newf_GLASS = all_glass.pivot(columns='Concentration', values='Force, pN')

    # выбрасываем все NaN там, где они есть для каждого столбца для FA и сохраняем значения в новый DataFrame
    for_FA = pd.DataFrame()
    for i in newf_FA.columns:
        ignore_nan = newf_FA[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True)
        for_FA.insert(loc=0, column=i, value=ignore_nan)
    for_FA = for_FA[for_FA.columns[::-1]]
    # выбрасываем все NaN там, где они есть для каждого столбца для FD и сохраняем значения в новый DataFrame
    for_FD = pd.DataFrame()
    for i in newf_FD.columns:
        ignore_nan = newf_FD[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True)
        for_FD.insert(loc=0, column=i, value=ignore_nan)
    for_FD = for_FD[for_FD.columns[::-1]]
    # выбрасываем все NaN там, где они есть для каждого столбца для END и сохраняем значения в новый DataFrame
    for_END = pd.DataFrame()
    for i in newf_END.columns:
        ignore_nan = newf_END[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True)
        for_END.insert(loc=0, column=i, value=ignore_nan)
    for_END = for_END[for_END.columns[::-1]]
    # выбрасываем все NaN там, где они есть для каждого столбца для GLASS и сохраняем значения в новый DataFrame
    for_GLASS = pd.DataFrame()
    for i in newf_GLASS.columns:
        ignore_nan = newf_GLASS[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True)
        for_GLASS.insert(loc=0, column=i, value=ignore_nan)
    for_GLASS = for_GLASS[for_GLASS.columns[::-1]]

    # рассчитываем отношение силы дезагрегации к силе агрегации
    all_FD_OVER_FA = pd.DataFrame({'Concentration': [], 'FD/FA, a.u.': [], 'SD(FD/FA)': []})
    if newf_FD.empty == False:
        for i in newf_FD.columns:
            FD_OVER_FA = newf_FD[i].mean() / newf_FA[i].mean()
            FD_OVER_FA_SD = ((newf_FD[i].std() ** 2) / (newf_FA[i].mean() ** 2) + (newf_FD[i].mean() ** 2) * (
                        newf_FA[i].std() ** 2) / (newf_FA[i].mean() ** 4)) ** 0.5

            just______ = pd.DataFrame({'Concentration': i, 'FD/FA, a.u.': FD_OVER_FA, 'SD(FD/FA)': FD_OVER_FA_SD},
                                      index=[0])
            all_FD_OVER_FA = pd.concat([all_FD_OVER_FA, just______], ignore_index=True)

    # сделаем так, чтобы индекс начинался с 1, а не с 0
    all_FA.index += 1
    all_FD.index += 1
    all_end.index += 1
    for_FA.index += 1
    for_FD.index += 1
    for_END.index += 1
    all_glass.index += 1
    for_GLASS.index += 1
    all_FD_OVER_FA.index += 1

    with pd.ExcelWriter(path + name_of_exp + '.xlsx', engine='openpyxl') as writer:
        if all_end.empty == False:
            all_end.to_excel(writer, sheet_name='Endothilium')
        all_FA.to_excel(writer, sheet_name='FA')
        all_FD.to_excel(writer, sheet_name='FD')
        if for_END.empty == False:
            for_END.to_excel(writer, sheet_name='sorted-Endothilium')
        for_FA.to_excel(writer, sheet_name='sorted-FA')
        for_FD.to_excel(writer, sheet_name='sorted-FD')
        all_FD_OVER_FA.to_excel(writer, sheet_name='FD_over_FA')
        if all_glass.empty == False:
            all_glass.to_excel(writer, sheet_name='glass')
            for_GLASS.to_excel(writer, sheet_name='sorted-glass')
        # отдельный лист для калибровки
        text_sheet = writer.book.create_sheet(title='a and b coefficient')
        text_sheet.cell(column=1, row=1,
                        value='Перевод значения измеренное на фотодетекторе (Вольт) в силу (пН) по параметрам калибровки:')
        text_sheet.cell(column=1, row=2, value='_______________________________________')
        text_sheet.cell(column=1, row=3, value='Калибровка для дополнительного пучка была сделана:' + date_of_cal)
        text_sheet.cell(column=1, row=4, value='y(пН)=a*x(Вольт)+b')
        text_sheet.cell(column=1, row=5, value='a:')
        text_sheet.cell(column=2, row=5, value='b:')
        text_sheet.cell(column=1, row=6, value=a)
        text_sheet.cell(column=2, row=6, value=b)
        text_sheet.cell(column=1, row=7, value='_______________________________________')
        if all_end.empty == False:
            text_sheet.cell(column=1, row=8, value='Калибровка для основного пучка была сделана:' + date_of_cal)
            text_sheet.cell(column=1, row=9, value='y(пН)=a*x(Вольт)+b')
            text_sheet.cell(column=1, row=10, value='a_end:')
            text_sheet.cell(column=2, row=10, value='b_end:')
            text_sheet.cell(column=1, row=11, value=a)
            text_sheet.cell(column=2, row=11, value=b)
    return messagebox.showinfo('Лазерный пинцет', f'Excel файл и все графики успешно сохранены')