# Loops & Comprehensions

## `for` vs `while`

A `for` loop controls its next value automatically. Use `while` when you need to manually change the loop index inside the loop.

Python supports an `else` block on `for` and `while` loops. The `else` block runs only when the loop finishes normally — not when it exits with `break`.

### Sliding windows

Use `range(len(value) - window_size + 1)` when checking slices of a fixed size:

```python
def cat_dog(s):
    count_cat = 0
    count_dog = 0
    for idx in range(len(s) - 2):
        if s[idx:idx + 3] == 'cat':
            count_cat += 1
    for idx in range(len(s) - 2):
        if s[idx:idx + 3] == 'dog':
            count_dog += 1
    return count_cat == count_dog
```

## Range

- `range(stop)` or `range(start, stop, step)`.
- `range` is a lightweight sequence — it does not store all values in memory; it computes them on demand.

## Enumerate

```python
for index, item in enumerate(iterable):
    ...
```

Returns tuples of `(index, element)`.

## Zip

- Pairs up elements at the same index as tuples.
- Extra elements from the longer iterable are discarded (unless you use `itertools.zip_longest`).

```python
list1 = [1, 2, 3]      # an extra element here would be discarded
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
    print(item)
# (1, 'a')
# (2, 'b')
# (3, 'c')
print(list(zip(list1, list2)))  # can be wrapped as list, set, tuple, dict
```

## List Comprehensions

List comprehensions can build and filter lists in a single expression.

```python
my_list = [x for x in "hello"]                      # ['h', 'e', 'l', 'l', 'o']
my_second_list = [num**2 for num in range(0, 11)]   # squares 0..100
my_third_list = [num for num in range(11) if num % 2 == 0]   # evens
my_fourth_list = [num if num % 2 == 0 else "ODD" for num in range(11)]
my_fifth_list = [x * y for x in [2, 4, 6] for y in [1, 2, 3]]  # cross product
```

```python
def count_evens(nums):
    return sum([1 for num in nums if num % 2 == 0])
```

```python
print([[X, Y, Z]
       for X in range(x + 1)
       for Y in range(y + 1)
       for Z in range(z + 1)
       if X + Y + Z != n])
```

> List comprehensions are usually clearer than `map()` and `filter()` when the logic is short.
