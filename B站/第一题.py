def is_same(s1, s2):
    map1 = {}
    map2 = {}
    for c in s1:
        if c not in map1:
            map1[c] = 1
        else:
            map1[c] += 1
    for c in s2:
        if c not in map2:
            map2[c] = 1
        else:
            map2[c] += 1
    map1 = list(map1.items())
    map2 = list(map2.items())
    map1.sort(key=lambda x:x[0])
    map2.sort(key=lambda x:x[0])
    if len(map1) != len(map2):
        return False
    if map1 == map2:
        return True
    else:
        return False

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    res = is_same(s1, s2)
    print(res)
