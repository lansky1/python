# Debugging & Timing

## Debugging with `pdb`

```python
import pdb

x = [1, 2, 3]
y = 2
z = 3

result_one = y + z
pdb.set_trace()
# result_two = y + x   # TypeError at runtime — debug interactively from here
```

Once `pdb` drops you into a prompt, common commands:

| Command | Action |
| --- | --- |
| `n` | step over (next line in same function) |
| `s` | step into (descend into a function call) |
| `c` | continue until the next breakpoint or end |
| `l` | list source around the current line |
| `p expr` | print the value of `expr` |
| `q` | quit the debugger |

## Timing Python Code

Three common approaches:

1. Tracking elapsed wall-clock time with `time.time()`.
2. Using the `timeit` module.
3. Using the `%%timeit` magic in Jupyter.

The two functions below produce the same list, but with different idioms — they're a fair test bench:

```python
def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))
```

### Tracking Time Elapsed

```python
import time

start_time_one = time.time()
result_one = func_one(1_000_000)
end_time_one = time.time()
elapsed_time_one = end_time_one - start_time_one
print("Function 1 ", elapsed_time_one)

start_time_two = time.time()
result_two = func_two(1_000_000)
end_time_two = time.time()
elapsed_time_two = end_time_two - start_time_two
print("Function 2 ", elapsed_time_two)
```

### timeit module

```python
import timeit

stmt_one = '''
func_one(100)
'''

stmt_two = '''
func_two(100)
'''

setup_one = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

setup_two = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print("Function 1: ", timeit.timeit(stmt_one, setup_one, number=100_000))
print("Function 2: ", timeit.timeit(stmt_two, setup_two, number=100_000))
```

### `%%timeit` magic in Jupyter

```python
%%timeit
func_one(100)
```

Jupyter's `%%timeit` runs the cell many times, returns mean and standard deviation, and works as cell-level (`%%timeit`) or line-level (`%timeit`).
