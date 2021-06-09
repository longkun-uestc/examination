def get_count(mat, i, j):
    if i >= 6 or j >= 6:
        return 1
    if mat[i][j] == 0:
        new_j = (j + 1) % 6
        new_i = i + (j + 1) // 6
        while new_i < 6 and mat[new_i][new_j] == 0:
            new_i = new_i + (new_j+1) // 6
            new_j = (new_j + 1) % 6
        count = get_count(mat, new_i, new_j)
    else:
        count = 0
        for k in range(1, 7):
            if mat[i - 1][j] != k and mat[i][j - 1] != k:
                mat[i][j] = k
                new_i = i + (j + 1) // 6
                new_j = (j + 1) % 6
                count += get_count(mat, new_i, new_j)
                count = count%1000000009
                print(count)
                mat[i][j] = -1
    return count

# #*****
# ******
# ******
# ******
# ******
# *****#

if __name__ == '__main__':
    array = []
    for i in range(6):
        a = list(input())
        array.append(a)
    flag = [[-1 for i in range(6)] for j in range(6)]
    for i in range(6):
        for j in range(6):
            if array[i][j] == '*':
                flag[i][j] = 0

    count = get_count(flag,0,0)
    print(count)
    exit()
    count = 0
    if flag[0][0] == -1:
        count = 6
        flag[0][0] = 1

    for i in range(1, 6):
        if flag[0][i] == -1:
            if flag[0][i - 1] == 0:
                count *= 6
            else:
                count *= 5
            flag[0][i] = 1
    for i in range(1, 6):
        if flag[i][0] == -1:
            if flag[i - 1][0] == 0:
                count *= 6
            else:
                count *= 5
            flag[i][0] = 1
    for i in range(1, 6):
        for j in range(1, 6):
            if flag[i][j] == -1:
                if flag[i - 1][j] == 0 and flag[i][j - 1] == 0:
                    count = (count * 6) % 1000000009
                elif flag[i - 1][j] == 0 and flag[i][j - 1] == 1 or flag[i - 1][j] == 1 and flag[i][j - 1] == 0:
                    count = (count * 5) % 1000000009
                elif flag[i - 1][j] == 1 and flag[i][j - 1] == 1:
                    count = (count * 4) % 1000000009

    print(count)
