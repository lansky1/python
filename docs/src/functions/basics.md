# Function Basics

## Function vs method

- **Function** — a reusable block of code called directly by name.
- **Method** — a function attached to an object or class, called using dot notation.

## `*args` and `**kwargs`

- Positional arguments (`*args`) are collected as a **tuple**.
- Keyword arguments (`**kwargs`) are collected as a **dictionary**.
- The `*` symbol collects extra positional arguments; the name `args` is only a convention.

```python
def func(normal_args, *args, keyword_only=None, **kwargs):
    pass
```

A **keyword-only parameter** (after `*` or `*args`) can only be passed by explicitly naming it in the call.

```python
def my_func(*args):
    return sum(args)

print(my_func(2, 3))   # 5
# print(sum(2, 3))     # TypeError — sum expects an iterable
```

## Lambda, map, filter

```python
def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]

# List comprehension (preferred Pythonic way)
print([square(num) for num in my_nums])

# map() — applies function to every element, returns iterator
print(list(map(square, my_nums)))

# filter() — keeps elements where the function returns True
my_numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda num: num % 2 == 0, my_numbers)))

# Lambda — anonymous one-line function
print(list(map(lambda num: num ** 2, my_nums)))
```

## `print()` and friends

- `print()` accepts multiple values. By default, it joins them with a space and ends with `\n`. Override with `sep=` and `end=`.

```python
print("a", "b", "c", sep=", ", end="!\n")  # a, b, c!
```

- In Jupyter notebooks, `clear_output()` from `IPython.display` clears the previous cell output. Useful inside loops.

```python
from IPython.display import clear_output
clear_output()
```

## Built-ins worth knowing

- `enumerate(iterable)` — index + value
- `zip(*iters)` — pair related items together
- `sum(iterable)` — also handy for counting truthy results: `sum(1 for x in xs if cond(x))`
- `min()` / `max()` — become more powerful with `key=`
- `any(iterable)` — at least one truthy
- `all(iterable)` — every item truthy
- `sorted()` / `list.sort()` — see [Lists](../data-structures/lists.md)
- `map()` / `filter()` / `reversed()`
- `list()`, `tuple()`, `set()`, `dict()`, `str()`, `int()`, `float()`, `bool()`
- `isinstance(obj, cls)` — check type membership. Prefer over `type(obj) is cls`.

## From `functools` and `operator`

- `functools.reduce(func, iterable[, initial])` — collapse an iterable into a single value.
- `functools.lru_cache` — memoize a pure function; great for recursion with repeated work.
- `operator.itemgetter(i)` — concise key for sorting tuples/lists/dicts.
- `operator.mul` — multiplication as a function (handy with `map()` or `reduce()`).
