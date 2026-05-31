# Just like the previous problem, but with e instead of &pi; (pi). Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
# Euler's number

"""
# Using Limit Formula
# Using Infinite Series
"""

import decimal

while True:
    digits_e = int(input("How many digits of e do you want to generate?: "))
    if digits_e < 0 or digits_e > 100000:
        continue
    else:
        break

# Using Limit Formula
# For 1,000,000 - it only gives 5-6 significant digits

limit_euler_num = (1 + 1 / 1000000) ** 1000000

# Using Taylor Series
taylor_euler_num = 0


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n)


print(str(limit_euler_num)[: 2 + digits_e])
print(str(taylor_euler_num)[: 2 + digits_e])
