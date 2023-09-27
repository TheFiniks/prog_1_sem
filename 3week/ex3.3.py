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
            if c - d == 1:
                return d, -c+1, nod
            else:
                k = 1
                while k*d-(k-1)*c!=nod:
                    k+=1
                return -k+1, k, nod
        else:
            if d -c == 1:
                return -c+1, d, nod
            else:
                k = 1
                while k*c-(k-1)*d!=nod:
                    k+=1
                return k, -k+1, nod
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

