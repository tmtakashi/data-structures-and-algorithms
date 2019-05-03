def permute(s):
    out = []

    if len(s) == 1:
        return [s]

    for i, let in enumerate(s):
        for perm in permute(s[:i] + s[i + 1:]):
            out += [let + perm]

    return out
