# String Problems

## String Explosion

Build the cumulative prefix string: `"Code"` → `"CCoCodCode"`.

=== "Approach 1: loop with concatenation"

    ```python
    def string_splosion(str):
        final_string = ""
        for n in range(len(str)):
            final_string += str[:n + 1]
        return final_string
    ```

=== "Approach 2: list comprehension + `join()`"

    ```python
    string = "Code"
    list = [string[:n + 1] for n in range(len(string))]
    "".join(list)
    ```

## Last 2

Count how many times the last 2 characters appear in the string (excluding the last 2 themselves).

=== "Approach 1: `str.count()`"

    > Does not handle overlaps — `count()` walks left to right and consumes matched characters.

    ```python
    def last2(str):
        substring = str[-2:]
        return str.count(substring)

    last2("axxxaaxx")
    ```

=== "Approach 2: regex"

    > Also misses overlaps for the same reason — `finditer` advances past each match.

    ```python
    import re

    string_ = "axxxaaxx"
    substring = string_[-2:]

    regex_pattern = f"{re.escape(substring)}"

    for item in re.finditer(regex_pattern, string_):
        print(item)

    # Lookahead version (catches overlaps):
    # for item in re.finditer(f"(?=({re.escape(substring)}))", string_):
    #     print(item.start(), item.group(1))
    ```

=== "Approach 3: sliding window"

    ```python
    def last2(str):
        substring = str[-2:]
        count = 0

        for i in range(len(str) - 2):
            if str[i:i + 2] == substring:
                count += 1

        return count

    last2("axxxaaxx")
    ```

=== "Approach 4: comprehension one-liner"

    ```python
    def last2(str):
        return sum([1 for i in range(len(str) - 2) if str[i:i + 2] == str[-2:]])

    last2("axxxaaxx")
    ```

## String Match

Count the number of positions where the two strings have the same length-2 substring.

```python
def string_match(a, b):
    len_ = len(a) if len(a) < len(b) else len(b)
    count = 0
    for i in range(len_ - 1):   # was missing -1 here
        print(a[i:i + 2], "\t", b[i:i + 2])
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
    return count

string_match('abc', 'abc')
# string_match('abc', 'axc')
```

## Replace Character at Index

Since strings are immutable in Python, you can't do `string[i] = 'x'`. Five ways to replace a character at a specific index:

=== "1. Slicing"

    Build a new string around the target index.

    ```python
    string = "abracadabra"
    i = 5
    string = string[:i] + 'k' + string[i + 1:]
    print(string)   # abrackdabra
    ```

=== "2. List + rejoin"

    Convert to list, replace, rejoin.

    ```python
    string = "abracadabra"
    chars = list(string)
    chars[5] = 'k'
    string = ''.join(chars)
    print(string)   # abrackdabra
    ```

=== "3. `str.replace()`"

    > Caveat: replaces by **value**, not index. Risky if the character appears multiple times and you need positional precision. The `1` limits to the first occurrence.

    ```python
    string = "abracadabra"
    string = string.replace(string[5], 'k', 1)
    print(string)   # abrackdabra
    ```

=== "4. `bytearray`"

    A `bytearray` is a **mutable** sequence of integers (0–255), where each integer represents one byte. Since it's mutable, you can do `b[5] = ord('k')` — direct index assignment, which strings don't allow.

    The workflow: convert the string to bytes (`bytearray(string, 'utf-8')`), mutate the byte at the desired index, then decode back to a string (`b.decode('utf-8')`).

    The limitation: this operates at the **byte** level, not the character level. For pure ASCII that's fine (1 byte = 1 char), but for multi-byte Unicode characters (e.g., emojis, accented letters), byte index ≠ character index — so this approach would corrupt the string.

    ```python
    string = "abracadabra"
    b = bytearray(string, 'utf-8')
    b[5] = ord('k')
    string = b.decode('utf-8')
    print(string)   # abrackdabra
    ```

=== "5. `io.StringIO`"

    `io.StringIO` creates an **in-memory text stream** — essentially a file-like object backed by a string instead of a file on disk. It supports `seek()` to jump to a position and `write()` to overwrite characters at that position, then `getvalue()` to extract the final string.

    For a single replacement this is overkill (slicing is simpler and faster). But if you need to make **many positional edits** to a large string, `StringIO` avoids the O(n) cost of creating a new string each time — you write into the buffer repeatedly, then extract once at the end.

    ```python
    import io

    string = "abracadabra"
    buf = io.StringIO(string)
    buf.seek(5)
    buf.write('k')
    string = buf.getvalue()
    print(string)   # abrackdabra
    ```
