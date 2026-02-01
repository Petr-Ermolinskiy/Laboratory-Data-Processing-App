"""Автогенерация Markdown + HTML документации UI."""

import base64
import json
import os
import re
import sys
import unicodedata
from contextlib import contextmanager
from pathlib import Path

from loguru import logger

sys.path.insert(0, str(Path(__file__).parent.parent))

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
)

from app.ui.ui_main import Ui_MainWindow

# ~~~~~ выставляем путь на 2 папки выше ~~~~~ #
os.chdir(str(Path(__file__).parent.parent))

# чтения json файла -- версия приложения
with open("config.json") as f:
    data = json.load(f)
    version_app = data["version"]

# ~~~~~ выставляем путь на 1 папку выше ~~~~~ #
os.chdir(str(Path(__file__).parent))

# чтения json файла -- доп. комментарий к скриншотам
with open("describe_tabs.json") as f:
    describe_tabs_dict = json.load(f)

# --------- ПУТИ ДЛЯ СОХРАНЕНИЯ ----------- #
OUTPUT_DIR = "files"
FIGS_DIR = os.path.join(OUTPUT_DIR, "figs")
os.makedirs(FIGS_DIR, exist_ok=True)

# ----------------------------------------------- #
logger.remove()

try:
    logger.add(
        sys.stderr, format="<green>{time:HH:mm:ss}</green> | {level} | {message}", level="INFO"
    )
except Exception as e:
    logger.info(f"Нельзя импортировать: {e}")
# ----------------------------------------------- #


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """Окно приложения."""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label_version.setText(version_app)


# ── helper functions ──────────────────────────────────
def clean_anchor(text: str) -> str:
    """Сделать безопасный якорь для MD/HTML."""
    text = text.lower()
    text = re.sub(r"[^\w\- ]+", "", text)  # буквы, цифры, дефисы, пробел
    text = text.replace(" ", "-")
    return re.sub(r"-+", "-", text)  # двойные дефисы → один


