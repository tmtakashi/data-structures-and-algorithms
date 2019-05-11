def is_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        if s1 in s2 * 2:
            return True
    return False


if __name__ == "__main__":
    print(is_rotation('waterbottle', 'erbottlewat'))
