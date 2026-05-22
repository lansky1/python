# Dictionaries

- Mutable
- Unordered mapping (use `collections.OrderedDict` for guaranteed insertion order semantics in older code; modern dicts preserve insertion order)
- Keys must be **hashable** (strings, integers, tuples, frozensets)
- Cannot use lists, dicts, or sets as keys — they are mutable

```python
d = {1: 'hello', 2: 'bye'}
print(type(d[1]).__name__)  # 'str'
```

## Useful dict methods

- `.get(key, default=None)` — safe read with optional default
- `.setdefault(key, default)` — creates a missing key with a default value (though `defaultdict` is often cleaner)
- `.items()` — loop through `(key, value)` pairs
- `.keys()` / `.values()` — direct views
- `.update(other)` — add or replace multiple entries
- `dict.fromkeys(iterable, value=None)` — build a dict from keys, each with the same starting value. Duplicate keys are removed because dict keys must be unique.
- `.pop(key[, default])` — remove and return a key
- `.copy()` / `.clear()`

## Building

```python
# from pairs
d = dict([("a", 1), ("b", 2)])

# from kwargs
d = dict(a=1, b=2)

# comprehension
squares = {n: n * n for n in range(5)}
```

## Looping idioms

```python
for key, value in d.items():
    ...

for key in d:        # equivalent to: for key in d.keys()
    ...
```
