# Regex Advanced

## Groups & capturing

```python
import re

text = "Please write down the phone number, (555)-134-3213"

# use \( and \) for literal parentheses — bare () are group syntax
phone_pattern = r'\(\d{3}\)-\d{3}-\d{4}'
phone_number = re.search(phone_pattern, text)
print(phone_number.group())  # or phone_number[0]

# capturing groups
phone_pattern = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})')
phone_number = re.search(phone_pattern, text)
print(phone_number.group(2))   # the middle 3 digits
```

## Operators: `|`, `.`, `^`, `$`

```python
# OR
re.search(r"cat|dog", "The cat is here")
re.search(r"(cat|dog)(man|nap)", "The catman is here")

# wildcard .
re.findall(r".at", "The cat in the hat went after a gnat")
re.findall(r"..at", "The cat in the hat went after a gnat")

# anchors
re.findall(r'^\d', '1 is a number')   # starts with a digit
re.findall(r'\d$', 'number 2')        # ends with a digit
```

`^` and `$` anchor the pattern to the start / end of the string. Together they force the pattern to match the **entire** string.

## Negated character classes

```python
phrase = "there are 3 numbers 34 inside 5 this sentence"

# digits only
re.findall(r'[\d]', phrase)

# everything except digits
re.findall(r'[^\d]+', phrase)
```

Notes:

- `[]` is a character class (match ONE character from the set).
- `()` is for grouping/capturing.
- `^` outside `[]` means **start of string**.
- `^` inside `[]` means **NOT these characters**.

```python
test_phrase = "This is a string! But it has punctuation. How can we remove it?"

cleaned_words = re.findall(r'[^?!. ]+', test_phrase)
# Inside [], the period loses its special meaning — it's treated as a literal.

' '.join(cleaned_words)
```

```python
text = "The well-known author wrote a best-selling book about state-of-the-art technology..."
re.findall(r'[\w]+-[\w]+', text)
```

## Splitting

```python
import re

n = "100,000,000.000"
regex_pattern = r"[,\.]"

print("\n".join(re.split(regex_pattern, n)))
```

## Named groups

`groupdict()` returns a dictionary of named capturing groups:

```python
import re
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)', 'myname@hackerrank.com')
m.groupdict()
# {'user': 'myname', 'website': 'hackerrank', 'extension': 'com'}
```

## Backreferences

`\1` refers to the **exact text** matched by the first capturing group. It does not mean "repeat once" — it means "match the same character again".

- `(\w)` — captures one character into group 1
- `\1` — matches that same character one more time
- So `(\w)\1` matches exactly **2** consecutive identical characters: `aa`, `11`, etc.

To match **2 or more** (`aa`, `aaa`, `aaaa`, …): apply a quantifier directly to the backreference: `(\w)\1+`.

| Pattern | Matches |
|---|---|
| `(\w)\1` | exactly 2 identical chars: `aa` |
| `(\w)\1+` | 2 or more identical chars: `aa`, `aaa`, `aaaa` |

```python
# find first repeating alphanumeric character
s = "__commit__"
re.search(r"([a-zA-Z0-9])\1+", s).group(1)
```

> **`findall` and groups**
>
> - One capturing group → list of group-matched strings.
> - Multiple groups → list of tuples, one element per group.


## Lookaheads

A **lookahead** checks if a pattern exists ahead in the string **without consuming** any characters. The regex engine "peeks" forward, then continues matching from the same position.

| Syntax | Name | Meaning |
|---|---|---|
| `(?=...)` | Positive lookahead | Asserts that `...` **does** match ahead |
| `(?!...)` | Negative lookahead | Asserts that `...` **does not** match ahead |

Lookaheads are **zero-width assertions** — they don't move the cursor forward.

### Example: password with at least 2 uppercase and at least 3 digits

```python
r"(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})^[a-zA-Z0-9]{10}$"
```

- `(?=(?:.*[A-Z]){2})` — peek ahead: at least 2 uppercase letters anywhere?
- `(?=(?:.*\d){3})` — peek ahead: at least 3 digits anywhere?
- `^[a-zA-Z0-9]{10}$` — then actually match: exactly 10 alphanumeric characters

Each lookahead runs from the same starting position, so you can **stack multiple constraints** at the front of a regex.

### Negative lookahead: no repeated characters

```python
r"(?!.*(.).*\1)"
```

- `(?!...)` — assert the following does NOT match
- `.*(.).*\1` — any char captured in group, then the same char appears again (backreference)

> **Sometimes plain Python wins**
>
> The multi-check approach (separate `re.findall` calls + `set()`) is often more readable than cramming everything into one regex with lookaheads.

