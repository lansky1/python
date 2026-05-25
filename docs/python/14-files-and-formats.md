# Files & Formats

## Plain Text Files

Create a file from a notebook cell with `%%writefile`:

```
%%writefile myfile.txt
Hello this is a text file
this is the second line
this is the third line
```

```python
myfile = open('myfile.txt')
myfile.read()
# 'Hello this is a text file\nthis is the second line\nthis is the third line\n'

myfile.read()
# ''   — cursor reached end-of-file
```

The cursor iterates to the end, so the next `read()` returns an empty string. Seek back to the start to read again:

```python
myfile.seek(0)   # 0
myfile.read()
# 'Hello this is a text file\nthis is the second line\nthis is the third line\n'
```

### `read()` vs `readline()` vs `readlines()`

| Method | Returns | Behavior |
| --- | --- | --- |
| `read()` | Single string | Reads the **entire** file |
| `readline()` | Single string | Reads ONE line (including `\n`) |
| `readlines()` | List of strings | Reads ALL lines into a list |

```python
myfile.seek(0)
myfile.readlines()
# ['Hello this is a text file\n',
#  'this is the second line\n',
#  'this is the third line\n']
```

```python
myfile.close()
```

For automatic closure, use `with`:

```python
with open('myfile.txt') as myfile:
    contents = myfile.read()
```

### File modes

| Mode | File must already exist? | Old content deleted on open? | Can read? | Can write? | Where writing happens |
| ---- | ------------------------ | ---------------------------- | --------- | ---------- | --------------------- |
| `r`  | Yes                      | No                           | Yes       | No         | Not allowed |
| `w`  | No                       | Yes                          | No        | Yes        | Starts from beginning after clearing |
| `a`  | No                       | No                           | No        | Yes        | Always at the end |
| `r+` | Yes                      | No                           | Yes       | Yes        | At current cursor position |
| `w+` | No                       | Yes                          | Yes       | Yes        | Starts from beginning after clearing |

```python
with open('myfile.txt', mode='w') as myfile:
    contents = myfile.read()
# UnsupportedOperation: not readable
```

`w` immediately truncates the file to 0 bytes as soon as it's opened.

```python
with open('myfile.txt', mode='r') as myfile:
    print(myfile.read())
```

## CSV Files

Use the built-in `csv` module for raw data. For larger or more shaped data, reach for `pandas`, `openpyxl` (Excel), or the Google Sheets Python API.

```python
import csv
```

```python
data = open('example.csv')   # add encoding='utf-8' to avoid UnicodeDecodeError
csv_data = csv.reader(data)
data_lines = list(csv_data)

# csv.writer.writerow(...) for the write path
```

## PDF Files

```python
import pypdf

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = pypdf.PdfReader(f)
pdf_reader.get_num_pages()        # 5

page_one = pdf_reader.get_page(0)
page_one_text = page_one.extract_text()
print(page_one_text)
```

To write PDFs, use `pypdf.PdfWriter` — add a page first and then write to disk.

```python
data.close()
f.close()
```

## Zipping and Unzipping Files

```python
f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()
```

### Using the standard `zipfile` library

```python
import zipfile

compressed_file = zipfile.ZipFile('compressed_folder.zip', 'w')
compressed_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()
```

```python
unzipped_folder = zipfile.ZipFile('compressed_folder.zip', 'r')
unzipped_folder.extractall('extracted_folder')
```

### Using `shutil` (one-liners)

```python
import shutil
shutil.make_archive('compressed_file', 'zip', 'extracted_folder')
shutil.unpack_archive('compressed_file.zip', 'extracted_folder', 'zip')
```
