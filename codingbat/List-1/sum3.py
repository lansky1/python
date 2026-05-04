# CodingBat Python List-1: sum3
#
# Question:
# Given an array of ints length 3, return the sum of all the elements.
#
# Examples:
# sum3([1, 2, 3]) -> 6
# sum3([5, 11, 2]) -> 18
# sum3([7, 0, 0]) -> 7


def sum3(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
