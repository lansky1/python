# Round Sum

Round each of three numbers to the nearest 10, then return the sum.

Rules:

- Rightmost digit ≥ 5 → round **up** to the next multiple of 10
- Rightmost digit < 5 → round **down** to the previous multiple of 10

```python
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    last_digit = num % 10
    if last_digit < 5:
        return num - last_digit
    else:
        return num + (10 - last_digit)

print(round_sum(16, 17, 18))   # 60
print(round_sum(12, 13, 14))   # 30
print(round_sum(6, 4, 4))      # 10
```

> **`% 10` over string slicing**
>
> Avoid `int(str(num)[-1])` — using `num % 10` is faster and works for negative numbers too.

