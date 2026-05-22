# Sum 13

Return the sum of numbers in a list, but skip 13 and the number immediately after it.

```python
def sum13(nums):
    return sum(
        num for i, num in enumerate(nums)
        if num != 13 and (i == 0 or nums[i - 1] != 13)
    )

print(sum13([1, 2, 13, 2, 1, 13]))  # 4
print(sum13([1, 2, 2, 1, 13]))      # 6
```

The trick: include `num` only when it isn't `13` AND the previous element wasn't `13` either.
