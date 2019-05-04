def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


if __name__ == "__main__":
    print(fib_rec(10))
