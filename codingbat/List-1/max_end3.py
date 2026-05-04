# CodingBat Python List-1: max_end3
#
# Question:
# Given an array of ints length 3, figure out which is larger, the first or last element
# in the array, and set all the other elements to be that value. Return the changed array.
#
# Examples:
# max_end3([1, 2, 3]) -> [3, 3, 3]
# max_end3([11, 5, 9]) -> [11, 11, 11]
# max_end3([2, 11, 3]) -> [3, 3, 3]


def max_end3(nums):
    if nums[0] < nums[-1]:
        nums[0] = nums[-1]
        nums[1] = nums[-1]
    else:
        nums[-1] = nums[0]
        nums[1] = nums[0]
    return nums


# Approach 2
def max_end3_2(nums):
    val = nums[0] if nums[0] > nums[-1] else nums[-1]
    nums[0] = nums[1] = nums[-1] = val
    return nums


# Approach 3
def max_end3_3(nums):
    val = max(nums[0], nums[-1])
    nums[:] = [val, val, val]
    return nums


# Approach 4
def max_end3_4(nums):
    val = max(nums[0], nums[-1])
    return [val, val, val]
