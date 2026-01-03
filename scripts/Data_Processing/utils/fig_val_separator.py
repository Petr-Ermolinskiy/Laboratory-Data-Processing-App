"""На графиках разделель: точки или запятые."""

import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from loguru import logger
from matplotlib import ticker

# Сохраняем оригинальные классы до внесения изменений
_ORIGINAL_CLASSES = {
    "ScalarFormatter": ticker.ScalarFormatter,
    "LogFormatter": ticker.LogFormatter,
    "LogFormatterExponent": ticker.LogFormatterExponent,
    "LogFormatterMathtext": ticker.LogFormatterMathtext,
    "FuncFormatter": ticker.FuncFormatter,
    "StrMethodFormatter": ticker.StrMethodFormatter,
    "Axis": mpl.axis.Axis,
    "Axes": mpl.axes.Axes,
    "Colorbar": mpl.colorbar.Colorbar,
}

# Сохраняем оригинальные методы
_ORIGINAL_METHODS = {
    "Axes.__init__": mpl.axes.Axes.__init__,
    "Colorbar.__init__": mpl.colorbar.Colorbar.__init__,
}

# Отслеживаем состояние патча
_IS_PATCHED = False


# Универсальный форматтер, обрабатывающий все случаи
class UniversalCommaFormatter(_ORIGINAL_CLASSES["ScalarFormatter"]):
    def __init__(self, useOffset=True, useMathText=False, useLocale=None):
        super().__init__(useOffset=useOffset, useMathText=useMathText, useLocale=useLocale)

    def __call__(self, x, pos=None):
        result = super().__call__(x, pos)
        return self._replace_dots_with_commas(result)

    def format_data(self, value):
        result = super().format_data(value)
        return self._replace_dots_with_commas(result)

    def format_data_short(self, value):
        result = super().format_data_short(value)
        return self._replace_dots_with_commas(result)

    def _replace_dots_with_commas(self, text):
        if not isinstance(text, str):
            return text

        # Обрабатываем все возможные форматы чисел:
        # 1. Обычные числа: 1.234, -0.567
        # 2. Научная нотация: 1.23e-04, 1.23E+04
        # 3. Смещение: 1.23 + 1e4
        # 4. Математический текст: $1.23 \times 10^{4}$

        # Проверяем математический текст (LaTeX)
        if text.startswith("$") and text.endswith("$"):
            # Извлекаем числовую часть из LaTeX
            inner = text[1:-1]
            # Простая замена для чисел в LaTeX
            inner = inner.replace(".", ",")
            return f"${inner}$"

        # Проверяем нотацию со смещением (например, "1.23 + 1e4")
        if " + " in text or " - " in text:
            parts = text.split(" ")
            for i, part in enumerate(parts):
                if "." in part and not ("e" in part.lower() or part.startswith("10^")):
                    parts[i] = part.replace(".", ",")
            return " ".join(parts)

        # Обрабатываем научную нотацию -- т.е. "е"
        if "e" in text.lower():
            lower_text = text.lower()
            e_index = lower_text.find("e")

            mantissa = text[:e_index]
            exponent = text[e_index:]

            mantissa = mantissa.replace(".", ",")
            return mantissa + exponent

        # для обычных чисел
        return text.replace(".", ",")


"""
----------------------------------------------------------
Создаем модифицированные версии для всех типов форматтеров
----------------------------------------------------------
"""


class CommaDecimalScalarFormatter(UniversalCommaFormatter):
    pass


class CommaDecimalLogFormatter(_ORIGINAL_CLASSES["LogFormatter"]):
    def __call__(self, x, pos=None):
        result = super().__call__(x, pos)
        if isinstance(result, str):
            return result.replace(".", ",")
        return result


class CommaDecimalLogFormatterExponent(_ORIGINAL_CLASSES["LogFormatterExponent"]):
    def __call__(self, x, pos=None):
        result = super().__call__(x, pos)
        if isinstance(result, str):
            return result.replace(".", ",")
        return result


class CommaDecimalLogFormatterMathtext(_ORIGINAL_CLASSES["LogFormatterMathtext"]):
    def __call__(self, x, pos=None):
        result = super().__call__(x, pos)
        if isinstance(result, str):
            return result.replace(".", ",")
        return result


class CommaDecimalFuncFormatter(_ORIGINAL_CLASSES["FuncFormatter"]):
    def __call__(self, x, pos=None):
        result = super().__call__(x, pos)
        if isinstance(result, str):
            return result.replace(".", ",")
        return result


class CommaDecimalStrMethodFormatter(_ORIGINAL_CLASSES["StrMethodFormatter"]):
    def __call__(self, x, pos=None):
        result = super().__call__(x, pos)
        if isinstance(result, str):
            return result.replace(".", ",")
        return result


