"""Проверка разделителя -- ',' вместо '.'."""  # noqa: INP001

import os
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from loguru import logger

# добавим возможность импорта из директории выше
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# основная логика изменения разделителя
from scripts.Data_Processing.utils.fig_val_separator import (
    apply_global_comma_patch,
    is_patched,
    restore_global_comma_patch,
)

# ----------------------------------------------- #
logger.remove()

try:
    logger.add(
        sys.stderr, format="<green>{time:HH:mm:ss}</green> | {level} | {message}", level="INFO"
    )
except Exception as e:
    print(f"Нельзя импортировать: {e}")
# ----------------------------------------------- #


"""
===============
Доп. функции
===============
"""


def find_out_comma_or_point(ax: plt.subplot, separator: str = ".") -> None:
    """Проверяет разделитель: точка или запятая."""
    # значения на графике
    tick_labels_x = [tick.get_text() for tick in ax.get_xticklabels()]
    tick_labels_y = [tick.get_text() for tick in ax.get_yticklabels()]

    assert all(separator in i for i in tick_labels_x), tick_labels_x
    assert all(separator in i for i in tick_labels_y), tick_labels_y


# Тестовая функция для line plot
def check_and_plot_comma_patch(separator: str) -> None:
    """Тестирует патч с запятыми на различных диапазонах чисел."""
    logger.info(
        f"\nТестирование десятичного разделителя {'запятая' if is_patched() else 'точка'}..."
    )

    _fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(0, 10, 100) / 100
    y = np.sin(x) * 3.14159

    ax.plot(x, y, "b-", linewidth=2)
    ax.set_xlabel("X Значения (0 - 0.1)")
    ax.set_ylabel("Y Значения = sin(x) × π")
    ax.set_title(f"РАЗДЕЛИТЕЛЬ: {('запятая' if is_patched() else 'точка')}")
    ax.grid(True, alpha=0.3)  # noqa: FBT003

    find_out_comma_or_point(ax, separator=separator)

    plt.tight_layout()
    plt.show(block=False)

    time.sleep(0.5)
    plt.close()


# Тест для Boxplot
def boxplot_separator(separator: str) -> None:
    """Тестирует патч с запятыми на boxplot."""
    logger.info(f"Тестирование boxplot с разделителем {'запятая' if is_patched() else 'точка'}...")

    _fig, ax = plt.subplots(figsize=(8, 6))

    # Создаем тестовые данные
    rng = np.random.default_rng(42)
    data = [
        rng.normal(0, 1, 100) * 0.1234 + 1,
        rng.normal(2, 1.5, 100) * 0.5,
        rng.normal(-1, 0.5, 100) * 0.5,
    ]

    # Создаем boxplot
    ax.boxplot(
        data,
        widths=0.6,
        whis=(5, 95),
        patch_artist=True,
        positions=range(len(data)),
        showmeans=True,
        showfliers=False,
        meanprops={
            "marker": "D",
            "markerfacecolor": "white",
            "markeredgecolor": "black",
            "markersize": 8,
        },
    )

    ax.set_xlabel("Группы данных")
    ax.set_ylabel("Значения (нормальное распределение)")
    ax.set_title(f"Boxplot - РАЗДЕЛИТЕЛЬ: {('запятая' if is_patched() else 'точка')}")
    ax.grid(visible=True, alpha=0.3)

    # Проверяем разделитель
    tick_labels_y = [tick.get_text() for tick in ax.get_yticklabels() if tick.get_text()]
    if tick_labels_y:
        print("))))))))")
        print(tick_labels_y)
        assert all(separator in i for i in tick_labels_y)
        logger.info(
            f"Boxplot проверен: разделитель '{separator}' найден в {len(tick_labels_y)} метках"
        )

    plt.tight_layout()
    plt.show(block=False)
    time.sleep(0.5)
    plt.close()


