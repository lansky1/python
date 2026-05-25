# Built-ins & Methods Cheatsheet

A quick-lookup catalog of the everyday functions and methods I want at my fingertips. Concept pages cover usage in depth; this page is the index.

## Output

- `print()` can receive multiple values, including variables. By default, it prints them on the same line separated by spaces. Use `sep=` to change the separator and `end=` to change what comes after the print.
- In Jupyter notebooks, `clear_output()` from `IPython.display` clears the previous cell output. Useful when updating output repeatedly, such as inside a loop.

```python
from IPython.display import clear_output

clear_output()
```

## Iteration & sequencing

- `enumerate()` gives both the index and the value while looping.
- `zip()` loops over multiple sequences together and pairs related items.
- `sum()` adds values and can also count truthy results.
- `min()` and `max()` find the smallest or largest item, and become more powerful with `key=`.
- `any()` checks if at least one item is true.
- `all()` checks if every item is true.
- `sorted(iterable, key=lambda x: x, reverse=True/False)` returns a new sorted list.
- `.sort(key=lambda x: x)` sorts a list in place.
- `reversed()` loops through a sequence backwards without manually managing indexes.
- `map()` transforms every item. Useful when one existing function should be applied to every value.
- `filter()` keeps only the items that pass a condition.
- List comprehensions are often clearer than `map()` and `filter()` when the logic is short.

## Constructors

- `list()` converts an iterable into a list.
- `tuple()` converts an iterable into a tuple.
- `set()` removes duplicates and gives fast membership checks.
- `dict()` can build dictionaries from pairs or keyword arguments.
- `str()` converts a value into a string.
- `int()` converts compatible values into integers.
- `float()` converts compatible values into decimal numbers.
- `bool()` converts a value into `True` or `False` based on truthiness.
- `isinstance()` checks whether a value belongs to a type. Prefer it over comparing `type()` directly.

## Dictionaries

- `.get()` safely reads a dictionary key with an optional default value.
- `.items()` loops through dictionary keys and values together.
- `.keys()` gets dictionary keys.
- `.values()` gets dictionary values.
- `.update()` adds or replaces multiple dictionary entries.
- `dict.fromkeys()` creates a dictionary from keys, giving each key the same starting value. If no value is passed, the value is `None`. Duplicate keys are removed because dictionary keys must be unique.

## Lists

- `.append()` adds one item to the end of a list.
- `.extend()` adds many items to the end of a list.
- `.insert()` adds an item at a specific list position.
- `.pop()` removes and returns an item from a list or dictionary. If no index is provided, it removes the last item by default.
- `.remove()` removes the first matching value from a list.
- `.count()` counts how many times a value appears.
- `.index()` finds the first position of a value.

## Strings

- `.split()` breaks a string into a list.
- `.join()` combines strings from a list or other iterable.
- `.strip()` removes whitespace or selected characters from the start and end.
- `.replace()` returns a string with text replaced.
- `.startswith()` and `.endswith()` check string prefixes and suffixes.
- `.find()` returns the first matching index, or `-1` if not found.
- `.lower()` and `.upper()` normalize text casing.
- `.capitalize()` makes the first character uppercase and the rest lowercase.
- `.title()` makes the first character of each word uppercase.
- `.islower()` checks whether the cased characters in a string are lowercase.
- `.isupper()` checks whether the cased characters in a string are uppercase.
- `.isdigit()`, `.isalpha()`, and `.isalnum()` check what kind of characters a string contains.
- `.casefold()` is stronger than `.lower()` for case-insensitive text comparisons.

## Sets

- `.add()` adds one item to a set.
- `.discard()` removes an item from a set without error if it is missing.
- `.union()`, `.intersection()`, and `.difference()` compare sets.

## `collections`

- `collections.Counter` counts how many times each value appears.
- `collections.Counter.most_common()` finds the most frequent elements, returning them as a sorted list of tuples.
- `collections.defaultdict` gives missing dictionary keys a default value automatically. Useful for grouping and counting.
- `collections.deque` is useful for queues because adding or removing from both ends is fast.

## `heapq`

- `heapq.heappush()` and `heapq.heappop()` help when repeatedly needing the smallest item.

## `itertools`

- `itertools.product()` creates all combinations from multiple iterables.
- `itertools.combinations()` creates unique groups where order does not matter.
- `itertools.permutations()` creates arrangements where order does matter.
- `itertools.chain()` treats multiple iterables as one continuous iterable.
- `itertools.groupby()` groups neighboring matching items. Sort first when you need all equal values grouped together.

## `functools` & `operator`

- `functools.reduce()` combines an iterable into one final value by repeatedly applying a function.
- `functools.lru_cache` remembers function results. Useful for recursive problems with repeated work.
- `operator.itemgetter()` is useful with `key=` when sorting or selecting tuple/list/dictionary values.
- `operator.mul()` is multiplication as a function. Useful with `map()` or `functools.reduce()` when a function is needed instead of the `*` operator.

## Math & numbers

- `abs()` returns the positive distance from zero.
- `round()` rounds numbers (banker's rounding).
- `divmod()` gives quotient and remainder together.
- `pow()` can calculate powers, and with three arguments can do modular exponentiation.

## Characters

- `chr()` converts a Unicode number to a character.
- `ord()` converts a character to its Unicode number.

## Other handy methods

- `.setdefault()` creates a missing dictionary key with a default value, though `defaultdict` is often cleaner.
- `.copy()` makes a shallow copy of a list, dictionary, or set.
- `.clear()` removes all items from a list, dictionary, or set.
