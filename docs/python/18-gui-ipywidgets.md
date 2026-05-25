# GUI — ipywidgets

`ipywidgets` provides interactive HTML widgets that work inside Jupyter notebooks. Widgets are paired with Python state so user interaction triggers callbacks live.

## Interact Functionality

```python
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
```

```python
def func(x):
    return x ** 2
```

```python
interact(func, x=10)
# Renders an IntSlider; min/max default around the seed value
```

The widget type is inferred from the argument's type:

```python
def func(x):
    return x
```

```python
interact(func, x=True)    # Checkbox (bool)
interact(func, x='True')  # Text box (str)
```

`fixed(...)` prevents user interaction with one of the parameters:

```python
@interact(x=True, y=fixed(1.0))
def g(x, y):
    return (x, y)
```

### Slider abbreviations

```python
interact(func, x=10)
# IntSlider — min defined by 0, max by x*3 (or -10..30 for positive seeds)

interact(func, x=widgets.IntSlider(min=-100, max=100, step=1, value=0))

interact(func, x=(-100.0, 100, 0.5))   # Tuple shorthand for FloatSlider
```

### Dropdowns

```python
interact(func, x=['hello', 'option 2'])

interact(func, x={'one': 10, 'two': 20});
# trailing semicolon hides the function __main__ in the output
```

### `interactive()` — keep the widget object

`interact(...)` returns a function. `interactive(...)` returns a widget you can introspect or render again.

```python
from IPython.display import display

def f(a, b):
    display(a + b)
    return a + b
```

```python
w = interactive(f, a=10, b=20)
w.children
# (IntSlider(value=10, description='a', max=30, min=-10),
#  IntSlider(value=20, description='b', max=60, min=-20),
#  Output())

display(w)

interact(f, a=10, b=20)
```

## GUI Widget Basics

```python
w = widgets.IntSlider()
display(w)        # IntSlider(value=0)
display(w)        # second display stays in sync with the first
w.close()         # closes both displayed instances
display(w)        # closed widgets re-display empty
```

### Reading and writing widget state

```python
w.value       # 660
w.keys        # list of all observable traitlets

w.max = 2000
w.value = 66
```

### Linking two widgets

```python
a = widgets.FloatText()
b = widgets.FloatSlider()

display(a, b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))
# Tuples of (widget, key) — value stays synchronized in both directions

mylink.unlink()
```

### Layout vs style

`layout` controls top-level CSS (margin, height, width). `style` is for non-layout widget styling.

```python
w = widgets.IntSlider()
display(w)

w.layout.margin = 'auto'
w.layout.height = '75px'

x = widgets.IntSlider(value=15, description="New Slider")
display(x)

x.layout = w.layout   # share layout objects
```

### Buttons

```python
widgets.Button(description="Ordinary Button", button_style="primary")
```

```python
b1 = widgets.Button(description="Custom Colour")
b1.style.button_color = 'lightgreen'
b1
```

```python
b1.style.keys
# ['_model_module', '_model_module_version', '_model_name',
#  '_view_count', '_view_module', '_view_module_version', '_view_name',
#  'button_color', 'font_family', 'font_size', 'font_style', 'font_variant',
#  'font_weight', 'text_color', 'text_decoration']
```