def apply_global_comma_patch() -> None:
    """Применяет глобальный патч для использования запятых как десятичных разделителей во всех графиках matplotlib."""
    global _IS_PATCHED  # noqa: PLW0603

    if _IS_PATCHED:
        logger.info("Патч с запятыми уже применен")
        return

    # Подавляем предупреждение FutureWarning из seaborn, если оно есть
    warnings.filterwarnings("ignore", message="use_inf_as_na")

    # Заменяем все классы форматтеров
    ticker.ScalarFormatter = CommaDecimalScalarFormatter
    ticker.LogFormatter = CommaDecimalLogFormatter
    ticker.LogFormatterExponent = CommaDecimalLogFormatterExponent
    ticker.LogFormatterMathtext = CommaDecimalLogFormatterMathtext
    ticker.FuncFormatter = CommaDecimalFuncFormatter
    ticker.StrMethodFormatter = CommaDecimalStrMethodFormatter

    # Сохраняем оригинальный метод создания Axis
    _ORIGINAL_METHODS["Axis.__init__"] = mpl.axis.Axis.__init__

    # СОХРАНЯЕМ ОРИГИНАЛЬНЫЕ МЕТОДЫ ГРАФИКОВ
    _ORIGINAL_METHODS["Axes.boxplot"] = mpl.axes.Axes.boxplot
    _ORIGINAL_METHODS["Axes.hist"] = mpl.axes.Axes.hist
    _ORIGINAL_METHODS["Axes.scatter"] = mpl.axes.Axes.scatter
    _ORIGINAL_METHODS["Axes.plot"] = mpl.axes.Axes.plot

    # СОХРАНЯЕМ ОРИГИНАЛЬНЫЕ МЕТОДЫ SEABORN ЕСЛИ ОН ЕСТЬ
    _ORIGINAL_METHODS["seaborn.heatmap"] = sns.heatmap

    # Модифицируем создание осей для гарантированной установки форматтеров
    def patched_Axes_init(self, *args, **kwargs):
        _ORIGINAL_METHODS["Axes.__init__"](self, *args, **kwargs)

        # Устанавливаем форматтеры с запятыми для осей x и y
        self.xaxis.set_major_formatter(CommaDecimalScalarFormatter())
        self.yaxis.set_major_formatter(CommaDecimalScalarFormatter())

        # Также устанавливаем форматтеры для второстепенных делений, если они существуют
        if self.xaxis.get_minor_formatter():
            self.xaxis.set_minor_formatter(CommaDecimalScalarFormatter())
        if self.yaxis.get_minor_formatter():
            self.yaxis.set_minor_formatter(CommaDecimalScalarFormatter())

    mpl.axes.Axes.__init__ = patched_Axes_init

    # Также модифицируем создание цветовой шкалы
    def patched_Colorbar_init(self, *args, **kwargs):
        _ORIGINAL_METHODS["Colorbar.__init__"](self, *args, **kwargs)
        if hasattr(self, "ax") and self.ax:
            self.ax.yaxis.set_major_formatter(CommaDecimalScalarFormatter())

    mpl.colorbar.Colorbar.__init__ = patched_Colorbar_init
    _ORIGINAL_METHODS["Colorbar.__init___patched"] = patched_Colorbar_init

    # ДОБАВЛЯЕМ ПАТЧ ДЛЯ BOXPLOT
    def patched_boxplot(self, *args, **kwargs):
        """Патч для boxplot с автоматической установкой форматтеров."""
        result = _ORIGINAL_METHODS["Axes.boxplot"](self, *args, **kwargs)

        # Обновляем форматтеры после создания boxplot
        self.xaxis.set_major_formatter(CommaDecimalScalarFormatter())
        self.yaxis.set_major_formatter(CommaDecimalScalarFormatter())

        # Обновляем уже созданные подписи
        for axis in [self.xaxis, self.yaxis]:
            labels = axis.get_ticklabels()
            for label in labels:
                text = label.get_text()
                if "." in text:
                    label.set_text(text.replace(".", ","))

        return result

    mpl.axes.Axes.boxplot = patched_boxplot

    # ДОБАВЛЯЕМ ПАТЧ ДЛЯ SEABORN HEATMAP ЕСЛИ SEABORN ЕСТЬ
    def patched_heatmap(*args, **kwargs):
        """Патч для seaborn heatmap с автоматической установкой форматтеров."""
        # Вызываем оригинальный heatmap
        result = _ORIGINAL_METHODS["seaborn.heatmap"](*args, **kwargs)
        # Получаем текущие оси
        ax = plt.gca()

        # ОСОБЕННО ВАЖНО: обрабатываем аннотации (annot=True)
        if kwargs.get("annot", False):
            # Получаем текстовые аннотации
            for text_obj in ax.texts:
                text = text_obj.get_text()
                # Заменяем точки на запятые в аннотациях
                if "." in text:
                    try:
                        # Пробуем преобразовать в число и обратно с запятой
                        num = float(text)
                        # Форматируем с нужным количеством знаков после запятой
                        # Определяем количество знаков после запятой из оригинального текста
                        if "." in text:
                            decimal_places = len(text.split(".")[1])
                            new_text = f"{num:.{decimal_places}f}".replace(".", ",")
                            text_obj.set_text(new_text)
                    except ValueError:
                        # Если не число, просто заменяем точки
                        text_obj.set_text(text.replace(".", ","))

        return result

    # Заменяем оригинальную функцию
    sns.heatmap = patched_heatmap
    logger.info("Патч применен для seaborn heatmap")

    _IS_PATCHED = True
    logger.info("Глобальный патч с запятыми в качестве десятичного разделителя ПРИМЕНЕН")
    logger.info("Все новые графики будут использовать запятые вместо точек для десятичных дробей")
    logger.info("Поддерживаемые графики: line, scatter, hist, boxplot, heatmap, colorbar")


