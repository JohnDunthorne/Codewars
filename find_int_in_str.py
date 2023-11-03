def filter_list(l):
    newlist = []
    for item in l:
        if isinstance(item, int):
            newlist.append(item)
    return newlist
