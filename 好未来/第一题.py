class Solution:
    def get_letters(self, input_num_list):
        # map_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.map_dict = {0: 'abc', 1: 'def', 2: 'ghi', 3: 'jkl', 4: 'mno', 5: 'pqr', 6: 'stu', 7: 'vwx', 8: 'y', 9: 'z'}
        self.s = ''
        self.res = []
        self.get_arr(input_num_list, 0)
        print(self.res)
        return self.res

    def get_arr(self, digits, idx):
        if idx == len(digits):
            self.res.append(self.s)
            return
        for c in self.map_dict[digits[idx]]:
            self.s = self.s + c
            self.get_arr(digits, idx+1)
            self.s = self.s[:-1]

if __name__ == '__main__':
    nums = [0,1,9]
    s = Solution()
    s.get_letters(nums)
