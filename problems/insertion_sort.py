def insertion_sort(A, N):
    print(A)
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print(A)


if __name__ == "__main__":
    insertion_sort([5, 2, 4, 6, 1, 3], 6)
