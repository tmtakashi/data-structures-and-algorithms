'''
Compress 'AAAABBBBCCCCCDDEEEE' to 'A4B4C5D2E4'.
Case sensitive.
'''


def compress(s):

    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s + '1'
    counter = {}
    for letter in s:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    output = ''
    for k, v in sorted(counter.items()):
        output += k + str(v)

    return output


if __name__ == "__main__":
    print(compress('AAAABBBBCCCCCDDEEEE'))
    print(compress('AAaaBBbbCCcccDDEEEE'))
