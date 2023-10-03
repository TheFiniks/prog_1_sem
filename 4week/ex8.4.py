import numpy as np
A = list(np.random.randint(1, 10, 10))
B = list(np.random.randint(1, 10, 10))
C = A+B
dic_A = dict()
dic_B = dict()
dic_C = dict()
for num in A:
    if num in dic_A:
        dic_A[num] = dic_A[num] + 1
    else:
        dic_A[num] = 1
for num in B:
    if num in dic_B:
        dic_B[num] = dic_B[num] + 1
    else:
        dic_B[num] = 1
for num in C:
    if num in dic_C:
        dic_C[num] = dic_C[num] + 1
    else:
        dic_C[num] = 1
keys1, keys2, keys = [], [], []
for key1 in dic_A.keys():
    if dic_A[key1] == 1:
        keys1.append(key1)
for key2 in dic_B.keys():
    if dic_B[key2] == 1:
        keys2.append(key2)
for key in dic_C.keys():
    if dic_C[key] == 1:
        keys.append(key)
print('A:', A)
print('B:', B)
print(f'unique for A:', *keys1)
print(f'unique for A:', *keys2)
print(f'unique for A|B:', *keys)
print('A&B:', *set(A)&set(B))

