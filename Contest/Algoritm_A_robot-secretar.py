import string


s = input()


def calc(s):
    shift = 0
    caps = 2
    res = 0

    for c in s:
        if c in string.ascii_uppercase:
            if caps > shift + 2:
                caps = shift + 2
            shift += 1
        elif c in string.ascii_lowercase:
            if shift > caps + 2:
                shift = caps + 2
            caps += 1

    if shift > caps:
        res = caps + len(s)
    else:
        res = shift + len(s)

    return res


print(calc(s))
