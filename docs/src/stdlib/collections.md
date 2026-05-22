# `collections`

## `Counter`

```python
from collections import Counter

mylist = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 1]
print(Counter(mylist))

mylist = ['a', 'b', 'a', 'c', ('b', 'f'), 'd']
print(Counter(mylist))

mystring = "How many times does each word show up in this sentence"
print(Counter(mystring))
print(Counter(mystring.split()))

mynumber = 11191101
print(Counter(str(mynumber)))
```

```python
letters = "aaaaaavvvvvvvveeeeeeeaaaaaccccccv"
c = Counter(letters)
print(c)
print(c.most_common())
```

### Useful `Counter` operations

Assume:

```python
from collections import Counter
c = Counter("banana")
# Counter({'a': 3, 'n': 2, 'b': 1})
```

| Goal | Code | Result |
|---|---|---|
| Total counted items | `sum(c.values())` | `6` |
| Remove every count | `c.clear()` | `Counter()` |
| Get unique elements | `list(c)` | `['b', 'a', 'n']` |
| Convert to set | `set(c)` | `{'b', 'a', 'n'}` |
| Convert to dict | `dict(c)` | `{'b': 1, 'a': 3, 'n': 2}` |
| `(element, count)` pairs | `list(c.items())` | `[('b', 1), ('a', 3), ('n', 2)]` |
| Build from pairs | `Counter(dict([('a', 3), ('b', 1)]))` | `Counter({'a': 3, 'b': 1})` |
| `n` least common | `c.most_common()[:-n - 1:-1]` | Slice from the end |
| Drop zero / negative counts | `c += Counter()` | Keeps only positive counts |

### Why `c += Counter()` cleans up

```python
c = Counter({'apple': 3, 'banana': 0, 'orange': -2})
print(c)
# Counter({'apple': 3, 'banana': 0, 'orange': -2})

c += Counter()
print(c)
# Counter({'apple': 3})
```

`Counter` keeps zero and negative counts if you create them manually or via subtraction. Adding an empty `Counter()` invokes `Counter`'s arithmetic-cleanup rule, which only keeps positive counts.

Think of a `Counter` as a bag of items — a bag cannot contain `0` or `-2` copies of something. Equivalent explicit form:

```python
c = Counter({key: count for key, count in c.items() if count > 0})
```

## `defaultdict`

```python
from collections import defaultdict

dd = defaultdict(lambda: 0)
dd['correct'] = 100
print(dd['wrong'])   # 0 — auto-created, no KeyError
print(dd)
```

`defaultdict` gives missing keys a default value automatically. Useful for grouping and counting.

## `namedtuple`

```python
from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(5, 'Husky', 'Sam')

print(sammy)        # Dog(age=5, breed='Husky', name='Sam')
print(sammy.breed)  # 'Husky'
```

## `deque`

Fast appends and pops from **both** ends. Useful for queues and sliding windows.

```python
from collections import deque
q = deque([1, 2, 3])
q.append(4)        # right
q.appendleft(0)    # left
q.pop()            # 4
q.popleft()        # 0
```
