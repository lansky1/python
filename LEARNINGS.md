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

```python
def combo_string(a, b):
  short, long = (a, b) if len(a) < len(b) else (b, a)
  return short + long + short
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
