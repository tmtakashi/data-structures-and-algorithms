def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    rows = set()
    cols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for row in list(rows):
        for j in range(n):
            matrix[row][j] = 0

    for col in list(cols):
        for i in range(m):
            matrix[i][col] = 0

    return matrix


if __name__ == "__main__":
    print(zero_matrix([
        [1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]))
