class Solution:
    def __init__(self):
        self.s = ""
        self.dict = {}
    # 返回对应char
    def FirstAppearingOnce(self):
        for i in self.s:
            if self.dict[i] == 1:
                return i
        return "#"
        # write code here
    def Insert(self, char):
        self.s = self.s + char
        if char in self.dict:
            self.dict[char] = self.dict[char] + 1
        else:
            self.dict[char] = 1

class Solution:
    def __init__(self):
        self.s=''
        self.dict={} #创建字典，key为读取的字符串中的每一个字符，val为每个字符出现的个数的计数值
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s: #遍历字符串s中的字符
            if self.dict[i]==1: #如果某个字符对应的计数为1，则返回该字符
                return i
        return '#' #在所有字符遍历完后，进行判断
    def Insert(self, char):
        # write code here
        self.s=self.s+char #从字符流中读入字符到字符串s中
        if char in self.dict:
            self.dict[char]=self.dict[char]+1 #如果读入的字符在字符串中已存在，在字典中对应的字符计数加一
        else:
            self.dict[char]=1

if __name__ == '__main__':
    s = Solution()
    s.Insert("g")
    s.Insert("o")
    s.Insert("o")
    # s.Insert("g")
    # s.Insert("l")
    # s.Insert("e")
    a = s.FirstAppearingOnce()
    print(a)
