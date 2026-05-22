# Make Bricks

You have `small` 1-inch bricks and `big` 5-inch bricks. Decide whether you can make a row exactly `goal` inches long.

## Idiomatic solution

Use the maximum number of big bricks possible without overshooting, then fill the rest with smalls:

```python
def make_bricks(small, big, goal):
    big_used = min(big, goal // 5)         # don't use more bigs than fit
    return (goal - big_used * 5) <= small
```

The key insight: **greedily use as many big bricks as the goal allows**, then the problem reduces to a single comparison.

## Original (roundabout) solution

```python
import math

def make_bricks(small, big, goal):
    # minimum number of bigs needed if we use all smalls first
    y = (goal - small) / 5

    if y.is_integer() and 0 <= y <= big:   # exact fit
        return True
    elif y > big:                          # not enough bigs even after using all smalls
        return False
    else:                                  # have more than enough bigs
        x = goal - 5 * math.ceil(y)
        return 0 <= x <= small

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
```

```python
print(make_bricks(6, 0, 11))
print(make_bricks(7, 1, 13))
print(make_bricks(40, 1, 46))
print(make_bricks(40, 2, 52))
print(make_bricks(22, 2, 33))
```

`y = (goal - small) / 5.0` is the **minimum number of big bricks needed** if you were to use all your small bricks first. Three cases follow:

1. **`y` is a whole number, 0 ≤ y ≤ big** — exact fit. Use all smalls + exactly `y` bigs.
2. **`y > big`** — even burning all your smalls, you still need more bigs than you have. Impossible.
3. **Otherwise** — you have more than enough bigs, so use `ceil(y)` of them, then check if the leftover gap fits within your small supply.

It works, but it's roundabout. You're approaching the problem from "how many bigs do I *need*?" when it's cleaner to ask "how many bigs *can* I use?"
