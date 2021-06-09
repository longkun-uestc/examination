N, M, T = list(map(int, input().split()))
arr1 = []
for i in range(N):
    a = list(map(int, input().split()))
    arr1.append(a)
arr2 = []
for j in range(M):
    a = list(map(int, input().split()))
    arr2.append(a)

if T == 0:
    print(0)
else:
    min_hot = 10000000000000
    i, j = 0, 0
    for i, x in enumerate(arr1):
        if x[1] >=T:
            min_hot = min(min_hot, x[0])
            continue
        for j, y in enumerate(arr2):
            if y[1] >= T:
                min_hot=min(min_hot, y[0])
                continue
            if x[1]+y[1] >= T:
                min_hot = min(min_hot, x[0]+y[0])
    if min_hot == 10000000000000:
        print(-1)
    else:
        print(min_hot)

