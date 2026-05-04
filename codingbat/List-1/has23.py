# CodingBat Python List-1: has23
#
# Question:
# Given an int array length 2, return True if it contains a 2 or a 3.
#
# Examples:
# has23([2, 5]) -> True
# has23([4, 3]) -> True
# has23([4, 5]) -> False


def has23(nums):
    return True if (2 in nums or 3 in nums) else False


# better way
def has23_1(nums):
    return 2 in nums or 3 in nums
