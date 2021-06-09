import numpy as np
if __name__ == '__main__':
    M, K, N = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a = list(map(int, input().split()))
        A.append(a)
    for j in range(K):
        b = list(map(int, input().split()))
        B.append(b)
    A = np.array(A)
    B = np.array(B)
    C = np.dot(A, B)
    for c in C:
        s = ' '.join(map(str, c))
        print(s)


