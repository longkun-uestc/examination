import re
if __name__ == '__main__':
    s = input()
    pattern = r'coc'
    p = re.compile(pattern, re.IGNORECASE)
    s = p.sub('', s)
    print(s)

