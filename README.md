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
Если у вас установилась версия _seaborn_ 0.11 ввиду конфликта с пакетом _statannotations_, то вручную установите версию 0.12:
```bash
pip install seaborn==0.12.2
```


Запустите программу:
```bash
python main.py
```

## Проблемы с установкой
- Если при установке библиотек не устанавливается pandas, то скорее всего это из-за отсутствия 
[Microsoft C++ Build Tools](https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/).
- Если всё ещё выдается ошибка, то надо провести установку последней версии pandas, и далее выполнить `pip install -r requirements.txt`.

## Создание _exe_ файла

Чтобы создать _exe_-файл в Windows, нужно выполнить следующую команду в терминале или командной строке:
```bash
pyinstaller --windowed --add-data "version.json;." --add-data "app/style/logo.ico;app/style" --add-data "app/style/style_dark.qss;app/style/" --name='Lab_App_3.6.3' --icon=app/style/logo.ico main.py
```
Я настоятельно рекомендую вам использовать [UPX](https://upx.github.io/) для уменьшения размера исполняемого файла. В этом случае вы можете выполнить следующую команду:
```bash
pyinstaller --windowed --add-data "version.json;." --add-data "app/style/logo.ico;app/style" --add-data "app/style/style_dark.qss;app/style/" --name='Lab_App_3.6.3' --icon=app/style/logo.ico --upx-dir C:\Users\petre\Desktop\Programes\upx-4.2.4-win64 main.py
```
Размер exe будет составлять порядка 130 МБ.

## Автор

Ермолинский Петр Борисович.

