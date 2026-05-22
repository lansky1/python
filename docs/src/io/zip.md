# Zip Archives

## Create temporary files for the demo

```python
with open('fileone.txt', 'w+') as f:
    f.write('ONE FILE')

with open('filetwo.txt', 'w+') as f:
    f.write('TWO FILE')
```

## Using `zipfile`

```python
import zipfile

with zipfile.ZipFile('compressed_folder.zip', 'w') as compressed_file:
    compressed_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
    compressed_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)

with zipfile.ZipFile('compressed_folder.zip', 'r') as unzipped_folder:
    unzipped_folder.extractall('extracted_folder')
```

## Using `shutil`

```python
import shutil

shutil.make_archive('compressed_file', 'zip', 'extracted_folder')
shutil.unpack_archive('compressed_file.zip', 'extracted_folder', 'zip')
```

`shutil.make_archive(base_name, format, root_dir)` archives the **contents** of `root_dir` into `base_name.<ext>`.
