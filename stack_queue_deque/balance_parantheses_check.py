# def bal_check(s):
#     pairs = {
#         '(': ')',
#         ')': '(',
#         '[': ']',
#         ']': '[',
#         '{': '}',
#         '}': '{'
#     }
#     counter = {}
#     for item in s:
#         if item in counter:
#             counter[item] += 1
#         else:
#             counter[item] = 1

#     for item in counter:
#         target = pairs[item]
#         if target not in counter or counter[item] != counter[target]:
#             return False

#     return True


# BETTER SOLUTION
def bal_check(s):

    if len(s) % 2 != 0:
        return False

    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(bal_check('[[[{}]]]'))
