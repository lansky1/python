# Debugging

Use the standard library `pdb` (Python Debugger) to set breakpoints and step through code.

```python
import pdb

x = [1, 2, 3]
y = 2
z = 3

result_one = y + z
pdb.set_trace()
# result_two = y + x  # TypeError at runtime — debug with pdb
```

Once at the prompt, common commands:

| Command | What it does |
|---|---|
| `n` | Next line (steps over calls) |
| `s` | Step into function call |
| `c` | Continue until next breakpoint |
| `l` | Show source around current line |
| `p var` | Print a variable |
| `pp var` | Pretty-print a variable |
| `w` / `bt` | Show the stack |
| `u` / `d` | Move up / down a frame |
| `q` | Quit |

> **Built-in `breakpoint()`**
>
> Since Python 3.7 you can use the built-in `breakpoint()` instead of `pdb.set_trace()`. It honors the `PYTHONBREAKPOINT` environment variable, so you can swap in alternative debuggers without code changes.

