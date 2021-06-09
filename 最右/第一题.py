if __name__ == '__main__':
    s = input()
    total = 0
    if s[0] == '-':
        flag = -1
        s = s[1:]
    else:
        flag = 1
    i = len(s)-1
    cnt = 1
    while i >= 0:
        if "0"<=s[i]<='9':
            total = total + (ord(s[i])-ord("0"))*cnt
        elif "a" <=s[i]<= "z":
            total = total + (ord(s[i])-ord("a") + 10)*cnt
        elif 'A' <= s[i]<= "Z":
            total = total + (ord(s[i])-ord("A") + 10)*cnt
        else:
            total = 0
            break
        cnt *= 36
        i -= 1
    total = total * flag
    if total > 9223372036854775807:
        total = 9223372036854775807
    if total < -9223372036854775807:
        total = -9223372036854775807
    print(total)

