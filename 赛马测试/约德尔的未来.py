s1 = input()
s2 = input()
print(s1)
print(s2)
s1_n = ''
for c in s1:
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
        s1_n += '1'
    else:
        s1_n += '0'
cnt = 0
for a, b in zip(s1_n, s2):
    if a == b:
        cnt += 1
rate = cnt / len(s2)
print('%.2f' % (rate * 100))
