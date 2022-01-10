def isValid(formula):
    if 5 in formula and 6 not in formula:
        return False
    elif 5 not in formula and 6 in formula:
        return False
    elif 1 in formula and 2 in formula:
        return False
    elif 3 in formula and 4 in formula:
        return False
    elif 7 in formula or 8 in formula:
        return True
    else:
        return False