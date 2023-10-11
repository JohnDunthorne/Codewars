n = int(input("integer: "))
y = 1
while y < n + 1:
    print(f"{y} sheep...", end="")
    y += 1
else:
    print("")


# like this


def count_sheep(n):
    result = ""
    for number in range(1, n + 1):
        result = result + str(number) + " sheep..."
    return result
