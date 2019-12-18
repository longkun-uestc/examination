class Solution:
    def ReverseSentence(self, s):
        if len(s) <= 1:
            return s
        s_array = s.split(" ")
        result = ""
        while s_array:
            result += s_array.pop() + " "
        result = result[:-1]
        return result


if __name__ == '__main__':
    s = Solution()
    x = "student. a am I"
    s.ReverseSentence(x)