# Тест для Heatmap
def heatmap_separator(separator: str) -> None:
    """Тестирует патч с запятыми на heatmap."""
    logger.info(f"Тестирование heatmap с разделителем {'запятая' if is_patched() else 'точка'}...")

    # Создаем корреляционную матрицу
    rng = np.random.default_rng(42)
    data = pd.DataFrame({
        "A": rng.normal(0, 1, 50) * 0.123,
        "B": rng.normal(0, 1, 50) * 0.456,
        "C": rng.normal(0, 1, 50) * 0.789,
        "D": rng.normal(0, 1, 50) * 0.234,
    })

    corr = data.corr()

    _fig, ax = plt.subplots(figsize=(8, 6))

    # Создаем heatmap с аннотациями
    heatmap = sns.heatmap(
        corr,
        cmap="coolwarm",
        annot=True,  # аннотации с числами
        linewidth=0.5,
        vmin=-1,
        vmax=1,
        ax=ax,
        fmt=".2f",  # формат с двумя знаками после запятой
    )

    ax.set_title(f"Heatmap - РАЗДЕЛИТЕЛЬ: {('запятая' if is_patched() else 'точка')}")

    # Проверяем аннотации (текст внутри ячеек)
    annotations = [text.get_text() for text in ax.texts if text.get_text()]
    if annotations:
        # Для heatmap проверяем только аннотации, не xticklabels/yticklabels
        annotation_with_separator = [anno for anno in annotations if separator in anno]
        if annotation_with_separator:
            logger.info(
                f"Heatmap: найдено {len(annotation_with_separator)} аннотаций с разделителем '{separator}'"
            )

    # Проверяем colorbar если есть
    if hasattr(heatmap, "collections"):
        for collection in heatmap.collections:
            if hasattr(collection, "colorbar"):
                cb = collection.colorbar
                if cb and hasattr(cb, "ax"):
                    cb_labels = [
                        tick.get_text() for tick in cb.ax.get_yticklabels() if tick.get_text()
                    ]
                    if cb_labels:
                        assert all(separator in i for i in cb_labels)
                        logger.info(f"Heatmap colorbar проверен: разделитель '{separator}' найден")

    plt.tight_layout()
    plt.show(block=False)
    time.sleep(0.5)
    plt.close()


# Тест для Jointplot
def jointplot_separator(separator: str) -> None:
    """Тестирует патч с запятыми на jointplot."""
    logger.info(
        f"Тестирование jointplot с разделителем {'запятая' if is_patched() else 'точка'}..."
    )

    # Создаем тестовые данные
    rng = np.random.default_rng(42)
    n_points = 100
    x = rng.normal(0, 1, n_points) * 0.1234
    y = x * 0.5 + rng.normal(0, 0.3, n_points) * 0.5678

    data = pd.DataFrame({"X": x, "Y": y})

    # Создаем jointplot
    joint_grid = sns.jointplot(data=data, x="X", y="Y", kind="scatter", alpha=0.6, height=7)

    joint_grid.ax_joint.set_title(
        f"Jointplot - РАЗДЕЛИТЕЛЬ: {('запятая' if is_patched() else 'точка')}"
    )

    # Проверяем оси на основном графике
    ax_main = joint_grid.ax_joint
    tick_labels_x = [tick.get_text() for tick in ax_main.get_xticklabels() if tick.get_text()]
    tick_labels_y = [tick.get_text() for tick in ax_main.get_yticklabels() if tick.get_text()]

    if tick_labels_x:
        assert all(separator in i for i in tick_labels_x)
        logger.info(f"Jointplot X-ось проверена: разделитель '{separator}' найден")

    if tick_labels_y:
        assert all(separator in i for i in tick_labels_y)
        logger.info(f"Jointplot Y-ось проверена: разделитель '{separator}' найден")

    # Проверяем гистограммы
    ax_marg_x = joint_grid.ax_marg_x
    ax_marg_y = joint_grid.ax_marg_y

    if ax_marg_x:
        marg_x_labels = [tick.get_text() for tick in ax_marg_x.get_xticklabels() if tick.get_text()]
        if marg_x_labels:
            assert all(separator in i for i in marg_x_labels)

    if ax_marg_y:
        marg_y_labels = [tick.get_text() for tick in ax_marg_y.get_yticklabels() if tick.get_text()]
        if marg_y_labels:
            assert all(separator in i for i in marg_y_labels)

    plt.show(block=False)
    time.sleep(0.5)
    plt.close()


# Тест для Scatter plot
def scatter_separator(separator: str) -> None:
    """Тестирует патч с запятыми на scatter plot."""
    logger.info(
        f"Тестирование scatter plot с разделителем {'запятая' if is_patched() else 'точка'}..."
    )

    _fig, ax = plt.subplots(figsize=(8, 6))

    rng = np.random.default_rng(42)
    n_points = 50
    x = rng.uniform(0.1, 0.9, n_points)
    y = rng.uniform(0.2, 1.5, n_points)
    sizes = rng.uniform(20, 200, n_points)

    scatter = ax.scatter(x, y, s=sizes, alpha=0.6, c=x, cmap="viridis")

    ax.set_xlabel("X координата (0.1 - 0.9)")
    ax.set_ylabel("Y координата (0.2 - 1.5)")
    ax.set_title(f"Scatter plot - РАЗДЕЛИТЕЛЬ: {('запятая' if is_patched() else 'точка')}")
    ax.grid(visible=True, alpha=0.3)

    # Добавляем colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label("Цветовая шкала (значения X)")

    # Проверяем оси
    find_out_comma_or_point(ax, separator=separator)

    # Проверяем colorbar
    cbar_labels = [tick.get_text() for tick in cbar.ax.get_yticklabels() if tick.get_text()]
    if cbar_labels:
        assert all(separator in i for i in cbar_labels)
        logger.info(f"Scatter plot colorbar проверен: разделитель '{separator}' найден")

    plt.tight_layout()
    plt.show(block=False)
    time.sleep(0.5)
    plt.close()


