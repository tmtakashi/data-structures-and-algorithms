def one_away(str1, str2):
    # zero edits away
    if str1 == str2:
        return True

    # find the longer string
    if len(str1) > len(str2)
    longer = str1
    shorter = str2
    else:
        longer = str2
        shorter = str1

    counts = dict()
    for let in shorter:
        if let in counts:
            counts[let] += 1
        else:
            counts[let] = 1

    for let in shorter:
        if
