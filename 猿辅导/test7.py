n, s = list(map(int, input().split()))
array = list(map(int, input().split()))
max_l = -1
C = [[0 for i in range(len(array))] for j in range(len(array))]
# M = [[True for i in range(len(array))] for j in range(len(array))]
for i in range(len(array)):
    C[i][i] = array[i]
#     if array[i] > s:
#         M[i][i] = False

# for r in range(2, len(array)):
#     for i in range(0, len(array)-r+1):
#         j = i + r - 1
#         if M[i][j-1] == False or M[i+1][j] == False:
#             M[i][j] = False
#         else:
#             p = sum(array[i:j+1])
#             if p > s:
#                 M[i][j] = False
#             else:
#                 M[i][j] = True
#                 max_l = max(max_l, j-i+1)
# print(max_l)
# for r in range(2, len(array)):
#     for i in range(0, len(array)-r+1):
#         j = i + r - 1
#         p = sum(array[i:j+1])
#         if p<=s:
#             max_l = max(max_l, r)
# print(max_l)

for r in range(2, len(array)):
    for i in range(0, len(array)-r+1):
        j = i + r - 1
        C[i][j] = C[i][j-1]+array[j]
        if C[i][j] <= s:
            max_l = max(max_l, r)

print(max_l)

