# Python Basics

# Batteries Included Philosophy
# Reference: https://peps.python.org/pep-0206/

# Division in Python
# '/' always performs floating-point division.~
# '//' performs integer division.
# print(5 // 2)

# Floating Point Arithmetic
# Why doesn't 0.1 + 0.2 - 0.3 equal 0.0?
# Reference: https://docs.python.org/3/tutorial/floatingpoint.html
# print(0.1 + 0.2)
# print(0.1 + 0.2 - 0.3)

# Exponentiation and Bitwise Operations
# print(6 ** 6)  # Exponentiation
# print(1 ^ 6)   # Bitwise XOR operation
# 001^110 = 111

# Strings
# my_string = "Hello"~
# print(my_string[::-2]) #Slice
# print(my_string[5])
# print("Hello World"[8])
# letter = 'a'
# print(letter*10)

# String Formatting
# print("This is a string {}".format("Inserted"))
# print("The {2} {1} {0}".format("fox", "brown", "quick"))
# print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
# print("The {} {} {}".format(f="fox", b="brown", q="quick"))
# {} are postitional placeholders. f=, b= are keyword arguments.
# Both are incompatible.

# Float Manipulation
# value:width.precision f
# print("The answer is {:1.1f}".format(100/77))

# F Strings
# name = "John"
# print(f"Hello, my name is {name}")
# Reference: https://pyformat.info

# Lists in Python
# TODO: How is a list implemented internally?
# example_list = [10, "hello", 200.3]
# print(example_list)
# print(example_list[1][3])
# print([10, "hello", 200.3])

# Dictionaries
# mutable
# Unordered Mapping - use ordereddict for ordered
# Keys should be hashable type
# strings, integers, tuples, mixed keys
# cannot use lists, dicts or sets - since they are mutable containers
# dict = {1: 'hello', 2: 'bye'}
# print(type(dict[1]).__name__)

# Tuples
# Immutable

# Sets
# unordered
# unique elements
# Like this is a hashset, while dicts are hashmaps
# example_list = [1,1,1,2,2,2,3,3,3]
# hashset = set(example_list) # can pass any iterable
# list, tuple, string, set, range
# passing dict would discard values, keep only keys
# hashset.add(3)
# hashset.add(4)
# hashset.add(3) # this doesnt throw an error
# silently rejects the duplicates
# print(hashset)
# hashset = set({1:'hello',2:'world'}.values())
# print(hashset) # order not guaranteed
# hashset = set({1:'hello',2:'world'}.items())
# print(hashset) # tuples are hashable

# Booleans
# True, False, None

# Useful Operators

# Range
# range(length)
# range(start, stop, step)
# range is a generator not a container. It doesn't store the list.

# Enumerate
# for item in enumerate(word)
# returns a tuple with the (index, element)

# Zip
# pair up same index as tuples
# list1 = [1,2,3] # an extra element would be discarded
# list2 = ['a','b','c']
# for item in zip(list1, list2):
# print(item)
# print(list(zip(list1,list2))) # can be a list, set, tuple, dict

# List Comprehensions
# my_list = [x for x in "hello"]
# print(my_list)
# my_second_list = [num**2 for num in range(0, 11)]
# print(my_second_list)
# my_third_list = [num for num in range(11) if num % 2 == 0]
# print(my_third_list)
# my_fourth_list = [num if num % 2 == 0 else "ODD" for num in range(11)]
# print(my_fourth_list)
# my_fifth_list = [x * y for x in [2, 4, 6] for y in [1, 2, 3]]
# print(my_fifth_list)
