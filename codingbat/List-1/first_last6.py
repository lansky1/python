# CodingBat Python List-1: first_last6
#
# Question:
# Given an array of ints, return True if 6 appears as either the first or last element in
# the array. The array will be length 1 or more.
#
# Examples:
# first_last6([1, 2, 6]) -> True
# first_last6([6, 1, 2, 3]) -> True
# first_last6([13, 6, 1, 2, 3]) -> False


def first_last6(nums):
    return True if (nums[0] == 6 or nums[-1] == 6) else False
