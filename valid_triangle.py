def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

    # used the Triangle Inequality Theorem to solve this.
