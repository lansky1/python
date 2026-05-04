# CodingBat Python Warmup-1: missing_char
#
# Question:
# Given a non-empty string and an int n, return a new string where the char at index n has
# been removed. The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).
#
# Examples:
# missing_char('kitten', 1) -> 'ktten'
# missing_char('kitten', 0) -> 'itten'
# missing_char('kitten', 4) -> 'kittn'


def missing_char(str, n):
    new_str = str[0:n] + str[n + 1 : len(str)]
    return new_str


# better way: Omits len(s) because a slice without an end already goes to the end.
def missing_char_1(s, n):
    return s[:n] + s[n + 1 :]
