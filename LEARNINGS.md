# Learnings

## Boolean Expressions

- No need to manually return `True` or `False` when the condition already produces a boolean result. Return the boolean result directly.

## Strings

- Slicing works on strings and arrays/lists using `value[start:stop:step]`.
  - `value[:]` means the complete value.
  - `value[start:]` means start from `start` and continue to the end.
  - `value[:stop]` means start from the beginning and stop before `stop`.
  - `value[start:stop]` means take the part from `start` up to, but not including, `stop`.
  - `value[::step]` means take items by skipping according to `step`.
  - `value[::-1]` means traverse in reverse.
  - Negative indexes count from the end, so they are useful for last items or slicing from the back.
  - Slicing is safe when the value is shorter than expected, so separate length checks are often unnecessary.

- Use string methods like `.lower()` and `.endswith()` to avoid manual character-by-character checks.

```python
def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)
```

- Use `join()` when building a new string from many pieces.

```python
def double_char(s):
    return ''.join([c + c for c in s])
```

## Conditional Expressions

- A conditional expression can choose between two values inline.
- The walrus operator `:=` assigns a value inside an expression. Use it sparingly, mainly when it avoids repeating the same calculation or lookup.
- In tuple assignment, the complete right-hand side is evaluated before any left-hand side assignment happens. If one assigned value depends on another new value, store the new value in a temporary variable first.

```python
def combo_string(a, b):
  short, long = (a, b) if len(a) < len(b) else (b, a)
  return short + long + short
```

## Scope And Global Variables

- Python looks for variable names using the LEGB rule:
  - `Local`: names inside the current function.
  - `Enclosing`: names in outer functions when functions are nested.
  - `Global`: names at the top level of the current file/module.
  - `Built-in`: names Python provides automatically, like `print`, `len`, and `sum`.
- A variable assigned inside a function is local to that function by default.
- The `global` keyword lets a function reassign a variable from the global/module scope.
- The `nonlocal` keyword lets a nested function reassign a variable from an enclosing function scope.
- Avoid using `global` when possible because it makes functions depend on outside state and can make code harder to reason about.
- Prefer returning the new value from the function and assigning it back outside the function.

```python
count = 0

def increase_count(count):
  return count + 1

count = increase_count(count)
```

## Modules And Script Entry Points

- Every Python file has a `__name__` value.
- When a file is run directly, Python sets `__name__` to `"__main__"`.
- When a file is imported, `__name__` becomes the module's name instead.
- Use `if __name__ == "__main__":` to run code only during direct execution, not during import.
- This helps organize code so functions/classes stay reusable, while script-specific code stays in one clear entry point.
- Keep reusable code outside this block, such as functions, classes, and constants.
- Keep script-only code inside this block, such as calling `main()`, user input, printing final output, demos, file reading, or command-line argument handling.
- This prevents another file from accidentally starting the whole program just because it imported one function.

```python
def greet(name):
  return f"Hello, {name}"

def main():
  name = input("Name: ")
  print(greet(name))

if __name__ == "__main__":
  main()
```

## List Comprehensions

- List comprehensions can build and filter lists in one expression.

```python
print([[X,Y,Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X+Y+Z != n])
```

```python
def count_evens(nums):
  return sum([1 for num in nums if num%2==0])
```

## Common Functions And Methods To Know

- `print()` can receive multiple values, including variables. By default, it prints them on the same line separated by spaces. Use `sep=` to change the separator and `end=` to change what comes after the print.
- In Jupyter notebooks, `clear_output()` from `IPython.display` clears the previous cell output. This is useful when updating output repeatedly, such as inside a loop.

```python
from IPython.display import clear_output

clear_output()
```

