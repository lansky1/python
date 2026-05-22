# Inheritance & Polymorphism

## Inheritance

```python
class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I'm eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    # override
    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("Woof!")


animal = Animal()
dog = Dog()

animal.who_am_i()  # I am an animal
dog.who_am_i()     # I am a dog (overridden)
```

### Why call `Animal.__init__(self)`?

To initialize the `Animal` part of the `Dog` instance — so the `Dog` instance inherits attributes from `Animal`. Creating a separate `Animal()` instance would not link it to the `Dog` instance, breaking the inheritance structure.

> **Prefer `super()`**
>
> `super().__init__()` is the modern equivalent — it handles the MRO (Method Resolution Order) automatically.
>
> ```python
> class Dog(Animal):
>     def __init__(self):
>         super().__init__()
>         print("Dog Created")
> ```


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
