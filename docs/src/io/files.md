# Files

## Opening a file

```python
myfile = open('myfile.txt')
myfile.read()
```

A second `read()` returns an empty string — the cursor is already at the end. Seek back to the start:

```python
myfile.seek(0)
myfile.read()
```

## `readline()` vs `readlines()`

| Method | Returns | Behavior |
|---|---|---|
| `readline()` | Single string | Reads ONE line (including `\n`) |
| `readlines()` | List of strings | Reads ALL lines into a list |

```python
myfile.seek(0)
myfile.readlines()
myfile.close()
```

## Auto-close with `with`

```python
with open('myfile.txt') as myfile:
    contents = myfile.read()
```

The file is automatically closed when the `with` block exits, even if an exception is raised inside it.

## File modes

| Mode | File must exist? | Old content deleted on open? | Read? | Write? | Where writing happens |
|------|------------------|------------------------------|-------|--------|-----------------------|
| `r`  | Yes | No  | Yes | No  | Not allowed |
| `w`  | No  | Yes | No  | Yes | Starts from beginning after clearing file |
| `a`  | No  | No  | No  | Yes | Always at the end |
| `r+` | Yes | No  | Yes | Yes | At current cursor position |
| `w+` | No  | Yes | Yes | Yes | Starts from beginning after clearing file |

> **`w` truncates immediately**
>
> `'w'` truncates the file to 0 bytes as soon as it's opened — even before you write anything.
>
> ```python
> with open('myfile.txt', mode='w') as myfile:
>     contents = myfile.read()  # always returns '' — file is empty now
> ```


## Writing files

```python
with open('myfile.txt', mode='w') as f:
    f.write('Hello\n')
    f.write('World\n')

with open('myfile.txt', mode='r') as f:
    print(f.read())
```

In Jupyter, you can use the magic `%%writefile` to drop a file's contents inline:

```
%%writefile myfile.txt
Hello this is a text file
this is the second line
this is the third line
```
