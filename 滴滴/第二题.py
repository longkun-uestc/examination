
def dfs(arr, x, y, s, idx):
    if idx == len(s):
        return 1
    count = 0
    if x - 1 >= 0 and arr[x - 1][y] == s[idx]:
        count += dfs(arr, x - 1, y, s, idx + 1)
    if x + 1 < len(arr) and arr[x + 1][y] == s[idx]:
        count += dfs(arr, x + 1, y, s, idx + 1)
    if y - 1 >= 0 and arr[x][y - 1] == s[idx]:
        count += dfs(arr, x, y - 1, s, idx + 1)
    if y + 1 < len(arr[0]) and arr[x][y + 1] == s[idx]:
        count += dfs(arr, x, y + 1, s, idx + 1)
    return count

C = 'CHINA'
def dfs1(arr, x, y, c):
    count = 0
    if not c:
        return 1
    n = len(arr)
    move = [[-1, 0], [1, 0], [0,1], [0,-1]]
    for i, j in move:
        tx, ty = x+i, y+j
        if 0<=tx<n and 0<= ty < n and arr[tx][ty] == c[0]:
            count += dfs1(arr, tx, ty, c[1:])
    return count


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        a = input()
        tmp = []
        for c in a:
            tmp.append(c)
        arr.append(tmp)

    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'C':
                count += dfs1(arr, i, j, C[1:])
    print(count)

# 9
# AAAAAAAAA
# AAAANAAAA
# AAANINAAA
# AANIHINAA
# ANIHCHINA
# AANIHINAA
# AAANINAAA
# AAAANAAAA
# AAAAAAAAA
# 7
# NNNNNNN
# NNNINNN
# NNIHINN
# NIHCHIN
# NNIHINN
# NNNINNN
# NNNNNNN
