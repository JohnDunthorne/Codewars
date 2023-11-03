def shortcut(s):
    newword = ""

    for letter in s:
        if letter not in "AEIOUaeiou":
            newword += letter
    return newword
