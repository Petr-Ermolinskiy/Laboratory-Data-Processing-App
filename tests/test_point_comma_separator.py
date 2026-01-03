import os
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
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

logger.add(sys.stderr, format="<green>{time:HH:mm:ss}</green> | {level} | {message}", level="INFO")
# ----------------------------------------------- #


"""
===============
Тесты
===============
"""


# Тестовая функция
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


def find_out_comma_or_point(ax, separator: str = ".") -> None:
    """Проверяет разделитель: точка или запятая."""
    # значения на графике
    tick_labels_x = [tick.get_text() for tick in ax.get_xticklabels()]
    tick_labels_y = [tick.get_text() for tick in ax.get_yticklabels()]

    assert all(separator in i for i in tick_labels_x)
    assert all(separator in i for i in tick_labels_y)


# Запуск теста при прямом выполнении скрипта
def test_point_separator() -> None:
    """Проверка функционала разделителя."""
    logger.info(f"РАЗДЕЛИТЕЛЬ: {'запятая' if is_patched() else 'точка'}")

    logger.info("Создаем график с оригинальными настройками...")
    check_and_plot_comma_patch(separator=".")

    logger.info("Восстанавливаем оригинальный разделитель (точка)...")
    restore_global_comma_patch()

    logger.info("Создаем график с оригинальными настройками...")
    check_and_plot_comma_patch(separator=".")

    logger.info("Применяем патч с запятыми...")
    apply_global_comma_patch()

    logger.info("Создаем график с запятыми в качестве разделителей...")
    check_and_plot_comma_patch(separator=",")

    logger.info("Восстанавливаем оригинальный разделитель (точка)...")
    restore_global_comma_patch()

    logger.info("Создаем график с восстановленным разделителем-точкой...")
    check_and_plot_comma_patch(separator=".")
