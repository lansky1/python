# Data Structures

## Lists

- Ordered, mutable sequence.
- Can hold mixed types.

```python
example_list = [10, "hello", 200.3]
print(example_list)
print(example_list[1][3])   # 'l' — second element is "hello", index 3 is 'l'
print([10, "hello", 200.3])
```

### Common list methods

```python
l = [1, 2, 3]
l.append(4)         # [1, 2, 3, 4]
l.count(1)          # 1
l.extend([5, 6])    # [1, 2, 3, 4, 5, 6]
l.index(2)          # 1  — index of first occurrence
# l.index(10)       # ValueError if not found
l.insert(2, 7)      # [1, 2, 7, 3, 4, 5, 6]
l.pop()             # 6  — removes and returns last item
l.pop(0)            # 1  — removes and returns by index
l.remove(7)         # removes first occurrence of value 7 in place
l.reverse()         # in place
l.sort()            # in place
```

`sorted(iterable, key=..., reverse=...)` returns a new sorted list without mutating the original.

### Reference vs shallow copy

Assigning one list variable to another creates another reference to the same list.

```python
numbers = [1, 2, 3, 4, 5]
alias = numbers

alias[4] = 7

print(numbers)                  # [1, 2, 3, 4, 7]
print(id(numbers) == id(alias)) # True
```

Use slicing or `.copy()` when you need a separate shallow copy.

```python
numbers = [1, 2, 3, 4, 5]
copy_one = numbers[:]
copy_two = numbers.copy()

copy_one[0] = 99

print(numbers)   # [1, 2, 3, 4, 5]
print(copy_one)  # [99, 2, 3, 4, 5]
```

## Dictionaries

- Mutable.
- Keys must be hashable: strings, integers, tuples (with hashable contents), frozensets — anything immutable.
- Lists, dicts, and sets cannot be used as keys because they are mutable.
- As of Python 3.7, dicts preserve insertion order. Use `collections.OrderedDict` only when you need its extra API (`move_to_end`, equality cares about order).

```python
d = {1: 'hello', 2: 'bye'}
print(type(d[1]).__name__)   # 'str'
```

### Safe lookups and defaults

Use `.get()` when a missing key should fall back to a default value.

```python
item = {'item': 'football', 'price': 10.00}

count = item.get('count', 0)
print(count)  # 0
```

Use `.setdefault()` when you also want to store the default on the dictionary.

```python
item = {'item': 'football', 'price': 10.00}

count = item.setdefault('count', 0)
print(count)  # 0
print(item)   # {'item': 'football', 'price': 10.0, 'count': 0}
```

```python
text = "It's the first of April. It's still cold in the UK."
counts = {}

for word in text.split():
    counts.setdefault(word, 0)
    counts[word] += 1

print(counts["It's"])  # 2
```

### Dictionary comprehension

```python
{x: x**2 for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

{k: v**2 for k, v in zip(['a', 'b'], range(2))}
# {'a': 0, 'b': 1}
```

### Iterating

```python
d = {'k1': 1, 'k2': 2}

for k in d.items():
    print(k)
# ('k1', 1)
# ('k2', 2)

for k in d.keys():
    print(k)
# k1
# k2

for k in d.values():
    print(k)
# 1
# 2

d.items()   # dict_items([('k1', 1), ('k2', 2)])
```

### Merging dictionaries

When keys overlap, the right-hand dictionary wins.

```python
d1 = {'name': 'Alex', 'age': 25}
d2 = {'name': 'Alex', 'city': 'New York'}

print(d1 | d2)        # {'name': 'Alex', 'age': 25, 'city': 'New York'}
print({**d1, **d2})   # {'name': 'Alex', 'age': 25, 'city': 'New York'}
```

The `|` merge operator is available in Python 3.9+. The `**` unpacking form works in older Python 3 versions too.

### Sorting dictionary items

`sorted()` returns a list of key/value tuples. Choose the sort field with `key=`.