def restore_global_comma_patch() -> None:
    """Восстанавливает оригинальное поведение matplotlib (точки как десятичные разделители)."""
    global _IS_PATCHED  # noqa: PLW0603

    if not _IS_PATCHED:
        logger.info("Патч с запятыми в настоящее время не применен.")
        return

    # Восстанавливаем все классы форматтеров
    ticker.ScalarFormatter = _ORIGINAL_CLASSES["ScalarFormatter"]
    ticker.LogFormatter = _ORIGINAL_CLASSES["LogFormatter"]
    ticker.LogFormatterExponent = _ORIGINAL_CLASSES["LogFormatterExponent"]
    ticker.LogFormatterMathtext = _ORIGINAL_CLASSES["LogFormatterMathtext"]
    ticker.FuncFormatter = _ORIGINAL_CLASSES["FuncFormatter"]
    ticker.StrMethodFormatter = _ORIGINAL_CLASSES["StrMethodFormatter"]

    # Восстанавливаем класс Axis
    mpl.axis.Axis = _ORIGINAL_CLASSES["Axis"]

    # Восстанавливаем оригинальные методы
    if "Axis.__init__" in _ORIGINAL_METHODS:
        mpl.axis.Axis.__init__ = _ORIGINAL_METHODS["Axis.__init__"]

    if "Axes.__init__" in _ORIGINAL_METHODS:
        mpl.axes.Axes.__init__ = _ORIGINAL_METHODS["Axes.__init__"]

    if "Colorbar.__init__" in _ORIGINAL_METHODS:
        mpl.colorbar.Colorbar.__init__ = _ORIGINAL_METHODS["Colorbar.__init__"]

    # ВОССТАНАВЛИВАЕМ МЕТОДЫ ГРАФИКОВ
    if "Axes.boxplot" in _ORIGINAL_METHODS:
        mpl.axes.Axes.boxplot = _ORIGINAL_METHODS["Axes.boxplot"]

    if "Axes.hist" in _ORIGINAL_METHODS:
        mpl.axes.Axes.hist = _ORIGINAL_METHODS["Axes.hist"]

    if "Axes.scatter" in _ORIGINAL_METHODS:
        mpl.axes.Axes.scatter = _ORIGINAL_METHODS["Axes.scatter"]

    if "Axes.plot" in _ORIGINAL_METHODS:
        mpl.axes.Axes.plot = _ORIGINAL_METHODS["Axes.plot"]

    # ВОССТАНАВЛИВАЕМ SEABORN ЕСЛИ ОН БЫЛ ПАТЧЕН
    if "seaborn.heatmap" in _ORIGINAL_METHODS:
        sns.heatmap = _ORIGINAL_METHODS["seaborn.heatmap"]
        logger.info("Восстановлен оригинальный seaborn.heatmap")
    # Также можно восстановить другие seaborn функции если они были патчены
    if "seaborn.barplot" in _ORIGINAL_METHODS:
        sns.barplot = _ORIGINAL_METHODS["seaborn.barplot"]
    if "seaborn.lineplot" in _ORIGINAL_METHODS:
        sns.lineplot = _ORIGINAL_METHODS["seaborn.lineplot"]

    # Закрываем существующие графики для гарантии, что новые используют восстановленные форматтеры
    plt.close("all")

    _IS_PATCHED = False
    logger.info("Глобальный патч с запятыми ВОССТАНОВЛЕН")
    logger.info("Все новые графики будут использовать точки вместо запятых для десятичных дробей")


def is_patched() -> bool:
    """Проверяет, применен ли патч с запятыми."""
    return _IS_PATCHED
