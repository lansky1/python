# Strings

## Basics

```python
my_string = "Hello"
print(my_string[:2])    # 'He'
print(my_string[::-2])  # 'olH' — slice with step
my_string[1:-1]         # skips first and last character
"Hello World"[8]        # 'r'
'a' * 10                # 'aaaaaaaaaa'
```

## Slicing

Slicing works on strings and arrays/lists using `value[start:stop:step]`.

| Syntax | Meaning |
|---|---|
| `value[:]` | The complete value |
| `value[start:]` | From `start` to the end |
| `value[:stop]` | From the beginning, stopping before `stop` |
| `value[start:stop]` | From `start` up to (not including) `stop` |
| `value[::step]` | Take items by skipping |
| `value[::-1]` | Reverse |

Negative indexes count from the end — useful for the last items or slicing from the back.

> **Slicing is safe**
>
> Slicing never raises `IndexError`, even when the value is shorter than expected. Separate length checks are often unnecessary.


## String methods over manual loops

Prefer the built-in methods — they are clearer and faster than character-by-character checks.

```python
def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)
```

```python
def double_char(s):
    return ''.join([c + c for c in s])
```

## Formatting with `.format()`

- `{}` are positional placeholders
- Named placeholders like `{q}` are keyword arguments
- Positional and keyword arguments cannot be mixed in the same call

```python
print("This is a string {}".format("Inserted"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
```

## f-strings

```python
name = "John"
print(f"Hello, my name is {name}")
```

## Concatenation performance

> **Avoid repeated `+=`**
>
> Repeated string concatenation (`s += other`) is O(n²) because strings are immutable. Use `''.join(...)` instead.


```python
parts = ["a", "b", "c"]
result = ''.join(parts)
```

## Useful string methods

- `.split()` / `.join()` — break apart and combine
- `.strip()` — remove whitespace or selected characters from the start and end
- `.replace(old, new)` — substitute substrings
- `.startswith()` / `.endswith()` — check prefixes/suffixes
- `.find(sub)` — first matching index, or `-1` if absent
- `.lower()` / `.upper()` — normalize casing
- `.capitalize()` — uppercase first character, rest lowercase
- `.title()` — uppercase first character of each word
- `.islower()` / `.isupper()` — check casing
- `.isdigit()` / `.isalpha()` / `.isalnum()` — character-type checks
- `.casefold()` — stronger than `.lower()` for case-insensitive comparison
- `.count(sub)` — count occurrences
- `.index(sub)` — first position of value (raises if missing)
