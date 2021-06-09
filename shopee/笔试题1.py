def merge(l1, l2):
    max_l = min(len(l1), len(l2))
    i, j = 0, 0
    flag = False
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            if flag:
                max_l = max(max_l, len(l1[:i])+len(l2[j:]))
                flag = False
            j += 1
        if l1[i] == l2[j]:
            flag = True
            max_l = max(max_l, len(l1[:i+1])+len(l2[j:]))
            i += 1
            j += 1
        if l1[i] < l2[j]:
            i += 1
    i, j = 0, 0
    flag = False
    while i < len(l2) and j < len(l1):
        if l2[i] > l1[j]:
            if flag:
                max_l = max(max_l, len(l2[:i]) + len(l1[j:]))
                flag = False
            j += 1
        if l2[i] == l1[j]:
            flag = True
            max_l = max(max_l, len(l2[:i + 1]) + len(l1[j:]))
            i += 1
            j += 1
        if l2[i] < l1[j]:
            i += 1
    print(max_l)


if __name__ == '__main__':
    n1, n2 = map(int, input().split())
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))
    merge(L1, L2)
