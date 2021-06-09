if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    shang = set()
    xia = set()
    start, end = None, None
    for i in range(m):
        a, b = list(map(int, input().split()))
        if b == 1:
            shang.add(a)
        else:
            xia.add(a)
        if i == 0:
            start = a
        if i == m-1:
            end = a
    may = set([i+1 for i in range(n)]).difference(shang.union(xia))
    # all = shang.union(xia)
    # may = []
    # for i in range(1, n+1):
    #     if i not in all:
    #         may.append(i)
    # may = set(may)
    if start != end:
        if xia.issubset(shang) and start not in xia:
            may.add(start)
        elif shang.issubset(xia) and end not in shang:
            may.add(end)
    else:
        shang = shang.remove(start)
        xia = xia.remove(end)
        if shang == xia:
            may.add(start)
    # if start == end:
    #     shang_c = shang.remove(start)
    #     xia_c = xia.remove(end)
    #     if shang_c == xia_c:
    #         may.add(start)
    # else:
    #     if xia.issubset(shang) and start not in xia:
    #         may.add(start)
    #     elif shang.issubset(xia) and end not in shang:
    #         may.add(end)
    may = list(may)
    may.sort()
    print(" ".join(map(str, may)))
