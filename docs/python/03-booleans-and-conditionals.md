# Booleans & Conditionals

## Booleans

- `True`, `False`, `None`.
- Booleans are themselves a subclass of `int`: `True == 1`, `False == 0`.

> No need to manually return `True` or `False` when the condition already produces a boolean result. Return the boolean expression directly.

```python
def is_even(n):
    return n % 2 == 0    # not: if n % 2 == 0: return True else: return False
```

## Conditional Expressions

A conditional expression chooses between two values inline:

```python
def combo_string(a, b):
    short, long = (a, b) if len(a) < len(b) else (b, a)
    return short + long + short
```

### Tuple assignment evaluation order

In tuple assignment, the **complete right-hand side is evaluated before any left-hand assignment happens**. If one assigned value depends on another new value, store the new value in a temporary first.

### The walrus operator `:=`

`:=` assigns a value inside an expression. Use it sparingly — mainly when it avoids repeating the same calculation or lookup:

```python
if (n := len(data)) > 10:
    print(f"List is too long ({n} elements)")
```
