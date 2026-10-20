from pathlib import Path
from datetime import datetime
import csv
import json

def is_valid(row: list)->bool:
    try:
        datetime.strptime(row['date'], '%Y-%m-%d')
        str(row['product'])
        int(row['quantity'])
        int(row['price'])
    except (TypeError, ValueError, KeyError):
        return False
    if not row['product'] or int(row['quantity']) <= 0 or int(row['price']) <= 0:
        return False
    return True

def build_report(csv_path: Path)->dict:
    
    reader = csv.DictReader(csv_path.read_text('UTF-8').splitlines())

    product_revenue = {}
    product_sold_amount = {}
    invalid_rows = []

    total_revenue = 0

    for row_num,row in enumerate(reader, start=2):
        if not is_valid(row):
            invalid_rows.append(row_num)
            print(f'Обнаружена битая строка под номером {row_num}')
            continue

        product = row['product']
        quantity = int(row['quantity'])
        revenue = quantity * int(row['price'])

        total_revenue += revenue
        product_revenue[product] = product_revenue.get(product,0) + revenue
        product_sold_amount[product] = product_sold_amount.get(product, 0) + quantity

    if product_sold_amount:
        top_product = max(product_sold_amount, key=lambda product: product_sold_amount[product])
    else:
        top_product = None

    report = {
        'total_revenue' : total_revenue,
        'product_revenue': product_revenue,
        'top_product': top_product,
        'invalid_rows': invalid_rows
    }
    return report


def save_report(report: dict, json_path: Path) -> None:
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=4), 'UTF-8')

if __name__ == '__main__':
    report = build_report(Path('sales.csv'))
    save_report(report, Path('report.json'))