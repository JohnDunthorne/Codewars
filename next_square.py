import math


def find_next_square(sq):
    sqrt = math.sqrt(sq)
    if sqrt.is_integer():
        next = (sqrt + 1) * (sqrt + 1)
        return next
    else:
        return -1
