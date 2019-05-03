def reverse(s):
    if len(s) <= 1:
        return s
    else:
        last = s[-1]
        s = s[:-1]
        return last + reverse(s)


if __name__ == "__main__":
    print(reverse('hello world'))
