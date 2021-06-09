def sort_by_f(s):
    count_dict = {}
    for i in range(len(s)):
        if s[i] not in count_dict:
            count_dict[s[i]] = 1
        else:
            count_dict[s[i]] += 1
    count_list = []
    for key, c in count_dict.items():
        count_list.append((key, c))
    count_list.sort(key=lambda x:(x[1], x[0]))
    res = ''
    for item in count_list:
        res += item[0] * item[1]
    return res



if __name__ == '__main__':
    s1 = input()
    res = sort_by_f(s1)
    print(res)
