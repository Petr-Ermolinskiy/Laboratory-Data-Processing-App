"""Создание линейного профиля для отчета RheoScan."""  # noqa: INP001

import os
import sys
import time

import matplotlib.pyplot as plt
import pandas as pd
from loguru import logger

# добавим возможность импорта из директории выше
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.Data_Processing.rheoscan_report.create_linear_profile import ParameterVisualizer

# ----------------------------------------------- #
logger.remove()

try:
    logger.add(
        sys.stderr, format="<green>{time:HH:mm:ss}</green> | {level} | {message}", level="INFO"
    )
except Exception as e:
    print(f"Нельзя импортировать: {e}")
# ----------------------------------------------- #


def test_create_profile() -> None:
    """Проверка генерации профиля."""
    data = {
        "parameter": [
            "Глюкоза (мг/дл)",
            "Холестерин (мг/дл)",
            "Гемоглобин (г/дл)",
            "Натрий (ммоль/л)",
        ],
        "normal_mean": [95, 180, 14.5, 140],
        "normal_SD": [10, 30, 1.2, 4],
        "patient_mean": [120, 220, 12.8, 138],
        "patient_SD": [8, 25, 0.9, 3],
    }

    df = pd.DataFrame(data)

    # Создание визуализации С легендой
    print("Создание визуализации С легендой...")
    visualizer = ParameterVisualizer(df, height_per_param=0.8)
    visualizer.visualize(
        title="Значения пациента vs Нормальные диапазоны",
        show_legend=True,
    )

    plt.show(block=False)
    time.sleep(1)
    plt.close()
