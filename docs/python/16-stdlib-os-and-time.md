# Stdlib — OS, Time, Math, Random

## `os` & `shutil`

```python
import os

print(os.getcwd())
print(os.listdir())   # provide a path argument for other directories
```

```python
import shutil

# shutil.move('source', 'dest')   # moves or renames
# os.unlink(path)                 # deletes a file
# os.rmdir(path)                  # deletes an empty folder
# shutil.rmtree(path)             # removes all files and folders at path
# Use the send2trash module to send to recycle bin instead of permanent delete

# os.walk(os.getcwd())            # yields (dirpath, dirnames, filenames)
```

> For most modern path code, prefer `pathlib.Path` over raw `os.path` strings — it gives object-oriented joins, glob, and read/write conveniences.

## `datetime`

```python
import datetime

# time object
my_time = datetime.time(2, 20)   # 24-hour format
print(my_time)          # 02:20:00
print(my_time.minute)   # 20
print(type(my_time))    # <class 'datetime.time'>
```

```python
# date object
today = datetime.date.today()
print(today)         # YYYY-MM-DD (ISO standard)
print(today.ctime()) # human-readable format
```

```python
from datetime import datetime

my_datetime = datetime(2021, 10, 3, 14, 20, 1)
print(my_datetime)
my_datetime = my_datetime.replace(year=2025)
print(my_datetime)
```

In Python's `datetime` module:

- `date` supports arithmetic with `timedelta`.
- `datetime` supports arithmetic with `timedelta`.
- `time` does **not** support arithmetic operations directly.

```python
from datetime import date, datetime

date1 = date(2021, 11, 3)
date2 = date(2015, 11, 3)
result = date1 - date2
print(type(result))     # <class 'datetime.timedelta'>
print(result)           # 2192 days, 0:00:00
print(result.days)      # 2192

datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)
result2 = datetime1 - datetime2
print(result2)                 # 365 days, 10:00:00
print(result2.seconds)         # 36000   (seconds component only)
print(result2.total_seconds()) # 31572000.0 (all time as seconds)
```

## `math`

| Function | Description |
| --- | --- |
| `math.floor(x)` | Round down |
| `math.ceil(x)` | Round up |
| `round(x)` | Banker's rounding (round half to even) |
| `math.pi` | π constant |
| `math.e` | Euler's number |
| `math.inf` | Positive infinity |
| `math.nan` | Not a Number |
| `math.log(math.e)` | Natural log → 1.0 |
| `math.sin(x)` | Sine (x in radians) |
| `math.degrees(x)` / `math.radians(x)` | Convert between degrees and radians |

## `random`

References: [Pseudorandom number generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator), [Random seed](https://en.wikipedia.org/wiki/Random_seed).

| Function | Description |
| --- | --- |
| `random.seed(42)` | Set seed for reproducibility |
| `random.randint(a, b)` | Random integer in `[a, b]` (both inclusive) |
| `random.choice(seq)` | Pick one random element |
| `random.choices(population, k=n)` | Pick n elements **with** replacement |
| `random.sample(population, k=n)` | Pick n elements **without** replacement |
| `random.shuffle(list)` | Shuffle in place |
| `random.uniform(a, b)` | Random float in `[a, b]` |
| `random.gauss(mu, sigma)` | Normal distribution sample |
