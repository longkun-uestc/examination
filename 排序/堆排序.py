def build(s, e):
    for i in range(2, e):
        j = i
        while j > 1 and s[j] > s[j//2]:
            tmp = s[j]
            s[j] = s[j//2]
            s[j//2] = tmp
            j = j//2
    return s

def out_dui(s):
    s = [-1] + s
    build(s, len(s))
    print(s)
    for i in range(len(s)-1, 1, -1):
        tmp = s[i]
        s[i] = s[1]
        s[1] = tmp
        build(s, i)
        print(s)


def build1(s, n, i):
    large = i
    l = i*2 + 1
    r = i*2 + 2
    if l < n and s[i] < s[l]:
        large = l
    if r < n and s[large] < s[r]:
        large = r
    if large != i:
        s[i], s[large] = s[large], s[i]
        build1(s, n, large)

def dui_sort(s):
    for i in range(len(s)-1, -1, -1):
        build1(s, len(s), i)
    for i in range(len(s)-1, 0, -1):
        s[i], s[0] = s[0], s[i]
        build1(s, i, 0)

def build_small(s, n, i):
    small = i
    l = i * 2 + 1
    r = i * 2 + 2
    if l < n and s[i] > s[l]:
        small = l
    if r < n and s[small] > s[r]:
        small = r
    if small != i:
        s[i], s[small] = s[small], s[i]
        build_small(s, n, small)

def top_k(s, k):
    top = s[:k]
    for i in range(k-1, -1, -1):
        build_small(top, k, i)
    print(top)
    for i in range(k, len(s)):
        if s[i] > top[0]:
            top[0] = s[i]
            build_small(top, k, 0)
    print(top)


if __name__ == '__main__':
    s = [6, 8, 3, 2, 4, 7, 5, 10, 1, 9]
    s = [5, 4, 7, 2, 1, 6, 3, 7, 8, 9]
    # dui_sort(s)
    # print(s)
    top_k(s, 4)
