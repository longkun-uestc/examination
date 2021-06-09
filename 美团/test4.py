if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        a = list(map(int, input().split()))
        arr.append(a)
    max1, max2 = 0, 0
    for a, b in arr:
        max1 += a if a>b else b
        max2 += (a-b) if a > b else 0
    print(max1, max2)
