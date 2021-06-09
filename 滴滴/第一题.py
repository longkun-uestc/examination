def fn(n):
    f = [1, 1]
    for i in range(2, n):
        x = f[i-2]+f[i-1]
        f.append(x)
    # print(f)
    return f

if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print('')
    elif n == 1:
        print(1)
    else:
        mat = [[0 for i in range(n)] for j in range(n)]
        direction = ['r', 'd', 'l', 't']
        fib = fn(n*n)
        x, y = 0, 0
        l, r = 0, len(mat[0])
        t, d = 0, len(mat)
        idx = len(fib)-1
        flag = 0
        while idx >= 0:
            if direction[flag%4] == 'r':
                while y < r:
                    mat[x][y] = fib[idx]
                    y += 1
                    idx -= 1
                y -= 1
                x += 1
                t += 1
                flag += 1
            elif direction[flag%4] == 'd':
                while x < d:
                    mat[x][y] = fib[idx]
                    x += 1
                    idx -= 1
                x -= 1
                y -= 1
                r -= 1
                flag += 1
            elif direction[flag%4] == 'l':
                while y >= l:
                    mat[x][y] = fib[idx]
                    y -= 1
                    idx -= 1
                y += 1
                x -= 1
                d -= 1
                flag += 1
            elif direction[flag%4] == 't':
                while x >= t:
                    mat[x][y] = fib[idx]
                    x -= 1
                    idx -= 1
                x += 1
                y += 1
                l += 1
                flag += 1
        for m in mat:
            s = ' '.join(map(str, m))
            print(s)

