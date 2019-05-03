def sum_func(n):
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_func(n // 10)


if __name__ == "__main__":
    print(sum_func(5345))
