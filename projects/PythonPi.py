# Enter a number and have the program generate &pi; (pi) up to that many decimal places. Keep a limit to how far the program will go.

"""
# Using Leibniz Formula
# The error after n terms is approximately 1/(2n+1).
# To get n decimal places you roughly need 10^n iterations:
# pi = 4 * sum([pow(-1, k) / (2 * k + 1) for k in range(400)])

# Nilakantha series
# Gauss-Legendre
# Chudnovsky algorithm

# There is a problem with float as well, it has a fixed 64 bit precision.
# We'll use decimal.Decimal and decimal.getcontext().prec
"""

import decimal

while True:
    digits_pi = int(input("How many digits of pi do you want to generate?: "))
    if digits_pi < 0 or digits_pi > 100000:
        continue
    else:
        break

# sys.exit()

# Iterations != digits
"""
For arctan(1/5), each successive term shrinks by a factor of (1/5)² = 1/25. To get n accurate decimal digits you need roughly: 
k > n/log10(25) ~ 0.715n iterations

For arctan(1/239) it converges even faster.
So if digits_pi = 50, you actually only need about 36 iterations for arctan(1/5). 

Currently over-iterating, not under-iterating. 
The problem with Leibniz was, digits_pi iterations gave far fewer digits than requested.
"""


# Machin's formula
def arctan(x):
    return sum(
        [pow(-1, k) * pow(x, 2 * k + 1) / (2 * k + 1) for k in range(int(digits_pi))]
    )


decimal.getcontext().prec = digits_pi + 10

# pi = 4 * (4 * math.atan(1 / 5) - math.atan(1 / 239))
pi = 4 * (
    4 * arctan(decimal.Decimal("1") / decimal.Decimal("5"))
    - arctan(decimal.Decimal("1") / decimal.Decimal("239"))
)

print(str(pi)[: 2 + digits_pi])
