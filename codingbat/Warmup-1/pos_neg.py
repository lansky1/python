# CodingBat Python Warmup-1: pos_neg
#
# Question:
# Given 2 int values, return True if one is negative and one is positive. Except if the
# parameter "negative" is True, then return True only if both are negative.
#
# Examples:
# pos_neg(1, -1, False) -> True
# pos_neg(-1, 1, False) -> True
# pos_neg(-4, -5, True) -> True


def pos_neg(a, b, negative):
    return (
        True
        if (
            (negative and a < 0 and b < 0)
            or (not negative and a < 0 and b > 0)
            or (not negative and a > 0 and b < 0)
        )
        else False
    )


# better way: Handles the special case first, then uses != to mean opposite signs.
def pos_neg_1(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0) != (b < 0)
