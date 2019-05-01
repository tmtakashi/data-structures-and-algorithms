'''
Finds if all characters in a string are unique.
'''


def uni_char(s):

    letters = set()
    for letter in s:
        if letter not in letters:
            letters.add(letter)
        else:
            return False
    return True


if __name__ == "__main__":
    print(uni_char('abcdefg'))
    print(uni_char('aaadddd'))
