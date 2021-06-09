class Solution:
    def intToRoman(self, num: int) -> str:
        map_dict = {1:'I', 5:'V', 10:'X', 50: 'L', 100: 'C', 500: 'D', 1000:'M'}
        cnt = 1
        s = ''
        while num > 0:
            now = num % 10
            if now == 0:
                cnt *= 10
                num = num // 10
                continue
            if now < 4:
                s = map_dict[cnt] * now + s
            elif now == 4:
                s = map_dict[cnt]+map_dict[5*cnt] + s
            elif 5 <= now < 9:
                s = map_dict[5*cnt] + map_dict[cnt]*(now-5) + s
            else:
                s = map_dict[cnt] + map_dict[10*cnt] + s
            num = num // 10
            cnt *= 10
        return s

if __name__ == '__main__':
    s = Solution()
    x = 9
    res = s.intToRoman(x)
    print(res)
