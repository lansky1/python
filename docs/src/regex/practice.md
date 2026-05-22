# Regex Practice

## Identify floating-point numbers

Requirements:

- Must start with a `+`, `-`, or `.`
- Must contain at least one decimal value
- Have only one decimal
- No exceptions when converted to `float(N)`

```python
import re

s = ["+4.5", "-1.0", ".5", "-.7", "+.4", "-+4.5", "12.", "12.0", "123..12"]
# Invalid: 12.  -+4.5  123..12

for num in s:
    print(num + "\t", re.search(r"^[-+]?\d*\.\d+$", num))
```

## Phone-number validation

```python
import re

numbers = ["9587456281", "1252478965", "8F54698745", "9898959398",
           "879546242", "999999999", "abc9999999999", "9999999999aaaa"]

for num in numbers:
    if re.search(r"^[789]\d{9}$", num):
        print(num + "\t", "YES")
    else:
        print(num + "\t", "NO")
```

> **Anchor your patterns**
>
> Without `$`, `"9999999999aaaa"` would match. Always anchor when validating an entire string.


## Email validation

Validation rules for `username@domain.extension`:

- Username: starts with an English letter, then alphanumerics (including `-`, `.`, `_`).
- Domain and extension: only English alphabetical characters.
- Extension: 1 to 3 characters.

```python
import re
import email.utils

inputs = [
    "DEXTER <dexter@hotmail.com>",
    "VIRUS <virus!@variable.:p>",
    "VARUN <varun1@hotmail.com>",
    "RICKY <3ricky@hotmail.com>",
]

for e in inputs:
    entry = email.utils.parseaddr(e)
    result = re.search(r"^[a-zA-Z][a-zA-Z0-9-._]+@[a-zA-Z]+[.][a-zA-Z]{1,3}$", entry[1])
    # Use \. for a literal dot — otherwise it's a wildcard.
    if result:
        print(email.utils.formataddr(entry))
```

> **`email.utils.parseaddr` is RFC-strict**
>
> Email strings that don't conform to RFC standards (like `virus!@variable.:p`) won't be parsed cleanly.


## Overlapping substring search

```python
import re

str_ = "aaadaa"
substr = "aa"

found = False
for match_ in re.finditer(f"(?={substr})", str_):
    print((match_.start(), match_.start() + len(substr) - 1))
    found = True

if not found:
    print((-1, -1))
```

`re.finditer` with a positive lookahead pattern `(?=...)` finds **overlapping** matches because the lookahead doesn't consume characters.
