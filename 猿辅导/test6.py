N, M = list(map(int, input().split()))
mat = []
for i in range(N):
    a = list(map(int, input().split()))
    mat.append(a)

n_start, n_end = 0, len(mat)-1
m_start, m_end = 0, len(mat[0])-1
direction = ['b', 'r', 't', 'l']
f = 0
res = []
while n_start <= n_end and m_start <= m_end:
    flag = direction[f % 4]
    if flag == 'b':
        for i in range(n_start, n_end+1):
            res.append(mat[i][m_start])
        m_start += 1
    elif flag == 'r':
        for i in range(m_start, m_end+1):
            res.append(mat[n_end][i])
        n_end -= 1
    elif flag == 't':
        for i in range(n_end, n_start-1, -1):
            res.append(mat[i][m_end])
        m_end -= 1
    elif flag == 'l':
        for i in range(m_end, m_start-1, -1):
            res.append(mat[n_start][i])
        n_start += 1
    f += 1
print(" ".join(list(map(str, res))))

# while n_start <= n_end and m_start <= m_end:
#     for i in range(n_start, n_end + 1):
#         res.append(mat[i][m_start])
#     m_start += 1
#     for i in range(m_start, m_end + 1):
#         res.append(mat[n_end][i])
#     n_end -= 1
#     for i in range(n_end, n_start - 1, -1):
#         res.append(mat[i][m_end])
#     m_end -= 1
#     for i in range(m_end, m_start - 1, -1):
#         res.append(mat[n_start][i])
#     n_start += 1




