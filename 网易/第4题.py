
if __name__ == '__main__':
    S, E = list(map(int, input().split()))
    if S == E:
        print(0)
        print(1)
        print(S)
    else:
        mod = [E % (i+1) for i in range(7)]
        diff = [abs(i+1 - S) for i in range(7)]
        total = [x + y for x, y in zip(mod, diff)]
        min_idx = 0
        min_val = float('inf')
        for i in range(len(total)):
            if total[i] < min_val:
                min_idx = i
                min_val = total[i]
        s1 = min_idx + 1
        e1 = (E // s1) * s1
        path = [S]
        if S != s1:
            path.append(s1)
        if s1 != e1:
            path.append(e1)
        if e1 != E:
            path.append(E)
        print(min_val)
        print(len(path))
        print(" ".join(map(str, path)))



