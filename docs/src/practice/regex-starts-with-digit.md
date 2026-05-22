# Regex: Starts With Digit

Match strings that **start with a digit** followed by one or more non-digit characters.

```python
import re

strings = ["12ABC", "AVS", "WF3FE", "1fe"]

for s in strings:
    result = re.search(r"^[\d][^\d]+", s)
    print(result)
```

Notes:

- `^` anchors the match to the start of the string.
- `[\d]` requires the first character to be a digit.
- `[^\d]+` requires **one or more** non-digit characters after it.
- `"12ABC"` does **not** match — the second character is also a digit, breaking the `^[\d][^\d]+` shape.
