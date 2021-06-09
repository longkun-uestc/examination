if __name__ == '__main__':
    count = 0
    ns = []
    arr = []
    while count < 10:
        n = input()
        if not n:
            break
        n = int(n)
        a = list(map(int, input().split()))
        ns.append(n)
        arr.append(a)
        count += 1
    for n, a in zip(ns, arr):
        i = 0
        ans = 0
        while i < n:
            ans += 1
            i1 = i
            while i1 < n and a[i1] == -1:
                i1 += 1
            if i1 == n:
                break
            i2 = i1 + 1
            while i2 < n and a[i2] == -1:
                i2 += 1
            if i2 == n:
                break
            dist = i2 - i1
            step = (a[i2]-a[i1])//dist
            if (a[i2]-a[i1])%dist != 0 or (step>0 and a[i1]-(i1-i)*step<=0):
                i = i2
                continue
            i3 = i2 + 1
            while i3 < n:
                nxt = a[i2] + step * (i3-i2)
                if nxt <=0 or (a[i3] != -1 and a[i3] != nxt):
                    break
                i3 += 1
            i = i3
        print(ans)



