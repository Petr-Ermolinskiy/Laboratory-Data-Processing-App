# Документация приложения Lab App v3.7.7

## Содержание

- [1. RheoScan](#1-rheoscan-0)
- [2. Биола](#1-биола-1)
- [3. Лазерный пинцет](#1-лазерный-пинцет-2)
- [4. Обработка данных](#1-обработка-данных-3)
  - [4.1. Графики](#2-графики-0)
    - [4.1.1. Box plot](#3-box-plot-0)
      - [4.1.1.1. Шрифт, цвета, размер точек](#4-шрифт-цвета-размер-точек-0)
      - [4.1.1.2. Настройка положения подписей и границ](#4-настройка-положения-подписей-и-границ-1)
      - [4.1.1.3. Стат.значимость](#4-статзначимость-2)
    - [4.1.2. Корреляционная матрица](#3-корреляционная-матрица-1)
    - [4.1.3. Корреляционный график](#3-корреляционный-график-2)
    - [4.1.4. Матрица рассеяния](#3-матрица-рассеяния-3)
    - [4.1.5. Распределение по двум параметрам](#3-распределение-по-двум-параметрам-4)
    - [4.1.6. Корреляция одного параметра](#3-корреляция-одного-параметра-5)
  - [4.2. Микрореологический профиль](#2-микрореологический-профиль-1)
  - [4.3. Сводная таблица](#2-сводная-таблица-2)
  - [4.4. Catplot](#2-catplot-3)
  - [4.5. Обработка RheoScan](#2-обработка-rheoscan-4)
  - [4.6. Доп. обработка](#2-доп-обработка-5)
    - [4.6.1. Рассчитать стат. значимость между 2 выборками](#3-рассчитать-стат-значимость-между-2-выборками-0)
    - [4.6.2. Кластеризация признаков](#3-кластеризация-признаков-1)
- [5. Доп.настройки](#1-допнастройки-4)

---

## 1. RheoScan

![RheoScan](figs/tab_L1_I0_RheoScan.png)
*Скриншот 1: вкладка — RheoScan*. Программа обрабатывает данные только txt файлов, полученных из RheoScan.

<a id="w1"></a>
<b>1. btn_save_exel_csv</b> (QPushButton)<br>
<html><head/><body><p>Произвести обработку данных исходя из введенных путей и дополнительных настроек.</p></body></html><br><br>

<a id="w2"></a>
<b>2. main_path</b> (QLineEdit)<br>
<html><head/><body><p>Путь к папке с подпапками с файлами RheoScan. </p><p>В случае <span style=" text-decoration: underline;">уровеня подпапок = 1</span> это должна быть папка с 3 подпапками: </p><p><span style=" font-style:italic;">- agg</span></p><p><span style=" font-style:italic;">- deform</span></p><p><span style=" font-style:italic;">- stress</span></p><p>Файлы уже должны быть рассортированы. Если это не так, то выберете путь и нажмите кнопку ниже для рассортировки. </p></body></html><br><br>

<a id="w3"></a>
<b>3. comboBox_RheoScan_path_save</b> (QComboBox)<br>
<html><head/><body><p>Сохранить результат обработки по всем подпапкам (в случае, если уровень подпапок &gt; 1), либо сохранить в корневой дирректории (введенный путь). Файлы excel сохранятся с теми именами, которые соответствуют папкам, в которых лежат 3 подпапки.</p></body></html><br><br>

<a id="w4"></a>
<b>4. tua_1_agg</b> (QSpinBox)<br>
<html><head/><body><p>Иногда надо подобрать данное значение для правильной аппроксимации агрегатограммы. </p></body></html><br><br>

<a id="w5"></a>
<b>5. tua_2_agg</b> (QSpinBox)<br>
<html><head/><body><p>Иногда надо подобрать данное значение для правильной аппроксимации агрегатограммы. </p></body></html><br><br>

<a id="w6"></a>
<b>6. r2_def</b> (QDoubleSpinBox)<br>
<html><head/><body><p>Иногда надо подобрать данное значение для правильной аппроксимации. </p></body></html><br><br>

<a id="w7"></a>
<b>7. spinBox_n_max_deform</b> (QSpinBox)<br>
<html><head/><body><p>Иногда надо подобрать данное значение для правильной аппроксимации. </p></body></html><br><br>

<a id="w8"></a>
<b>8. check_approx_agg</b> (QCheckBox)<br>
<html><head/><body><p>Произвести дополнительную аппроксимацию кривой светорассеяния для маленькой кюветы?</p><p>Аппроксимация производится с помощью 2 экспонент с разными характерными временами:</p><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#6a9955;"># функция, которой аппроксимируется кривая</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;">def </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#dcdcaa;">f</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">x</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">y0</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">A1</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">A2</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">t1</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">t2</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">):</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#c586c0;">return </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">y0</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">+</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">A1</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">*</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;">np</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">.</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">exp</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">-</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">x</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">/</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">t1</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">)) </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">+</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">A2</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">*</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;">np</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">.</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">exp</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">-</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">x</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">/</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">t2</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">))</span></pre><pre style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc; background-color:#1f1f1f;"><br/></pre><p>Идет расчет данных показателей, а также индекс агрегации для разных времен: 2.5, 5, 10, 50, 100 и MAX кол-ва секунд.</p></body></html><br><br>

<a id="w9"></a>
<b>9. check_figs_for_agg</b> (QCheckBox)<br>
<html><head/><body><p>Построить графики для аппроксимации кривых?</p><p>Рекомендуется всегда смотреть на корректность аппроксимации.</p></body></html><br><br>

<a id="w10"></a>
<b>10. check_approx_deform</b> (QCheckBox)<br>
<html><head/><body><p>Произвести дополнительную аппроксимацию кривой индекса деформируемости и сдвигового напряжения для большой кюветы?</p><p>Аппроксимация производится с помощью линейной функции, где напряжения приведены в логарифм:</p><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#6a9955;"># функция, которой будем аппроксимировать - линейная функция от логарифма напряжений сдвига</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;">def</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#dcdcaa;">f</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">x</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">: </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;">float</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">a</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">: </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;">float</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">b</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">: </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;">float</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">):</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;&quot;&quot;Линейная функция.&quot;&quot;&quot;</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#c586c0;">return</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">a</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">*</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">x</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">+</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">b</span></pre><p>Рассчитываются параметры предела текучести (<span style=" font-weight:700;">b</span>) и вязкости внутреклеточного содержимого (<span style=" font-weight:700;">1/a</span>).</p></body></html><br><br>

<a id="w11"></a>
<b>11. check_for_deform</b> (QCheckBox)<br>
<html><head/><body><p>Построить графики для аппроксимации кривых?</p><p>Рекомендуется всегда смотреть на корректность аппроксимации.</p></body></html><br><br>

<a id="w12"></a>
<b>12. check_stat_for_column</b> (QCheckBox)<br>
<html><head/><body><p>Создание доп. листов, где будет приведена статистика по столбцам.</p></body></html><br><br>

<a id="w13"></a>
<b>13. vibros_delete</b> (QCheckBox)<br>
<html><head/><body><p>Убрать выбросы. Использовать, когда вы обрабатываете <span style=" font-weight:700;">только 1 пациента</span>! </p></body></html><br><br>

<a id="w14"></a>
<b>14. iqr_vibros</b> (QDoubleSpinBox)<br>
<html><head/><body><p>Коэффициент кол-ва интерквантильных размахов для определения выбросов.</p><p>Используется, только когда обрабатываете 1 пациента или 1 образец.</p></body></html><br><br>

<a id="w15"></a>
<b>15. spinBox_level</b> (QSpinBox)<br>
<html><head/><body><p>Уровень подпапок позволяет обрабатывать несколько папок пациентов/образцов одновременно.</p><p>К примеру, если вы ввели выше путь к папке с папками, названия которых совпадает с названием образцов, и в каждой такой папке есть 3 подпапки (agg, stress, deform), то для обновременной обработки нужно использовать <span style=" font-weight:700;">уровень подпапок=2</span>. Соответственно, чем больше у вас вложенных папок до 3 искомых подпапок, тем больше уровень подпапок вам нужно слелать.</p></body></html><br><br>

<a id="w16"></a>
<b>16. check_save_exel</b> (QCheckBox)<br>
<html><head/><body><p>Сохранить excel файл/файлы. Будет несколько листов в зависимости от выбранных настроек.</p></body></html><br><br>

<a id="w17"></a>
<b>17. check_save_csv</b> (QCheckBox)<br>
<html><head/><body><p>Сохранить csv файл/файлы. Будет несколько файлов в зависимости от выбранных настроек.</p></body></html><br><br>

<a id="w18"></a>
<b>18. check_save_RheoScan_overall</b> (QCheckBox)<br>
<html><head/><body><p>Сводная таблица по всем измерениям. По большей части не нужна из-за наличия доп. обработки данных RheoScan (см. 4 вкладку).</p></body></html><br><br>

<a id="w19"></a>
<b>19. separator_for_data</b> (QLineEdit)<br>
<html><head/><body><p>Выбрать разделитель данных. Бывает полезно для образцов.</p><p>К примеру, у вас все образцы называюся по типу &quot;sample-##-##&quot;.</p><p>Вы можете выбрать разделителем дефис &quot;-&quot; и у вас появится дополнительные стролбцы.</p></body></html><br><br>

<a id="w20"></a>
<b>20. check_agg</b> (QCheckBox)<br>
<html><head/><body><p>Обработать ли папку <span style=" font-weight:700;">agg</span>. Иногда требуется обработать только одну какую-то папку, а не все сразу.</p></body></html><br><br>

<a id="w21"></a>
<b>21. check_stress</b> (QCheckBox)<br>
<html><head/><body><p>Обработать ли папку <span style=" font-weight:700;">stress</span>. Иногда требуется обработать только одну какую-то папку, а не все сразу.</p></body></html><br><br>

<a id="w22"></a>
<b>22. check_deform</b> (QCheckBox)<br>
<html><head/><body><p>Обработать ли папку <span style=" font-weight:700;">deform</span>. Иногда требуется обработать только одну какую-то папку, а не все сразу.</p></body></html><br><br>

<a id="w23"></a>
<b>23. check_dop_CSS_parameter</b> (QCheckBox)<br>
<html><head/><body><p>Дополнительный параметр CSS, который вытаскивается из графика: светорассеяние VS напряжения сдвига. </p><p>Идет аппроксимация экспонентной и вытаскивается параметр затухания (<span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; font-weight:700; color:#000000;">new_parameter</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">)</span>.</p><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">                    (</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">_</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">_</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">new_parameter</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">), </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">_</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">=</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;">opt</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">.</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#dcdcaa;">curve_fit</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;">lambda</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">t</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">a</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">b</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">c</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">: </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">a</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">+</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">b</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">*</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#4ec9b0;">np</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">.</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">exp</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">-</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">t</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#d4d4d4;">/</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">c</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">),</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">                        сдвиговое напряжение,</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">                        интенсивность обратного светорассеяния,</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">                    )</span></pre></body></html><br><br>

## 2. Биола

![Биола](figs/tab_L1_I1_.png)
*Скриншот 2: вкладка — Биола*. Обработка данных, выгруженных из программы в txt.

<a id="w24"></a>
<b>24. path_for_biola</b> (QLineEdit)<br>
<html><head/><body><p>В данное поле необходимо ввести путь к папке, в которой находится txt файл с измерениями biola (борн и флуктуации) или pdf файл с измерениями концентрации тромбоцитов.</p></body></html><br><br>

<a id="w25"></a>
<b>25. comboBox_biola</b> (QComboBox)<br>
<html><head/><body><p>Выберете txt файл, экспортированный из программы для Биолы.</p><p>Файлы появляются автоматически при добавлении путя к папке с файлом</p></body></html><br><br>

<a id="w26"></a>
<b>26. comboBox_biola_concentration</b> (QComboBox)<br>
<html><head/><body><p>Выберете pdf файл с данными касательно концентрации тромбоцитов.</p><p>Файлы появляются автоматически при добавлении путя к папке с файлом</p></body></html><br><br>

<a id="w27"></a>
<b>27. spinBox_biola_born_odd</b> (QSpinBox)<br>
Длина окна для сглаживания для данных светопропускания по Борну. Подбиралось эмпирически, чтобы соответствовать данным, рассчитанным в приложении Биола<br><br>

<a id="w28"></a>
<b>28. spinBox_biola_fluc_odd</b> (QSpinBox)<br>
<html><head/><body><p>Длина окна для сглаживания для данных флуктуаций светопропускания. Подбиралось эмпирически, чтобы соответствовать данным, рассчитанным в приложении Биола</p></body></html><br><br>

<a id="w29"></a>
<b>29. spinBox_biola_born</b> (QSpinBox)<br>
<html><head/><body><p>Длина окна для сглаживания для данных производной светопропускания по Борну. Подбиралось эмпирически, чтобы соответствовать данным, рассчитанным в приложении Биола</p></body></html><br><br>

<a id="w30"></a>
<b>30. spinBox_biola_fluc</b> (QSpinBox)<br>
<html><head/><body><p>Длина окна для сглаживания для данных производной флуктуаций светопропускания. Подбиралось эмпирически, чтобы соответствовать данным, рассчитанным в приложении Биола</p></body></html><br><br>

<a id="w31"></a>
<b>31. check_biola_plot_figs</b> (QCheckBox)<br>
<html><head/><body><p>Начертить ли усредненные графики по Борну и флуктуациям, а также производным?</p><p>Имеет место использовать для группы однаковых образцов или одного пациента.</p><p><br/></p></body></html><br><br>

<a id="w32"></a>
<b>32. doubleSpinBox_Biola</b> (QDoubleSpinBox)<br>
Относительный размер шрифта<br><br>

<a id="w33"></a>
<b>33. comboBox_Biola_SD_or</b> (QComboBox)<br>
Погрешности на графиках<br><br>

<a id="w34"></a>
<b>34. check_setka_biola</b> (QCheckBox)<br>
Сделать сетку на графиках?<br><br>

<a id="w35"></a>
<b>35. comboBox_Biola_language</b> (QComboBox)<br>
Язык для графиков<br><br>

<a id="w36"></a>
<b>36. btn_biola</b> (QPushButton)<br>
Обработать данные из txt файла<br><br>

<a id="w37"></a>
<b>37. btn_biola_concentration</b> (QPushButton)<br>
Обработать данные из pdf файла<br><br>

## 3. Лазерный пинцет

![Лазерный пинцет](figs/tab_L1_I2__.png)
*Скриншот 3: вкладка — Лазерный пинцет*. Вытаскивание значений сил из названий к видео-записям измерения сила агрегации/дезагрегации или времени агрегации.

<a id="w38"></a>
<b>38. path_for_LT</b> (QLineEdit)<br>
<html><head/><body><p><span style=" font-family:'Helvetica';">Необходимо в данное поле ввести путь к папке с подпапками разных концентраций/пациентов/образцов.</span></p><p><span style=" font-family:'Helvetica';">К примеру, в данной папке могут быть подпапки с концентрациями:</span></p><p><span style=" font-family:'Helvetica';">0</span></p><p><span style=" font-family:'Helvetica';">1</span></p><p><span style=" font-family:'Helvetica';">10</span></p><p><span style=" font-family:'Helvetica';">100</span></p><p><br/></p><p><span style=" font-family:'Helvetica';">В каждой подпапке должны быть видео, записанные через какой-то разделитель. Сила агрегации обозначается, как FA/fa/Fa; сила дезагрегации, как FD/fd/Fd. Сила взаимодействия эритроцита и эндотелия, как End/end. Важно, чтобы первые 2 буквы имени силы было правильным. Значение силы должно быть записано без доп. Знаков (к примеру, так нельзя: «Fd3-12.2+.avi». Будут обрабатываться названия только видеофайлов. Т.е. между разделителем и «.avi» должна быть только сила. </span></p></body></html><br><br>

<a id="w39"></a>
<b>39. sep_for_LT</b> (QLineEdit)<br>
<html><head/><body><p><span style=" font-family:'Helvetica';">Разделитель для имени подпапок. Необходим, чтобы в excel файле были выделены интерисующие имена. </span></p><p><span style=" font-family:'Helvetica';">К примеру, если подпапки назывались по шаблону &quot;образец-концентрация&quot;:</span></p><p><span style=" font-family:'Helvetica';">dextran-0</span></p><p><span style=" font-family:'Helvetica';">dextran-10</span></p><p><span style=" font-family:'Helvetica';">dextran-100</span></p><p><span style=" font-family:'Helvetica';">То с разделителем &quot;-&quot; и позицией имени &quot;2&quot; в качестве образцов в excel будут: [0, 10, 100]</span></p></body></html><br><br>

<a id="w40"></a>
<b>40. position</b> (QSpinBox)<br>
<html><head/><body><p><span style=" font-family:'Helvetica';">Позиция, на которой находится имя при использовании разделителя для имени подпапок. </span></p><p><span style=" font-family:'Helvetica';">К примеру, если подпапки назывались по шаблону &quot;образец-концентрация&quot;:</span></p><p><span style=" font-family:'Helvetica';">dextran-0</span></p><p><span style=" font-family:'Helvetica';">dextran-10</span></p><p><span style=" font-family:'Helvetica';">dextran-100</span></p><p><span style=" font-family:'Helvetica';">То с позицией &quot;2&quot; в качестве образцов в excel будут: [0, 10, 100]</span></p></body></html><br><br>

<a id="w41"></a>
<b>41. sep_for_LT_values</b> (QLineEdit)<br>
<html><head/><body><p><span style=" font-family:'Helvetica';">Важно внести в программу разделитель значения названия и значения силы.</span></p><p><span style=" font-family:'Helvetica';">К примеру, чаще всего это &quot;-&quot;. Силы записываются в этом случае для примера:</span></p><p><span style=" font-family:'Helvetica';">FA-19.9.avi</span></p><p><span style=" font-family:'Helvetica';">fa-17.0.avi</span></p><p><span style=" font-family:'Helvetica';">Fd-11.1.avi</span></p></body></html><br><br>

<a id="w42"></a>
<b>42. comboBox_LT_calibration</b> (QComboBox)<br>
<html><head/><body><p>Калибровка для дополнительного пучка может быть как линейной, так и экспоненциальной. Необходимо выбрать одно</p></body></html><br><br>

<a id="w43"></a>
<b>43. btn_LT</b> (QPushButton)<br>
Произвести обработку данных для лазерного пинцета<br><br>

<a id="w44"></a>
<b>44. check_LT_raw_data</b> (QCheckBox)<br>
Дополнительно сохранить данные в развернутом виде? <br><br>

## 4. Обработка данных

![Обработка данных](figs/tab_L1_I3__.png)
*Скриншот 4: вкладка — Обработка данных*. В данном модуле можно строить различные графики и обрабатывать данные.

<a id="w45"></a>
<b>45. tabWidget_2</b> (QTabWidget)<br>
Путь к папке с excel файлом<br><br>

<a id="w46"></a>
<b>46. path_for_plot</b> (QLineEdit)<br>
Путь к папке с excel файлом<br><br>

<a id="w47"></a>
<b>47. comboBox</b> (QComboBox)<br>
Название excel файла -- подставится автоматически. Надо только выбрать<br><br>

<a id="w48"></a>
<b>48. check_box_figs_all_sheets</b> (QCheckBox)<br>
Произвести обработку по всем листам в excel файле?<br><br>

<a id="w49"></a>
<b>49. comboBox_figs_sheets</b> (QComboBox)<br>
Название листа в excel файле -- подставится автоматически. Надо только выбрать<br><br>

<a id="w50"></a>
<b>50. comboBox_2</b> (QComboBox)<br>
<html><head/><body><p>Название столбца для категориальных групп.</p><p>Это может быть любая колонка, где есть определенные категории.</p><p>К примеру, &quot;Пол&quot;.</p></body></html><br><br>

<a id="w51"></a>
<b>51. checkBox_point_comma_separator</b> (QCheckBox)<br>
Разделитель значений на графике запятая?<br><br>

<a id="w52"></a>
<b>52. check_box_plot</b> (QCheckBox)<br>
<html><head/><body><p>Построить график box plot, в котором представлены разные категории?</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w53"></a>
<b>53. check_corr_matrix</b> (QCheckBox)<br>
<html><head/><body><p>Построить график корреляционной матрицы? Одна матрица на каждую категорию.</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w54"></a>
<b>54. check_corr_figs</b> (QCheckBox)<br>
<html><head/><body><p>Построить корреляционный график, где цветами будут выделены категории?</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w55"></a>
<b>55. check_box_pairplot</b> (QCheckBox)<br>
<html><head/><body><p>Построить матрицу рассеяния, где цветами будут выделены категории?</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w56"></a>
<b>56. check_jointplot</b> (QCheckBox)<br>
<html><head/><body><p>Построить график распределение по двум параметрам?</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w57"></a>
<b>57. check_corr_one_parameter</b> (QCheckBox)<br>
<html><head/><body><p>Построить корреляцию одного параметра? </p><p>То есть строится корреляция между выбранной колонки и всеми остальными.</p><p>Строится отдельно от других графиков. </p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w58"></a>
<b>58. comboBox_color_pal_box</b> (QComboBox)<br>
<html><head/><body><p>Цветовая палитра для box</p></body></html><br><br>

<a id="w59"></a>
<b>59. comboBox_color_pal_points</b> (QComboBox)<br>
<html><head/><body><p>Цветовая палитра для точек</p></body></html><br><br>

<a id="w60"></a>
<b>60. pushButton_HEX_box</b> (QPushButton)<br>
<html><head/><body><p>Возможно делать кастомные цвета для box.</p><p>Для этого выберайте итерационно цвета в палитре.</p><p>В панеле слева будет формироваться строка, которая будет использована для создания палитры.</p></body></html><br><br>

<a id="w61"></a>
<b>61. pushButton_HEX_points</b> (QPushButton)<br>
<html><head/><body><p>Возможно делать кастомные цвета для точек.</p><p>Для этого выберайте итерационно цвета в палитре.</p><p>В панеле слева будет формироваться строка, которая будет использована для создания палитры.</p></body></html><br><br>

<a id="w62"></a>
<b>62. comboBox_fonts</b> (QComboBox)<br>
Шрифт для подписей на графиках<br><br>

<a id="w63"></a>
<b>63. spinBox_x_label</b> (QSpinBox)<br>
Размер шрифта подписи X<br><br>

<a id="w64"></a>
<b>64. spinBox_y_label</b> (QSpinBox)<br>
Размер шрифта подписи Y<br><br>

<a id="w65"></a>
<b>65. btn_plot_and_save_figs</b> (QPushButton)<br>
Построить все графики и сохранить их в соответствующих папках<br><br>

### 4.1. Графики

![Графики](figs/tab_L2_I0_.png)
*Скриншот 4.1: вкладка — Графики*. Построение разных графиков. Используется только данные в 'длинном' формате.

<a id="w66"></a>
<b>66. path_for_plot</b> (QLineEdit)<br>
Путь к папке с excel файлом<br><br>

<a id="w67"></a>
<b>67. comboBox</b> (QComboBox)<br>
Название excel файла -- подставится автоматически. Надо только выбрать<br><br>

<a id="w68"></a>
<b>68. check_box_figs_all_sheets</b> (QCheckBox)<br>
Произвести обработку по всем листам в excel файле?<br><br>

<a id="w69"></a>
<b>69. comboBox_figs_sheets</b> (QComboBox)<br>
Название листа в excel файле -- подставится автоматически. Надо только выбрать<br><br>

<a id="w70"></a>
<b>70. comboBox_2</b> (QComboBox)<br>
<html><head/><body><p>Название столбца для категориальных групп.</p><p>Это может быть любая колонка, где есть определенные категории.</p><p>К примеру, &quot;Пол&quot;.</p></body></html><br><br>

<a id="w71"></a>
<b>71. checkBox_point_comma_separator</b> (QCheckBox)<br>
Разделитель значений на графике запятая?<br><br>

<a id="w72"></a>
<b>72. check_box_plot</b> (QCheckBox)<br>
<html><head/><body><p>Построить график box plot, в котором представлены разные категории?</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w73"></a>
<b>73. check_corr_matrix</b> (QCheckBox)<br>
<html><head/><body><p>Построить график корреляционной матрицы? Одна матрица на каждую категорию.</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w74"></a>
<b>74. check_corr_figs</b> (QCheckBox)<br>
<html><head/><body><p>Построить корреляционный график, где цветами будут выделены категории?</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w75"></a>
<b>75. check_box_pairplot</b> (QCheckBox)<br>
<html><head/><body><p>Построить матрицу рассеяния, где цветами будут выделены категории?</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w76"></a>
<b>76. check_jointplot</b> (QCheckBox)<br>
<html><head/><body><p>Построить график распределение по двум параметрам?</p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w77"></a>
<b>77. check_corr_one_parameter</b> (QCheckBox)<br>
<html><head/><body><p>Построить корреляцию одного параметра? </p><p>То есть строится корреляция между выбранной колонки и всеми остальными.</p><p>Строится отдельно от других графиков. </p><p>В отдельной вкладке внизу можно изменить некоторые настройки построения графика.</p></body></html><br><br>

<a id="w78"></a>
<b>78. comboBox_color_pal_box</b> (QComboBox)<br>
<html><head/><body><p>Цветовая палитра для box</p></body></html><br><br>

<a id="w79"></a>
<b>79. comboBox_color_pal_points</b> (QComboBox)<br>
<html><head/><body><p>Цветовая палитра для точек</p></body></html><br><br>

<a id="w80"></a>
<b>80. pushButton_HEX_box</b> (QPushButton)<br>
<html><head/><body><p>Возможно делать кастомные цвета для box.</p><p>Для этого выберайте итерационно цвета в палитре.</p><p>В панеле слева будет формироваться строка, которая будет использована для создания палитры.</p></body></html><br><br>

<a id="w81"></a>
<b>81. pushButton_HEX_points</b> (QPushButton)<br>
<html><head/><body><p>Возможно делать кастомные цвета для точек.</p><p>Для этого выберайте итерационно цвета в палитре.</p><p>В панеле слева будет формироваться строка, которая будет использована для создания палитры.</p></body></html><br><br>

<a id="w82"></a>
<b>82. comboBox_fonts</b> (QComboBox)<br>
Шрифт для подписей на графиках<br><br>

<a id="w83"></a>
<b>83. spinBox_x_label</b> (QSpinBox)<br>
Размер шрифта подписи X<br><br>

<a id="w84"></a>
<b>84. spinBox_y_label</b> (QSpinBox)<br>
Размер шрифта подписи Y<br><br>

<a id="w85"></a>
<b>85. btn_plot_and_save_figs</b> (QPushButton)<br>
Построить все графики и сохранить их в соответствующих папках<br><br>

#### 4.1.1. Box plot

![Box plot](figs/tab_L3_I0_Box_plot.png)
*Скриншот 4.1.1: вкладка — Box plot*. Построение box-plot.

<a id="w86"></a>
<b>86. comboBox_color_pal_box</b> (QComboBox)<br>
<html><head/><body><p>Цветовая палитра для box</p></body></html><br><br>

<a id="w87"></a>
<b>87. comboBox_color_pal_points</b> (QComboBox)<br>
<html><head/><body><p>Цветовая палитра для точек</p></body></html><br><br>

<a id="w88"></a>
<b>88. pushButton_HEX_box</b> (QPushButton)<br>
<html><head/><body><p>Возможно делать кастомные цвета для box.</p><p>Для этого выберайте итерационно цвета в палитре.</p><p>В панеле слева будет формироваться строка, которая будет использована для создания палитры.</p></body></html><br><br>

<a id="w89"></a>
<b>89. pushButton_HEX_points</b> (QPushButton)<br>
<html><head/><body><p>Возможно делать кастомные цвета для точек.</p><p>Для этого выберайте итерационно цвета в палитре.</p><p>В панеле слева будет формироваться строка, которая будет использована для создания палитры.</p></body></html><br><br>

<a id="w90"></a>
<b>90. comboBox_fonts</b> (QComboBox)<br>
Шрифт для подписей на графиках<br><br>

<a id="w91"></a>
<b>91. spinBox_x_label</b> (QSpinBox)<br>
Размер шрифта подписи X<br><br>

<a id="w92"></a>
<b>92. spinBox_y_label</b> (QSpinBox)<br>
Размер шрифта подписи Y<br><br>

##### 4.1.1.1. Шрифт, цвета, размер точек

![Шрифт, цвета, размер точек](figs/tab_L4_I0______.png)
*Скриншот 4.1.1.1: вкладка — Шрифт, цвета, размер точек*. 

<a id="w93"></a>
<b>93. comboBox_color_pal_box</b> (QComboBox)<br>
<html><head/><body><p>Цветовая палитра для box</p></body></html><br><br>

<a id="w94"></a>
<b>94. comboBox_color_pal_points</b> (QComboBox)<br>
<html><head/><body><p>Цветовая палитра для точек</p></body></html><br><br>

<a id="w95"></a>
<b>95. pushButton_HEX_box</b> (QPushButton)<br>
<html><head/><body><p>Возможно делать кастомные цвета для box.</p><p>Для этого выберайте итерационно цвета в палитре.</p><p>В панеле слева будет формироваться строка, которая будет использована для создания палитры.</p></body></html><br><br>

<a id="w96"></a>
<b>96. pushButton_HEX_points</b> (QPushButton)<br>
<html><head/><body><p>Возможно делать кастомные цвета для точек.</p><p>Для этого выберайте итерационно цвета в палитре.</p><p>В панеле слева будет формироваться строка, которая будет использована для создания палитры.</p></body></html><br><br>

<a id="w97"></a>
<b>97. comboBox_fonts</b> (QComboBox)<br>
Шрифт для подписей на графиках<br><br>

<a id="w98"></a>
<b>98. spinBox_x_label</b> (QSpinBox)<br>
Размер шрифта подписи X<br><br>

<a id="w99"></a>
<b>99. spinBox_y_label</b> (QSpinBox)<br>
Размер шрифта подписи Y<br><br>

##### 4.1.1.2. Настройка положения подписей и границ

![Настройка положения подписей и границ](figs/tab_L4_I1_____.png)
*Скриншот 4.1.1.2: вкладка — Настройка положения подписей и границ*. 

<a id="w100"></a>
<b>100. check_sort_or_not</b> (QCheckBox)<br>
Упорядочить значения в группе? Используется базовая сортировка<br><br>

<a id="w101"></a>
<b>101. check_sort_or_not_ascending</b> (QCheckBox)<br>
Упорядочить значения в группе по возрастанию?<br><br>

<a id="w102"></a>
<b>102. order_box_plot</b> (QLineEdit)<br>
<html><head/><body><p>Изменить порядок подписей. </p><p>Для этого необходимо через пробел цифрами ввести настоящий порядок.</p><p>Важно, чтобы количество элементов соответствовало кол-ву категорий в группе.</p><p>К примеру, можно ввести следующее:</p><p>1 2 4 3</p><p>Тогда будет порядок, как он представлен выше относительно начального порядка без упорядочивания</p></body></html><br><br>

##### 4.1.1.3. Стат.значимость

![Стат.значимость](figs/tab_L4_I2_..png)
*Скриншот 4.1.1.3: вкладка — Стат.значимость*. 

<a id="w103"></a>
<b>103. check_stat_znachimost</b> (QCheckBox)<br>
Рассчитать статистическую значимость?<br><br>

<a id="w104"></a>
<b>104. spinBox_size_stat_znachimost</b> (QSpinBox)<br>
Шрифт значков статистической значимости<br><br>

<a id="w105"></a>
<b>105. comboBox_box_plot_sign_stat_znachimost</b> (QComboBox)<br>
<html><head/><body><p>Значок статистической значимости.</p><p>Один из трех:</p><p>- звездочка (*)</p><p>- точное значение p (p=0.03)</p><p>- относительное p (p&lt;0.05)</p><p>Статистическая значимость для здездочек обозначается следующим:</p><p>* p&lt;0.05, ** p&lt;0.01, *** p&lt;0.001, **** p&lt;0.0001</p></body></html><br><br>

<a id="w106"></a>
<b>106. spinBox_max_n_stars</b> (QSpinBox)<br>
<html><head/><body><p>Максимальное кол-во знаков для статистической значимости.</p><p>Работает для значка стат.значимости &quot;звездочка&quot; и &quot;точное значение p&quot;.</p><p>Если макс.кол-во знаков = 1, то будет выведены только:</p><p>* или p&lt;0.05, даже если p=0.00001</p></body></html><br><br>

<a id="w107"></a>
<b>107. comboBox_alter_hep</b> (QComboBox)<br>
<html><head/><body><p>Альтернативная гипотеза для теста.</p><p>Если не знаете, то используйте всегда two-sided</p></body></html><br><br>

<a id="w108"></a>
<b>108. comboBox_stat_test</b> (QComboBox)<br>
<html><head/><body><p>Статистический тест для расчета стат.значимости. </p><p>В списке есть как параметрические, так и непараметрические тесты.</p></body></html><br><br>

#### 4.1.2. Корреляционная матрица

![Корреляционная матрица](figs/tab_L3_I1__.png)
*Скриншот 4.1.2: вкладка — Корреляционная матрица*. 

<a id="w109"></a>
<b>109. comboBox_correlation_figs_matrix</b> (QComboBox)<br>
<html><head/><body><p>Метод расчета корреляций: Пирсон, Спирмен или Кендал.</p></body></html><br><br>

<a id="w110"></a>
<b>110. comboBox_correlation_color_map_for_figs</b> (QComboBox)<br>
Цветовая схема для корреляционной матрицы.<br><br>

<a id="w111"></a>
<b>111. corr_mat_figsize</b> (QDoubleSpinBox)<br>
<html><head/><body><p>Размер рисунка для корреляционной матрицы. </p><p>Подбирается вручную. Влияет на размер конечного файла.</p></body></html><br><br>

<a id="w112"></a>
<b>112. font_for_in</b> (QDoubleSpinBox)<br>
<html><head/><body><p>Масштаб шрифта подписей для корреляционных матриц.</p><p>Подбирается вручную.</p></body></html><br><br>

<a id="w113"></a>
<b>113. font_for_out</b> (QDoubleSpinBox)<br>
Размер шрифта заголовка. Подбирается вручную.<br><br>

<a id="w114"></a>
<b>114. name_of_corr_matrix</b> (QLineEdit)<br>
<html><head/><body><p>Дополнительное название заголовка &lt;title&gt;. </p><p>Конечное название формулируется следующим образом:</p><p>&lt;title&gt; + название_категории + (N=&lt;кол-во образцов&gt;)</p></body></html><br><br>

#### 4.1.3. Корреляционный график

![Корреляционный график](figs/tab_L3_I2__.png)
*Скриншот 4.1.3: вкладка — Корреляционный график*. 

<a id="w115"></a>
<b>115. comboBox_color_pal_corr</b> (QComboBox)<br>
Цветовая палитра для корреляционного графика.<br><br>

<a id="w116"></a>
<b>116. doubleSpinBox_corr_figs</b> (QDoubleSpinBox)<br>
Нижняя граница для корреляционного графика. Иногда полезно, если нужно сделать четко "0" или другое число.<br><br>

<a id="w117"></a>
<b>117. spinBox_points_corrFIGS</b> (QSpinBox)<br>
Размер точек для корреляционного графика.<br><br>

<a id="w118"></a>
<b>118. doubleSpinBox_corr_figs_fontscale</b> (QDoubleSpinBox)<br>
Относительный размер шрифта для графика.<br><br>

<a id="w119"></a>
<b>119. check_sort_or_not_corr_figs</b> (QCheckBox)<br>
Сортировать значения в группе?<br><br>

<a id="w120"></a>
<b>120. check_setka</b> (QCheckBox)<br>
Включить сетку?<br><br>

#### 4.1.4. Матрица рассеяния

![Матрица рассеяния](figs/tab_L3_I3__.png)
*Скриншот 4.1.4: вкладка — Матрица рассеяния*. 

<a id="w121"></a>
<b>121. check_pairplot</b> (QCheckBox)<br>
<html><head/><body><p>Не учитвать группу в матрице рассеяния? </p><p>В этом случае все категории будут объеденены.</p></body></html><br><br>

#### 4.1.5. Распределение по двум параметрам

![Распределение по двум параметрам](figs/tab_L3_I4____.png)
*Скриншот 4.1.5: вкладка — Распределение по двум параметрам*. 

<a id="w122"></a>
<b>122. comboBox_color_jointplot</b> (QComboBox)<br>
Цветовая палитра для графика распределение по двум параметрам.<br><br>

<a id="w123"></a>
<b>123. comboBox_pairplot_jointplot</b> (QComboBox)<br>
Возможные настройки по отображению распределений.<br><br>

<a id="w124"></a>
<b>124. comboBox_style_jointplot</b> (QComboBox)<br>
Стиль графика. Используются стили seaborn.<br><br>

<a id="w125"></a>
<b>125. spinBox_point_size_for_jointplot</b> (QSpinBox)<br>
Размер точек на графике.<br><br>

#### 4.1.6. Корреляция одного параметра

![Корреляция одного параметра](figs/tab_L3_I5___.png)
*Скриншот 4.1.6: вкладка — Корреляция одного параметра*. 

<a id="w126"></a>
<b>126. comboBox_correlation_one_parameter</b> (QComboBox)<br>
Метод расчета корреляций: Пирсон, Спирмен или Кендал.<br><br>

<a id="w127"></a>
<b>127. doubleSpinBox_size_for_one_correlation</b> (QDoubleSpinBox)<br>
Относительный размер шрифта для корреляции одного параметра.<br><br>

<a id="w128"></a>
<b>128. doubleSpinBox_one_correlation</b> (QDoubleSpinBox)<br>
Отсечка по корреляциям. Все корреляции, которые ниже заданного числа, не будут учитываться.<br><br>

<a id="w129"></a>
<b>129. check_corr_one_parameter_plot_sep_wind</b> (QCheckBox)<br>
<html><head/><body><p>Построить график в отдельном окне?</p><p>Используйте, только если запускаете приложение не через десктопную версию.</p></body></html><br><br>

### 4.2. Микрореологический профиль

![Микрореологический профиль](figs/tab_L2_I1__.png)
*Скриншот 4.2: вкладка — Микрореологический профиль*. 

<a id="w130"></a>
<b>130. path_for_profile</b> (QLineEdit)<br>
Путь к папке, в которую будут сохранены микрореологические профили.<br><br>

<a id="w131"></a>
<b>131. patient_data</b> (QLineEdit)<br>
<html><head/><body><p>Данные пациента.</p><p>Должны быть скопированы из excel и вставлены в данную ячейку.</p><p>Должно быть скопировано 3 столбца, к примеру:</p><p><br/></p><table border="0" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; border-collapse:collapse;" cellspacing="2" cellpadding="0"><thead><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">Параметр</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">Среднее</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">SD</span></p></td></tr></thead><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">CSS, мПа</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">300</span></p></td><td style=" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">15</span></p></td></tr><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">AI, %</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">62</span></p></td><td style=" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">5</span></p></td></tr><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">AMP</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">0,06</span></p></td><td style=" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">0.01</span></p></td></tr></table><p><br/></p><p><span style=" font-family:'Helvetica';">Параметры должны обязательно называться одинаково для нормы и пациента.</span></p><p><span style=" font-family:'Helvetica';">Называться параметры могут произвольно. Latex поддерживается.</span></p></body></html><br><br>

<a id="w132"></a>
<b>132. norm_data</b> (QLineEdit)<br>
<html><head/><body><p>Данные нормы.</p><p>Должны быть скопированы из excel и вставлены в данную ячейку.</p><p>Должно быть скопировано 3 столбца, к примеру:</p><p><br/></p><table border="0" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; border-collapse:collapse;" cellspacing="2" cellpadding="0"><thead><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">Параметр</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">Среднее</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-top:7px; border-bottom:1px; border-top-color:#000000; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">SD</span></p></td></tr></thead><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">CSS, мПа</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">300</span></p></td><td style=" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">15</span></p></td></tr><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">AI, %</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">62</span></p></td><td style=" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">5</span></p></td></tr><tr><td style=" padding-left:0; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">AMP</span></p></td><td style=" padding-left:16; padding-right:16; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">0,06</span></p></td><td style=" padding-left:16; padding-right:0; padding-top:10; padding-bottom:10; border-bottom:1px; border-bottom-color:#000000; border-bottom-style:solid;"><p><span style=" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:16px; color:#0f1115;">0.01</span></p></td></tr></table><p><br/></p><p><span style=" font-family:'Helvetica';">Параметры должны обязательно называться одинаково для нормы и пациента.</span></p><p><span style=" font-family:'Helvetica';">Называться параметры могут произвольно. Latex поддерживается.</span></p></body></html><br><br>

<a id="w133"></a>
<b>133. profile_title_rad</b> (QLineEdit)<br>
<html><head/><body><p>Название для радиального профиля.</p></body></html><br><br>

<a id="w134"></a>
<b>134. profile_title_lin</b> (QLineEdit)<br>
Название для оси для линейного профиля.<br><br>

<a id="w135"></a>
<b>135. check_profile_legend</b> (QCheckBox)<br>
Вставить легенду?<br><br>

<a id="w136"></a>
<b>136. comboBox_profile_lin_spin</b> (QComboBox)<br>
Вращать подписи для линейного профиля?<br><br>

<a id="w137"></a>
<b>137. doubleSpinBoX_profile</b> (QDoubleSpinBox)<br>
Относительный размер шрифта на графиках.<br><br>

<a id="w138"></a>
<b>138. patient_prof</b> (QLineEdit)<br>
Имя пациента/образца.<br><br>

<a id="w139"></a>
<b>139. color_for_patient</b> (QLineEdit)<br>
Цвет для пациента. Используются только цвета HEX.<br><br>

<a id="w140"></a>
<b>140. check_profile_pat_line</b> (QCheckBox)<br>
Пациент -- добавить линию на графике.<br><br>

<a id="w141"></a>
<b>141. check_profile_pat_sd</b> (QCheckBox)<br>
Пациент -- добавить область с стандартным отклонением на графике.<br><br>

<a id="w142"></a>
<b>142. norm_prof</b> (QLineEdit)<br>
Имя для нормы.<br><br>

<a id="w143"></a>
<b>143. color_for_norm</b> (QLineEdit)<br>
Цвет для нормы. Используются только цвета HEX.<br><br>

<a id="w144"></a>
<b>144. check_profile_norm_line</b> (QCheckBox)<br>
Норма -- добавить линию на графике.<br><br>

<a id="w145"></a>
<b>145. check_profile_norm_sd</b> (QCheckBox)<br>
Норма -- добавить область с стандартным отклонением на графике.<br><br>

<a id="w146"></a>
<b>146. btn_plot_and_save_profile</b> (QPushButton)<br>
Построить и сохранить радиальный и линейный профили.<br><br>

<a id="w147"></a>
<b>147. check_profile_relative</b> (QCheckBox)<br>
Добавить значения относительных различий на радиальном графике?<br><br>

<a id="w148"></a>
<b>148. tableWidget</b> (QTableWidget)<br>
<html><head/><body><p>Интервал параметров нужно писать через тире. Индекс начинается с нуля, а не единицы.</p><p><span style=" font-style:italic;">Пример</span>: если всего 8 параметров, то можно сделать так:</p><p>(1 группа) &quot;0-3&quot;</p><p>(2 группа) &quot;4-5&quot;</p><p>(3 группа) &quot;6-7&quot;</p><p>Цвета: matplotlib.colors</p><p>Стиль линии: см. matplotlib </p><p><span style=" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#7a7e85;">solid, dashed, dashdot, dotted</span><br/></p></body></html><br><br>

### 4.3. Сводная таблица

![Сводная таблица](figs/tab_L2_I2__.png)
*Скриншот 4.3: вкладка — Сводная таблица*. 

<a id="w149"></a>
<b>149. path_for_pivot_table</b> (QLineEdit)<br>
Путь к папке, где лежит(ат) excel файл(ы) для сводных таблиц.<br><br>

<a id="w150"></a>
<b>150. comboBox_pivot_table</b> (QComboBox)<br>
Название excel файла -- подставится автоматически. Надо только выбрать<br><br>

<a id="w151"></a>
<b>151. comboBox_pivot_table_excel_sheet</b> (QComboBox)<br>
Название листа в excel файле -- подставится автоматически. Надо только выбрать<br><br>

<a id="w152"></a>
<b>152. comboBox_pivot_hue</b> (QComboBox)<br>
Выберете столбец для групп. Это категориальная группа. К примеру, "Пол".<br><br>

<a id="w153"></a>
<b>153. spinBox_pivot_table</b> (QSpinBox)<br>
Округлить значения до выбранного знака после запятой.<br><br>

<a id="w154"></a>
<b>154. comboBox_sd_or_se_pivot</b> (QComboBox)<br>
Погрешность SD или SE.<br><br>

<a id="w155"></a>
<b>155. btn_plot_and_save_pivot_table</b> (QPushButton)<br>
Получить и сохранить сводную таблицу.<br><br>

<a id="w156"></a>
<b>156. comboBox_correlation_person_or_not</b> (QComboBox)<br>
<html><head/><body><p>Метод расчета корреляций: Пирсон, Спирмен или Кендал.</p></body></html><br><br>

<a id="w157"></a>
<b>157. check_color_for_corr_pivot</b> (QCheckBox)<br>
Выделить ячейки цветом?<br><br>

<a id="w158"></a>
<b>158. comboBox_correlation_color_map</b> (QComboBox)<br>
Цветовая схема для корреляционной матрицы?<br><br>

<a id="w159"></a>
<b>159. btn_plot_and_save_corr_table</b> (QPushButton)<br>
<html><head/><body><p>Получить и сохранить корреляционную матрицу по всем данным.</p><p>Используются все столбцы для анализа.</p></body></html><br><br>

<a id="w160"></a>
<b>160. comboBox_index_data_or_raw</b> (QComboBox)<br>
<html><head/><body><p>Перевести таблицу из широкого к длинному формату или наоборот.</p><p>Под <span style=" font-style:italic;">индексируемыми</span> полагается -- длинный формат.</p><p>Под <span style=" font-style:italic;">сырым</span> -- широкий формат.</p></body></html><br><br>

<a id="w161"></a>
<b>161. btn_save_pivot_or_melt</b> (QPushButton)<br>
<html><head/><body><p>Перевести данные из широкого в длинный формат или наоборот и сохранить excel файл.</p></body></html><br><br>

### 4.4. Catplot

![Catplot](figs/tab_L2_I3_Catplot.png)
*Скриншот 4.4: вкладка — Catplot*. Построение графика catplot. Используется только данные в 'длинном' формате.

<a id="w162"></a>
<b>162. path_for_catplot</b> (QLineEdit)<br>
Путь к папке с excel файлом<br><br>

<a id="w163"></a>
<b>163. comboBox_excel_catplot</b> (QComboBox)<br>
Название excel файла -- подставится автоматически. Надо только выбрать<br><br>

<a id="w164"></a>
<b>164. comboBox_excel_sheet_catplot</b> (QComboBox)<br>
Название листа в excel файле -- подставится автоматически. Надо только выбрать<br><br>

<a id="w165"></a>
<b>165. comboBox_catplot_x</b> (QComboBox)<br>
<html><head/><body><p>Основная группа, в которой представлены категории.</p><p>К примеру, группа &quot;Диагноз&quot;.</p></body></html><br><br>

<a id="w166"></a>
<b>166. comboBox_catplot_form_x</b> (QComboBox)<br>
<html><head/><body><p>Явно привести тип для группы по оси X в заданный тип.</p></body></html><br><br>

<a id="w167"></a>
<b>167. comboBox_catplot_y</b> (QComboBox)<br>
<html><head/><body><p>Таргетный параметры для вывода на ось Y.</p><p>К примеру, &quot;Сила агрегации&quot;. </p><p>Обычно подразумевается, что значения в данном параметре:</p><p>- float</p><p>- int</p><p> То есть непрерывные или дискретные.</p></body></html><br><br>

<a id="w168"></a>
<b>168. comboBox_catplot_form_y</b> (QComboBox)<br>
<html><head/><body><p>Явно привести тип для значений по оси Y в заданный тип.</p></body></html><br><br>

<a id="w169"></a>
<b>169. comboBox_catplot_hue</b> (QComboBox)<br>
<html><head/><body><p>Дополнительная подгруппа в группе.</p><p>К примеру, группа может быть &quot;Диагноз&quot;, а подгруппа &quot;Пол&quot;.</p><p>На графике будут всевозможные комбинации категорий из двух групп.</p></body></html><br><br>

<a id="w170"></a>
<b>170. comboBox_catplot_form_hue</b> (QComboBox)<br>
<html><head/><body><p>Явно привести тип для подгруппы в заданный тип.</p></body></html><br><br>

<a id="w171"></a>
<b>171. doubleSpinBox_catplot</b> (QDoubleSpinBox)<br>
Относительный размер шрифта.<br><br>

<a id="w172"></a>
<b>172. comboBox_color_catplot</b> (QComboBox)<br>
Цветовая палитра для catplot.<br><br>

<a id="w173"></a>
<b>173. comboBox_template_catplot</b> (QComboBox)<br>
<html><head/><body><p>Шаблон для графика:</p><p>1. strip - точечный график, показывает все точки данных с легким разбросом по горизонтали чтобы избежать перекрытия</p><p>2. swarm - точечный график без перекрытия, точки располагаются плотно, сохраняя положение по оси Y</p><p>3. box - боксплот, показывает медиану, квартили, выбросы и разброс данных</p><p>4. violin - график плотности, показывает распределение данных и его форму</p><p>5. boxen - улучшенный боксплот для больших наборов данных, показывает больше квантилей</p><p>6. point - график со средними значениями и доверительными интервалами, соединяет точки линиями</p><p>7. bar - столбчатая диаграмма со средними значениями и доверительными интервалами</p></body></html><br><br>

<a id="w174"></a>
<b>174. comboBox_catplot_SD_or_not</b> (QComboBox)<br>
Погрешности для вывода: SD, SE, доверительный или перцентильный интервал.<br><br>

<a id="w175"></a>
<b>175. spinBox_catplot_angle</b> (QSpinBox)<br>
Вращать подписи на заданный угол.<br><br>

<a id="w176"></a>
<b>176. check_stat_znachimost_catplot</b> (QCheckBox)<br>
Рассчитать статистическую значимость?<br><br>

<a id="w177"></a>
<b>177. comboBox_stat_test_catplot</b> (QComboBox)<br>
Статистический тест для расчета статистической значимости для catplot.<br><br>

<a id="w178"></a>
<b>178. check_stat_znachimost_catplot_inside_subgroup</b> (QCheckBox)<br>
Рассчитать статистическую значимость только внутри подгруппы?<br><br>

<a id="w179"></a>
<b>179. comboBox_catplot_stat_formatt</b> (QComboBox)<br>
<html><head/><body><p>Формат подписей для стат. значимости:</p><p>Один из трех:</p><p>- звездочка (*)</p><p>- точное значение p (p=0.03)</p><p>- относительное p (p&lt;0.05)</p><p>Статистическая значимость для здездочек обозначается следующим:</p><p>* p&lt;0.05, ** p&lt;0.01, *** p&lt;0.001, **** p&lt;0.0001</p><p>Данная расшифровка сохраняется в txt файл рядом с рисунком.</p></body></html><br><br>

<a id="w180"></a>
<b>180. comboBox_catplot_mult_stat</b> (QComboBox)<br>
<html><head/><body><p>Поправка на множественную проверку гипотез. Важно когда много попарных сравнений.</p></body></html><br><br>

<a id="w181"></a>
<b>181. btn_plot_and_save_catplot</b> (QPushButton)<br>
Построить график catplot и сохранить png файл.<br><br>

### 4.5. Обработка RheoScan

![Обработка RheoScan](figs/tab_L2_I4__RheoScan.png)
*Скриншот 4.5: вкладка — Обработка RheoScan*. Доп. обработка данных, полученных с помощью данной программы.

<a id="w182"></a>
<b>182. path_for_RheoScan_describe</b> (QLineEdit)<br>
<html><head/><body><p>Путь папке к excel файлу или файлам, которые были получены путем расчета из первой вкладки.</p><p>Важно, что будут рассмотрены все excel файлы из папки.</p></body></html><br><br>

<a id="w183"></a>
<b>183. toolButton_RheoScan</b> (QToolButton)<br>
<html><head/><body><p>Выбрать папку, в которой лежат excel файлы интерактивно.</p></body></html><br><br>

<a id="w184"></a>
<b>184. comboBox_RheoScan_describe</b> (QComboBox)<br>
<html><head/><body><p>Можно выбрать следующее: </p><p>1. Либо у вас есть много файлов, где каждый файл -- это измерения по одному образцу/пациенту.</p><p>2. Либо у вас один файл, <span style=" text-decoration: underline;">где первая колонка соответствует названию образца или ФИО пациента</span>. Важно, чтобы это была первая колонка.</p></body></html><br><br>

<a id="w185"></a>
<b>185. RheoScan_describe_mask_sheets</b> (QLineEdit)<br>
<html><head/><body><p>Возможность расчета/игнорирование SD на разных листах.</p><p>По дефолту SD расчитывается для всех листов excel.</p><p>По сути это маска, которая должна состоять из:</p><p><span style=" font-weight:700;">положительных</span> -- оставить SD  -- <span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;y&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;yes&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;t&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;true&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;on&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;1&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">)</span></p><p>или</p><p><span style=" font-weight:700;">отрицательных</span> -- убрать SD -- <span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">(</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;n&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;no&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;f&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;false&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;off&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">, </span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;0&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">)</span></p><p>К примеру, если у вас 3 листа и нужно только для первых двух посчитать SD, а для третьего -- НЕТ, то нужно ввести:</p><p>&quot;1 1 0&quot; -- ввести без кавычек.</p></body></html><br><br>

<a id="w186"></a>
<b>186. btn_RheoScan_describe_file_or_files</b> (QPushButton)<br>
<html><head/><body><p>Рассчитать средние значения и SD для файла или файлов и сохранить данные в excel файл.</p></body></html><br><br>

<a id="w187"></a>
<b>187. path_for_rheoscan_report</b> (QLineEdit)<br>
Путь к папке с excel файлом<br><br>

<a id="w188"></a>
<b>188. comboBox_rheoscan_report</b> (QComboBox)<br>
Название excel файла -- подставится автоматически. Надо только выбрать<br><br>

<a id="w189"></a>
<b>189. calendarWidget_rheoscan_report</b> (QCalendarWidget)<br>
Дата измерения.<br><br>

<a id="w190"></a>
<b>190. rheoscan_report_name_exp</b> (QLineEdit)<br>
<html><head/><body><p>ФИО того, кто проводил эксперимент.</p></body></html><br><br>

<a id="w191"></a>
<b>191. rheoscan_report_name_process</b> (QLineEdit)<br>
<html><head/><body><p>ФИО того, кто обрабатывал данные.</p></body></html><br><br>

<a id="w192"></a>
<b>192. rheoscan_report_parameters_dict</b> (QPlainTextEdit)<br>
<html><head/><body><p>Здесь нужно в виде Python словаря ввести переименование параметров.</p><p>К примеру, в excel файле параметр индекса агрегации называется &quot;AI&quot;, а в отчете мы хотим видеть &quot;AI, %&quot;.</p><p>К примеру:</p><p>{&quot;AI&quot;:&quot;AI, %&quot;, &quot;CSS&quot;:&quot;CSS, мПа&quot;, &quot;T1/2&quot;: &quot;T1/2, сек.&quot;}</p></body></html><br><br>

<a id="w193"></a>
<b>193. btn_make_rheoscan_report</b> (QPushButton)<br>
Сделать отчет по одному образцу/пациенту и сохранить его в pdf.<br><br>

### 4.6. Доп. обработка

![Доп. обработка](figs/tab_L2_I5_._.png)
*Скриншот 4.6: вкладка — Доп. обработка*. 

<a id="w194"></a>
<b>194. path_for_dop_stat</b> (QLineEdit)<br>
Путь к папке с excel файлом<br><br>

<a id="w195"></a>
<b>195. comboBox_excel_dop_stat</b> (QComboBox)<br>
Название excel файла -- подставится автоматически. Надо только выбрать<br><br>

<a id="w196"></a>
<b>196. comboBox_excel_sheet_dop_stat</b> (QComboBox)<br>
<html><head/><body><p>Название листа в excel файле -- подставится автоматически. Надо только выбрать</p></body></html><br><br>

<a id="w197"></a>
<b>197. comboBox_dop_stat_x</b> (QComboBox)<br>
Колонка №1/2 для выбора.<br><br>

<a id="w198"></a>
<b>198. comboBox_dop_stat_y</b> (QComboBox)<br>
Колонка №2/2 для выбора.<br><br>

<a id="w199"></a>
<b>199. comboBox_stat_test_dop_stat</b> (QComboBox)<br>
<html><head/><body><p>Статистический тест для выбора.</p><p>Не используйте пермутационные тесты, если у вас много значений в колонках.</p></body></html><br><br>

<a id="w200"></a>
<b>200. comboBox_alter_hep_dop_stat</b> (QComboBox)<br>
Альтернативная гипотеза.<br><br>

<a id="w201"></a>
<b>201. p_value_dop_stat</b> (QLineEdit)<br>
<html><head/><body><p>Выводимое значение p.</p></body></html><br><br>

<a id="w202"></a>
<b>202. btn_dop_stat_calc</b> (QPushButton)<br>
Рассчитать статистическую значимость между двумя столбцами.<br><br>

#### 4.6.1. Рассчитать стат. значимость между 2 выборками

![Рассчитать стат. значимость между 2 выборками](figs/tab_L3_I0__.___2_.png)
*Скриншот 4.6.1: вкладка — Рассчитать стат. значимость между 2 выборками*. 

<a id="w203"></a>
<b>203. path_for_dop_stat</b> (QLineEdit)<br>
Путь к папке с excel файлом<br><br>

<a id="w204"></a>
<b>204. comboBox_excel_dop_stat</b> (QComboBox)<br>
Название excel файла -- подставится автоматически. Надо только выбрать<br><br>

<a id="w205"></a>
<b>205. comboBox_excel_sheet_dop_stat</b> (QComboBox)<br>
<html><head/><body><p>Название листа в excel файле -- подставится автоматически. Надо только выбрать</p></body></html><br><br>

<a id="w206"></a>
<b>206. comboBox_dop_stat_x</b> (QComboBox)<br>
Колонка №1/2 для выбора.<br><br>

<a id="w207"></a>
<b>207. comboBox_dop_stat_y</b> (QComboBox)<br>
Колонка №2/2 для выбора.<br><br>

<a id="w208"></a>
<b>208. comboBox_stat_test_dop_stat</b> (QComboBox)<br>
<html><head/><body><p>Статистический тест для выбора.</p><p>Не используйте пермутационные тесты, если у вас много значений в колонках.</p></body></html><br><br>

<a id="w209"></a>
<b>209. comboBox_alter_hep_dop_stat</b> (QComboBox)<br>
Альтернативная гипотеза.<br><br>

<a id="w210"></a>
<b>210. p_value_dop_stat</b> (QLineEdit)<br>
<html><head/><body><p>Выводимое значение p.</p></body></html><br><br>

<a id="w211"></a>
<b>211. btn_dop_stat_calc</b> (QPushButton)<br>
Рассчитать статистическую значимость между двумя столбцами.<br><br>

#### 4.6.2. Кластеризация признаков

![Кластеризация признаков](figs/tab_L3_I1__.png)
*Скриншот 4.6.2: вкладка — Кластеризация признаков*. 

<a id="w212"></a>
<b>212. path_for_excel_cluster</b> (QLineEdit)<br>
Путь к папке с excel файлом для кластеризации признаков по корреляции.<br><br>

<a id="w213"></a>
<b>213. comboBox_cluster_file</b> (QComboBox)<br>
Название excel файла -- подставится автоматически. Надо только выбрать<br><br>

<a id="w214"></a>
<b>214. comboBox_cluster_excel_sheet</b> (QComboBox)<br>
Название листа в excel файле -- подставится автоматически. Надо только выбрать<br><br>

<a id="w215"></a>
<b>215. spinBox_cluster_n</b> (QSpinBox)<br>
Кол-во класстеров для выделения.<br><br>

<a id="w216"></a>
<b>216. comboBox_cluster_coord</b> (QComboBox)<br>
Координаты пространства для 2D отображения: MDS или PSA.<br><br>

<a id="w217"></a>
<b>217. spinBox_cluster_buble_size</b> (QSpinBox)<br>
Размер пузырьков на графике.<br><br>

<a id="w218"></a>
<b>218. btn_cluster_save_file</b> (QPushButton)<br>
Сделать кластеризацию и сохранить график.<br><br>

## 5. Доп.настройки

![Доп.настройки](figs/tab_L1_I4_..png)
*Скриншот 5: вкладка — Доп.настройки*. Автозаполнение полей приложения из JSON файла.

<a id="w219"></a>
<b>219. lineEdit_json_load</b> (QLineEdit)<br>
Полный путь к JSON файлу<br><br>

<a id="w220"></a>
<b>220. btn_json_load</b> (QPushButton)<br>
<html><head/><body><p>Подгрузить настройки из JSON файла. </p><p>Это может быть полезно, если у вас есть готовый шаблон настроек для построения графиков и обработки и вам не хочется каждый раз при открытии приложения изменять настройки.</p><p>JSON файл должен быть по типу:</p><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">{</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">&quot;rheoscan_report_name_exp&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">:</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;ФИО&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">,</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">&quot;rheoscan_report_parameters_dict&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">:{</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">&quot;AAA&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">:</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#ce9178;">&quot;aaa&quot;</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">   },</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">&quot;check_approx_agg&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">:</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;">true</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">,</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;"/><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#9cdcfe;">&quot;check_approx_deform&quot;</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">:</span><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#569cd6;">true</span></pre><pre style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#1f1f1f;"><span style=" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:12px; color:#cccccc;">}</span></pre><p>То есть ключ -- это имя объекта (в документации явно указано в подзаголовках), значение -- значение, которое в данное поле подставить.</p></body></html><br><br>

