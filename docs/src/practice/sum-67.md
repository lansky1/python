# Sum 67

Return the sum of numbers in a list, but skip any section starting with `6` and ending with the next `7`.

```python
def sum67(nums):
    total = 0
    i = 0
    while i != len(nums):
        if nums[i] != 6:
            total += nums[i]
            i += 1
        else:
            i += 1
            while nums[i] != 7:
                i += 1
            i += 1   # skip the 7 itself
    return total

print(sum67([1, 2, 2]))                    # 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))      # 5
print(sum67([1, 1, 6, 7, 2]))              # 4
```

This is naturally a two-pointer / state-machine problem — `while` with manual index control is the cleanest fit because the inner loop has to skip a variable-length run.
