
def delete(s, idx):
    if idx >= len(s)-1:
        return s
    if s[idx] != s[idx-1]:
        s = delete(s, idx+1)
    else:
        if idx < len(s)-1 and s[idx] == s[idx+1]:
            s = s[:idx+1] + s[idx+2:]
            s = delete(s, idx)
        elif idx < len(s) - 2 and s[idx+1] == s[idx+2]:
            s = s[:idx+2] + s[idx+3:]
            s = delete(s, idx)
        else:
            s = delete(s, idx+1)
    return s

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        s = input()
        a = delete(s, 1)
        arr.append(a)
    for a in arr:
        print(a)