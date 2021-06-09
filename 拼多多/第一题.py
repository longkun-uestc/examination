K, N = list(map(int, input().split()))
array = list(map(int, input().split()))
count = 0
start = 0
flag = False
for i, x in enumerate(array):
    start = start + x
    if start == K and i < N-1:
        flag = True
        break
    elif start > K:
        start = K-(start-K)
        count += 1

if flag or K == 0:
    print('paradox')
else:
    print("%d %d" % (K-start, count))
