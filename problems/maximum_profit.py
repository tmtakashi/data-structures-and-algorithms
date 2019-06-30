def maximum_profit(n, R):
    minv = R[0]
    maxv = -200000000
    for i in range(1, n):
        maxv = max(maxv, R[i] - minv)
        minv = min(minv, R[i])

    return maxv


if __name__ == "__main__":
    print(maximum_profit(6, [5, 3, 1, 3, 4, 3]))
    print(maximum_profit(3, [4, 3, 2]))
