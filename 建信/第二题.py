
if __name__ == '__main__':
    s1 = input()
    s2 = input()
    s1 = s1[1:-1]
    s2 = s2[1:-1]
    s1_arr = s1.split()
    s2_arr = s2.split()
    s1_set = set(s1_arr)
    s2_set = set(s2_arr)
    s = s1_set.union(s2_set).difference(s1_set.intersection(s2_set))
    s = list(s)
    s = ['"'+x+'"' for x in s if s1_arr.count(x) == 1 or s2_arr.count(x) == 1]
    res = ','.join(s)
    print("["+res+"]")

