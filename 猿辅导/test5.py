C = int(input())
pi_list = []
for i in range(C):
    arr = list(map(int, input().split()))
    pi_list.append([x for x in arr[1:] if x > 0])

for pi in pi_list:
    count = 0
    pi.sort(reverse=True)
    while pi[0] > 0 and pi[1] > 0 and pi[2] > 0:
        count += pi[2]
        pi[0] -= pi[2]
        pi[1] -= pi[2]
        pi[2] -= pi[2]
        j = 3
        while j < len(pi) and pi[j] > pi[2]:
            j += 1
        pi[2], pi[j-1] = pi[j-1], pi[2]
        j = 2
        while j < len(pi) and pi[j] > pi[1]:
            j += 1
        pi[1], pi[j - 1] = pi[j - 1], pi[1]
        j = 1
        while j < len(pi) and pi[j] > pi[0]:
            j += 1
        pi[0], pi[j-1] = pi[j-1], pi[0]

        # pi.sort(reverse=True)

    print(count)

