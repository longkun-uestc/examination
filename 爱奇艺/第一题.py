if __name__ == '__main__':
    s = input()
    words = input().split()
    for word in words:
        i, j = 0, 0
        length = len(s)
        tag = -1
        while j < length:
            if s[j] == word[i]:
                if tag == -1:
                    tag = j
                j += 1
                i += 1
            elif s[j] == " ":
                j += 1
            else:
                if tag == -1:
                    j += 1
                tag = -1
                i = 0
            if i == len(word):
                pair = s[tag:j]
                pair = pair.replace(" ", '')
                s1 = s[:tag].strip()
                s2 = s[j:].strip()
                s = s1 + " " + pair + " " + s2
                length = len(s)
                i = 0
                tag = -1
    print(s.strip())

