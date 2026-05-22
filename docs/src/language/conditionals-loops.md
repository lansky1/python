# Conditionals & Loops

## Conditional expressions

A conditional expression can choose between two values inline:

```python
short, long = (a, b) if len(a) < len(b) else (b, a)
```

> **Tuple assignment evaluates RHS first**
>
> The complete right-hand side is evaluated **before** any left-hand side assignment happens. If one assigned value depends on another new value, store the new value in a temporary variable first.


## The walrus operator `:=`

The walrus operator assigns a value inside an expression. Use it sparingly — mainly when it avoids repeating the same calculation or lookup.

```python
if (n := len(data)) > 10:
    print(f"List is long ({n} items)")
```

## Truthiness

`bool(x)` converts a value into `True` or `False` based on truthiness. Empty containers (`[]`, `{}`, `""`, `set()`), `0`, `0.0`, and `None` are falsy. Everything else is truthy.

> **Return boolean expressions directly**
>
> No need to manually return `True` or `False` when the condition already produces a boolean.
>
> ```python
> # Don't
> if x > 0:
>     return True
> return False
>
> # Do
> return x > 0
> ```


## `for` and `while`

- A `for` loop controls its next value automatically.
- Use `while` when you need to manually change the loop index inside the loop.

## `else` on loops

Python supports an `else` block on `for` and `while`. The `else` block runs only when the loop finishes **normally** — not when it exits with `break`.

```python
for item in collection:
    if condition(item):
        break
else:
    print("never broke out")
```

## Sliding windows over slices

Use `range(len(value) - window_size + 1)` when checking slices of a fixed size:

```python
def cat_dog(s):
    count_cat = sum(1 for i in range(len(s) - 2) if s[i:i+3] == 'cat')
    count_dog = sum(1 for i in range(len(s) - 2) if s[i:i+3] == 'dog')
    return count_cat == count_dog
```

## `range`, `enumerate`, `zip`, `reversed`

- `range(stop)` or `range(start, stop, step)` — lazy integer sequence.
- `enumerate(iterable)` — pairs each item with its index.
- `zip(a, b, ...)` — loops through multiple sequences together; extra items from the longer iterable are discarded.
- `reversed(seq)` — iterate backwards without manually managing indexes.

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
    print(item)
# (1, 'a'), (2, 'b'), (3, 'c')

print(list(zip(list1, list2)))  # can also pass to set, tuple, dict
```
