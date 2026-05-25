# Strings

```python
my_string = "Hello"
print(my_string[:2])     # 'He'
print(my_string[::-2])   # 'olH'  — reverse, every 2nd char
my_string[1:-1]          # 'ell' — skips first and last character
print(my_string[5])      # IndexError
print("Hello World"[8])  # 'r'
letter = 'a'
print(letter * 10)       # 'aaaaaaaaaa'
```

## Slicing

Slicing works on strings and any other sequence using `value[start:stop:step]`.

| Form | Meaning |
| --- | --- |
| `value[:]` | The complete value |
| `value[start:]` | From `start` to the end |
| `value[:stop]` | From the beginning, stopping before `stop` |
| `value[start:stop]` | From `start` up to, but not including, `stop` |
| `value[::step]` | Skip items by `step` |
| `value[::-1]` | Traverse in reverse |

- Negative indexes count from the end, useful for last items or slicing from the back.
- Slicing is safe when the value is shorter than expected, so separate length checks are often unnecessary.

## String Formatting with `.format()`

- `{}` are positional placeholders.
- Named placeholders like `{name}` are keyword arguments.
- Positional and keyword arguments cannot be mixed in the same call.

```python
print("This is a string {}".format("Inserted"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
print("The {} {} {}".format(f="fox", b="brown", q="quick"))   # KeyError
```

## F-Strings

```python
name = "John"
print(f"Hello, my name is {name}")
```

## String Concatenation

Repeated string concatenation (`+=`) is O(n²) in Python because strings are immutable — every `+=` allocates a fresh string. Use `''.join(...)` instead when assembling a string from many pieces.

```python
def double_char(s):
    return ''.join([c + c for c in s])
```

Adjacent string literals are joined by Python before runtime. Parentheses make this useful for splitting one long string over several lines.

```python
text = (
    "Lorem ipsum dolor sit amet. "
    "Lorem ipsum dolor sit amet. "
    "Lorem ipsum dolor sit amet."
)
```

## String Methods That Avoid Manual Loops

Prefer built-in methods like `.lower()` and `.endswith()` over hand-rolled character-by-character checks.

```python
def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)
```

> Return the boolean expression directly when it already produces `True` / `False`. Don't wrap it with an `if` that returns `True` or `False` literals.

## Common String Methods

```python
s = 'hello world'

s.capitalize()    # 'Hello world'
s.upper()         # 'HELLO WORLD'
s.lower()         # 'hello world'
s.count('o')      # 2
s.find('o')       # 4
s.center(20, 'z') # 'zzzzhello worldzzzzz'  — 20 is total final length

mixed = 'SoMe RaNDoM sTriNg'
mixed.swapcase()  # 'sOmE rAndOm StRInG'
```

```python
print('hello\thi')             # hello\thi  (tab kept literal)
'hello\thi'.expandtabs()       # 'hello   hi'
```

### Useful string constants

The `string` module provides ready-made groups of characters.

```python
import string

letters = list(string.ascii_lowercase)
print(letters[:5])  # ['a', 'b', 'c', 'd', 'e']
```

### Predicate methods

```python
s = 'hello'
s.isalnum()    # True
s.isalpha()    # True
s.islower()    # True
s.isspace()    # False
s.istitle()    # False
s.isupper()    # False
s.endswith('o')  # True

s1 = 'Hello World'
s2 = 'HELLO'
s3 = 'Hello'
s4 = 'HeLLo Wo'
print(s1.istitle(), s2.istitle(), s3.istitle(), s4.istitle())
# True False True False
```

> `.casefold()` is stronger than `.lower()` for case-insensitive text comparisons across Unicode (e.g., German `ß`).

### Splitting & partitioning

```python
'helloei'.split('e')        # ['h', 'llo', 'i']
'hello world'.partition('e')  # ('h', 'e', 'llo world')  — separator around 1st instance
```
