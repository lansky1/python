# CodingBat Python Warmup-1: not_string
#
# Question:
# Given a string, return a new string where "not " has been added to the front. However,
# if the string already begins with "not", return the string unchanged.
#
# Examples:
# not_string('candy') -> 'not candy'
# not_string('x') -> 'not x'
# not_string('not bad') -> 'not bad'


def not_string(str):
    return str if (str[0:3] == "not") else "not " + str


# better way: startswith() states the prefix check more clearly than manual slicing.
def not_string_1(s):
    return s if s.startswith("not") else "not " + s