def safe_filename(text: str) -> str:
    """Сделать безопасное имя файла ASCII-only для скриншота."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^\w\d_\-.]", "_", text)


def image_to_base64(image_path: str) -> str:
    """Конвертировать изображение в base64 строку."""
    with open(image_path, "rb") as img_file:
        # Определяем тип файла по расширению
        ext = os.path.splitext(image_path)[1].lower()
        if ext == ".png":
            mime_type = "image/png"
        elif ext in [".jpg", ".jpeg"]:
            mime_type = "image/jpeg"
        elif ext == ".gif":
            mime_type = "image/gif"
        elif ext == ".bmp":
            mime_type = "image/bmp"
        else:
            mime_type = "image/png"  # по умолчанию

        encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
        return f"data:{mime_type};base64,{encoded_string}"


@contextmanager
def auto_expand_scrollable_widget(widget: QWidget, level: int):
    """Контекстный менеджер для автоматического расширения виджета со скроллом."""
    window = widget.window()
    original_window_size = window.size()
    original_max_size = window.maximumSize()
    original_pos = window.pos()

    # Проверяем, есть ли скролл
    has_scroll = False
    scroll_areas = widget.findChildren(QAbstractScrollArea)

    for scroll_area in scroll_areas:
        if scroll_area.isVisible():
            v_scroll = scroll_area.verticalScrollBar()
            h_scroll = scroll_area.horizontalScrollBar()
            if (v_scroll.isVisible() and v_scroll.maximum() > 0) or (
                h_scroll.isVisible() and h_scroll.maximum() > 0
            ):
                has_scroll = True
                break

    if has_scroll or level <= 2:  # Для корневых табов всегда расширяем
        try:
            window.setMaximumSize(16777215, 16777215)

            if level <= 2:
                screen_size = QApplication.primaryScreen().availableGeometry().size()
                new_width = min(screen_size.width() * 0.9, window.width() * 2)
                new_height = min(screen_size.height() * 0.9, window.height() * 2)
                window.resize(int(new_width), int(new_height))

                window.move(
                    int((screen_size.width() - new_width) / 2),
                    int((screen_size.height() - new_height) / 2),
                )
            else:
                window.resize(int(window.width() * 1.5), int(window.height() * 1.5))

            widget.updateGeometry()
            window.updateGeometry()
            QApplication.processEvents()
            QTimer.singleShot(300, lambda: None)
            QApplication.processEvents()
            QTimer.singleShot(100, lambda: None)
            QApplication.processEvents()

            yield widget
        finally:
            window.setMaximumSize(original_max_size)
            window.resize(original_window_size)
            window.move(original_pos)
            QApplication.processEvents()
            QTimer.singleShot(100, lambda: None)
            QApplication.processEvents()
    else:
        yield widget


def ensure_widget_visible(widget: QWidget, tab_widget: QTabWidget):
    """Убедиться, что виджет видим и таб активирован."""
    parent = widget.parent()
    while parent and parent != tab_widget.currentWidget():
        if isinstance(parent, QTabWidget):
            for i in range(parent.count()):
                if parent.widget(i) == widget or widget in parent.widget(i).findChildren(QWidget):
                    parent.setCurrentIndex(i)
                    QApplication.processEvents()
                    QTimer.singleShot(50, lambda: None)
                    QApplication.processEvents()
                    break
        parent = parent.parent()


def build_toc_hierarchy(toc_items):
    """Построение иерархической структуры TOC с простой нумерацией."""
    if not toc_items:
        return [], {}

    # Создаем простую структуру для нумерации
    section_number_map = {}

    # Глобальный счетчик для всех уровней
    current_number = [0] * 10  # Предполагаем максимальную глубину 10 уровней

    for level, title, sec_id in toc_items:
        # Увеличиваем счетчик для текущего уровня
        current_number[level] += 1

        # Сбрасываем все дочерние уровни
        for lvl in range(level + 1, len(current_number)):
            current_number[lvl] = 0

        # Формируем номер раздела (только ненулевые уровни)
        parts = []
        for lvl in range(level + 1):
            if current_number[lvl] > 0:
                parts.append(str(current_number[lvl]))

        number = ".".join(parts)

        # Сохраняем в мапу
        section_number_map[sec_id] = {
            "numbered_title": f"{number}. {title}",
            "number": number,
            "level": level,
            "title": title,
        }

    # Создаем плоский список для TOC
    toc_list = []
    for sec_id, info in section_number_map.items():
        toc_list.append((info["level"], info["numbered_title"], sec_id))

    # Сортируем по номеру
    toc_list.sort(
        key=lambda x: tuple(map(int, section_number_map[x[2]]["number"].split(".")))
        if section_number_map[x[2]]["number"]
        else (0,)
    )

    return toc_list, section_number_map


def document_tab(
    tab_widget,
    content_md,
    content_html,
    toc_items,
    level,
    counter,
    visited,
    parent_path: str = "",
) -> None:
    """Рекурсивная документация табов."""
    if tab_widget in visited:
        return
    visited.add(tab_widget)

    for i in range(tab_widget.count()):
        tab_widget.setCurrentIndex(i)
        QApplication.processEvents()
        QTimer.singleShot(150, lambda: None)
        QApplication.processEvents()

        title = tab_widget.tabText(i)
        page = tab_widget.widget(i)

        # Создаем уникальный идентификатор
        sec_id = clean_anchor(f"{level}-{title}-{i}")

        # Добавляем в структуру для TOC
        toc_items.append((level, title, sec_id))

        # Сохраняем информацию о заголовке
        content_md.append(f"HEADER_PLACEHOLDER:{level}:{sec_id}:{title}\n")
        content_html.append(f"HEADER_PLACEHOLDER:{level}:{sec_id}:{title}\n")

        # ── screenshot (только текущий tab) ─────
        img_name = safe_filename(f"tab_L{level}_I{i}_{title}.png")
        img_path = os.path.join(FIGS_DIR, img_name)

        # Используем контекстный менеджер для расширения скроллируемых виджетов
        with auto_expand_scrollable_widget(page, level):
            QApplication.processEvents()
            QTimer.singleShot(200, lambda: None)
            QApplication.processEvents()

            pixmap = page.grab()
            annotated = pixmap.copy()

            painter = QPainter(annotated)
            pen = QPen(QColor("red"))
            pen.setWidth(2)
            painter.setPen(pen)

            widgets = [
                w
                for w in page.findChildren(QWidget)
                if w.isVisible() and w.whatsThis() and w.objectName()
            ]

            for w in widgets:
                counter["value"] += 1
                idx = counter["value"]

                ensure_widget_visible(w, tab_widget)

                pos = w.mapTo(page, w.rect().center())
                x, y = pos.x(), pos.y()

                if 0 <= x < pixmap.width() and 0 <= y < pixmap.height():
                    painter.drawEllipse(x - 6, y - 6, 12, 12)

                    # белый фон
                    text = str(idx)
                    font_metrics = painter.fontMetrics()
                    text_width = font_metrics.horizontalAdvance(text)
                    text_height = font_metrics.height()

                    # нарисуем фон под номером
                    painter.fillRect(
                        x + 8 - 1,
                        y + 4 - text_height + 2,
                        text_width + 2,
                        text_height,
                        QColor(255, 255, 255, 190),
                    )

                    painter.drawText(x + 8, y + 4, str(idx))

            painter.end()
            annotated.save(img_path)

        # Сохраняем информацию для изображений
        content_md.append(f"IMG_PLACEHOLDER:{sec_id}:{img_name}:{title}\n")
        # Для HTML сохраняем полный путь к изображению для конвертации в base64
        content_html.append(f"IMG_PLACEHOLDER:{sec_id}:{img_path}:{img_name}:{title}\n")

        # ── widget docs ──────────────────────────
        start = counter["value"] - len(widgets) + 1
        for idx, w in enumerate(widgets, start=start):
            wid = f"w{idx}"

            # HTML разметка вместо Markdown
            content_md.append(f'<a id="{wid}"></a>\n')
            content_md.append(f"<b>{idx}. {w.objectName()}</b> ({w.__class__.__name__})<br>\n")
            content_md.append(f"{w.whatsThis()}<br><br>\n\n")

            content_html.append(
                f'<p id="{wid}"><b>{idx}. {w.objectName()}</b> '
                f"({w.__class__.__name__})<br>{w.whatsThis()}</p>\n"
            )

        # ── nested tabs ──────────────────────────
        for nested in page.findChildren(QTabWidget, options=Qt.FindDirectChildrenOnly):
            document_tab(
                nested,
                content_md,
                content_html,
                toc_items,
                level + 1,
                counter,
                visited,
                f"{parent_path}-{title}",
            )


def generate() -> None:
    window = MainWindow()
    window.show()
    window.raise_()
    window.activateWindow()

    QApplication.processEvents()
    QTimer.singleShot(500, lambda: None)
    QApplication.processEvents()

    # Инициализируем структуры
    md = [f"# Документация приложения Lab App {version_app}\n\n", "## Содержание\n\n"]
    html = [
        "<html><head><meta charset='utf-8'>\n"
        f"<title>Документация приложения Lab App {version_app} </title>\n"
        "<style>\n"
        "  body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 1200px; margin: 0 auto; padding: 20px; }\n"
        "  .toc { background-color: #f5f5f5; padding: 15px 20px; border-radius: 5px; margin-bottom: 30px; }\n"
        "  .toc ul { list-style-type: none; padding-left: 20px; margin: 5px 0; }\n"
        "  .toc > ul { padding-left: 0; }\n"
        "  .toc li { margin: 8px 0; }\n"
        "  .toc a { text-decoration: none; color: #0066cc; }\n"
        "  .toc a:hover { text-decoration: underline; }\n"
        "  .toc .level-1 { margin-left: 0px; }\n"
        "  .toc .level-2 { margin-left: 20px; }\n"
        "  .toc .level-3 { margin-left: 40px; }\n"
        "  .toc .level-4 { margin-left: 60px; }\n"
        "  .toc .level-5 { margin-left: 80px; }\n"
        "  .toc .level-6 { margin-left: 100px; }\n"
        "  img { border: 1px solid #ddd; border-radius: 4px; padding: 5px; margin: 15px 0; }\n"
        "  hr { margin: 30px 0; border: none; border-top: 2px solid #eee; }\n"
        "  h1, h2, h3, h4, h5 { color: #333; margin-top: 30px; }\n"
        "  h2:before, h3:before, h4:before, h5:before { color: #666; margin-right: 10px; }\n"
        "  p { margin: 10px 0; }\n"
        "  b, strong { font-weight: bold; }\n"
        "  .numbered-header { display: flex; align-items: baseline; margin: 20px 0 10px 0; }\n"
        "  .header-number { color: #666; margin-right: 10px; font-weight: bold; font-size: 1.2em; }\n"
        "  .header-text { flex: 1; }\n"
        "  .header-text h1, .header-text h2, .header-text h3, .header-text h4, .header-text h5 {\n"
        "    margin: 0;\n"
        "    display: inline;\n"
        "  }\n"
        "  .figure-caption { font-style: italic; color: #666; margin-top: 5px; margin-bottom: 20px; }\n"
        "  .widget-doc { margin: 15px 0; padding: 10px; background-color: #f9f9f9; border-left: 3px solid #0066cc; }\n"
        "</style>\n"
        "</head><body>\n"
        f"<h1>Документация приложения Lab App {version_app}</h1>\n"
        "<h2>Содержание</h2>\n"
    ]

    # Собираем структуру для TOC и контент
    toc_items = []
    visited = set()
    counter = {"value": 0}
    content_md = []
    content_html = []

    # Находим корневые табы
    root_tabs = window.centralWidget().findChildren(QTabWidget, options=Qt.FindDirectChildrenOnly)

    # Определяем начальный уровень
    if hasattr(window.centralWidget(), "count"):
        start_level = 1
        document_tab(
            window.centralWidget(),
            content_md,
            content_html,
            toc_items,
            start_level,
            counter,
            visited,
        )
    else:
        start_level = 1
        for tab in root_tabs:
            document_tab(tab, content_md, content_html, toc_items, start_level, counter, visited)

    # Строим иерархическую структуру TOC с нумерацией
    toc_list, section_number_map = build_toc_hierarchy(toc_items)

    # Генерируем Markdown TOC
    md_toc_lines = []
    for level, numbered_title, sec_id in toc_list:
        indent = "  " * (level - 1)
        md_toc_lines.append(f"{indent}- [{numbered_title}](#{sec_id})\n")

    # Добавляем TOC в Markdown
    md.extend(md_toc_lines)
    md.append("\n---\n\n")

    # Генерируем HTML TOC с отступами
    html.append('<div class="toc">\n')
    html.append("<ul>\n")

    # Группируем элементы по уровням для создания вложенных списков
    def generate_nested_html(toc_items, start_idx, current_level) -> tuple:
        """Рекурсивно генерирует вложенные списки HTML."""
        lines = []
        i = start_idx

        while i < len(toc_items):
            level, numbered_title, sec_id = toc_items[i]

            if level < current_level:
                # Вернулись на более высокий уровень
                break
            if level == current_level:
                # Текущий уровень
                lines.append(f'<li class="level-{level}">\n')
                lines.append(f'  <a href="#{sec_id}">{numbered_title}</a>\n')

                # Проверяем есть ли дочерние элементы
                has_children = False
                for j in range(i + 1, len(toc_items)):
                    if toc_items[j][0] == level + 1:
                        has_children = True
                        break
                    if toc_items[j][0] <= level:
                        break

                if has_children:
                    lines.append("  <ul>\n")
                    child_lines, next_idx = generate_nested_html(toc_items, i + 1, level + 1)
                    lines.extend(child_lines)
                    lines.append("  </ul>\n")
                    i = next_idx
                else:
                    i += 1

                lines.append("</li>\n")
            else:
                i += 1

        return lines, i

    # Генерируем вложенную HTML структуру
    html_lines, _ = generate_nested_html(toc_list, 0, 1)
    html.extend(html_lines)

    html.append("</ul>\n")
    html.append("</div>\n")
    html.append("<hr>\n")

    # Обрабатываем сохраненный контент и добавляем номера разделов
    processed_md = []
    processed_html = []

    for line in content_md:
        if line.startswith("HEADER_PLACEHOLDER:"):
            # Разбираем информацию о заголовке
            parts = line.strip().split(":")
            original_level = int(parts[1])
            sec_id = parts[2]
            title = parts[3]

            # Получаем пронумерованный заголовок из карты
            if sec_id in section_number_map:
                numbered_info = section_number_map[sec_id]
                number = numbered_info["number"]
                numbered_title = numbered_info["numbered_title"]
                header_title = numbered_info["title"]

                # Определяем уровень заголовка для Markdown
                # Для первого уровня (вкладки верхнего уровня) используем ##
                if original_level == 1:
                    md_level = 2  # ##
                    html_level = 2  # h2
                else:
                    md_level = min(original_level + 1, 6)
                    html_level = min(original_level + 1, 6)
            else:
                number = ""
                numbered_title = title
                header_title = title
                if original_level == 1:
                    md_level = 2
                    html_level = 2
                else:
                    md_level = min(original_level + 1, 6)
                    html_level = min(original_level + 1, 6)

            # Добавляем заголовок с номером в Markdown
            md_prefix = "#" * md_level
            processed_md.append(f"{md_prefix} {numbered_title}\n\n")

        elif line.startswith("IMG_PLACEHOLDER:"):
            # Разбираем информацию об изображении
            parts = line.strip().split(":")
            sec_id = parts[1]
            img_name = parts[2]
            title = parts[3]

            logger.info(f"{title}")

            # Получаем номер раздела для подписи
            number = section_number_map[sec_id]["number"] if sec_id in section_number_map else ""

            # Добавляем изображение в Markdown
            if number:
                processed_md.append(f"![{title}](figs/{img_name})\n")
                processed_md.append(
                    f"*Скриншот {number}: вкладка — {title}*. {describe_tabs_dict.get(title, '')}\n\n"
                )
            else:
                processed_md.append(f"![{title}](figs/{img_name})\n")
                processed_md.append(f"*{title}*\n\n")

        else:
            # Обычный контент (описание виджетов)
            processed_md.append(line)

    # Обрабатываем HTML контент отдельно для изображений
    for line in content_html:
        if line.startswith("HEADER_PLACEHOLDER:"):
            # Разбираем информацию о заголовке (уже обработано выше)
            parts = line.strip().split(":")
            original_level = int(parts[1])
            sec_id = parts[2]
            title = parts[3]

            # Получаем пронумерованный заголовок из карты
            if sec_id in section_number_map:
                numbered_info = section_number_map[sec_id]
                number = numbered_info["number"]
                header_title = numbered_info["title"]
            else:
                number = ""
                header_title = title

            # Определяем уровень заголовка для HTML
            html_level = 2 if original_level == 1 else min(original_level + 1, 6)

            # Добавляем заголовок с номером в HTML
            if number:
                processed_html.append('<div class="numbered-header">\n')
                processed_html.append(f'  <span class="header-number">{number}.</span>\n')
                processed_html.append(
                    f'  <span class="header-text"><h{html_level} id="{sec_id}">{header_title}</h{html_level}></span>\n'
                )
                processed_html.append("</div>\n")
            else:
                processed_html.append(
                    f'<h{html_level} id="{sec_id}">{header_title}</h{html_level}>\n'
                )

        elif line.startswith("IMG_PLACEHOLDER:"):
            # Разбираем информацию об изображении для HTML
            parts = line.strip().split(":")
            sec_id = parts[1]
            img_path = parts[2]  # Полный путь к изображению
            img_name = parts[3]
            title = parts[4]

            # Конвертируем изображение в base64
            try:
                base64_data = image_to_base64(img_path)

                # Получаем номер раздела для подписи
                number = (
                    section_number_map[sec_id]["number"] if sec_id in section_number_map else ""
                )

                # Добавляем изображение в HTML с встроенным base64
                processed_html.append('<div style="margin: 20px 0;">\n')
                processed_html.append(
                    f'  <img src="{base64_data}" alt="{title}" style="max-width: 60%; border: 1px solid #ddd; border-radius: 4px; padding: 5px;">\n'
                )
                if number:
                    processed_html.append(
                        f'  <p class="figure-caption">Скриншот {number}: вкладка — {title}. {describe_tabs_dict.get(title, "")}</p>\n'
                    )
                else:
                    processed_html.append(f'  <p class="figure-caption">{title}</p>\n')
                processed_html.append("</div>\n")

                logger.info(f"✅ Изображение встроено в HTML: {img_name}")
            except Exception as e:
                logger.warning(f"⚠️ Ошибка при встраивании изображения {img_name}: {e}")
                # Если не удалось встроить, добавляем обычную ссылку
                processed_html.append(f"<!-- Ошибка при встраивании изображения {img_name} -->\n")
                if number:
                    processed_html.append(
                        f'  <p class="figure-caption">Скриншот {number}: вкладка — {title} (изображение отсутствует)</p>\n'
                    )

        else:
            # Обычный контент (описание виджетов)
            processed_html.append(line)

    # Добавляем обработанный контент
    md.extend(processed_md)
    html.extend(processed_html)

    # Завершаем HTML
    html.append("</body></html>")

    # Записываем MD файл
    md_filename = os.path.join(OUTPUT_DIR, f"Документация_Lab_App_{version_app}.md")
    with open(md_filename, "w", encoding="utf-8") as f:
        f.writelines(md)

    # Записываем автономный HTML файл
    html_filename = os.path.join(OUTPUT_DIR, f"Документация_Lab_App_{version_app}.html")
    with open(html_filename, "w", encoding="utf-8") as f:
        f.writelines(html)

    logger.info("Документация приложения Lab App сгенерирована:")
    logger.info(f"   - Markdown: {md_filename}")
    logger.info(f"   - HTML (автономный): {html_filename}")

    # Отладочная информация
    logger.info("Нумерация разделов:")
    for _, info in sorted(
        section_number_map.items(),
        key=lambda x: tuple(map(int, x[1]["number"].split("."))) if x[1]["number"] else (0,),
    ):
        logger.info(f"  {info['number']}: {info['title']}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QTimer.singleShot(800, generate)
    sys.exit(app.exec())
