# CodingBat Python Warmup-1: front3
#
# Question:
# Given a string, we'll say that the front is the first 3 chars of the string. If the
# string length is less than 3, the front is whatever is there. Return a new string which
# is 3 copies of the front.
#
# Examples:
# front3('Java') -> 'JavJavJav'
# front3('Chocolate') -> 'ChoChoCho'
# front3('abc') -> 'abcabcabc'


def front3(str):
    front = str if len(str) < 3 else str[0:3]
    return 3 * front


# better way: Slicing handles short strings, so no length check is needed.
def front3_1(s):
    return s[:3] * 3
