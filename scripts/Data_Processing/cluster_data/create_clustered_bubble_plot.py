"""Создание пузырьковой диаграммы с класстерами."""  # noqa: INP001

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Polygon
from scipy.spatial import ConvexHull
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import MDS


def create_clustered_bubble_plot(  # noqa: C901, PLR0912, PLR0913, PLR0915
    corr_matrix: pd.DataFrame,
    *,
    importance_weights: np.array = None,
    n_clusters: int = 3,
    method: str = "MDS",
    show_hull: bool = True,
    hull_alpha: float = 0.2,
    figsize: tuple = (16, 10),
    title_font_size: int = 8,
) -> tuple:
    """Создает 2D пузырьковую диаграмму с класстерами.

    - X, Y: координаты PCA или MDS
    - Размер пузырьков: важность
    - Цвет пузырьков: принадлежность к кластеру
    - Название для каждого пузырька по центру (без рамки)
    - Объединенная легенда справа
    - Центры кластеров как черные точки с информацией о кластере.

    Args:
        corr_matrix (pd.DataFrame): матрица корреляции
        importance_weights (np.array, optional): важность -- размер пузурьков. Defaults to None.
        n_clusters (int, optional): кол-во класстеров. Defaults to 3.
        method (str, optional): метод для уменьшения размерности. Defaults to "MDS".
        show_hull (bool, optional): оболочка класстера. Defaults to True.
        hull_alpha (float, optional): прозрачность оболочки. Defaults to 0.2.
        figsize (tuple, optional): размер рисунка. Defaults to (16, 10).
        title_font_size (int, optional): Размер шрифта для названий пузырьков.. Defaults to 8.

    Returns:
        tuple: рисунок и др.

    """
    # Создаем цветовую палитру для кластеров
    colors = plt.cm.tab20(np.linspace(0, 1, n_clusters))

    # Вычисляем важность, если не предоставлена
    if importance_weights is None:
        importance_weights = np.abs(corr_matrix).sum(axis=0).to_numpy()

    # Масштабируем важность для размеров пузырьков (нелинейное масштабирование для лучшей визуализации)
    bubble_sizes = 100 + (importance_weights / importance_weights.max()) ** 1.5 * 900

    # Получаем 2D координаты с помощью PCA или MDS
    if method == "PCA":
        # PCA на матрице корреляций
        pca = PCA(n_components=2, random_state=42)
        coordinates = pca.fit_transform(corr_matrix)
        explained_var = pca.explained_variance_ratio_
        dim_labels = [
            f"ГК1 ({explained_var[0] * 100:.1f}% дисперсии)",
            f"ГК2 ({explained_var[1] * 100:.1f}% дисперсии)",
        ]

    else:  # MDS
        # Преобразуем корреляцию в расстояние (используя 1 - абсолютную корреляцию)
        distance_matrix = 1 - np.abs(corr_matrix)
        mds = MDS(
            n_components=2,
            dissimilarity="precomputed",
            random_state=42,
            normalized_stress="auto",
        )
        coordinates = mds.fit_transform(distance_matrix)
        dim_labels = ["Измерение MDS 1", "Измерение MDS 2"]

    # Выполняем кластеризацию KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(coordinates)
    cluster_centers = kmeans.cluster_centers_

    # Создаем фигуру с большей шириной для размещения легенды
    fig, ax = plt.subplots(figsize=figsize)

    # Сохраняем статистику кластеров
    cluster_stats = []

    # Отображаем каждый кластер с выпуклой оболочкой
    for cluster_id in range(n_clusters):
        # Получаем точки для этого кластера
        cluster_mask = cluster_labels == cluster_id
        cluster_coords = coordinates[cluster_mask]
        cluster_sizes = bubble_sizes[cluster_mask]
        cluster_features = corr_matrix.columns[cluster_mask]
        cluster_importance = importance_weights[cluster_mask]

        # Вычисляем статистику кластера
        cluster_size = np.sum(cluster_mask)
        avg_importance = cluster_importance.mean()
        cluster_stats.append({
            "id": cluster_id,
            "size": cluster_size,
            "avg_importance": avg_importance,
            "center": cluster_centers[cluster_id],
            "features": list(cluster_features),
        })

        # Отображаем выпуклую оболочку (прозрачная область)
        if show_hull and len(cluster_coords) >= 3:  # noqa: PLR2004
            try:
                hull = ConvexHull(cluster_coords)
                hull_points = cluster_coords[hull.vertices]

                # Создаем полигональный патч
                polygon = Polygon(
                    hull_points,
                    closed=True,
                    alpha=hull_alpha,
                    color=colors[cluster_id],
                    edgecolor=colors[cluster_id],
                    linewidth=1,
                    linestyle="--",
                )
                ax.add_patch(polygon)
            except:  # noqa: E722, S110
                # Если оболочка не строится (коллинеарные точки), просто пропускаем
                pass

        # Отображаем пузырьки для этого кластера
        ax.scatter(
            cluster_coords[:, 0],
            cluster_coords[:, 1],
            s=cluster_sizes,
            color=colors[cluster_id],
            alpha=0.7,
            edgecolors="black",
            linewidth=1.5,
            zorder=5,
        )

        # Добавляем названия признаков ПО ЦЕНТРУ каждого пузырька
        for (x, y), feature, size in zip(
            cluster_coords, cluster_features, cluster_sizes, strict=False
        ):
            # Определяем размер шрифта
            if title_font_size == "auto":
                # Автоматический размер на основе размера пузырька
                base_size = 6
                size_factor = np.sqrt(size / 100) * 0.8
                fontsize = max(base_size, min(12, base_size + size_factor))
            else:
                fontsize = title_font_size

            # Определяем жирность шрифта на основе важности
            percentile = (
                np.sum(
                    importance_weights
                    < importance_weights[cluster_mask][list(cluster_features).index(feature)]
                )
                / len(importance_weights)
                * 100
            )
            fontweight = "bold" if percentile > 75 else "normal"  # noqa: PLR2004

            # Вычисляем цвет текста на основе цвета пузырька (для контраста)
            bubble_color = colors[cluster_id]
            # Используем белый текст для темных пузырьков, черный для светлых
            luminance = 0.299 * bubble_color[0] + 0.587 * bubble_color[1] + 0.114 * bubble_color[2]
            text_color = "white" if luminance < 0.6 else "black"  # noqa: PLR2004

            # Добавляем текст по центру пузырька
            ax.text(
                x,
                y,
                feature,
                ha="center",
                va="center",
                fontsize=fontsize,
                fontweight=fontweight,
                color=text_color,
                zorder=6,
            )  # Выше пузырьков

    # Отображаем центры кластеров как черные точки с информацией о кластере
    for i, (center, stats) in enumerate(zip(cluster_centers, cluster_stats, strict=False)):
        # Отображаем черную точку для центра
        ax.scatter(
            center[0],
            center[1],
            s=200,
            c="black",
            marker="o",
            edgecolors="white",
            linewidth=2,
            zorder=10,
            label=f"Центр кластера {i + 1}",
        )

        # Добавляем номер кластера и размер как текст ПОД точкой центра
        label_text = f"Кластер {i + 1}\n(n={stats['size']})"

        ax.annotate(
            label_text,
            xy=(center[0], center[1]),
            xytext=(0, -25),  # Позиция под точкой
            textcoords="offset points",
            ha="center",
            va="top",
            fontsize=10,
            fontweight="bold",
            color="black",
            bbox={
                "boxstyle": "round,pad=0.3",
                "facecolor": "#CCCCCC",
                "alpha": 0.8,
                "edgecolor": "black",
                "linewidth": 1,
            },
        )

    # Форматирование
    ax.set_xlabel(dim_labels[0], fontsize=12, fontweight="bold")
    ax.set_ylabel(dim_labels[1], fontsize=12, fontweight="bold")

    # Создаем информативный заголовок
    method_name = "Анализ главных компонент" if method == "PCA" else "Многомерное шкалирование"
    title_text = (
        f"{method_name} - Кластеризованная пузырьковая диаграмма\nВыявлено {n_clusters} кластеров"
    )
    ax.set_title(title_text, fontsize=14, fontweight="bold", pad=20)

    ax.grid(True, alpha=0.2, linestyle="--", zorder=0)  # noqa: FBT003
    ax.axhline(y=0, color="gray", linestyle="-", alpha=0.3, linewidth=0.5)
    ax.axvline(x=0, color="gray", linestyle="-", alpha=0.3, linewidth=0.5)

    # Создаем полную легенду на правой стороне
    # Настраиваем подграфик для размещения легенды
    plt.subplots_adjust(right=0.75)

    # Создаем пользовательские элементы легенды
    legend_elements = []

    # 1. Примеры размеров пузырьков
    size_percentiles = [25, 50, 75]
    size_values = np.percentile(bubble_sizes, size_percentiles)
    importance_values = np.percentile(importance_weights, size_percentiles)

    for size_val, imp_val, pct in zip(
        size_values, importance_values, size_percentiles, strict=False
    ):
        legend_elements.append(
            plt.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor="gray",
                markersize=np.sqrt(size_val) / 8,
                alpha=0.7,
                markeredgecolor="black",
                markeredgewidth=1,
                label=f"P{pct} Важность\n({imp_val:.2f})",
            )
        )

    # Добавляем разделительную линию
    legend_elements.append(plt.Line2D([0], [0], color="none", label=" "))

    # 2. Цвета кластеров
    for cluster_id in range(n_clusters):
        legend_elements.append(  # noqa: PERF401
            plt.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor=colors[cluster_id],
                markersize=8,
                alpha=0.7,
                markeredgecolor="black",
                label=f"Кластер {cluster_id + 1}\n({cluster_stats[cluster_id]['size']} признаков)",
            )
        )

    # Добавляем разделительную линию
    legend_elements.append(plt.Line2D([0], [0], color="none", label=" "))

    # 3. Маркеры центров
    legend_elements.append(
        plt.Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor="black",
            markersize=8,
            markeredgecolor="white",
            markeredgewidth=2,
            label="Центры кластеров",
        )
    )

    # 4. Области оболочек
    if show_hull:
        legend_elements.append(
            plt.Line2D(
                [0],
                [0],
                color=colors[0],
                alpha=hull_alpha,
                linewidth=8,
                linestyle="--",
                label="Область кластера",
            )
        )

    # Добавляем разделительную линию
    legend_elements.append(plt.Line2D([0], [0], color="none", label=" "))

    # 5. Сводка статистики
    total_features = len(corr_matrix.columns)
    avg_imp_all = importance_weights.mean()

    stats_text = f"Всего признаков: {total_features}\nСредняя важность: {avg_imp_all:.2f}"
    legend_elements.append(plt.Line2D([0], [0], color="none", label=stats_text))

    # Создаем легенду снаружи справа
    legend = ax.legend(
        handles=legend_elements,
        title="Легенда",
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        borderaxespad=0.0,
        frameon=True,
        framealpha=0.9,
        fancybox=True,
        shadow=True,
        fontsize=9,
        labelspacing=1.2,
        handlelength=2,
        handletextpad=1,
    )

    # Стилизуем заголовок легенды
    legend.get_title().set_fontweight("bold")
    legend.get_title().set_fontsize(11)

    # Равное соотношение сторон
    ax.set_aspect("auto")

    # Добавляем информацию о методе внизу
    method_info = f"Метод: {method} | "
    if method == "PCA":
        method_info += f"Объясненная дисперсия: {explained_var.sum() * 100:.1f}%"
    else:
        method_info += f"Стресс: {mds.stress_:.3f}"

    fig.text(0.5, 0.02, method_info, ha="center", fontsize=10, style="italic", color="gray")

    plt.tight_layout(rect=[0, 0.05, 0.85, 0.95])

    # Возвращаем дополнительную информацию
    cluster_info = {}
    for stats in cluster_stats:
        cluster_info[f"Кластер_{stats['id'] + 1}"] = {
            "признаки": stats["features"],
            "центр": stats["center"],
            "средняя_важность": stats["avg_importance"],
            "размер": stats["size"],
            "координаты": coordinates[cluster_labels == stats["id"]],
        }

    return fig, coordinates, cluster_labels, cluster_info
