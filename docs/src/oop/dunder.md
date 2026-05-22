# Dunder (Magic) Methods

Using built-in Python functions on user-defined objects. *Dunder* = double underscores.

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


b = Book("Python Rocks", "Jose", 200)
print(b)       # calls __str__
print(len(b))  # calls __len__
del b          # calls __del__
```

## Common dunder methods

| Method | Triggered by |
|---|---|
| `__init__` | `Cls(...)` construction |
| `__repr__` | `repr(obj)`, debugger display |
| `__str__` | `str(obj)`, `print(obj)` |
| `__len__` | `len(obj)` |
| `__iter__`, `__next__` | `for x in obj`, `iter(obj)`, `next(obj)` |
| `__eq__`, `__lt__`, … | `==`, `<`, … (see `functools.total_ordering`) |
| `__hash__` | `hash(obj)`, set/dict key use |
| `__getitem__`, `__setitem__`, `__delitem__` | `obj[k]`, `obj[k] = v`, `del obj[k]` |
| `__contains__` | `x in obj` |
| `__call__` | `obj(...)` |
| `__enter__`, `__exit__` | `with obj as x:` (context managers) |
| `__del__` | object finalization (rarely needed) |
