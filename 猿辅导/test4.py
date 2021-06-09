N, M = list(map(int, input().split()))
r = list(map(int, input().split()))
dic = {}
for i in r:
    dic[i] = dic.get(i, 0) + 1

for i in r:
    if dic[i] > M:
        continue
    else:
        print(i, end=' ')