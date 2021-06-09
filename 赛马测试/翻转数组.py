n = int(input())
a = list(map(int, input().split()))
i = 0
flag = True
first = True
while i < len(a):
    while i + 1 < len(a) and a[i] <= a[i + 1]:
        i += 1
    j = i
    while j + 1 < len(a) and a[j] >= a[j + 1]:
        j += 1
    if i != j:
        left = False
        if i > 0 and a[j] >= a[i - 1] or i == 0:
            left = True
        right = False
        if j < len(a) - 1 and a[i] <= a[j + 1] or j == len(a) - 1:
            right = True
        if first:
            flag = left and right
            first = False
        else:
            flag = False
        if not flag:
            break
        else:
            i = j + 1
    else:
        if first:
            flag = True
            first = False
        i += 1
if flag:
    print('yes')
else:
    print('no')
