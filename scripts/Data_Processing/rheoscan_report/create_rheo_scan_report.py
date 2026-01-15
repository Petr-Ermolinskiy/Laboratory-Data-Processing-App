"""Создание отчета по одному пациенту -- RheoScan."""  # noqa: INP001

import json
from pathlib import Path

import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
from PySide6.QtWidgets import QMessageBox

from .create_linear_profile import ParameterVisualizer
from .rheoscan_report import create_pdf_microrheology_report


def plot_fig_and_create_report(  # noqa: PLR0913
    path: str,
    exel_name: str,
    df: pd.DataFrame,
    date_of_measurement: str,
    date_of_processing: str,
    exp_name: str,
    process_name: str,
) -> None:
    """Генерация рисунка и вызов ф-ии генерации pdf."""
    visualizer = ParameterVisualizer(df, height_per_param=0.8)
    fig, _ = visualizer.visualize(
        title="Микрореологический профиль пациента",
        show_legend=True,
    )

    surname = exel_name.replace(".xlsx", "")
    path_to_save = str(Path(path) / f"{surname}.pdf")

    comments = """• """

    # создание отчета
    create_pdf_microrheology_report(
        path_to_save,
        surname,
        date_of_measurement,
        date_of_processing,
        exp_name,
        process_name,
        fig,
        comments,
    )

    plt.close(fig)


def prepare_and_create_rheo_scan_report(self) -> None:  # noqa: ANN001, PLR0911, PLR0915
    """Создание отчета RheoScan."""
    dlg = QMessageBox(self)

    # параметры, которые нам понадобятся
    path = self.ui.path_for_rheoscan_report.text()
    exel_name = self.ui.comboBox_rheoscan_report.currentText()

    if path == "":
        dlg.setWindowTitle("Отчет RheoScan")
        dlg.setText("Не введен путь к папкам")
        dlg.exec()
        return

    file_path = Path(path) / exel_name

    # -- доп параметры -- #
    # дата измерения
    date_of_measurment = self.ui.calendarWidget_rheoscan_report.selectedDate()
    date_of_measurment = date_of_measurment.toString("yyyy-MM-dd")

    # имя исполнителя эксперимента
    name_experiment_executor = self.ui.rheoscan_report_name_exp.text()
    # имя обработчика
    name_experiment_processer = self.ui.rheoscan_report_name_process.text()

    if name_experiment_executor == "" or name_experiment_processer == "":
        dlg.setWindowTitle("Отчет RheoScan")
        dlg.setText("Введите имена исполнителей")
        dlg.exec()
        return

    # выбранные параметры
    select_parameters_dict = self.ui.rheoscan_report_parameters_dict.toPlainText()
    # диапазон нормы
    norm_range_dict = self.ui.rheoscan_report_norm_dict.toPlainText()

    # приведение к JSON словарю
    try:
        select_parameters_dict = json.loads(select_parameters_dict)
        norm_range_dict = json.loads(norm_range_dict)
    except Exception as e:
        dlg.setWindowTitle("Отчет RheoScan")
        dlg.setText("Приведение строк к словарю: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    # -- проверки -- #

    check_list = {
        "В поле параметров и диапазона нормы разные параметры.": set(
            select_parameters_dict.values()
        )
        == set(norm_range_dict.keys()),
        "В норме значения среднего и SD должны разделяться с помощью ±": all(
            "±" in i for i in norm_range_dict.values()
        ),
    }

    for message_, check_ in check_list.items():
        if not check_:
            dlg.setWindowTitle("Отчет RheoScan")
            dlg.setText(message_)
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()

            return

    # -- ЧТЕНИЕ excel файла -- #

    try:
        # читаем exel файл - index_col=0,
        df = pd.read_excel(str(file_path), sheet_name=None)
    except Exception as e:
        dlg.setWindowTitle("Отчет RheoScan")
        dlg.setText("Ошибка: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    # дату измерения также найдем
    try:
        wb = openpyxl.load_workbook(file_path, data_only=True)
        props = wb.properties
        date_of_processing = str(props.created)
    except Exception as e:
        dlg.setWindowTitle("Отчет RheoScan")
        dlg.setText("Ошибка: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    # модификация excel файла
    df = pd.concat(df.values(), ignore_index=True)

    to_left_cols = df.dtypes.where(lambda x: x != "object").dropna().index

    columns_to_select = select_parameters_dict.keys()

    columns_not_presented = set(columns_to_select) - set(to_left_cols)
    if columns_not_presented != set():
        dlg.setWindowTitle("Отчет RheoScan")
        dlg.setText("Нет следующих колонок (либо они не числа): " + str(columns_not_presented))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    # выделение нужных колонок
    df = df[columns_to_select]
    # переименование колонок
    df.columns = [select_parameters_dict[i] for i in df.columns]

    # вычисление статистик
    mean_vals = df.mean().rename("patient_mean").to_frame().reset_index(names=["parameter"])
    std_vals = df.std().rename("patient_SD").to_frame().reset_index(names=["parameter"]).fillna(0)

    # диапазон нормы
    norm_range = (
        pd.Series(norm_range_dict, name="norm_range").to_frame().reset_index(names=["parameter"])
    )
    norm_range[["normal_mean", "normal_SD"]] = (
        norm_range["norm_range"].str.split("±", expand=True, n=1).astype(float)
    )

    # в строки
    norm_range["parameter"] = norm_range["parameter"].astype(str)
    mean_vals["parameter"] = mean_vals["parameter"].astype(str)
    std_vals["parameter"] = std_vals["parameter"].astype(str)

    print(mean_vals)
    print(std_vals)
    print(norm_range)

    # объединяем данные
    overall_data = norm_range.merge(mean_vals, on="parameter").merge(std_vals, on="parameter")

    plot_fig_and_create_report(
        path,
        exel_name,
        overall_data,
        date_of_measurment,
        date_of_processing,
        name_experiment_executor,
        name_experiment_processer,
    )

    return
