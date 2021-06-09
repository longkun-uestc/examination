n = int(input())
st = []
for i in range(n):
    st.append(input())

for s in st:
    index = 0
    t = ['']
    while index < len(s):
        if s[index] == '(':
            t.append('')
            index += 1
        elif s[index] == ')':
            k = index + 1
            index += 1
            while index < len(s) and ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'):
                index += 1
            number = int(s[k: index])
            now = t.pop()
            t[-1] += now * number
        elif ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'):
            k = index
            index += 1
            while index < len(s) and ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'):
                index += 1
            number = int(s[k: index])
            t[-1] += t[-1][-1]*(number-1)
        else:
            t[-1] += s[index]
            index += 1
    print(t[0])
