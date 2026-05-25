# Regular Expressions

## Basics: `search`, `findall`, `finditer`

The `in` keyword only tells us if a substring exists. `re` gives us location and pattern matching.

```python
"dog" in "my dog is a Husky"   # True
```

Phone number pattern example:

```
(555)-555-5555
```

- `r"(\d\d\d)-\d\d\d-\d\d\d\d"` — basic pattern.
- `r"(\d{3})-\d{3}-\d{4}"` — using quantifiers.
- `\d` means digit.

```python
import re

text = "The agent's phone number is 408-555-1234"

# 1. `in` keyword only checks existence
print("phone" in text)

# 2. re.search — first match only, returns a Match object
search_result = re.search("phone", text)
print(search_result)
print(search_result.span())   # (12, 17)
print(search_result.start())
print(search_result.end())

text2 = "This is my phone, that is his phone"

# 3. re.findall — returns every non-overlapping match (no location)
re.findall("phone", text2)    # ['phone', 'phone']

# 4. re.finditer — iterator of Match objects, gives location too
for item in re.finditer("phone", text2):
    print(item)
    print(item.span())
    print(item.group())   # actual text that matched
# <re.Match object; span=(11, 16), match='phone'>
# <re.Match object; span=(30, 35), match='phone'>
```

## Character Classes & Quantifiers

| Class | Description | Example pattern | Example match |
| --- | --- | --- | --- |
| `\d` | A digit | `file_\d\d` | `file_25` |
| `\w` | Alphanumeric or `_` | `\w-\w\w\w` | `A-b_1` |
| `\s` | Whitespace | `a\sb\sc` | `a b c` |
| `\D` | Non-digit | `\D\D\D` | `ABC` |
| `\W` | Non-alphanumeric | `\W\W\W\W\W` | `*-+=)` |
| `\S` | Non-whitespace | `\S\S\S\S` | `Yoyo` |

| Quantifier | Description | Example pattern | Example match |
| --- | --- | --- | --- |
| `+` | One or more | `Version \w-\w+` | `Version A-b1_1` |
| `{3}` | Exactly 3 times | `\D{3}` | `abc` |
| `{2,4}` | 2 to 4 times | `\d{2,4}` | `123` |
| `{3,}` | 3 or more | `\w{3,}` | `anycharacters` |
| `*` | Zero or more | `A*B*C*` | `AAACC` |
| `?` | Once or none | `plurals?` | `plural` |

### `\` Backslash — Escaping

Escapes the character immediately after it, making it literal. Works **everywhere** in a pattern.

- `\.` = literal dot, `\*` = literal asterisk, `\(` = literal parenthesis.

### `[]` Character Class — Match One Character from a Set

Matches exactly **one** character from the set defined inside the brackets.

Most special regex characters (`. * + ? ( ) { } | $`) **lose their meaning** inside `[]` — they are treated as literals.

However, these four still have special meaning inside `[]`:

| Character | Meaning inside `[]` |
| --- | --- |
| `^` at the start | Negate — match anything NOT in this set |
| `-` between chars | Range — e.g., `[a-z]`, `[0-9]` |
| `\` | Escape — still works, e.g., `[\.]` |
| `]` | Closes the character class |

### `\w`, `\d`, `\s` inside `[]`

Shorthand classes **keep their meaning** inside `[]`:

- `[\w]` is the same as `[a-zA-Z0-9_]`.
- `[\d]` is the same as `[0-9]`.
- `[^\d]` is anything that is NOT a digit.

## Groups & Capturing

```python
text = "Please write down the phone number, (555)-134-3213"

# Cannot use bare parentheses — they mean "group" in regex
phone = re.search(r'\(\d{3}\)-\d{3}-\d{4}', text)
print(phone)

phone_pattern = r'\(\d{3}\)-\d{3}-\d{4}'
phone_number = re.search(phone_pattern, text)
print(phone_number.group())   # same as phone_number[0]

phone_pattern = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})')   # capturing groups
phone_number = re.search(phone_pattern, text)
print(phone_number.group(2))  # second group
```

## Operators: `|`, `.`, `^`, `$`

```python
# Or statement |
or_result = re.search(r"cat|dog", "The cat is here")
print("or_result:", or_result)

or_result_2 = re.search(r"(cat|dog)(man|nap)", "The catman is here")
print("or_result_2:", or_result_2)

# wildcard character .
wildcard_result = re.findall(r".at", "The cat in the hat went after a gnat")
print("wildcard_result:", wildcard_result)

wildcard_result_2 = re.findall(r"..at", "The cat in the hat went after a gnat")
print("wildcard_result_2:", wildcard_result_2)

# starts with operator ^
starts_with_a_number = re.findall(r'^\d', '1 is a number')
print("starts_with_a_number:", starts_with_a_number)

