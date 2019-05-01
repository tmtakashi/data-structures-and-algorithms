'''
Create an anagram checker
'''


def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    count = {}
    for a in s1:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    for b in s2:
        if b in count:
            count[b] -= 1
        else:
            return False
    for char in count:
        if count[char] != 0:
            return False
    return True


if __name__ == "__main__":
    print(anagram('anagrams', 'ARS MAGNA'))
