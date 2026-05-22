# Datetime, Math & Random

## `datetime`

```python
import datetime

# time object
my_time = datetime.time(2, 20)  # 24-hour format
print(my_time)         # 02:20:00
print(my_time.minute)  # 20
print(type(my_time))   # <class 'datetime.time'>
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

### Arithmetic

In Python's `datetime` module:

- `date` supports arithmetic with `timedelta`
- `datetime` supports arithmetic with `timedelta`
- `time` does **not** support arithmetic operations directly

```python
from datetime import date, datetime

date1 = date(2021, 11, 3)
date2 = date(2015, 11, 3)
result = date1 - date2
print(type(result))   # <class 'datetime.timedelta'>
print(result)         # 2192 days, 0:00:00
print(result.days)    # 2192

datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)
result2 = datetime1 - datetime2
print(result2)                 # 365 days, 10:00:00
print(result2.seconds)         # 36000 (seconds component only)
print(result2.total_seconds()) # 31572000.0 (all time as seconds)
```

