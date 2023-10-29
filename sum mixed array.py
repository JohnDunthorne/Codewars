def sum_mix(arr):
    numbers = 0
    for i in arr:
        i = int(i)
        if isinstance(i, int):
            numbers += i
    return numbers  # your code here
