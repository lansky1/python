# String Explosion

Given a string, return its "explosion" — each prefix concatenated together.

`"Code"` → `"CCoCodCode"`.

## Approach 1: Loop with string concatenation

```python
def string_splosion(s):
    final_string = ""
    for n in range(len(s)):
        final_string += s[:n + 1]
    return final_string
```

Readable but uses repeated `+=` on a string — O(n³) in the worst case.

## Approach 2: List comprehension + `join()`

```python
string = "Code"
parts = [string[:n + 1] for n in range(len(string))]
"".join(parts)
```

Idiomatic and avoids the quadratic concatenation cost. Prefer this.
