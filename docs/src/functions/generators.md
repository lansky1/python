# Generators

A generator function can send back a value and later resume to pick up where it left off.

```python
def create_cubes(n):
    results = []
    for x in range(n):
        results.append(x ** 3)
    return results

def generate_cubes(n):
    for x in range(n):
        yield x ** 3
```

```python
list(generate_cubes(10))
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

## Performance: generator vs list

```python
from timeit import repeat

def create_cubes_for_timing(n):
    results = []
    for x in range(n):
        results.append(x ** 3)
    return results

def generate_cubes_for_timing(n):
    for x in range(n):
        yield x ** 3

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

Generators are memory-efficient because they yield one item at a time instead of materializing the whole list up front.

## `next()` and `iter()`

- `iter(obj)` — get an iterator from an iterable.
- `next(iterator)` — ask for one value. Raises `StopIteration` when exhausted.
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
# next(s)         # TypeError: 'str' object is not an iterator
next(iter(s))     # 'h'
```

## Generator expressions vs list comprehensions

```python
my_list = [1, 2, 3, 4, 5]

# Generator expression — lazy, memory efficient
gen_expr = (item for item in my_list if item > 3)

# List comprehension — eager, builds full list
list_comp = [item for item in my_list if item > 3]
```

## References

- [Understanding generators in Python](http://stackoverflow.com/questions/1756096/understanding-generators-in-python)
- [What does the yield keyword do?](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python)
