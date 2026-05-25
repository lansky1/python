# Modules & Scope

## Scope and the LEGB Rule

Python looks for variable names using the **LEGB** rule:

- **L**ocal — names inside the current function.
- **E**nclosing — names in outer functions when functions are nested.
- **G**lobal — names at the top level of the current file/module.
- **B**uilt-in — names Python provides automatically, like `print`, `len`, and `sum`.

A variable assigned inside a function is local to that function by default.

- The `global` keyword lets a function reassign a variable from the global/module scope.
- The `nonlocal` keyword lets a nested function reassign a variable from an enclosing function scope.

> Avoid `global` when possible. It makes functions depend on outside state and harder to reason about.

Prefer returning the new value from the function and assigning it back outside the function:

```python
count = 0

def increase_count(count):
    return count + 1

count = increase_count(count)
```

## Modules and Script Entry Points

- Every Python file has a `__name__` value.
- When a file is run directly, Python sets `__name__` to `"__main__"`.
- When a file is imported, `__name__` becomes the module's name instead.
- Use `if __name__ == "__main__":` to run code only during direct execution, not during import.
- This helps organize code so functions and classes stay reusable, while script-specific code stays in one clear entry point.

Keep reusable code outside this block:

- Functions, classes, constants.

Keep script-only code inside this block:

- Calling `main()`, user input, printing final output, demos, file reading, command-line argument handling.

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

## Object Identity (`is`)

The `is` operator checks for **object identity** — whether two variables refer to the exact same object in memory.

- `==` checks value equality (delegates to `__eq__`).
- `is` checks reference equality (no method dispatch).

Use `is` only with singletons like `None`, `True`, `False`:

```python
if x is None:
    ...
```

For everything else, prefer `==`. Small integers and short interned strings may share memory, but relying on that is unsafe.
