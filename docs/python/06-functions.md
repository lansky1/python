# Functions

## Function vs Method

- **Function**: reusable block of code called directly by name.
- **Method**: function attached to an object or class, called using dot notation.

## `*args` and `**kwargs`

- Positional arguments (`*args`) are collected as a **tuple**.
- Keyword arguments (`**kwargs`) are collected as a **dictionary**.
- The `*` symbol is what does the collecting; the name `args` is convention only.

```python
def func(normal_args, *args, keyword_only=None, **kwargs):
    pass
```

A **keyword-only parameter** (after `*args`) can only be passed by explicitly naming it in the call.

```python
def my_func(*args):
    return sum(args)

print(my_func(2, 3))    # 5
# print(sum(2, 3))      # TypeError — sum expects an iterable
```

## Lambda Expressions, Map, and Filter

```python
def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]

print([square(num) for num in my_nums])       # list comprehension (preferred)
print(list(map(square, my_nums)))              # map — returns iterator
```

```python
my_numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda num: num % 2 == 0, my_numbers)))  # [2, 4, 6]
print(list(map(lambda num: num ** 2, my_nums)))            # squares
```

- `map(func, iterable)` transforms every item.
- `filter(func, iterable)` keeps items where `func` returns true.
- `lambda` is an anonymous, single-expression function — fine for a quick callback, but a `def` is clearer once the body grows.

## Why prefer comprehensions over `map`/`filter`

Comprehensions read top-to-bottom: "what to keep, then where it comes from, then under what condition". `map`/`filter` chain function calls and require you to wrap them in `list(...)` to materialize. Reach for `map`/`filter` mostly when you already have a named function that fits.
