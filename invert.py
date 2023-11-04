def invert(lst):
    newlst = []
    for item in lst:
        if item != 0:
            newlst.append(item - item - item)
        else:
            newlst.append(item)
    return newlst
