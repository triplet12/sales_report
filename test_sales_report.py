from sales_report import build_report

def test_normal(tmp_path):
    csv_file = tmp_path / 'sales.csv'
    csv_file.write_text('date,product,quantity,price\n' \
    '2026-10-01,Кофе,3,200\n' \
    '2026-10-02,Кофе,1,200\n' \
    '2026-10-01,Кофе,3,200\n' \
    '2026-10-01,Чай,2,150\n' \
    '2026-10-03,Круассан,4,150' , encoding='utf-8')

    report = build_report(csv_file)
    assert report.get('invalid_rows') == []


def test_all_rows_invalid(tmp_path):
    csv_file = tmp_path / 'sales.csv'
    csv_file.write_text('date,product,quantity,price\n' \
    '2026-10-01,,3,200\n' \
    '2026-10-01,Чай,2,0\n' \
    '2026-10-02,Кофе,-1,200\n' \
    '2026-10-02,Круассан,abc,180' , encoding='utf-8')

    report = build_report(csv_file)
    assert report.get('invalid_rows') == [2,3,4,5]
    