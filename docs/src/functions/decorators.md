# Decorators

In Python, assigning one variable to another (e.g., `greet = hello`) creates a **reference**, not a copy. Both point to the same function object in memory.

- Deleting `hello` with `del hello` removes the name but does not delete the function object as long as `greet` still references it.
- Python uses reference-based memory management; objects are only deleted when no references remain (garbage collection).

## Functions as first-class objects

```python
def hello(name="Jose"):
    print("This is the hello function")

    def greet():
        print("This is the greet function inside the hello function")

    def welcome():
        print("This is the welcome function inside the hello function")

    return greet if name == "Jose" else welcome


my_func = hello()
my_func()
```

## Passing functions as arguments

```python
def my_new_func(some_function):
    print("The input method will be executed.")
    print(some_function())

my_new_func(hello)
```

## Building a decorator

```python
def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the execution of the original function.")
        original_func()
        print("Some extra code, after the execution of the original function.")
    return wrap_func


def func_needs_decorator():
    print("I want to be decorated")


# Manual decoration
decorated_function = new_decorator(func_needs_decorator)
decorated_function()
```

## Using `@` syntax

```python
@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator()
```

The `@new_decorator` line above is exactly equivalent to:

```python
func_needs_decorator = new_decorator(func_needs_decorator)
```
