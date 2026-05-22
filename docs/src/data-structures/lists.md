# Lists & Comprehensions

## Lists

- Ordered, mutable sequence
- Can hold mixed types

```python
example_list = [10, "hello", 200.3]
print(example_list[1][3])  # 'l' — index into the inner string
```

## List comprehensions

```python
my_list = [x for x in "hello"]
print(my_list)  # ['h', 'e', 'l', 'l', 'o']

squares = [num ** 2 for num in range(0, 11)]
evens = [num for num in range(11) if num % 2 == 0]
labelled = [num if num % 2 == 0 else "ODD" for num in range(11)]
products = [x * y for x in [2, 4, 6] for y in [1, 2, 3]]
```

With filters and conditional expressions:

```python
def count_evens(nums):
    return sum(1 for num in nums if num % 2 == 0)
```

Nested:

```python
print([[X, Y, Z]
       for X in range(x + 1)
       for Y in range(y + 1)
       for Z in range(z + 1)
       if X + Y + Z != n])
```

> **When to prefer comprehensions**
>
> List comprehensions are usually clearer than `map()` and `filter()` when the logic is short.


## List methods

- `.append(x)` — add one item to the end
- `.extend(iterable)` — add many items to the end
- `.insert(i, x)` — add at a specific position
- `.pop([i])` — remove and return; defaults to last item
- `.remove(x)` — remove the first matching value
- `.count(x)` — how many times a value appears
- `.index(x)` — first position of value (raises `ValueError` if missing)
- `.sort(key=..., reverse=...)` — sort in place
- `.copy()` — shallow copy
- `.clear()` — remove all items

## Sorting

- `sorted(iterable, key=..., reverse=...)` — returns a **new** list
- `list.sort(key=..., reverse=...)` — sorts **in place**
- Use `operator.itemgetter()` with `key=` when sorting tuples/lists/dicts by a specific field.
