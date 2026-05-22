# Timing Python Code

Three common approaches:

1. Simply tracking time elapsed
2. Using the `timeit` module
3. `%%timeit` in Jupyter notebooks

Reference functions used below:

```python
def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))
```

## Tracking time elapsed

```python
import time

start_time_one = time.time()
result_one = func_one(1_000_000)
elapsed_time_one = time.time() - start_time_one
print("Function 1 ", elapsed_time_one)

start_time_two = time.time()
result_two = func_two(1_000_000)
elapsed_time_two = time.time() - start_time_two
print("Function 2 ", elapsed_time_two)
```

## `timeit` module

```python
import timeit

stmt_one = "func_one(100)"
stmt_two = "func_two(100)"

setup_one = """
def func_one(n):
    return [str(num) for num in range(n)]
"""

setup_two = """
def func_two(n):
    return list(map(str, range(n)))
"""

print("Function 1:", timeit.timeit(stmt_one, setup_one, number=100_000))
print("Function 2:", timeit.timeit(stmt_two, setup_two, number=100_000))
```

## Jupyter magics

```python
%%timeit
func_one(100)
```

`%timeit` is the line-magic version for a single expression.

> **Profile, don't guess**
>
> `timeit` is great for **microbenchmarks**. For real programs, use `cProfile` or `profile` to find where time is actually spent.

