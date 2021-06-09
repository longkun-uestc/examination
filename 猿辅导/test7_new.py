n, s = list(map(int, input().split()))
array = list(map(int, input().split()))
i,j = 0,0
max_l = 0
total = 0
while i < len(array) and j < len(array):
    while j < len(array) and total <= s:
        total += array[j]
        j += 1
    max_l = max(max_l, j-i-1)
    while total > s:
        total -= array[i]
        i += 1
    # print(i, j, max_l, total)
print(max_l)



