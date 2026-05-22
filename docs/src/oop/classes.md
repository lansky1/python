# Classes

Python's built-in types are classes but use lowercase names. This violates [PEP 8's convention](https://peps.python.org/pep-0008/#class-names) that classes should use PascalCase (CapWords).

In Python 3, `class Dog:` and `class Dog():` are identical.

## Basic class

```python
class PascalCase:
    # constructor
    # self — the instance of the class
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)
```

## Class attributes & instances

```python
class Dog:
    # Class Attribute — shared by all instances
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self):
        print("Woof! My Name is {}".format(self.name))

my_dog = Dog(breed='Lab', name="Sammy")
print(my_dog.__dict__)   # instance attributes
my_dog.bark()
```

### Lookup chain

Being able to call and modify a class attribute via an instance is something C# forbids (it requires `static`). Python allows it.

**Lookup chain:** instance → class → parent classes.

```python
class Circle:
    pi = 3.14  # class attribute — accessible via Circle.pi or self.pi
```

## Class as an object

- In Python, everything is an object including classes.
- Classes are instances of the `type` class.
- `type` is the metaclass responsible for creating classes.
- `type` is unique because it is both a class and an instance of itself.

## Permission scope

Python has **no enforced access control** — it's convention-based:

| Naming | Convention | Enforced? |
|---|---|---|
| `species` | Public | No |
| `_species` | Internal, don't touch from outside | No |
| `__species` | Name mangling, harder to access | Partially |

`__species` gets mangled to `_Dog__species` — still accessible, just deliberately inconvenient. Python's position is explicit: **convention over enforcement**. There is no true `private`.
