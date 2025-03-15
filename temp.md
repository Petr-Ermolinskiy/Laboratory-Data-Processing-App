ЭТО ДЛЯ ФАЙЛОВ QT
```bash
pyside6-uic app/ui/ui_main.ui -o app/ui/ui_main.py
```
ЭТО ДЛЯ СОЗДАНИЯ exe
```bash
pyinstaller --windowed --add-data "version.json;." --add-data "app/style/logo.ico;app/style" --add-data "app/style/style_dark.qss;app/style/" --name='Lab_App_3.6.3' --icon=app/style/logo.ico --upx-dir C:\Users\petre\Desktop\Programes\upx-4.2.4-win64 main.py
```