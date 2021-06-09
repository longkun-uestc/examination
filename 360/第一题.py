if __name__ == '__main__':

    while True:
        line = input()
        if not line:
            break
        flag = [False] * 5
        # print(flag)
        for i, ch in enumerate(line):
            if '0' <= ch <= '9':
                flag[0] = True
            elif 'a' <= ch <= 'z':
                flag[1] = True
            elif 'A' <= ch <= 'Z':
                flag[2] = True
            else:
                flag[3] = True
        if len(line) >= 8:
            flag[4] = True
        flag = list(set(flag))
        if len(flag) == 1 and flag[0]:
            print('Ok')
        else:
            print("Irregular password")


