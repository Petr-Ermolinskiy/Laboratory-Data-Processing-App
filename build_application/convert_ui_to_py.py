"""Скрипт для компиляции UI PySide6 и проверок Ruff."""  # noqa: INP001

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


def run_command(
    command: str,
    description: str | None = None,
    *,
    shell: bool = True,
    show_warnings: bool = True,
) -> bool:
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
        if show_warnings:
            logger.warning(f"❌ Ошибка выполнения команды: {command}")
            logger.warning(f"   Ошибка: {e.stderr if e.stderr else str(e)}")
            return False
    except Exception as e:
        if show_warnings:
            logger.warning(f"❌ Неожиданная ошибка: {e!s}")
            return False
    return True


def main() -> int:
    """Главная функция для выполнения всех команд."""
    commands = [
        {
            "command": "pyside6-uic app/ui/ui_main.ui -o app/ui/ui_main.py",
            "description": "Компиляция UI файла в Python код",
            "check_errors": True,
        },
        {
            "command": "ruff check .",
            "description": "Проверка кода с помощью Ruff linter",
            "check_errors": False,
        },
        {
            "command": "ruff format .",
            "description": "Форматирование кода с помощью Ruff formatter",
            "check_errors": False,
        },
    ]

    logger.info("🚀 Начало выполнения команд")
    logger.info("=" * 50)

    all_success = True

    for cmd_info in commands:
        success = run_command(
            command=cmd_info["command"],
            description=cmd_info["description"],
            show_warnings=cmd_info["check_errors"],
        )

        if not success and cmd_info["check_errors"]:
            all_success = False
            logger.warning(f"Команда завершилась с ошибкой: {cmd_info['command']}")

        logger.info("-" * 50)

    if all_success:
        logger.info("✅ Все команды выполнены успешно!")
        return 0
    logger.error("❌ Некоторые команды завершились с ошибками")
    return 1


if __name__ == "__main__":
    main()
