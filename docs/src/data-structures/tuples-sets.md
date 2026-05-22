# Tuples & Sets

## Tuples

- Immutable ordered sequence
- Hashable when their contents are hashable — so tuples can be dict keys or set members

```python
my_tuple = (10, 20, 30)
print(my_tuple[0])  # 10
```

Tuple unpacking:

```python
a, b = b, a       # swap
x, *rest = [1, 2, 3, 4]   # x=1, rest=[2, 3, 4]
```

## Sets

- Unordered collection of **unique** elements
- Think of it as a hash set, while dicts are hash maps
- Can be created from any iterable: list, tuple, string, set, range
- Passing a dict discards values, keeps only keys
- Silently rejects duplicates (no error)

```python
example_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
hashset = set(example_list)
hashset.add(3)
hashset.add(4)
hashset.add(3)  # no error, just ignored
print(hashset)  # {1, 2, 3, 4}

hashset = set({1: 'hello', 2: 'world'}.values())
print(hashset)  # {'hello', 'world'} — order not guaranteed

hashset = set({1: 'hello', 2: 'world'}.items())
print(hashset)  # {(1, 'hello'), (2, 'world')} — tuples are hashable
```

## Set methods

- `.add(x)` — add one item
- `.discard(x)` — remove without error if missing
- `.remove(x)` — remove; raises `KeyError` if missing
- `.union(other)`, `.intersection(other)`, `.difference(other)`
- `.issubset(other)` / `.issuperset(other)`

## Subset checks

```python
# method form
{1, 2, 3}.issubset({1, 2, 3, 4, 5})   # True

# operator form
{1, 2, 3} <= {1, 2, 3, 4, 5}          # True
```

## Booleans

- `True`, `False`, `None` are singletons.
- Compare against `None` with `is` / `is not`, not `==`.
