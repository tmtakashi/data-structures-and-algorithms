def finder(arr1, arr2):
    '''
    arr2 is shuffled arr1 with a number missing.
    This function returns the missing number.
    '''

    counter = {}
    for num in arr1:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    for num in arr2:
        counter[num] -= 1

    for num in counter:
        if counter[num] != 0:
            return num


if __name__ == "__main__":

    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [3, 7, 2, 1, 4, 6]
    print('arr1: {}, arr2: {}'.format(arr1, arr2))
    print(finder(arr1, arr2))

    arr1 = [5, 5, 7, 7]
    arr2 = [5, 7, 7]
    print('arr1: {}, arr2: {}'.format(arr1, arr2))
    print(finder(arr1, arr2))
