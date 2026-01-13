"""Скрипт сборки для замены Makefile."""  # noqa: INP001

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys

from loguru import logger

# ----------------------------------------------- #
logger.remove()

try:
    logger.add(
        sys.stderr, format="<green>{time:HH:mm:ss}</green> | {level} | {message}", level="INFO"
    )
except Exception as e:
    print(f"Нельзя импортировать: {e}")
# ----------------------------------------------- #


def run_command(command: str, description: str | None = None, *, shell: bool = True) -> bool:
    """Выполнить shell-команду с обработкой ошибок."""
    if description:
        logger.info(f"Выполнение: {description}...")
        logger.info(f"Команда: {command}")

    try:
        result = subprocess.run(  # noqa: S603
            command, shell=shell, check=True, capture_output=True, text=True, encoding="utf-8"
        )
        if result.stdout:
            logger.info(result.stdout)
    except subprocess.CalledProcessError as e:
        logger.warning(f"❌ Ошибка выполнения команды: {command}")
        logger.warning(f"   Ошибка: {e.stderr if e.stderr else str(e)}")
        return False
    except Exception as e:
        logger.warning(f"❌ Неожиданная ошибка: {e!s}")
        return False
    return True


def check_dependencies() -> None:
    """Проверить установлены ли необходимые инструменты."""
    logger.info("🔍 Проверка зависимостей...")

    dependencies = [
        ("python", "--version"),
        ("pyinstaller", "--version"),
        ("pytest", "--version"),
    ]

    for dep, version_arg in dependencies:
        try:
            subprocess.run([dep, version_arg], capture_output=True, check=True)  # noqa: S603
            logger.info(f"   ✅ {dep} установлен")
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.warning(f"   ❌ {dep} не установлен или нет в PATH")
            if dep == "pytest":
                logger.warning("      Установить: pip install pytest")
            elif dep == "pyinstaller":
                logger.warning("      Установить: pip install pyinstaller")


def run_tests() -> bool:
    """Запустить pytest тесты."""
    logger.info("--- ЗАПУСК ТЕСТОВ ---")

    if not run_command("pytest -s", "Запуск тестов"):
        logger.info("⚠️  Пробуем альтернативный подход...")
        return run_command("python -m pytest -s", "Запуск тестов через python -m")
    return True


def command_for_build_windows(config: dict) -> list:
    """Команда для сборки -- Windows."""
    app_name = config["APP_NAME"] + "_" + config["version"] + "_win"
    return [
        "pyinstaller",
        "--windowed",
        f"--add-data={config['VERSION_JSON']};.",
        f"--add-data={config['ICON_PATH']};app/style",
        f"--add-data={config['STYLE_QSS']};app/style/",
        f"--name={app_name}",
        f"--icon={config['ICON_PATH']}",
        f"--upx-dir={config['UPX_DIR']}",
        config["MAIN_SCRIPT"],
    ]


def command_for_build_mac(config: dict) -> list:
    """Команда для сборки -- Mac."""
    app_name = config["APP_NAME"] + "_" + config["version"] + "_mac"
    return [
        "pyinstaller",
        "--windowed",
        f"--add-data={config['VERSION_JSON']}:.",
        f"--add-data={config['ICON_PATH_MAC']}:app/style",
        f"--add-data={config['STYLE_QSS']}:app/style",
        f"--name={app_name}",
        f"--icon={config['ICON_PATH_MAC']}",
        config["MAIN_SCRIPT"],
    ]


def build_app(config: dict) -> bool:
    """Собрать приложение с помощью PyInstaller."""
    logger.info("--- СБОРКА ПРИЛОЖЕНИЯ ---")

    # Сформировать команду pyinstaller
    if platform.system() == "Windows":
        cmd = command_for_build_windows(config)
    else:
        cmd = command_for_build_mac(config)

    # Преобразовать список в строку для выполнения в shell
    cmd_str = " ".join(cmd)

    return run_command(cmd_str, "Сборка с PyInstaller")


def clean_build(config: dict) -> None:
    """Очистить артефакты сборки."""
    logger.info("--- ОЧИСТКА ---")

    folders_to_remove = ["build", "dist", "__pycache__"]
    files_to_remove = [f"{config['APP_NAME']}.spec"]

    for folder in folders_to_remove:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"Удалена папка: {folder}")
            except Exception as e:
                print(f"Ошибка удаления {folder}: {e}")

    for file in files_to_remove:
        if os.path.exists(file):
            try:
                os.remove(file)
                logger.info(f"Удален файл: {file}")
            except Exception as e:
                logger.error(f"Ошибка удаления {file}: {e}")


def main() -> None:
    """Главная функция."""
    with open("config.json") as f:
        config = json.load(f)

    parser = argparse.ArgumentParser(description="Скрипт сборки для Lab_App")
    parser.add_argument(
        "action",
        nargs="?",
        choices=["test", "build", "all", "clean", "check"],
        default="all",
        help="Действие для выполнения (по умолчанию: all)",
    )

    args = parser.parse_args()

    logger.info("~~~ Python Скрипт Сборки ~~~")

    # Сначала надо проверить зависимости
    check_dependencies()

    success = True

    if args.action == "test":
        success = run_tests()

    elif args.action == "build":
        success = build_app(config)

    elif args.action == "all":
        success = run_tests() and build_app(config)

    elif args.action == "clean":
        clean_build(config)

    elif args.action == "check":
        # Просто проверить зависимости, уже сделано выше
        pass

    if success:
        logger.info("✅ Операции завершены успешно!")
    else:
        logger.error("❌ Операция завершилась ошибкой!")


if __name__ == "__main__":
    # на директорию выше
    # -- при запуске скрипта не из терминала из папки файла добавить >>> os.chdir("..")
    logger.info(f"Дирректория: {os.getcwd()}")  # noqa: PTH109
    main()
