x = []
def out_put1(n, arrs):
    new_arrs = []
    flag = True
    for a in arrs:
        if len(a) == n:
            x.append(a)
            continue
        for i in range(1, n+1):
            if i not in a and a[-1] != i+1 and a[-1]!=i-1:
                s = a + [i]
                new_arrs.append(s)
    if len(new_arrs) == 0:
        return
    out_put1(n, new_arrs)

if __name__ == '__main__':
    n = int(input())
    if n > 3:
        arrays = [[i] for i in range(1, n + 1)]
        out_put1(n, arrays)
        for a in x:
            s = ' '.join(list(map(str, a)))
            print(s)