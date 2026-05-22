# Errors & Testing

## `try` / `except` / `else` / `finally`

```python
try:
    result = 10 + 10
except Exception:        # avoid bare `except:` — it catches KeyboardInterrupt too
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

| Block | When it runs |
|---|---|
| `try` | Always — its statements may raise |
| `except` | Only if an exception was raised and matched |
| `else` | Only if the `try` block completed without raising |
| `finally` | Always — even if an exception was raised or `return` was hit |

> **Never use bare `except:`**
>
> A bare `except:` catches **all** exceptions, including `KeyboardInterrupt` and `SystemExit`. Always specify the class — `except Exception:` at the broadest, more specific subclasses when you can.


## Unit testing

A test checks whether a function gives the expected result. If the expected and actual values do not match, the test fails.

Python ships with `unittest` (testing) and you can use `pylint` for linting.

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

> **Running unittest in Jupyter**
>
> `argv=['']` tells `unittest` to ignore Jupyter's hidden command-line arguments. `exit=False` prevents `unittest` from stopping the notebook kernel after the tests finish.

