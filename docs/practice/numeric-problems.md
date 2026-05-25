# Numeric Problems

## Sum 13

Return the sum of numbers in a list, but skip 13 and the number immediately after it.

```python
def sum13(nums):
    return sum([num for i, num in enumerate(nums)
                if (num != 13 and (i == 0 or nums[i - 1] != 13))])

print(sum13([1, 2, 13, 2, 1, 13]))   # 4
print(sum13([1, 2, 2, 1, 13]))       # 6
```

## Sum 67

Return the sum of numbers in a list, but skip any section of numbers starting with 6 and ending with 7.

```python
def sum67(nums):
    sum_ = 0
    i = 0

    while i != len(nums):
        if nums[i] != 6:
            sum_ += nums[i]
            i += 1
        else:
            i += 1
            while nums[i] != 7:
                i += 1
            i += 1

    return sum_

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
```

## Round Sum

Round each number to the nearest 10, then return the sum.

- Rightmost digit ≥ 5 → round up to next multiple of 10.
- Rightmost digit < 5 → round down to previous multiple of 10.

```python
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


# rightmost digit is 5 or more -> round to next multiple of 10 (15 -> 20)
# rightmost digit is less than 5 -> round to previous multiple of 10 (14 -> 10)
def round10(num):
    last_digit = int(str(num)[-1])
    if last_digit < 5:
        return num - last_digit
    else:
        return num


print(round_sum(12, 13, 14))
```

## Make Bricks

You want to make a row of bricks that is `goal` cm long. You have `small` 1 cm bricks and `big` 5 cm bricks. Return whether the row is achievable.

=== "Original approach"

    `y = (goal - small) / 5.0` is the **minimum number of big bricks needed** if you were to use *all* your small bricks first. Three cases follow:

    1. `y` is a whole number, `0 ≤ y ≤ big` — exact fit. Use all smalls + exactly `y` bigs.
    2. `y > big` — even burning all your smalls, you still need more bigs than you have. Impossible.
    3. Otherwise — you have more than enough bigs, so use `ceil(y)` of them, then check if the leftover gap fits within your small supply.

    ```python
    import math

    def make_bricks(small, big, goal):
        y = (goal - small) / 5

        if y.is_integer() and 0 <= y <= big:
            return True
        elif y > big:
            return False
        else:
            x = goal - 5 * (math.ceil(y))
            return 0 <= x <= small

    print(make_bricks(3, 1, 8))
    print(make_bricks(3, 1, 9))
    print(make_bricks(3, 2, 10))
    print(make_bricks(6, 0, 11))
    print(make_bricks(7, 1, 13))
    print(make_bricks(40, 1, 46))
    print(make_bricks(40, 2, 52))
    print(make_bricks(22, 2, 33))
    ```

    It works, but it's roundabout. You're approaching it from "how many bigs do I *need*?" when it's cleaner to ask "how many bigs *can* I use?"

=== "Cleaner approach"

    Use the maximum big bricks possible without overshooting, then fill the rest with smalls:

    ```python
    def make_bricks(small, big, goal):
        big_used = min(big, goal // 5)   # don't use more bigs than fit
        return (goal - big_used * 5) <= small
    ```

    The key insight: **greedily use as many big bricks as the goal allows**, then the problem reduces to a single comparison. The original solution was working around the problem rather than through it.

## Second Lowest Scores

Sort by score, drop the lowest tier, then keep the next-lowest tier and sort by name:

```python
records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
records.sort(key=lambda x: x[1])
records = list(filter(lambda x: x[1] != records[0][1], records))
records = list(filter(lambda x: x[1] == records[0][1], records))
records.sort(key=lambda x: x[0])
print(records)
```
