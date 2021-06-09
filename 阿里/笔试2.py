def max_count(array):
    count = {}
    for x in array:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    max_cnt = -1
    for key, val in count.items():
        if val > max_cnt:
            max_cnt = val
    return max_cnt

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        for j in range(i+1, n+1):
            array = a[i:j]
            if max_count(array) >= m:
                c += 1
    print(c)
