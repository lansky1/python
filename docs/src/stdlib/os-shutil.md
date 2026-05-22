# OS & Shutil

## `os`

```python
import os

print(os.getcwd())
print(os.listdir())  # provide a path for other directories
```

### Walking a directory tree

```python
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    ...
```

## `shutil`

```python
import shutil

# shutil.move(src, dst)   — moves or renames
# os.unlink(path)         — deletes a file
# os.rmdir(path)          — deletes an empty folder
# shutil.rmtree(path)     — removes a folder and all its contents
```

> **Send to trash, not /dev/null**
>
> Use the [`send2trash`](https://pypi.org/project/Send2Trash/) third-party module to move files to the recycle bin instead of permanent deletion.


## `pathlib` (modern alternative)

Prefer `pathlib.Path` for new code:

```python
from pathlib import Path

cwd = Path.cwd()
for entry in cwd.iterdir():
    print(entry.name, entry.is_dir())

(cwd / "out").mkdir(exist_ok=True)
(cwd / "notes.txt").write_text("hello")
```