# ends with operator $
ends_with_a_number = re.findall(r'\d$', 'number 2')
print("ends_with_a_number:", ends_with_a_number)
```

The caret `^` anchors the pattern to the start of the string and `$` anchors to the end. Together, `^...$` forces the pattern to match the entire string from beginning to end.

## Character Class Exclusion with `[^]`

```python
# Find numbers inside a string
phrase = "there are 3 numbers 34 inside 5 this sentence"
pattern = r'[\d]'
print("Attempt 1: Identified Numbers", re.findall(pattern, phrase))

# Then keep everything that is not a digit
pattern = r'[^\d]+'
print("Attempt 2: Non-digit chunks", re.findall(pattern, phrase))
```

Quick summary of bracket meanings:

- `[]` defines a **character class**: matches any ONE character from the set inside.
- `()` defines a **group** for capturing: groups parts of the pattern together and captures matched text for later use.
- `^` outside `[]` means **start of string**.
- `^` inside `[]` means **NOT these characters**.

```python
test_phrase = "This is a string! But it has punctuation. How can we remove it?"
cleaned_words = re.findall(r'[^?!. ]+', test_phrase)
# Inside [], the period loses its special meaning — it is a literal '.'

' '.join(cleaned_words)
```

```python
text = "The well-known author wrote a best-selling book about state-of-the-art technology, but some people dislike hyphen-words or non-hyphenated words."
re.findall(r'[\w]+-[\w]+', text)
# ['well-known', 'best-selling', 'state-of', 'the-art', 'hyphen-words', 'non-hyphenated']
```

## Practice: Identify Floating Point Numbers

Rules:

- Must start with `+`, `-`, or `.`.
- Number must contain at least one decimal value.
- Have only one decimal.

```python
s = ["+4.5", "-1.0", ".5", "-.7", "+.4", "-+4.5", "12.", "12.0", "123..12"]

for num in s:
    print(num + "\t", re.search(r"^[-+]?\d*\.\d+$", num))
```

## Splitting & Named Groups

```python
import re

n = "100,000,000.000"
regex_pattern = r"[,\.]"

print("\n".join(re.split(regex_pattern, n)))
```

`groupdict()` returns a dictionary of named capturing groups:

```python
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)', 'myname@hackerrank.com')
m.groupdict()
# {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
```

### Backreferences

`\1` refers to the **exact text** matched by the first capturing group `()`. It does not mean "repeat once" — it means "match the same character again."

- `(\w)` — captures one character into group 1.
- `\1` — matches that **same character** one more time.
- So `(\w)\1` matches exactly **2** consecutive identical characters: `aa`, `11`, etc.

To match **2 or more** (i.e., `aa`, `aaa`, `aaaa`, ...):

- Apply a quantifier directly to the backreference: `(\w)\1+`.
- `\1+` = "one or more additional occurrences of the captured character".

| Pattern | Matches |
| --- | --- |
| `(\w)\1` | exactly 2 identical chars: `aa` |
| `(\w)\1+` | 2 or more identical chars: `aa`, `aaa`, `aaaa` |

```python
# find first repeating substring alphanumeric character
s = "__commit__"
re.search(r"([a-zA-Z0-9])\1+", s).group(1)
```

> If your pattern has one capturing group (e.g. `(\w)\1+`), `findall()` returns a list of the text matched by that group (just the character).
> If your pattern has multiple capturing groups (e.g. `((\w)\2+)`), `findall()` returns a list of tuples: each tuple contains the text matched by each group.

### Lookaheads

A **lookahead** checks if a pattern exists ahead in the string **without consuming** any characters. The regex engine peeks forward, then continues matching from the same position.

| Syntax | Name | Meaning |
| --- | --- | --- |
| `(?=...)` | Positive lookahead | Asserts that `...` **does** match ahead |
| `(?!...)` | Negative lookahead | Asserts that `...` **does not** match ahead |

Lookaheads are **zero-width assertions** — they don't move the cursor forward.

**Example: Password must have at least 2 uppercase and at least 3 digits**

```python
r"(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})^[a-zA-Z0-9]{10}$"
```

- `(?=(?:.*[A-Z]){2})` — peek ahead: are there at least 2 uppercase letters anywhere?
- `(?=(?:.*\d){3})` — peek ahead: are there at least 3 digits anywhere?
- `^[a-zA-Z0-9]{10}$` — then actually match: exactly 10 alphanumeric characters.

Each lookahead runs from the same starting position, so you can **stack multiple constraints** at the front of a regex.

**Negative lookahead example: no repeated characters**

```python
r"(?!.*(.).*\1)"
```

- `(?!...)` — assert the following does NOT match.
- `.*(.).*\1` — any char captured in group, then the same char appears again (backreference).

> The multi-check approach (separate `re.findall` calls + `set()`) is often more readable than cramming everything into one regex with lookaheads.
