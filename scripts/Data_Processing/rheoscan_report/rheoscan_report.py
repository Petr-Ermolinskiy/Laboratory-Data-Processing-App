import base64  # noqa: D100, INP001
import io
from datetime import datetime

import matplotlib.pyplot as plt
from jinja2 import Template
from weasyprint import HTML


def create_pdf_microrheology_report(  # noqa: PLR0913
    path_to_save: str,
    surname: str,
    date_of_measurement: str,
    date_of_processing: str,
    exp_name: str,
    process_name: str,
    fig: plt.Figure,
    comments: str,
) -> None:
    """Создание отчета RheoScan."""
    # конвертируем рисунок base64 для вставки в HTML
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=200, bbox_inches="tight")
    buf.seek(0)
    figure_base64 = base64.b64encode(buf.read()).decode("utf-8")

    # настоящая дата
    date_of_report = datetime.now().strftime("%Y-%m-%d, %H:%M")  # noqa: DTZ005

    # темплейт html
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {
                size: A4;
                margin: 0;
            }
            body {
                font-family: 'Helvetica', Arial, sans-serif;
                margin: 0;
                padding: 0;
                width: 21cm;
                height: 29.7cm;
                position: relative;
                background: white;
            }
            .container {
                width: 100%;
                height: 100%;
                position: relative;
                box-sizing: border-box;
            }
            .header {
                background: linear-gradient(to right, #2C3E50, #4CA1AF);
                color: white;
                padding: 20px 30px;
                box-sizing: border-box;
            }
            .title-section {
                text-align: center;
                margin-bottom: 20px;
            }
            .main-title {
                font-size: 24px;
                font-weight: 300;
                margin: 0;
                letter-spacing: 1px;
            }
            .surname {
                font-size: 42px;
                font-weight: bold;
                margin: 5px 0 10px 0;
                letter-spacing: 2px;
            }
            .info-table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 15px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 5px;
                overflow: hidden;
                font-size: 13px;
            }
            .info-table th {
                background: rgba(0, 0, 0, 0.2);
                padding: 8px 15px;
                text-align: left;
                font-size: 12px;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            .info-table td {
                padding: 10px 15px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                font-size: 13px;
            }
            .info-table tr:last-child td {
                border-bottom: none;
            }
            .info-table .first-col {
                width: 15%;
                font-weight: 600;
            }
            .content {
                padding: 20px 30px;
                box-sizing: border-box;
                height: calc(100% - 240px); /* Adjust based on header and footer heights */
                overflow: hidden;
            }
            .section-title {
                color: #2C3E50;
                font-size: 20px;
                margin: 0 0 15px 0;
                padding-bottom: 8px;
                border-bottom: 2px solid #3498DB;
            }
            .figure-container {
                text-align: center;
                margin: 15px 0;
                padding: 15px;
                background: #f8f9fa;
                border-radius: 8px;
                border: 1px solid #e9ecef;
                box-sizing: border-box;
            }
            .figure-container img {
                max-width: 95%;
                height: auto;
                max-height: 250px;
                border-radius: 4px;
            }
            .figure-caption {
                margin-top: 8px;
                font-size: 12px;
                color: #666;
                font-style: italic;
            }
            .comments-section {
                background: #f8f9fa;
                padding: 15px 20px;
                border-radius: 8px;
                margin: 15px 0;
                border-left: 4px solid #3498DB;
                font-size: 14px;
                box-sizing: border-box;
                max-height: 180px;
                overflow-y: auto;
            }
            .comments-text {
                line-height: 1.5;
                color: #333;
                white-space: pre-wrap;
                margin: 0;
            }
            .footer {
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                background: #2C3E50;
                color: white;
                text-align: center;
                padding: 15px;
                font-size: 11px;
                box-sizing: border-box;
                width: 100%;
            }
            .scrollable-content {
                height: calc(100% - 40px); /* Adjust based on section titles */
                overflow-y: auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="title-section">
                    <div class="main-title">Результаты измерений</div>
                    <div class="surname">{{ surname }}</div>
                </div>

                <table class="info-table">
                    <tr>
                        <th class="first-col"></th>
                        <th>Эксперимент</th>
                        <th>Обработка данных</th>
                    </tr>
                    <tr>
                        <td class="first-col">Дата</td>
                        <td>{{ date_measurement }}</td>
                        <td>{{ date_processing }}</td>
                    </tr>
                    <tr>
                        <td class="first-col">Исполнитель</td>
                        <td>{{ exp_name }}</td>
                        <td>{{ process_name }}</td>
                    </tr>
                </table>
            </div>

            <div class="content">
                <div class="section-title">Микрореологический профиль</div>

                <div class="scrollable-content">
                    <div class="figure-container">
                        <img src="data:image/png;base64,{{ figure_data }}"
                             alt="Microrheology Analysis Figure" />
                        <div class="figure-caption"> </div>
                    </div>

                    <div class="section-title">Комментарий</div>

                    <div class="comments-section">
                        <p class="comments-text">{{ comments }}</p>
                    </div>
                </div>
            </div>

            <div class="footer">
                Конфеденциально • Создано автоматически • {{ date_report }}
            </div>
        </div>
    </body>
    </html>
    """

    # подготовка темплейта
    template_data = {
        "surname": surname.upper(),
        "date_measurement": date_of_measurement,
        "date_processing": date_of_processing,
        "date_report": date_of_report,
        "exp_name": exp_name,
        "process_name": process_name,
        "figure_data": figure_base64,
        "comments": comments,
    }

    # рендеринг
    template = Template(html_template)
    rendered_html = template.render(**template_data)

    # генерация pdf
    HTML(string=rendered_html).write_pdf(path_to_save)
    print(f"Отчет RheoScan создан: {path_to_save}")
