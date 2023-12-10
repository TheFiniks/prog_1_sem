def prime_factors(n):
    decomposion = ''
    if n == '':
        return '-1'
    if '-' in n:
        decomposion += '-'
        n = n[1:]
    if n.isdigit():
        n = int(n)
    if n == 1:
        decomposion += '1'
        return decomposion
    for i in range(2, int(n ** 0.5) + 1):
        degree_indicator = 0
        while n % i == 0:
            degree_indicator += 1
            n /= i
        if degree_indicator != 0 and degree_indicator != 1 and n == 1:
            decomposion += f'{i}^{degree_indicator}'
        elif degree_indicator != 0 and degree_indicator != 1:
            decomposion += f'{i}^{degree_indicator}*'
        elif degree_indicator == 1 and n == 1:
            decomposion += f'{i}'
        elif degree_indicator == 1:
            decomposion += f'{i}*'
    if n != 1:
        decomposion += f'{int(n)}'
    return decomposion

