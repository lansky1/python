# Enter a number and have the program generate the Fibonacci sequence
# to that number or to the Nth number.

n = int(input("Upto what number do you want to generate the Fibonacci sequence? "))
fibonacci_series = []

# Iterative


# Recursive

# Still not ideal, have to call n times

def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(*list(map(lambda x: fibonacci(x), range(1, n+1))))