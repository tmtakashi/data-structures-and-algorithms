# given two strings, check if one is a permutation of the other
def check_perm(s1, s2):
    if s1 == s2:
        return True

    if len(s1) != len(s2):
        return False

    counter = {}
    for l in s1:
        if l in counter:
            counter[l] += 1
        else:
            counter[l] = 1

    for l in s2:
        if l in counter:
            counter[l] -= 1
        else:
            return False

    for key in counter:
        if counter[key] != 0:
            return False

    return True


if __name__ == "__main__":
    print(check_perm('abcde', 'acdeb'))
    print(check_perm('abcde', 'acdet'))
