def bubble_sort(A, N):
    flag = 1
    i = 0  # 未ソート部分列の先頭インデックス
    count = 0  # 要素の交換回数
    while flag:
        flag = 0
        for j in reversed(range(i + 1, N)):
            if A[j] < A[j - 1]:
                count += 1
                tmp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = tmp
                flag = 1
        i += 1
    print(A)
    print(count)


if __name__ == "__main__":
    bubble_sort([5, 3, 2, 4, 1], 5)
