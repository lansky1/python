# Regex Basics

The `in` keyword only tells us if a substring exists. `re` gives us location and pattern matching.

```python
"dog" in "my dog is a Husky"   # True — but no position
```

## Search, findall, finditer

Phone-number pattern example:

```
(555)-555-5555
```

- `r"(\d\d\d)-\d\d\d-\d\d\d\d"` — basic pattern
- `r"(\d{3})-\d{3}-\d{4}"` — using quantifiers
- `\d` means digit

```python
import re

text = "The agent's phone number is 408-555-1234"

# `in` only tells us if it is there or not
print("phone" in text)

# search() — returns the first match (or None)
search_result = re.search("phone", text)
print(search_result)
print(search_result.span())
print(search_result.start())
print(search_result.end())

text2 = "This is my phone, that is his phone"

# findall() — all matches as a list of strings (no positions)
print(re.findall("phone", text2))

# finditer() — iterator of match objects
for item in re.finditer("phone", text2):
    print(item)
    print(item.span())
    print(item.group())  # the actual matched text
```

## Character classes

| Character | Description | Example pattern | Example match |
|---|---|---|---|
| `\d` | A digit | `file_\d\d` | `file_25` |
| `\w` | Alphanumeric (incl. `_`) | `\w-\w\w\w` | `A-b_1` |
| `\s` | Whitespace | `a\sb\sc` | `a b c` |
| `\D` | A non-digit | `\D\D\D` | `ABC` |
| `\W` | Non-alphanumeric | `\W\W\W\W\W` | `*-+=)` |
| `\S` | Non-whitespace | `\S\S\S\S` | `Yoyo` |

## Quantifiers

| Character | Description | Example | Match |
|---|---|---|---|
| `+` | One or more times | `Version \w-\w+` | `Version A-b1_1` |
| `{3}` | Exactly 3 times | `\D{3}` | `abc` |
| `{2,4}` | 2 to 4 times | `\d{2,4}` | `123` |
| `{3,}` | 3 or more times | `\w{3,}` | `anycharacters` |
| `*` | Zero or more times | `A*B*C*` | `AAACC` |
| `?` | Once or none | `plurals?` | `plural` |

## Escaping & character classes

### `\` — escaping
Escapes the character immediately after it, making it literal. Works **everywhere** in a pattern.
`\.` = literal dot, `\*` = literal asterisk, `\(` = literal parenthesis.

### `[]` — character class
Matches exactly **one** character from the set inside the brackets.

Most special regex characters (`. * + ? ( ) { } | $`) **lose their meaning** inside `[]` — they are treated as literals.

However, these four still have special meaning inside `[]`:

| Character | Meaning inside `[]` |
|---|---|
| `^` at the start | Negate — match anything NOT in this set |
| `-` between chars | Range — e.g., `[a-z]`, `[0-9]` |
| `\` | Escape — still works, e.g., `[\.]` |
| `]` | Closes the character class |

### Shorthand classes inside `[]`
`\w`, `\d`, `\s` keep their meaning inside `[]`:

- `[\w]` = `[a-zA-Z0-9_]`
- `[\d]` = `[0-9]`
- `[^\d]` = anything that is NOT a digit
