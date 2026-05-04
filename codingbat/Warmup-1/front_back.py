# CodingBat Python Warmup-1: front_back
#
# Question:
# Given a string, return a new string where the first and last chars have been exchanged.
#
# Examples:
# front_back('code') -> 'eodc'
# front_back('a') -> 'a'
# front_back('ab') -> 'ba'


def front_back(str):
    if len(str) == 0 or len(str) == 1:
        return str
    elif len(str) == 2:
        return str[-1] + str[0]
    else:
        return str[-1] + str[1:-1] + str[0]


# better way
def front_back_1(s):
    return s if len(s) <= 1 else s[-1] + s[1:-1] + s[0]
