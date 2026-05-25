# Generators

Generators let us write a function that can send back a value and later resume to pick up where it left off.

```python
def create_cubes(n):
    results = []
    for x in range(n):
        results.append(x**3)
    return results

def generate_cubes(n):
    for x in range(n):
        yield x**3
```

```python
list(generate_cubes(10))
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

## Performance: Generator vs List

```python
from timeit import repeat

def create_cubes_for_timing(n):
    results = []
    for x in range(n):
        results.append(x**3)
    return results

def generate_cubes_for_timing(n):
    for x in range(n):
        yield x**3

n = 100_000
number = 20
repeats = 5

assert create_cubes_for_timing(10) == list(generate_cubes_for_timing(10))

def best_time(label, statement):
    times = repeat(statement, globals=globals(), number=number, repeat=repeats)
    best = min(times) / number
    print(f"{label:28} {best:.6f} seconds per run")

best_time("create list directly", "create_cubes_for_timing(n)")
best_time("list from generator", "list(generate_cubes_for_timing(n))")
```

## `next()` and `iter()`

- `iter(obj)` returns an iterator; `next(iterator)` asks for one value.
- `list(generator)` keeps calling `next()` until the generator is exhausted.
- A `for` loop automatically catches `StopIteration` and stops.

```python
def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
# print(next(g))  # raises StopIteration
```

Strings are iterable but not iterators — you need `iter()` first:

```python
s = 'hello'
# next(s)        # TypeError: 'str' is not an iterator
next(iter(s))    # 'h'
```

## Generator Expressions vs List Comprehensions

```python
my_list = [1, 2, 3, 4, 5]

gen_expr = (item for item in my_list if item > 3)   # lazy, memory efficient
list_comp = [item for item in my_list if item > 3]  # eager, builds full list
```

```python
doubled_list = [x * 2 for x in range(10)]
doubled_generator = (x * 2 for x in range(10))

print(doubled_list)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print(doubled_generator)
# <generator object ...>

print(list(doubled_generator))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Printing a generator expression shows the generator object, not its values. The values are produced only when you iterate over it.

References:

- [Understanding generators in Python](https://stackoverflow.com/questions/1756096/understanding-generators-in-python)
- [What does the yield keyword do?](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python)
