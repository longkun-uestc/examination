import re
word = 'abc'
s =  "a"
for i in range(1, len(word)):
    s += " *" + word[i]
print(s)
p = re.compile(s)
x = "a       bc desfewsfew"
res=p.search(x)
print(res)
