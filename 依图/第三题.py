map_dict = {
    ".-": "A", '-...': "B", "-.-.": "C", '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K',
    '.-..': 'L', '--': 'M', '-.': "N", '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': "S",
    '-': 'T',
    '..-': 'U',
    '...-': 'V', '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': "1",
    '..---': "2", '...--': "3",
    '....-': "4",
    '.....': "5",
    '-....': "6",
    '--...': "7",
    '---..': "8",
    '----.': "9",
    '-----': "0"
}
dict2 = {
    '1': ".",
    '111': '-',
    '0': '',
    '000': '',
    "0000000": " "
}
if __name__ == '__main__':
    s = input()
    i = 0
    res = ''
    word = ""
    while i < len(s):
        if s[i] == "1":
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            sub = s[i:j]
            item = dict2[sub]
            word += item
            i = j
        else:
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            if j == i + 1:
                i = j
            elif j - i == 3:
                res += map_dict[word]
                word = ''
                i = j
            elif j-i == 7:
                res += map_dict[word] + " "
                word = ''
                i = j
    # print(word, map_dict[word])
    res += map_dict[word]
    print(res)

