if __name__ == '__main__':
    T = int(input())
    dict1 = {'4': '43231323', '5':'53231323', '6':'63231323'}
    for _ in range(T):
        s = input()
        i = 0
        cnt = 0
        while i < len(s) - 7:
            now = dict1.get(s[i], '')
            if not now:
                i += 1
                continue
            else:
                if s[i:i+8] == now:
                    cnt += 1
                    i = i+8
                else:
                    i += 1
        print(cnt)





