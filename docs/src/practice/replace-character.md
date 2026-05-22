# Replace Character in String

Strings are **immutable** in Python, so `string[i] = 'x'` is illegal. Here are five ways to replace a character at a specific index.

## Approach 1: Slicing — build a new string around the index

```python
string = "abracadabra"
i = 5
string = string[:i] + 'k' + string[i + 1:]
print(string)   # abrackdabra
```

## Approach 2: Convert to list, replace, rejoin

```python
string = "abracadabra"
chars = list(string)
chars[5] = 'k'
string = ''.join(chars)
print(string)   # abrackdabra
```

## Approach 3: `str.replace()` — replaces by *value*, not index

```python
string = "abracadabra"
string = string.replace(string[5], 'k', 1)
print(string)   # abrackdabra
```

> **Caveat**
>
> `replace` works by **value**, so it's risky if the same character appears earlier in the string and you need positional precision. The `1` limits to the first occurrence — useful here, but still fragile.


## Approach 4: `bytearray`

A `bytearray` is a **mutable** sequence of integers (0–255), where each integer represents one byte. Since it's mutable, you can do `b[5] = ord('k')` — direct index assignment, which strings don't allow.

The workflow: convert the string to bytes (`bytearray(string, 'utf-8')`), mutate the byte at the desired index, then decode back to a string (`b.decode('utf-8')`).

```python
string = "abracadabra"
b = bytearray(string, 'utf-8')
b[5] = ord('k')
string = b.decode('utf-8')
print(string)   # abrackdabra
```

> **Bytes ≠ characters**
>
> This operates at the **byte** level, not the character level. For pure ASCII that's fine (1 byte = 1 char), but for multi-byte Unicode characters (emojis, accented letters), byte index ≠ character index — this approach would corrupt the string.


## Approach 5: `io.StringIO`

`io.StringIO` creates an **in-memory text stream** — essentially a file-like object backed by a string instead of a file on disk. It supports `seek()` to jump to a position and `write()` to overwrite characters at that position, then `getvalue()` to extract the final string.

```python
import io

string = "abracadabra"
buf = io.StringIO(string)
buf.seek(5)
buf.write('k')
string = buf.getvalue()
print(string)   # abrackdabra
```

For a single replacement this is overkill (slicing is simpler and faster). But if you need to make **many positional edits** to a large string, `StringIO` avoids the O(n) cost of creating a new string each time — you write into the buffer repeatedly, then extract once at the end.
