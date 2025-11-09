"""Скрипт сборки для замены Makefile."""

import argparse
import json
import os
import shutil
import subprocess


def run_command(command: str, description: str | None = None, *, shell: bool = True) -> bool:
    """Выполнить shell-команду с обработкой ошибок."""
    if description:
        print(f"Выполнение: {description}...")
        print(f"Команда: {command}")

    try:
        result = subprocess.run(
            command, shell=shell, check=True, capture_output=True, text=True, encoding="utf-8"
        )  # noqa: S603
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка выполнения команды: {command}")
        print(f"   Ошибка: {e.stderr if e.stderr else str(e)}")
        return False
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e!s}")
        return False
    return True


def check_dependencies() -> None:
    """Проверить установлены ли необходимые инструменты."""
    print("🔍 Проверка зависимостей...")

    dependencies = [
        ("python", "--version"),
        ("pyinstaller", "--version"),
        ("pytest", "--version"),
    ]

    for dep, version_arg in dependencies:
        try:
            subprocess.run([dep, version_arg], capture_output=True, check=True)  # noqa: S603
            print(f"   ✅ {dep} установлен")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"   ❌ {dep} не установлен или нет в PATH")
            if dep == "pytest":
                print("      Установить: pip install pytest")
            elif dep == "pyinstaller":
                print("      Установить: pip install pyinstaller")


def run_tests() -> bool:
    """Запустить pytest тесты."""
    print("\n" + "=" * 50)
    print("--- ЗАПУСК ТЕСТОВ ---")
    print("=" * 50)

    if not run_command("pytest -s", "Запуск тестов"):
        print("⚠️  Пробуем альтернативный подход...")
        return run_command("python -m pytest -s", "Запуск тестов через python -m")
    return True


def build_app(config: dict) -> bool:
    """Собрать приложение с помощью PyInstaller."""
    print("\n" + "=" * 50)
    print("--- СБОРКА ПРИЛОЖЕНИЯ ---")
    print("=" * 50)

    app_name = config["APP_NAME"] + "_" + config["version"]

    # Сформировать команду pyinstaller
    cmd = [
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

    # Преобразовать список в строку для выполнения в shell
    cmd_str = " ".join(cmd)

    return run_command(cmd_str, "Сборка с PyInstaller")


def clean_build(config: dict) -> None:
    """Очистить артефакты сборки."""
    print("\n" + "=" * 50)
    print("--- ОЧИСТКА ---")
    print("=" * 50)

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
                print(f"Удален файл: {file}")
            except Exception as e:
                print(f"Ошибка удаления {file}: {e}")


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

    print("~~~ Python Скрипт Сборки ~~~")
    print("=" * 50)

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

    print("\n" + "=" * 50)
    if success:
        print("✅ Операции завершены успешно!")
    else:
        print("❌ Операция завершилась ошибкой!")


if __name__ == "__main__":
    # на директорию выше
    os.chdir("..")

    main()
