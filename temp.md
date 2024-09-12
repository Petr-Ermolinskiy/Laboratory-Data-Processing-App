ЭТО ДЛЯ ФАЙЛОВ QT
```bash
pyside6-uic ui_main.ui -o ui_main.py
```
ЭТО ДЛЯ СОЗДАНИЯ exe
```bash
pyinstaller --windowed --add-data "logo.ico;." --add-data "style_dark.qss;." --name='Lab_App_3.6' --icon=logo.ico --upx-dir C:\Users\Petr\Desktop\upx-4.2.2-win64 main.py
```