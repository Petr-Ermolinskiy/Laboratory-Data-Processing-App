# Приложение для обработки экспериментальных данных лаборатории **Биомедицинской фотоники** МГУ имени М.В. Ломоносова

В этом репозитории представлен код приложения на Python для построения графиков и обработки экспериментальных данных, полученных на приборе RheoScan, Биоле и лазерном пинцете.

## Использование
Последнюю версию программы можно скачать в разделе `Releases`. Подробные инструкции использования программы доступны на яндекс диске лаборатории.

## Ручная установка

Если вы используете **git**, вы можете клонировать проект в [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/) или где-либо ещё:
```bash
git clone https://github.com/Petr-Ermolinskiy/Laboratory-Data-Processing-App.git
```
И далее создать виртуальное окружение, используя Python 3.11.5 (тестировалась только эта версия).

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
scripts venv/bin/activate
```

Далее установите все необходимые библиотеки:

```bash
pip install -r requirements.txt
```

Запустите программу:
```bash
python main.py
```

NOTE: для обновления UI используйте команду в терминале:
```bash
pyside6-uic app/ui/ui_main.ui -o app/ui/ui_main.py
```

## Проблемы с установкой
- Если при установке библиотек не устанавливается pandas, то скорее всего это из-за отсутствия 
[Microsoft C++ Build Tools](https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/).
- Если всё ещё выдается ошибка, то надо провести установку последней версии pandas, и далее выполнить `pip install --no-deps -r requirements.txt`.

## Тесты

Для тестов используйте: 
```bash
python -m pytest -s tests/
```

## Создание исполняемого файла

Для создания _exe_ файла можно запустить скрипт [build_application/build.py](build_application/build.py) с изменением переменных в [config.json](config.json):

| Параметр в JSON | Описание                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------- |
| version         | версия приложения                                                                                  |
| UPX_DIR         | путь к [UPX](https://upx.github.io/), к примеру "C:/Users/petre/Desktop/Programes/upx-4.2.4-win64" |
| APP_NAME        | имя приложения -- "Lab_App"                                                                        |
| MAIN_SCRIPT     | входная точка приложения, т.е., "main.py"                                                          |
| ICON_PATH       | путь до иконки Windows -- "app/style/logo.ico"                         |
| ICON_PATH_MAC   | путь до иконки для Mac -- "app/style/logo.icns"                            |
| VERSION_JSON    | доп. файлы для добавления в архив -- "version.json"                                                |
| STYLE_DIR       | доп. файлы для добавления в архив: стили                                    |


### _exe_ файл (Windows)

Или же, чтобы создать _exe_-файл в Windows, можно выполнить следующую команду в терминале или командной строке:
```bash
pyinstaller --windowed --add-data "config.json;." --add-data "app/style/*;app/style" --name='Lab_App_*.*.*' --icon=app/style/logo.ico main.py
```
Я настоятельно рекомендую вам использовать [UPX](https://upx.github.io/) для уменьшения размера исполняемого файла. В этом случае вы можете выполнить следующую команду (изменив путь):
```bash
pyinstaller --windowed --add-data "config.json;." --add-data "app/style/*;app/style" --name='Lab_App_*.*.*' --icon=app/style/logo.ico --upx-dir C:\path\to\the\folder\upx-4.2.4-win64 main.py
```

Размер _exe_ будет составлять порядка 130 МБ.

### Application (Mac)

Для Mac, чтобы создать Application, можно также использовать скрипт [build_application/build.py](build_application/build.py) или же выполнить следующую команду: 
```bash
pyinstaller --onefile --windowed --add-data "config.json:." --add-data "app/style/logo.icns:app/style" --add-data "app/style/style_dark.qss:app/style" --name='Lab_App_*.*.*' --icon=app/style/logo.icns main.py
```


## Автор

Ермолинский Петр Борисович.

## Цитирование

Если вы используете это приложение в своей научной работе, пожалуйста, укажите ссылку на данный репозиторий.

**В формате BibTeX**:
```bibtex
@software{ErmolinskiyLaboratoryDataProcessingApp,
  author = {Ермолинский, Пётр Борисович},
  title = {Приложение для обработки экспериментальных данных лаборатории Биомедицинской фотоники МГУ},
  url = {https://github.com/Petr-Ermolinskiy/Laboratory-Data-Processing-App},
  year = {2026},
  note = {Версия 3.7.7}
}
```

**В формате APA**:
Ermolinskiy, P. B. (2026). Приложение для обработки экспериментальных данных лаборатории Биомедицинской фотоники МГУ [Компьютерное программное обеспечение]. GitHub. https://github.com/Petr-Ermolinskiy/Laboratory-Data-Processing-App

