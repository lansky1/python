# Stdlib — Collections, itertools, functools

## `Counter`

```python
from collections import Counter

mylist = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 1]
print(Counter(mylist))

mylist = ['a', 'b', 'a', 'c', ('b', 'f'), 'd']
print(Counter(mylist))

mystring = "How many times does each word show up in this sentence"
print(Counter(mystring))           # counts characters
print(Counter(mystring.split()))   # counts words

mynumber = 11191101
print(Counter(str(mynumber)))      # counts digit characters
```

```python
letters = "aaaaaavvvvvvvveeeeeeeaaaaaccccccv"
c = Counter(letters)
print(c)
print(c.most_common())
```

### Useful `Counter` Operations

Assume:

```python
from collections import Counter

c = Counter("banana")
# Counter({'a': 3, 'n': 2, 'b': 1})
```

| What you want to do | Code | Result / meaning |
| --- | --- | --- |
| Get the total number of counted items | `sum(c.values())` | `6` |
| Remove every count | `c.clear()` | `c` becomes `Counter()` |
| Get only the unique elements | `list(c)` | `['b', 'a', 'n']` |
| Convert the unique elements to a set | `set(c)` | `{'b', 'a', 'n'}` |
| Convert to a normal dictionary | `dict(c)` | `{'b': 1, 'a': 3, 'n': 2}` |
| Get `(element, count)` pairs | `list(c.items())` | `[('b', 1), ('a', 3), ('n', 2)]` |
| Build a `Counter` from pairs | `Counter(dict([('a', 3), ('b', 1)]))` | `Counter({'a': 3, 'b': 1})` |
| Get the `n` least common elements | `c.most_common()[:-n - 1:-1]` | Slices from the end of `most_common()` |
| Clean up zero or negative counts | `c += Counter()` | Keeps only elements whose count is greater than `0` |

Example for least common elements:

```python
n = 2
c.most_common()[:-n - 1:-1]
# [('b', 1), ('n', 2)]
```

Why `c += Counter()` removes zero and negative counts:

```python
c = Counter({'apple': 3, 'banana': 0, 'orange': -2})
print(c)
# Counter({'apple': 3, 'banana': 0, 'orange': -2})

c += Counter()
print(c)
# Counter({'apple': 3})
```

`Counter` keeps zero and negative counts if they are created manually or by subtraction. Adding an empty `Counter()` tells Python to rebuild the counter using only positive counts.

> Intuition: think of a `Counter` as a bag of items. A positive count means the item is actually in the bag. A zero or negative count means the item is not really in the bag anymore.

When Python does `Counter` arithmetic, such as `+`, it returns only positive counts because a bag cannot contain `0` or `-2` copies of something. So `c += Counter()` means:

1. Add an empty counter, so the actual counts do not change.
2. Apply `Counter`'s arithmetic cleanup rule.
3. Remove every item whose count is `0` or less.

The same idea written more obviously:

```python
c = Counter({key: count for key, count in c.items() if count > 0})
```

So `c += Counter()` is just a shorter cleanup shortcut.

## `defaultdict`

```python
from collections import defaultdict

d = {'a': 10}
print(d['a'])

# defaultdict assigns a default value where a normal dict would raise KeyError
dd = defaultdict(lambda: 0)

d['b'] = 20
dd['correct'] = 100
print(dd['wrong'])  # 0  — auto-created with default

print(d)
print(dd)
```

Common factories:

- `defaultdict(int)` — counters.
- `defaultdict(list)` — bucketing items into groups.
- `defaultdict(set)` — bucketing into unique groups.

## `namedtuple`

```python
my_tuple = (10, 20, 30)
print(my_tuple[0])

from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(5, 'Husky', 'Sam')

print(sammy)        # Dog(age=5, breed='Husky', name='Sam')
print(sammy.breed)  # 'Husky' — attribute access
```

`namedtuple` keeps tuple efficiency but adds readable field access. For richer types, prefer `dataclasses.dataclass`.

## `deque`

`collections.deque` is useful for queues because adding or removing from both ends is O(1):

- `dq.append(x)` / `dq.appendleft(x)`.
- `dq.pop()` / `dq.popleft()`.
- Pass `maxlen=` to get a bounded ring buffer.

```python
from collections import deque

langs = deque(['c', 'python', 'java', 'c++', 'kotlin', 'rust'])

langs.popleft()         # 'c' — takes no argument
langs.appendleft('go')  # add to the left end
langs.pop()             # 'rust'
langs.append('scala')   # add to the right end
```

## `heapq`

- `heapq.heappush(heap, item)` and `heapq.heappop(heap)` help when repeatedly needing the smallest item.
- Python's heap is a min-heap; negate values to simulate a max-heap.

## `itertools`

- `itertools.product(*iterables)` — Cartesian product, all combinations from multiple iterables.
- `itertools.combinations(iterable, r)` — unique groups where order does not matter.
- `itertools.permutations(iterable, r)` — arrangements where order does matter.
- `itertools.chain(*iterables)` — treats multiple iterables as one continuous iterable.
- `itertools.groupby(iterable, key=...)` — groups **neighboring** matching items. Sort first when you need all equal values grouped together.

## `functools`

- `functools.reduce(func, iterable, initial=...)` — combines an iterable into one final value by repeatedly applying a function.
- `functools.lru_cache` — remembers function results. Useful for recursive problems with repeated work.
- `functools.partial(func, *args, **kwargs)` — creates a new callable with some arguments already filled in.

```python
from functools import partial

def multiply(factor, value):
	return factor * value


times_three = partial(multiply, 3)

print(times_three(5))  # 15
```

## `operator`

- `operator.itemgetter(...)` — useful with `key=` when sorting or selecting tuple/list/dictionary values.
- `operator.mul` — multiplication as a function. Useful with `map()` or `functools.reduce()` when a function is needed instead of the `*` operator.
