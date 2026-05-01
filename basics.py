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
example_list = [10, "hello", 200.3]
# print(example_list)
print(example_list[1][3])