if __name__ == '__main__':
    count = 0
    while count < 10:
        n = input()
        if not n:
            break
        n = int(n)
        a = list(map(int, input().split()))
        idx = 0
        ans = 0
        while idx < n:
            ans += 1
            idx1 = idx
            while idx1 < n and a[idx1] == -1:
                idx1 += 1
            if idx1 == n:
                break
            idx2 = idx1 + 1
            while idx2 < n and a[idx2] == -1:
                idx2 += 1
            if idx2 == n:
                break
            distance = idx2 - idx1
            step = (a[idx2]-a[idx1])//distance
            if (a[idx2]-a[idx1]) % distance != 0 or (step>0 and a[idx1]-(idx1-idx)*step<=0):
                idx = idx2
                continue
            idx3 = idx2 + 1
            while idx3 < n:
                next = a[idx2] + step * (idx3-idx2)
                if next <= 0 or (a[idx3] != -1 and a[idx3] != next):
                    break
                idx3 += 1
            idx = idx3
        print(ans)
        count += 1

    s = '123'
    s.sta



