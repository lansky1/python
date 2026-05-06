# Learnings

- No need to manually return true or false when the condition already produces a boolean result. Return the boolean result directly.
- Slicing works on strings and arrays/lists using `value[start:stop:step]`.
  - `value[:]` means the complete value.
  - `value[start:]` means start from `start` and continue to the end.
  - `value[:stop]` means start from the beginning and stop before `stop`.
  - `value[start:stop]` means take the part from `start` up to, but not including, `stop`.
  - `value[::step]` means take items by skipping according to `step`.
  - `value[::-1]` means traverse in reverse.
  - Negative indexes count from the end, so they are useful for last items or slicing from the back.
  - Slicing is safe when the value is shorter than expected, so separate length checks are often unnecessary.

```python
def combo_string(a, b):
  short, long = (a, b) if len(a) < len(b) else (b, a)
  return short + long + short
```

```python
print([[X,Y,Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X+Y+Z != n])
```

```python
def count_evens(nums):
  return sum([1 for num in nums if num%2==0])
```

```python
def double_char(s):
    return ''.join([c + c for c in s])
```

- `for` loop doesn't allow manual index control, so switch to `while`.

```python
def cat_dog(str):
  count_cat = 0
  count_dog = 0
  for idx in range(len(str)-2):
    if str[idx:idx+3] == 'cat':
      count_cat+=1
  for idx in range(len(str)-2):
    if str[idx:idx+3] == 'dog':
      count_dog+=1
  return count_cat == count_dog
```

```python
def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)
```