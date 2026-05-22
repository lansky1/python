# Scope & Globals

Python looks for variable names using the **LEGB** rule:

| Scope | Where |
|---|---|
| **L**ocal | Names inside the current function |
| **E**nclosing | Names in outer functions when functions are nested |
| **G**lobal | Names at the top level of the current file/module |
| **B**uilt-in | Names Python provides automatically (`print`, `len`, `sum`, …) |

## Default: local on assignment

A variable assigned inside a function is local to that function by default.

## `global`

The `global` keyword lets a function reassign a variable from the global/module scope.

```python
counter = 0

def bad_increment():
    global counter
    counter += 1
```

## `nonlocal`

The `nonlocal` keyword lets a nested function reassign a variable from an enclosing function scope.

```python
def make_counter():
    count = 0
    def step():
        nonlocal count
        count += 1
        return count
    return step
```

## Prefer returning over mutating

> **Avoid `global` when possible**
>
> `global` makes functions depend on outside state and makes code harder to reason about. Prefer returning the new value from the function and assigning it back outside the function.


```python
count = 0

def increase_count(count):
    return count + 1

count = increase_count(count)
```
