# Modules & Packages

## Script entry points

- Every Python file has a `__name__` value.
- When a file is **run directly**, Python sets `__name__` to `"__main__"`.
- When a file is **imported**, `__name__` becomes the module's name instead.
- Use `if __name__ == "__main__":` to run code only during direct execution, not during import.

This helps organize code so functions/classes stay reusable, while script-specific code stays in one clear entry point.

- Keep reusable code **outside** the block: functions, classes, constants.
- Keep script-only code **inside** the block: `main()` calls, `input()`, final output, demos, file reading, command-line arguments.

This prevents another file from accidentally starting the whole program just because it imported one function.

```python
def greet(name):
    return f"Hello, {name}"

def main():
    name = input("Name: ")
    print(greet(name))

if __name__ == "__main__":
    main()
```

## Packages

A **package** is a directory containing an `__init__.py` (which may be empty). Sub-packages nest the same way.

```
MainPackage/
    __init__.py
    some_main_script.py
    SubPackage/
        __init__.py
        mysubscript.py
```

Importing from packages:

```python
from MainPackage import some_main_script
from MainPackage.SubPackage import mysubscript
```

## Running external commands

```python
import os
os.system("pylint test.py")
```

```python
import subprocess
subprocess.run(["pylint", "test.py", "-r", "y"])
```

```python
import subprocess
import sys
subprocess.run([sys.executable, "-m", "pylint", "test.py", "-r", "y"])
```

Using `sys.executable` ensures the subprocess uses the **same Python interpreter** as the parent — important inside virtual environments.
