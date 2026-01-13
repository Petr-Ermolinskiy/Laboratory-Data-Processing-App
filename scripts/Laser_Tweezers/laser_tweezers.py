import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
from loguru import logger
from numpy import exp as np_exp
from PySide6.QtWidgets import QMessageBox

# ----------------------------------------------- #
logger.remove()

try:
    logger.add(
        sys.stderr, format="<green>{time:HH:mm:ss}</green> | {level} | {message}", level="INFO"
    )
except Exception as e:
    print(f"Нельзя импортировать: {e}")
# ----------------------------------------------- #


def parse_date_string(date_str: str) -> datetime:
    """Парсинг формата дат.

    - 03.04.2025 (European format: день.месяц.год)
    - 03/04/2025 (US format: месяц/день/год or день/месяц/год)
    """
    # убираем
    date_str = date_str.strip()

    # пробуем разные форматы
    formats = [
        "%d.%m.%Y",  # 03.04.2025 (день.месяц.год)
        "%d/%m/%Y",  # 03/04/2025 (день/месяц/год)
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    # если ничто не сработало, то ошибка
    msg = f"Unable to parse date string: {date_str}"
    raise ValueError(msg)


def change_format_date(date_str_: str, separator="/") -> str:
    """Возращает дату в формате день/месяц/год."""
    # не используем strftime("%d/%m/%Y"), потому что есть разница на Windows и Mac
    # а изначально день-месяц без нуля сначала
    parsed_date = parse_date_string(date_str_)

    day = str(parsed_date.day)
    month = str(parsed_date.month)
    year = str(parsed_date.year)

    return f"{day}{separator}{month}{separator}{year}"


def laser_tweezers(self) -> None:
    dlg = QMessageBox(self)
    #########################
    # параметры, которые нам понадобятся
    path = self.ui.path_for_LT.text()
    split_subfold = self.ui.sep_for_LT.text()
    a, b = self.ui.a_dop.value(), self.ui.b_dop.value()
    date_of_cal = self.ui.dateEdit_2.text()
    date_of_cal_quadratic = self.ui.dateEdit_3.text()
    a_end, b_end = self.ui.a_main.value(), self.ui.b_main.value()
    date_of_cal_end = self.ui.dateEdit.text()
    split = self.ui.sep_for_LT_values.text()
    position = self.ui.position.value()
    #########################
    if path == "":
        dlg.setWindowTitle("Лазерный пинцет")
        dlg.setText("Не введен путь к папкам")
        dlg.exec()
        return

    path_obj = Path(path)
    # имя файла
    name_of_exp = path_obj.name

    # все даты переводим в единый формат
    date_of_cal = change_format_date(date_of_cal)
    date_of_cal_quadratic = change_format_date(date_of_cal_quadratic)
    date_of_cal_end = change_format_date(date_of_cal_end)

    # Считываем все данные и сохраняем их в 2 DataFrame.
    # Считываются все имена подпапок, и в каждой подпапке считываются имена файлов,
    # в которых есть значения сил агрегации и дезагрегации
    all_FA = pd.DataFrame({"Concentration": [], "Force, pN": []})
    all_FD = pd.DataFrame({"Concentration": [], "Force, pN": []})
    all_end = pd.DataFrame({"Concentration": [], "Force, pN": []})
    all_glass = pd.DataFrame({"Concentration": [], "Force, pN": []})
    for sub_folders in path_obj.iterdir():
        if sub_folders.is_dir():
            name = sub_folders.name
            files = list(sub_folders.glob("*.avi"))
            # разделить имя подпапки, если это нужно
            if split_subfold != "":
                name_dop = name.split(split_subfold)
                try:
                    name = name_dop[position - 1]
                except:  # noqa: E722, S112
                    continue
            for i in files:
                m = i.name
                m = m.replace(".avi", "")
                # разделитель между FA или FD или др и разделителем "-"! Указать другой, если он другой.
                m = m.split(split)
                if len(m) < 2:
                    continue
                kk = m[0]
                # по условию просто записывает в DataFrames всё, что есть -- тут у m нужно поставить -1
                add__add = pd.DataFrame({"Concentration": name, "Force, pN": m[-1]}, index=[0])
                if len(kk) > 1 and len(m) > 0:
                    if kk[0:2] == "FA" or kk[0:2] == "fa" or kk[0:2] == "Fa":
                        all_FA = pd.concat([all_FA, add__add], ignore_index=True)
                    if kk[0:2] == "En" or kk[0:2] == "en" or kk[0:2] == "EN":
                        all_end = pd.concat([all_end, add__add], ignore_index=True)
                    if kk[0:2] == "FD" or kk[0:2] == "fd" or kk[0:2] == "Fd":
                        all_FD = pd.concat([all_FD, add__add], ignore_index=True)
                    if kk[0:2] == "Gl" or kk[0:2] == "gl" or kk[0:2] == "Gl":
                        all_glass = pd.concat([all_glass, add__add], ignore_index=True)
    # не обязательная вещь! не всегда нужна! привести имена папок к INT -- если имена содержат буквы, то надо изменить!
    try:
        all_FA["Concentration"] = all_FA["Concentration"].astype(int)
        all_FD["Concentration"] = all_FD["Concentration"].astype(int)
        all_end["Concentration"] = all_end["Concentration"].astype(int)
        all_glass["Concentration"] = all_glass["Concentration"].astype(int)
    except Exception:
        logger.info("Нельзя перевести имена папок в формат int")
    # приводим значения к float
    try:
        all_FA["Force, pN"] = all_FA["Force, pN"].astype(float)
        all_FD["Force, pN"] = all_FD["Force, pN"].astype(float)
        all_end["Force, pN"] = all_end["Force, pN"].astype(float)
        all_glass["Force, pN"] = all_glass["Force, pN"].astype(float)
    except Exception as e:
        dlg.setWindowTitle("Лазерный пинцет")
        dlg.setText(
            "Некоторые значения сил нельзя перевести в float.\nПроверьте данные.\n" + str(e),
        )
        dlg.exec()
        return

    # переводим значения в силы - для линейной или экспоненциальной калибровки
    if self.ui.comboBox_LT_calibration.currentText() == "Линейная":
        all_FA["Force, pN"] = all_FA["Force, pN"] * a + b
        all_FD["Force, pN"] = all_FD["Force, pN"] * a + b
    else:
        all_FA["Force, pN"] = (
            self.ui.dop_cal_k.value()
            * (
                self.ui.dop_cal_y0.value()
                + self.ui.dop_cal_A.value()
                * np_exp(self.ui.dop_cal_R0.value() * all_FA["Force, pN"])
            )
            + self.ui.dop_cal_b.value()
        )
        all_FD["Force, pN"] = (
            self.ui.dop_cal_k.value()
            * (
                self.ui.dop_cal_y0.value()
                + self.ui.dop_cal_A.value()
                * np_exp(self.ui.dop_cal_R0.value() * all_FD["Force, pN"])
            )
            + self.ui.dop_cal_b.value()
        )

    all_end["Force, pN"] = all_end["Force, pN"] * a_end + b_end
    all_glass["Force, pN"] = all_glass["Force, pN"] * a_end + b_end

    # сортируем по концентрации
    all_FA = all_FA.sort_values(by=["Concentration", "Force, pN"], ascending=[True, False])
    all_FD = all_FD.sort_values(by=["Concentration", "Force, pN"], ascending=[True, False])
    all_end = all_end.sort_values(by=["Concentration", "Force, pN"], ascending=[True, False])
    all_glass = all_glass.sort_values(by=["Concentration", "Force, pN"], ascending=[True, False])

    # сортируем по индексу столбца
    newf_FA = all_FA.pivot(columns="Concentration", values="Force, pN")
    newf_FD = all_FD.pivot(columns="Concentration", values="Force, pN")
    newf_END = all_end.pivot(columns="Concentration", values="Force, pN")
    newf_GLASS = all_glass.pivot(columns="Concentration", values="Force, pN")

    # выбрасываем все NaN там, где они есть для каждого столбца для FA и сохраняем значения в новый DataFrame
    for_FA = pd.DataFrame()
    for i in newf_FA.columns:
        ignore_nan = newf_FA[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True).sort_values(ascending=False)
        for_FA.insert(loc=0, column=i, value=ignore_nan)
    for_FA = for_FA[for_FA.columns[::-1]]
    # выбрасываем все NaN там, где они есть для каждого столбца для FD и сохраняем значения в новый DataFrame
    for_FD = pd.DataFrame()
    for i in newf_FD.columns:
        ignore_nan = newf_FD[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True).sort_values(ascending=False)
        for_FD.insert(loc=0, column=i, value=ignore_nan)
    for_FD = for_FD[for_FD.columns[::-1]]
    # выбрасываем все NaN там, где они есть для каждого столбца для END и сохраняем значения в новый DataFrame
    for_END = pd.DataFrame()
    for i in newf_END.columns:
        ignore_nan = newf_END[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True).sort_values(ascending=False)
        for_END.insert(loc=0, column=i, value=ignore_nan)
    for_END = for_END[for_END.columns[::-1]]
    # выбрасываем все NaN там, где они есть для каждого столбца для GLASS и сохраняем значения в новый DataFrame
    for_GLASS = pd.DataFrame()
    for i in newf_GLASS.columns:
        ignore_nan = newf_GLASS[i]
        ignore_nan = ignore_nan.dropna()
        ignore_nan = ignore_nan.reset_index(drop=True).sort_values(ascending=False)
        for_GLASS.insert(loc=0, column=i, value=ignore_nan)
    for_GLASS = for_GLASS[for_GLASS.columns[::-1]]

    # рассчитываем отношение силы дезагрегации к силе агрегации
    all_FD_OVER_FA = pd.DataFrame({"Concentration": [], "FD/FA, a.u.": [], "SD(FD/FA)": []})
    if newf_FD.empty == False:
        for i in newf_FD.columns:
            FD_OVER_FA = newf_FD[i].mean() / newf_FA[i].mean()
            FD_OVER_FA_SD = (
                (newf_FD[i].std() ** 2) / (newf_FA[i].mean() ** 2)
                + (newf_FD[i].mean() ** 2) * (newf_FA[i].std() ** 2) / (newf_FA[i].mean() ** 4)
            ) ** 0.5

            just______ = pd.DataFrame(
                {"Concentration": i, "FD/FA, a.u.": FD_OVER_FA, "SD(FD/FA)": FD_OVER_FA_SD},
                index=[0],
            )
            all_FD_OVER_FA = pd.concat([all_FD_OVER_FA, just______], ignore_index=True)

    # делаем reset_index -- на Mac и Windows индексы будут различаться, если это не сделать
    all_FA = all_FA.reset_index(drop=True)
    all_FD = all_FD.reset_index(drop=True)
    all_end = all_end.reset_index(drop=True)
    for_FA = for_FA.reset_index(drop=True)
    for_FD = for_FD.reset_index(drop=True)
    for_END = for_END.reset_index(drop=True)
    all_glass = all_glass.reset_index(drop=True)
    for_GLASS = for_GLASS.reset_index(drop=True)
    all_FD_OVER_FA = all_FD_OVER_FA.reset_index(drop=True)

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

    with pd.ExcelWriter(str(path_obj / f"{name_of_exp}.xlsx"), engine="openpyxl") as writer:
        if all_end.empty == False:
            all_end.to_excel(writer, sheet_name="Endothilium")
        if all_FA.empty == False:
            all_FA.to_excel(writer, sheet_name="FA")
        if all_FD.empty == False:
            all_FD.to_excel(writer, sheet_name="FD")
        if self.ui.check_LT_raw_data.isChecked():
            if for_END.empty == False:
                for_END.to_excel(writer, sheet_name="sorted-Endothilium")
            if for_FA.empty == False:
                for_FA.to_excel(writer, sheet_name="sorted-FA")
            if for_FD.empty == False:
                for_FD.to_excel(writer, sheet_name="sorted-FD")
        if all_FD_OVER_FA.empty == False:
            all_FD_OVER_FA.to_excel(writer, sheet_name="FD_over_FA")
        if all_glass.empty == False:
            all_glass.to_excel(writer, sheet_name="glass")
            if self.ui.check_LT_raw_data.isChecked():
                for_GLASS.to_excel(writer, sheet_name="sorted-glass")
        # отдельный лист для калибровки
        text_sheet = writer.book.create_sheet(title="a and b coefficient")
        text_sheet.cell(
            column=1,
            row=1,
            value="Перевод значения измеренное на фотодетекторе (Вольт) в силу (пН) по параметрам калибровки:",
        )
        if self.ui.comboBox_LT_calibration.currentText() == "Линейная":
            text_sheet.cell(column=1, row=2, value="_______________________________________")
            text_sheet.cell(
                column=1,
                row=3,
                value="Калибровка для дополнительного пучка была сделана:" + date_of_cal,
            )
            text_sheet.cell(column=1, row=4, value="y(пН)=a*x(Вольт)+b")
            text_sheet.cell(column=1, row=5, value="a:")
            text_sheet.cell(column=2, row=5, value="b:")
            text_sheet.cell(column=1, row=6, value=a)
            text_sheet.cell(column=2, row=6, value=b)
            text_sheet.cell(column=1, row=7, value="_______________________________________")
        else:
            text_sheet.cell(column=1, row=2, value="_______________________________________")
            text_sheet.cell(
                column=1,
                row=3,
                value="Калибровка для дополнительного пучка была сделана:" + date_of_cal_quadratic,
            )
            text_sheet.cell(column=1, row=4, value="y(пН)=k*(y0 + A*exp(R0 * x(Вольт)))+b")
            text_sheet.cell(column=1, row=5, value="k:")
            text_sheet.cell(column=2, row=5, value="y0:")
            text_sheet.cell(column=3, row=5, value="A:")
            text_sheet.cell(column=4, row=5, value="R0:")
            text_sheet.cell(column=5, row=5, value="b:")
            # значения
            text_sheet.cell(column=1, row=6, value=self.ui.dop_cal_k.value())
            text_sheet.cell(column=2, row=6, value=self.ui.dop_cal_y0.value())
            text_sheet.cell(column=3, row=6, value=self.ui.dop_cal_A.value())
            text_sheet.cell(column=4, row=6, value=self.ui.dop_cal_R0.value())
            text_sheet.cell(column=5, row=6, value=self.ui.dop_cal_b.value())

            text_sheet.cell(column=1, row=7, value="_______________________________________")
        if all_end.empty == False:
            text_sheet.cell(
                column=1,
                row=8,
                value="Калибровка для основного пучка была сделана:" + date_of_cal_end,
            )
            text_sheet.cell(column=1, row=9, value="y(пН)=a*x(Вольт)+b")
            text_sheet.cell(column=1, row=10, value="a_end:")
            text_sheet.cell(column=2, row=10, value="b_end:")
            text_sheet.cell(column=1, row=11, value=a)
            text_sheet.cell(column=2, row=11, value=b)

    dlg.setWindowTitle("Лазерный пинцет")
    dlg.setText("Excel файл и все графики успешно сохранены")
    dlg.exec()
    return
