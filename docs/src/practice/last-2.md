# Last 2

Count how many times the last 2 characters of a string appear elsewhere in the string (excluding the trailing pair itself).

`"axxxaaxx"` → ends in `"xx"`; appears 2 more times earlier → return `2`.

## Approach 1: `str.count()` (does NOT handle overlaps)

```python
def last2(s):
    substring = s[-2:]
    return s.count(substring)

last2("axxxaaxx")
```

This counts the trailing pair itself **and** misses overlapping occurrences.

## Approach 2: Regex (also misses overlaps)

```python
import re

string_ = "axxxaaxx"
substring = string_[-2:]

regex_pattern = re.escape(substring)
for item in re.finditer(regex_pattern, string_):
    print(item)

# Overlapping requires a lookahead:
# for item in re.finditer(f"(?=({re.escape(substring)}))", string_):
#     print(item.start(), item.group(1))
```

## Approach 3: Sliding window

```python
def last2(s):
    substring = s[-2:]
    count = 0
    for i in range(len(s) - 2):     # exclude the trailing pair
        if s[i:i + 2] == substring:
            count += 1
    return count

last2("axxxaaxx")
```

## Approach 4: One-liner

```python
def last2(s):
    return sum(1 for i in range(len(s) - 2) if s[i:i + 2] == s[-2:])

last2("axxxaaxx")
```
