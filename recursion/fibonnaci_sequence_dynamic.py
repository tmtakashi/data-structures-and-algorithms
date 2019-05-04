n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]
