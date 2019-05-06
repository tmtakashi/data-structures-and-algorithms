def is_palin_perm(input_str):
    input_str = input_str.lower()
    input_str = input_str.replace(' ', '')

    counts = dict()

    for let in input_str:
        if let in counts:
            counts[let] += 1
        else:
            counts[let] = 1

    odd_count = 0

    for k, v in counts.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False

    return True


if __name__ == "__main__":
    print(is_palin_perm('Tact Coa'))
    print(is_palin_perm('wefqewfe'))
