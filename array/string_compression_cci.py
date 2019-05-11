def string_compression(string):
    compressed_string = []
    count_consecutive = 0

    for i in range(len(string)):
        count_consecutive += 1
        if (i + 1 >= len(string)) or (string[i] != string[i + 1]):
            compressed_string.append(string[i] + str(count_consecutive))
            count_consecutive = 0

    return ''.join(compressed_string) if len(compressed_string) < len(string) else string


if __name__ == "__main__":
    print(string_compression('aabcccccaaa'))
