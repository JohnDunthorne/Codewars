def get_grade(s1, s2, s3):
    if (s1 + s2 + s3) / 3 > 89:
        return "A"
    elif (s1 + s2 + s3) / 3 > 79:
        return "B"
    elif (s1 + s2 + s3) / 3 > 69:
        return "C"
    elif (s1 + s2 + s3) / 3 > 59:
        return "D"
    else:
        return "F"
