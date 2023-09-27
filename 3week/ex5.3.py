N, M = list(map(int, input().split()))
A = [['0'] * M for i in range(N)]
cnt = 0
mistake_ratio = 0
while cnt != N*M:
    i = mistake_ratio
    for j in range(mistake_ratio, M - mistake_ratio):
        cnt += 1
        A[i][j] = cnt
    if cnt == N*M:
        break
    j = M - 1 - mistake_ratio
    for i in range(mistake_ratio+1, N - mistake_ratio):
        cnt += 1
        A[i][j] = cnt
    if cnt == N*M:
        break
    i = N - 1 - mistake_ratio
    for j in range(M - 2 - mistake_ratio, -1 + mistake_ratio, -1):
        cnt += 1
        A[i][j] = cnt
    if cnt == N*M:
        break
    j = mistake_ratio
    for i in range(N - 2 - mistake_ratio, mistake_ratio, -1):
        cnt += 1
        A[i][j] = cnt
    mistake_ratio += 1
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()
print()
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] *= i
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()

