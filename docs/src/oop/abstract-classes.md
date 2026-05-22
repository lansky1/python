# Abstract Classes

A class that defines a method signature but no implementation. It cannot be instantiated directly. Any class inheriting from it must implement the abstract methods or Python throws an error.

Two approaches:

## Approach 1: `abc` module (recommended)

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


Dog()     # works
# Cat()   # TypeError — Can't instantiate abstract class Cat
# Animal() # TypeError — Can't instantiate abstract class Animal
```

## Approach 2: `NotImplementedError`

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Derived classes must implement this abstract method.")
```

The first approach catches mistakes at **instantiation time**; the second only catches them when the method is actually called. Prefer the `abc` module.
