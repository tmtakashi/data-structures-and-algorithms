def urlify(input_str, true_length):
    new_index = len(input_str)
    input_str = list(input_str)
    for i in reversed(range(true_length)):
        if input_str[i] != ' ':
            input_str[new_index - 1] = input_str[i]
            new_index -= 1
        else:
            input_str[new_index - 3:new_index] = '%20'
            new_index -= 3

    return ''.join(input_str)


if __name__ == "__main__":
    print(urlify('Mr John Smith    ', 13))
