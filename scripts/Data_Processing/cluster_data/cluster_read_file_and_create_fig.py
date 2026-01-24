"""Чтение файла excel и построения класстеров."""  # noqa: INP001

from pathlib import Path

import pandas as pd
from PySide6.QtWidgets import QMessageBox

from .create_clustered_bubble_plot import create_clustered_bubble_plot


def cluster_read_file_and_create_fig(self) -> None:  # noqa: ANN001
    """Создание класстеров и сохранение рисунков."""
    dlg = QMessageBox(self)

    # параметры, которые нам понадобятся
    path = self.ui.path_for_excel_cluster.text()
    exel_name = self.ui.comboBox_cluster_file.currentText()
    sheet_name = self.ui.comboBox_cluster_excel_sheet.currentText()

    # доп. параметры
    n_cluster = self.ui.spinBox_cluster_n.value()
    method_coordinate = self.ui.comboBox_cluster_coord.currentText()
    size_buble = self.ui.spinBox_cluster_buble_size.value()

    if path == "":
        dlg.setWindowTitle("Класстеризация")
        dlg.setText("Не введен путь к папкам")
        dlg.exec()
        return

    files = Path(path) / exel_name

    try:
        # читаем exel файл
        df = pd.read_excel(str(files), sheet_name=sheet_name)
        corr_df = df.astype(float).corr()
    except Exception as e:
        dlg.setWindowTitle("Класстеризация")
        dlg.setText("Ошибка: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    try:
        fig, _, _, _ = create_clustered_bubble_plot(
            corr_df,
            method=method_coordinate,
            n_clusters=n_cluster,
            title_font_size=size_buble,
        )

        file_name_cluster = exel_name.replace(".xlsx", "")

        fig.savefig(
            str(Path(path) / f"{file_name_cluster}_{sheet_name}.png"),
            dpi=600,
            format="png",
            bbox_inches="tight",
        )

    except Exception as e:
        dlg.setWindowTitle("Класстеризация")
        dlg.setText("Ошибка при расчете: " + str(e))
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()
        return

    dlg.setWindowTitle("Класстеризация")
    dlg.setText("Файл успешно сохранен.")
    dlg.exec()
    return
