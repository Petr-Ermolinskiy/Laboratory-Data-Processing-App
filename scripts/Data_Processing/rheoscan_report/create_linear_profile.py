"""Построить линейный профиль."""  # noqa: INP001

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


class ParameterVisualizer:
    """Класс для визуализации сравнения параметров."""

    # Константы цветов
    COLOR_NORMAL_RANGE = "#2A968D"
    COLOR_NORMAL_MEAN = "blue"
    COLOR_PATIENT = "#DB4900"
    COLOR_TEXT_GRAY = "gray"

    def __init__(self, df: pd.DataFrame, height_per_param: float = 0.8) -> None:
        """
        Используется датафрейм, по которому строится график.

        Датафрейм содержит колонки:
        ['parameter', 'normal_mean', 'normal_SD', 'patient_mean', 'patient_SD']
        """
        self.df = df
        self.height_per_param = height_per_param
        self.fig = None
        self.axes = None

    @staticmethod
    def format_clean(value: float) -> str:
        """Форматирует число адаптивно, убирая конечные нули и десятичную точку."""
        return f"{value:.2f}".rstrip("0").rstrip(".")

    def create_figure(self) -> tuple:
        """Создает фигуру и оси."""
        self.fig, self.axes = plt.subplots(
            len(self.df),
            1,
            figsize=(12, self.height_per_param * len(self.df)),
            gridspec_kw={"hspace": 0.8},
        )

        if len(self.df) == 1:
            self.axes = [self.axes]

        return self.fig, self.axes

    def create_legend_elements(self) -> list:
        """Создает элементы легенды для графика."""
        return [
            # Красная точка: значение пациента
            Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor=self.COLOR_PATIENT,
                markersize=10,
                label="Пациент (среднее ± SD)",
            ),
            # Синяя затененная область: нормальный диапазон
            Patch(
                facecolor=self.COLOR_NORMAL_RANGE,
                alpha=0.3,
                edgecolor="blue",
                label="Диапазон нормы",
            ),
            # Синяя пунктирная линия: среднее нормального диапазона
            Line2D(
                [0],
                [0],
                color=self.COLOR_NORMAL_MEAN,
                alpha=0.7,
                linestyle="--",
                linewidth=2,
                label="Среднее значение нормы",
            ),
        ]

    def add_legend(self, location: str = "upper center", ncol: int = 3) -> plt.figure:
        """Добавляет легенду к фигуре."""
        legend_elements = self.create_legend_elements()
        legend = self.fig.legend(
            handles=legend_elements,
            loc=location,
            ncol=ncol,
            framealpha=0.9,
            fontsize=10,
            borderaxespad=0.5,
            bbox_to_anchor=(0.5, 1.05),
        )  # Позиция над фигурой

        # Делаем фон легенды более заметным
        legend.get_frame().set_facecolor("white")
        legend.get_frame().set_edgecolor("gray")
        legend.get_frame().set_alpha(0.95)

        return legend

    def visualize(
        self,
        title: str = "Patient Values vs Normal Ranges",
        *,
        show_legend: bool = True,
    ) -> tuple:
        """Создает полную визуализацию."""
        self.create_figure()

        for idx, (_, row) in enumerate(self.df.iterrows()):
            ax = self.axes[idx]
            self._plot_parameter(ax, row)

        # Настраиваем макет в зависимости от того, показывается ли легенда
        if show_legend:
            # Сначала добавляем заголовок, затем легенду
            self.add_legend(location="upper center", ncol=3)
            self.fig.suptitle(title, fontsize=14, fontweight="bold", y=1.15)
            # Настраиваем макет, чтобы освободить место для обоих
            # -- plt.tight_layout() -- не делаем
        else:
            # Просто добавляем заголовок
            self.fig.suptitle(title, fontsize=14, fontweight="bold", y=0.98)
            # -- plt.tight_layout() -- не делаем

        return self.fig, self.axes

    def _plot_parameter(self, ax, row: pd.Series) -> None:  # noqa: ANN001
        """Отображает один параметр."""
        # Настройка
        x_min, x_max = self._calculate_limits(row)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(-0.05, 0.05)
        ax.set_yticks([])

        # Метки
        ax.set_ylabel(
            row["parameter"],
            rotation=0,
            ha="right",
            va="center",
            fontweight="bold",
            fontsize=10,
        )
        ax.yaxis.set_label_coords(-0.05, 0.5)

        # Сетка
        ax.grid(True, alpha=0.1, axis="x", which="major")  # noqa: FBT003

        # Нормальный диапазон
        normal_low, normal_high = self._calculate_normal_range(row)
        ax.axvspan(normal_low, normal_high, alpha=0.3, color=self.COLOR_NORMAL_RANGE)
        ax.axvline(
            x=row["normal_mean"],
            color=self.COLOR_NORMAL_MEAN,
            alpha=0.7,
            linestyle="--",
            linewidth=1,
        )

        # Значение пациента
        ax.errorbar(
            row["patient_mean"],
            0,
            xerr=row["patient_SD"],
            fmt="o",
            color=self.COLOR_PATIENT,
            ecolor=self.COLOR_PATIENT,
            elinewidth=2,
            capsize=6,
            capthick=2,
            markersize=8,
        )

        # Деления на оси X
        custom_ticks = [normal_low, row["normal_mean"], normal_high]
        custom_labels = [self.format_clean(t) for t in custom_ticks]
        ax.set_xticks(custom_ticks)
        ax.set_xticklabels(custom_labels, fontsize=9, color=self.COLOR_NORMAL_MEAN)

        # Аннотации
        self._add_annotations(ax, row)

        # Убираем верхнюю и правую границы для более чистого вида
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    def _calculate_limits(self, row: pd.Series) -> tuple:
        """Вычисляет пределы графика для параметра."""
        x_min = min(
            row["normal_mean"] - row["normal_SD"] * 2, row["patient_mean"] - row["patient_SD"] * 2
        )
        x_max = max(
            row["normal_mean"] + row["normal_SD"] * 2, row["patient_mean"] + row["patient_SD"] * 2
        )

        x_range = x_max - x_min
        return x_min - x_range * 0.05, x_max + x_range * 0.05

    @staticmethod
    def _calculate_normal_range(row: pd.Series) -> tuple:
        """Вычисляет границы нормального диапазона."""
        return (row["normal_mean"] - row["normal_SD"], row["normal_mean"] + row["normal_SD"])

    def _add_annotations(self, ax, row: pd.Series) -> None:  # noqa: ANN001
        """Добавляет все аннотации для параметра."""
        # Аннотация значения пациента
        patient_text = self.format_clean(row["patient_mean"])
        ax.text(
            row["patient_mean"],
            0.01,
            patient_text,
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
            color=self.COLOR_PATIENT,
        )

        # Аннотация процентного различия
        self._add_percentage_annotation(ax, row)

    def _add_percentage_annotation(self, ax, row: pd.Series) -> None:  # noqa: ANN001
        """Добавляет аннотацию процентного различия."""
        if row["normal_mean"] == 0:
            ax.text(
                0.98,
                0.5,
                "N/A",
                transform=ax.transAxes,
                ha="right",
                va="center",
                fontsize=12,
                fontweight="bold",
                color="black",
                bbox={
                    "boxstyle": "round,pad=0.3",
                    "facecolor": "lightgray",
                    "edgecolor": "white",
                    "alpha": 0.4,
                },
            )
            return

        # Вычисляем проценты
        percentage_diff = (row["patient_mean"] / row["normal_mean"] * 100) - 100
        diff_text = (
            f"+{percentage_diff:.1f}%" if percentage_diff >= 0 else f"{percentage_diff:.1f}%"
        )

        # Определяем цвет
        diff_color, diff_alpha = self._classify_status(row)

        # Добавляем аннотацию
        ax.text(
            0.98,
            0.5,
            diff_text,
            transform=ax.transAxes,
            ha="right",
            va="center",
            fontsize=14,
            fontweight="bold",
            color="black",
            bbox={
                "boxstyle": "round,pad=0.3",
                "facecolor": diff_color,
                "edgecolor": "white",
                "alpha": diff_alpha,
            },
        )

    def _classify_status(self, row: pd.Series) -> tuple:
        """Классифицирует статус значения пациента для цветового кодирования."""
        normal_low, normal_high = self._calculate_normal_range(row)
        patient_low = row["patient_mean"] - row["patient_SD"]
        patient_high = row["patient_mean"] + row["patient_SD"]

        mean_within = normal_low <= row["patient_mean"] <= normal_high
        ranges_overlap = not (patient_high < normal_low or patient_low > normal_high)

        if mean_within:
            return "limegreen", 0.4
        if ranges_overlap:
            return "orange", 0.4
        return "red", 0.5
