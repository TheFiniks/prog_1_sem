def NOD(a, b):
    c, d = a, b
    while a > 0 and b > 0:
        if a >= b:
            a -= b
        else:
            b -= a
    nod = max(a, b)
    ratio1, ratio2 = 1, 1
    if c==d:
        return 0, 1, nod
    elif nod == 1:
        if c > d:
            return d, -c+1, nod
        else:
            return -c+1, d, nod
    elif d == nod:
        return 0, 1, nod
    elif c == nod:
        return 1, 0, nod
    elif c > d:
        additional = (c - d) // nod
        return ratio1, -ratio2 * additional, nod
    elif d > c:
        additional = (d - c) // nod
        return -ratio1 * additional, ratio2, nod


a, b = list(map(int, input().split()))
print(NOD(a, b))

