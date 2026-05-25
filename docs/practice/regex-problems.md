# Regex Problems

## Starts with Digit

Match strings that start with a digit followed by one or more non-digit characters.

```python
import re

strings = ["12ABC", "AVS", "WF3FE", "1fe"]

for s in strings:
    result = re.search(r"^[\d][^\d]+", s)
    print(result)
```

## Phone Number Validation

Indian mobile numbers: must be 10 digits and start with 7, 8, or 9.

```python
import re

numbers = ["9587456281", "1252478965", "8F54698745", "9898959398",
           "879546242", "999999999", "abc9999999999", "9999999999aaaa"]

for num in numbers:
    if re.search(r"^[789]\d{9}", num):
        print(num + "\t", "YES")
    else:
        print(num + "\t", "NO")

# Need to add a `$` anchor — otherwise "9999999999aaaa" matches as valid.
```

## Email Validation

Validation rules for `username@domain.extension`:

- Username: starts with English letter + alphanumeric characters (including `-`, `.`, `_`).
- Domain and Extension: only English alphabetical characters.
- Extension: 1 to 3 characters max.

```python
import re
import email.utils

inputs = [
    "DEXTER <dexter@hotmail.com>",
    "VIRUS <virus!@variable.:p>",
    "VARUN <varun1@hotmail.com>",
    "RICKY <3ricky@hotmail.com>",
]

# The second one is against RFC standards, so parseaddr returns no result for it.

for e in inputs:
    entry = email.utils.parseaddr(e)
    # entry looks like ('DEXTER', 'dexter@hotmail.com')
    # email.utils.formataddr(entry) reverses it back to "DEXTER <dexter@hotmail.com>"
```

A wider test set:

```python
inputs = [
    # --- VALID ---
    "DEXTER <dexter@hotmail.com>",
    "ALICE <alice@gmail.org>",
    "BOB <b.o.b@domain.io>",
    "CARL <carl_99@sub.net>",
    "DAN <d-a-n@company.co>",
    "EVE <a1.b2_c3-d4@mail.uk>",

    # --- INVALID USERNAME: bad starting char ---
    "RICKY <3ricky@hotmail.com>",
    "SCOTT <_scott@hotmail.com>",
    "TOM <-tom@hotmail.com>",
    "UMA <.uma@hotmail.com>",
    "VERA <@hotmail.com>",

    # --- INVALID USERNAME: illegal characters ---
    "VIRUS <virus!@variable.com>",
    "WILL <wi ll@domain.com>",
    "XENA <xe#na@domain.com>",
    "YARA <ya$ra@domain.com>",
    "ZACK <za*ck@domain.com>",
    "ADAM <ad@m@domain.com>",

    # --- INVALID DOMAIN: illegal characters ---
    "VARUN <varun@hot1mail.com>",
    "BILL <bill@hot-mail.com>",
    "CARA <cara@hot_mail.com>",
    "DAVE <dave@hot.mail.com>",
    "EMMA <emma@.com>",

    # --- INVALID EXTENSION: wrong length ---
    "VARUN <varun1@hotmail.comc>",
    "FINN <finn@mail.c>",
    "GINA <gina@mail.toolongext>",
    "HANS <hans@mail.>",

    # --- INVALID EXTENSION: illegal characters ---
    "IAN <ian@variable.:p>",
    "JADE <jade@mail.c0m>",
    "KYLE <kyle@mail.co!>",
    "LENA <lena@mail.c_m>",

    # --- STRUCTURAL / FORMAT ISSUES ---
    "MIKE <mike@>",
    "NINA <@domain.com>",
    "OMAR <omardomain.com>",
    "PAM <pam@domaincom>",
    "QUINN <>",
]

for e in inputs:
    entry = email.utils.parseaddr(e)
    result = re.search(r"^[a-zA-Z][a-zA-Z0-9-._]+@[a-zA-Z]+[.][a-zA-Z]{1,3}$", entry[1])
    if result:
        print(email.utils.formataddr(entry))
```

> Use `\.` for a literal dot. Without escaping, `.` is the wildcard.

## Overlapping Substring Search

Plain `re.finditer` advances the cursor past each match, so overlapping occurrences are skipped. A zero-width lookahead lets the engine peek without consuming:

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
