# String Match

Count the number of positions where two strings have the same length-2 substring.

```python
def string_match(a, b):
    n = min(len(a), len(b))
    count = 0
    for i in range(n - 1):              # `-1` because we read i and i+1
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
    return count

string_match('abc', 'abc')
# string_match('abc', 'axc')
```

> **Off-by-one**
>
> The common bug here is forgetting the `-1` in `range(n - 1)`. A length-2 slice starting at index `i` reads `i` and `i+1`, so `i` can be at most `n - 2`.

