# CodingBat Python List-1: make_pi
#
# Question:
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
#
# Examples:
# make_pi() -> [3, 1, 4]


def make_pi():
    return [int(x) for x in str(3.14159)[:4] if x != "."]
