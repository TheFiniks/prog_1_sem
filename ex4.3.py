def triangle(size, symb):
    corner = ''
    for i in range(1, size//2+1+size%2):
        corner += f'{symb*i}\n'
    for j in range(size//2, 0, -1):
        corner += f'{symb * j}\n'
    return corner
size, symb = input().split()
print(triangle(int(size), symb))