- `enumerate()` gives both the index and the value while looping.
- `zip()` loops over multiple sequences together and pairs related items.
- `sum()` adds values and can also count truthy results.
- `min()` and `max()` find the smallest or largest item, and become more powerful with `key=`.
- `any()` checks if at least one item is true.
- `all()` checks if every item is true.
- `sorted()` returns a new sorted list.
- `.sort()` sorts a list in place.
- `reversed()` loops through a sequence backwards without manually managing indexes.
- `map()` transforms every item. It is useful when one existing function should be applied to every value.
- `filter()` keeps only the items that pass a condition.
- List comprehensions are often clearer than `map()` and `filter()` when the logic is short.
- `list()` converts an iterable into a list.
- `tuple()` converts an iterable into a tuple.
- `set()` removes duplicates and gives fast membership checks.
- `dict()` can build dictionaries from pairs or keyword arguments.
- `str()` converts a value into a string.
- `int()` converts compatible values into integers.
- `float()` converts compatible values into decimal numbers.
- `bool()` converts a value into `True` or `False` based on truthiness.
- `isinstance()` checks whether a value belongs to a type. Prefer it over comparing `type()` directly.
- `.get()` safely reads a dictionary key with an optional default value.
- `.items()` loops through dictionary keys and values together.
- `.keys()` gets dictionary keys.
- `.values()` gets dictionary values.
- `.update()` adds or replaces multiple dictionary entries.
- `dict.fromkeys()` creates a dictionary from keys, giving each key the same starting value. If no value is passed, the value is `None`. Duplicate keys are removed because dictionary keys must be unique.
- `.append()` adds one item to the end of a list.
- `.extend()` adds many items to the end of a list.
- `.insert()` adds an item at a specific list position.
- `.pop()` removes and returns an item from a list or dictionary.
- `.remove()` removes the first matching value from a list.
- `.count()` counts how many times a value appears.
- `.index()` finds the first position of a value.
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
- `.add()` adds one item to a set.
- `.discard()` removes an item from a set without error if it is missing.
- `.union()`, `.intersection()`, and `.difference()` compare sets.
- `collections.Counter` counts how many times each value appears.
- `collections.defaultdict` gives missing dictionary keys a default value automatically. Useful for grouping and counting.
- `collections.deque` is useful for queues because adding or removing from both ends is fast.
- `heapq.heappush()` and `heapq.heappop()` help when repeatedly needing the smallest item.
- `itertools.product()` creates all combinations from multiple iterables.
- `itertools.combinations()` creates unique groups where order does not matter.
- `itertools.permutations()` creates arrangements where order does matter.
- `itertools.chain()` treats multiple iterables as one continuous iterable.
- `itertools.groupby()` groups neighboring matching items. Sort first when you need all equal values grouped together.
- `functools.reduce()` combines an iterable into one final value by repeatedly applying a function.
- `functools.lru_cache` remembers function results. Useful for recursive problems with repeated work.
- `operator.itemgetter()` is useful with `key=` when sorting or selecting tuple/list/dictionary values.
- `operator.mul()` is multiplication as a function. Useful with `map()` or `functools.reduce()` when a function is needed instead of the `*` operator.
- `abs()` returns the positive distance from zero.
- `round()` rounds numbers.
- `divmod()` gives quotient and remainder together.
- `pow()` can calculate powers, and with three arguments can do modular exponentiation.
- `chr()` converts a Unicode number to a character.
- `ord()` converts a character to its Unicode number.
- `.setdefault()` creates a missing dictionary key with a default value, though `defaultdict` is often cleaner.
- `.copy()` makes a shallow copy of a list, dictionary, or set.
- `.clear()` removes all items from a list, dictionary, or set.
- `.isdigit()`, `.isalpha()`, and `.isalnum()` check what kind of characters a string contains.
- `.casefold()` is stronger than `.lower()` for case-insensitive text comparisons.

## Loops

- A `for` loop controls its next value automatically. Use `while` when you need to manually change the loop index inside the loop.
- Python supports an `else` block on `for` and `while` loops. The `else` block runs only when the loop finishes normally, not when it exits with `break`.
- Use `range(len(value) - window_size + 1)` when checking slices of a fixed size.

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

## Subset 

```python
# Method
{1, 2, 3}.issubset({1, 2, 3, 4, 5})  # True

# Operator
{1, 2, 3} <= {1, 2, 3, 4, 5}         # True
```

## Classes

Python's built-in types are classes but use lowercase names. This violates PEP 8's convention that classes should use PascalCase (CapWords).

**Reference:** [PEP 8 — Class Names](https://peps.python.org/pep-0008/#class-names)

- In Python 3, `class Dog:` and `class Dog():` are identical. 

### Permission Scope

Python has no enforced access control. It's convention-based:

| Naming | Convention | Enforced? |
|---|---|---|
| `species` | Public | No |
| `_species` | Internal, don't touch from outside | No |
| `__species` | Name mangling, harder to access | Partially |

`__species` gets mangled to `_Dog__species` — still accessible, just deliberately inconvenient. Python's position is explicit: **convention over enforcement**. There is no true `private`.

#### Console execution inside shell

```python
import os
os.system("pylint test.py")
```

```python
import subprocess

subprocess.run(["pylint", "test.py", "-r", "y"])
```

```python
import subprocess
import sys

subprocess.run([sys.executable, "-m", "pylint", "test.py", "-r", "y"])
```
