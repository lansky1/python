# Error Handling & Testing

## try / except / else / finally

```python
try:
    result = 10 + 10
# except:                  # Do not use bare except
#     print("Something went wrong!")
except Exception:
    print("Something went wrong!")
else:
    print("Add went well!")
    print(result)
```

```python
try:
    file = open("test.txt")
except FileNotFoundError:
    print("No file")
else:
    print(file.read())
finally:
    print("Done")
```

| Block | Runs when |
| --- | --- |
| `try` | Always — protected code |
| `except` | Only if a matching exception is raised inside `try` |
| `else` | Only when `try` finished **without** raising |
| `finally` | Always — for cleanup that must happen either way |

## Unit Testing

A test checks whether a function gives the expected result. If the expected and actual values do not match, the test fails.

Python ships with `pylint` (linting) and `unittest` (testing) — no extra installs needed.

```python
import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_and_positive_numbers(self):
        self.assertEqual(add_numbers(-1, 1), 0)

unittest.main(argv=[''], exit=False)
```

> `argv=['']` tells `unittest` to ignore Jupyter's hidden command-line arguments. `exit=False` prevents `unittest` from stopping the notebook kernel after the tests finish.

## Running pylint from a script

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

The `sys.executable` form is the most portable — it uses the same Python interpreter that's running your script, even if `pylint` isn't on `PATH`.
