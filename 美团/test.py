arr = list(map(int, input().split()))
cnt = 0
all_count = 0
for i, count in enumerate(arr):
    cnt += (i+1)*count
    all_count += count
if all_count == 0:
    print('0.0')
else:
    rate = cnt/all_count
    rate = str(float(rate))
    print(rate[:3])

