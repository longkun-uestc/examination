T = int(input())
array = []
for i in range(T):
    n = int(input())
    array.append(n)

for n in array:
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    count += 1
    print(count)