```python
scores = {1: 3, 4: 2, 5: 1, 2: 9}

print(sorted(scores.items(), key=lambda pair: pair[0]))
# [(1, 3), (2, 9), (4, 2), (5, 1)]

print(sorted(scores.items(), key=lambda pair: pair[1]))
# [(5, 1), (4, 2), (1, 3), (2, 9)]
```

## Tuples

- Immutable ordered sequence.
- Hashable when their contents are hashable, so they can be dict keys or set elements.

### Tuple unpacking

Tuple assignment works with any sequence. A starred target collects the middle values into a list.

```python
first, *rest, last = [42, 771, 256, 1337]

print(first)  # 42
print(rest)   # [771, 256]
print(last)   # 1337
```

### Tuple size

Tuples usually use less memory than lists because they are immutable and do not need extra capacity for growth.

```python
import sys

as_list = [1, 2, 3, 4, 5]
as_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(as_list))
print(sys.getsizeof(as_tuple))
# Exact byte counts vary by Python version and platform.
```

## Sets

- Unordered collection of unique elements.
- Think of a set as a hash set; a dict is a hash map.
- Constructible from any iterable: list, tuple, string, set, range.
- Passing a dict discards values and keeps only keys.
- Silently rejects duplicates (no error).

```python
example_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
hashset = set(example_list)
hashset.add(3)
hashset.add(4)
hashset.add(3)   # no error — duplicates ignored
print(hashset)   # {1, 2, 3, 4}

set({1: 'hello', 2: 'world'}.values())  # {'hello', 'world'}  (order not guaranteed)
set({1: 'hello', 2: 'world'}.items())   # {(1, 'hello'), (2, 'world')}
```

### `add()` vs `update()`

- `add()` — adds a **single element**.
- `update()` — adds **multiple elements** from an iterable (list, tuple, set, string, dict, etc.).

```python
my_set = {1, 2, 3}

my_set.add(4)
# {1, 2, 3, 4}

my_set.update([5, 6, 7])
# {1, 2, 3, 4, 5, 6, 7}

my_set.update("abc")    # iterates over characters
# {1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c'}

my_set.update({10, 11})
# {1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c', 10, 11}
```

The same `update()` exists on dictionaries — it merges or replaces multiple key/value pairs:

```python
my_dict = {'a': 1, 'b': 2}
my_dict.update({'c': 3, 'd': 4})       # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_dict.update({'a': 100})              # 'a' overwritten to 100
my_dict.update([('e', 5), ('f', 6)])    # accepts pairs as well
```

### Set methods

```python
s = set()
s.add(1)
s.add(2)
s.clear()

sc = s.copy()  # shallow copy — original is not affected by edits to sc
```

```python
s1 = {1, 2, 3}
s2 = {1, 4, 5}

s1.difference(s2)         # {2, 3}  — extras in s1
s1.difference_update(s2)  # mutates s1 to {2, 3}
```

```python
s1 = {1, 2, 3}
s2 = {1, 2, 4}

s1.intersection(s2)         # {1, 2}
s1.intersection_update(s2)  # mutates s1 to {1, 2}
```

```python
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

s1.isdisjoint(s2)   # False  — they share elements
s1.isdisjoint(s3)   # True

s1.issubset(s2)     # True
s2.issuperset(s1)   # True

s1.symmetric_difference(s2)         # {4}  — items not in both
s1.symmetric_difference_update(s2)  # mutates s1 to {4}

s1 = {1, 2}
s1.union(s2)        # {1, 2, 4}  — returns a new set
s1.update(s2)       # mutates s1 in place
```

### Subset checks

```python
{1, 2, 3}.issubset({1, 2, 3, 4, 5})   # True
{1, 2, 3} <= {1, 2, 3, 4, 5}          # True (operator form)
```

### Removal — three flavors

| Method | Missing element | Returns |
| --- | --- | --- |
| `remove(x)` | raises `KeyError` | `None` |
| `discard(x)` | silently ignored | `None` |
| `pop()` | raises `KeyError` if empty | the popped element |
| `clear()` | always succeeds | `None`, set is now empty |
