# Object-Oriented Programming

Python's built-in types are classes but use lowercase names. This violates PEP 8's convention that classes should use PascalCase (CapWords).

**Reference:** [PEP 8 — Class Names](https://peps.python.org/pep-0008/#class-names)

In Python 3, `class Dog:` and `class Dog():` are identical.

## Classes & Instances

```python
class PascalCase:
    # constructor; self is the instance
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)
```

```python
class Dog():
    # class attribute — shared across instances
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self):
        print("Woof! My Name is {}".format(self.name))

my_dog = Dog(breed='Lab', name="Sammy")
print(my_dog.__dict__)   # instance attributes
my_dog.bark()            # method call
```

### Class Attributes & Lookup Chain

Being able to call and modify a class attribute through an instance was against the design philosophy of C# (where this would be a `static` attribute). Python allows it.

**Lookup Chain in Python**: instance → class → parent classes.

```python
class Circle():
    pi = 3.14   # class attribute — accessible via Circle.pi or self.pi
```

### Class as an object

- In Python, everything is an object — including classes.
- Classes are instances of the `type` class.
- `type` is the metaclass responsible for creating classes.
- `type` is unique because it is both a class and an instance of itself.

### Permission Scope

Python has no enforced access control. It's convention-based:

| Naming | Convention | Enforced? |
|---|---|---|
| `species` | Public | No |
| `_species` | Internal, don't touch from outside | No |
| `__species` | Name mangling, harder to access | Partially |

`__species` gets mangled to `_Dog__species` — still accessible, just deliberately inconvenient. Python's position is explicit: **convention over enforcement**. There is no true `private`.

## Inheritance

Why call `Animal.__init__(self)` in the derived class?

In the `Dog` class, `Animal.__init__(self)` is called to initialize the `Animal` part of the `Dog` instance. This ensures the `Dog` instance inherits attributes and methods from `Animal`. Creating a separate `Animal` instance would not link it to the `Dog` instance, breaking the inheritance structure.

> `super().__init__()` is the modern equivalent — it handles the MRO (Method Resolution Order) automatically.

```python
class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I'm eating")
```

```python
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    # override
    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("Woof!")
```

```python
animal = Animal()
dog = Dog()

animal.who_am_i()  # I am an animal
dog.who_am_i()     # I am a dog (overridden)
```

## Polymorphism

Same method call, different behavior depending on the object receiving it.

```python
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

class Person:
    def speak(self):
        print("Hello")

def make_it_speak(thing):
    thing.speak()

make_it_speak(Dog())     # Woof
make_it_speak(Cat())     # Meow
make_it_speak(Person())  # Hello
```

## Abstract Classes

A class that defines a method signature but no implementation. It cannot be instantiated directly. Any class inheriting from it must implement the abstract methods, or Python raises an error.

### Approach 1: Using `abc` module (recommended)

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    pass  # forgot to implement speak
```

```python
Dog()      # works
# Cat()    # TypeError — Can't instantiate abstract class Cat
# Animal() # TypeError — Can't instantiate abstract class Animal
```

### Approach 2: Using `NotImplementedError`

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Derived classes must implement this abstract method.")
```

## Special (Magic / Dunder) Methods

Using built-in Python functions on user-defined objects. Dunder = double underscores.

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
```

```python
b = Book("Python Rocks", "Jose", 200)
print(b)        # calls __str__
print(len(b))   # calls __len__
del b           # calls __del__
```

### Callable Instances with `__call__`

Defining `__call__` lets an instance behave like a function while still carrying its own state.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


times_three = Multiplier(3)

print(times_three(5))  # 15
print([times_three(number) for number in [1, 2, 3, 4]])
# [3, 6, 9, 12]
```

Use a callable object when the behavior has meaningful state. Use `functools.partial` when you only need to pre-fill a few function arguments.
