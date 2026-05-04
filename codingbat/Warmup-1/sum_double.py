# CodingBat Python Warmup-1: sum_double
#
# Question:
# Given two int values, return their sum. Unless the two values are the same, then return
# double their sum.
#
# Examples:
# sum_double(1, 2) -> 3
# sum_double(3, 2) -> 5
# sum_double(2, 2) -> 8


def sum_double(a, b):
    return 4 * a if (a == b) else a + b
