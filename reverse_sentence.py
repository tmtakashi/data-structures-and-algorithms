def rev_word(s):
    s = s.strip()  # remove trailing white space
    words = s.split(' ')

    # reverse array
    num_words = len(words)
    start = 0
    end = num_words - 1
    while start < end:
        tmp = words[start]
        words[start] = words[end]
        words[end] = tmp
        start += 1
        end -= 1

    reversed_s = ' '
    for word in words:
        reversed_s.join(word)

    return reversed_s


if __name__ == "__main__":
    print(rev_word('Hi my name is Takashi'))
