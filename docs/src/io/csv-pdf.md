# CSV & PDF

## CSV files

CSV files contain raw tabular data. Use the built-in `csv` module, or one of `pandas`, `openpyxl` (Excel), or the Google Sheets Python API for richer needs.

```python
import csv

data = open('example.csv')  # add encoding='utf-8' if UnicodeDecodeError
csv_data = csv.reader(data)
data_lines = list(csv_data)
data.close()
```

Writing:

```python
with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['Sam', 30])
```

## PDF files

```python
import pypdf

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = pypdf.PdfReader(f)

pdf_reader.get_num_pages()

page_one = pdf_reader.get_page(0)
page_one_text = page_one.extract_text()
print(page_one_text)

f.close()
```

Writing: use `pypdf.PdfWriter` to add pages, then write to a new file.
