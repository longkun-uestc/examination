import sys
data = input()
n = int(input())
i = 0
j = 0
length = len(data)
while j <length:
    a, b = int(data[0]), int(data[1])
    if b >= a:
        i += 1
        data = data[0] + data[2:]
    elif a > b:
        i += 1
        data = data[1:]
        length -= 1
    if i == n:
        break
length = len(data)
i = 0
while i < length:
    if int(data[i]) != 0:
        break
    else:
        data = data[:i] + data[i+1:]
        length -= 1
result = []
if data == '':
    print(0)
else:
    print(data)