# Тест для Histogram
def histogram_separator(separator: str) -> None:
    """Тестирует патч с запятыми на histogram."""
    logger.info(
        f"Тестирование histogram с разделителем {'запятая' if is_patched() else 'точка'}..."
    )

    _fig, ax = plt.subplots(figsize=(8, 6))

    rng = np.random.default_rng(42)
    data = rng.normal(0, 1, 1000) * 0.1

    ax.hist(
        data,
        bins=8,
        alpha=0.7,
        color="steelblue",
        edgecolor="black",
        density=True,
    )

    ax.set_xlabel("Значения (нормальное распределение)")
    ax.set_ylabel("Частота")
    ax.set_title(f"Histogram - РАЗДЕЛИТЕЛЬ: {('запятая' if is_patched() else 'точка')}")
    ax.grid(visible=True, alpha=0.3)

    # Проверяем оси
    find_out_comma_or_point(ax, separator=separator)

    # Проверяем, что на оси Y тоже есть числа с разделителем
    y_labels = [tick.get_text() for tick in ax.get_yticklabels() if tick.get_text()]
    if y_labels and any(separator in label for label in y_labels):
        logger.info(f"Histogram Y-ось проверена: разделитель '{separator}' найден")

    plt.tight_layout()
    plt.show(block=False)
    time.sleep(0.5)
    plt.close()


"""
===============
Тесты
===============
"""


# Быстрый тест (только основные графики)
def test_run_quick_separator() -> None:
    """Запускает быстрый тест основных графиков."""
    logger.info("Быстрый тест разделителей...")

    # 1. Точки
    restore_global_comma_patch()
    logger.info("Режим: ТОЧКИ")
    check_and_plot_comma_patch(separator=".")

    # 2. Запятые
    apply_global_comma_patch()
    logger.info("Режим: ЗАПЯТЫЕ")
    check_and_plot_comma_patch(separator=",")

    # 3. Возвращаем точки
    restore_global_comma_patch()
    logger.info("Возврат к ТОЧКАМ")
    check_and_plot_comma_patch(separator=".")


# Комплексный тест всех типов графиков
def test_run_comprehensive_separator() -> None:
    """Запускает комплексный тест всех типов графиков."""
    logger.info("=" * 60)
    logger.info("НАЧАЛО КОМПЛЕКСНОГО ТЕСТИРОВАНИЯ РАЗДЕЛИТЕЛЕЙ")
    logger.info("=" * 60)

    # Тест 1: Оригинальные настройки (точки)
    logger.info("\n" + "=" * 60)
    logger.info("ТЕСТ 1: Оригинальные настройки (точки)")
    logger.info("=" * 60)

    restore_global_comma_patch()

    boxplot_separator(separator=".")
    histogram_separator(separator=".")
    scatter_separator(separator=".")
    heatmap_separator(separator=".")
    jointplot_separator(separator=".")
    check_and_plot_comma_patch(separator=".")

    # Тест 2: Применяем патч (запятые)
    logger.info("\n" + "=" * 60)
    logger.info("ТЕСТ 2: Применяем патч (запятые)")
    logger.info("=" * 60)

    apply_global_comma_patch()

    boxplot_separator(separator=",")
    histogram_separator(separator=",")
    scatter_separator(separator=",")
    heatmap_separator(separator=",")
    jointplot_separator(separator=",")
    check_and_plot_comma_patch(separator=",")

    # Тест 3: Восстанавливаем обратно (точки)
    logger.info("\n" + "=" * 60)
    logger.info("ТЕСТ 3: Восстанавливаем обратно (точки)")
    logger.info("=" * 60)

    restore_global_comma_patch()

    boxplot_separator(separator=".")
    histogram_separator(separator=".")
    scatter_separator(separator=".")
    heatmap_separator(separator=".")
    jointplot_separator(separator=".")
    check_and_plot_comma_patch(separator=".")

    logger.info("\n" + "=" * 60)
    logger.info("КОМПЛЕКСНОЕ ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО!")
    logger.info("=" * 60)
