# Отчет о продажах

Программа принимает файл sales.csv вида
```
date,product,quantity,price
2026-10-01,Кофе,3,200
2026-10-01,Чай,2,150
```

И создает/изменяет файл report.json
```
{
    "total_revenue": 900,
    "product_revenue": {
        "Кофе": 600,
        "Чай": 300
    },
    "top_product": "Кофе",
    "invalid_rows": []
}
```
___
## Установка
В консоле выполните 
```
pip install -r requirements.txt
```
## Запуск программы

Запустите файл sales_report.py
```
python sales_report.py
```
## Запуск тестов

В консоле выполните 
```
pytest
```