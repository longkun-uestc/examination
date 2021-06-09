def triangles():
    now = [1]
    max_count = 0
    while True:
        yield now
        next = []
        i = 0
        next.append(1)
        while i + 1 < len(now):
            next.append(now[i] + now[i + 1])
            i += 1
        next.append(1)
        now = next
        max_count += 1


# for x in triangles(10):
#     print(x)
# exit()
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)
