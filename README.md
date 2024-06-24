# Среда для обработки экспериментальных данных лаборатории **Биомедицинской фотоники** МГУ имени М.В. Ломоносова

В этом репозитории представлен код приложения на Python для построения графиков и обработки экспериментальных данных, полученных на приборе RheoScan, Биоле и лазерном пинцете.

## Использование
Последнюю версию программы можно скачать в разделе `Releases`. Подробные инструкции использования программы доступны на яндекс диске лаборатории.

## Ручная установка

Если вы используете **git**, вы можете клонировать проект, используя Python 3.11.6 (тестировалась только эта версия) в [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/) или где-либо ещё:
```bash
git clone https://github.com/Petr-Ermolinskiy/OCT_B-Scan-processing_GUI.git
```
В противном случае вы можете загрузить файлы вручную. Затем вы можете открыть терминал или командную строку и перейти в папку, куда вы поместили файлы из этого репозитория. Можно использовать команду `cd your/path/to/the/directory`.

Выполните следующую команду для создания нового виртуального окружения с именем `venv` (убедитесь, что у вас установлен Python 3.11.5):

```bash
python3.11 -m venv venv
```

Активируйте виртуальное окружение (на Windows):
```bash
venv\Scripts\activate
```
На macOS или Linux:
```bash
source venv/bin/activate
```

Далее установите все необходимые библиотеки:

```bash
pip install -r requirements.txt
```
Запустите программу:
```bash
python main.py
```

## Создание _exe_ файла

Чтобы создать _exe_-файл в Windows, нужно выполнить следующую команду в терминале или командной строке:
```bash
pyinstaller --windowed --add-data "LOGO.ico;." --add-data "style_dark.qss;." --name='Lab_App_version' --icon=LOGO.ico main.py
```
Я настоятельно рекомендую вам использовать [UPX](https://upx.github.io/) для уменьшения размера исполняемого файла. В этом случае вы можете выполнить следующую команду:
```bash
pyinstaller --windowed --add-data "LOGO.ico;." --add-data "style_dark.qss;." --name='Lab_App_version' --icon=LOGO.ico --upx-dir Path\to\the\upx-4.2.2-win64 main.py
```

## Автор

Ермолинский Петр Борисович.