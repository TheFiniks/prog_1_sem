import numpy as np
N, M = list(map(int, input().split()))
A = np.array([[0]*M for i in range(N)])
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        A[i][j] = data[j]
A = A.transpose()
system_of_eq = np.array(A[:-1].transpose())
right_side = np.array(A[-1])
ans = np.linalg.solve(system_of_eq, right_side)
print(*ans)
