# CodingBat Python List-1: middle_way
#
# Question:
# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their
# middle elements.
#
# Examples:
# middle_way([1, 2, 3], [4, 5, 6]) -> [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) -> [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) -> [2, 4]


def middle_way(a, b):
    return [a[1], b[1]]


# better way: Computes the middle index instead of hard-coding position 1.
def middle_way_1(a, b):
    return [a[len(a) // 2], b[len(b) // 2]]
