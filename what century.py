def century(year):
    if len(str(year)) == 1:
        return 0
    if len(str(year)) == 2:
        return 1
    if len(str(year)) == 3:
        year = year - 1
        return year[0] + 1
    if len(str(year)) == 4:
        year = year - 1
        return year[0:1] + 1

    #
