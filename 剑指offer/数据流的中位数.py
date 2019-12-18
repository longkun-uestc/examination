class Solution:
    num_list = []
    def Insert(self, num):
        self.num_list.append(num)
        self.num_list.sort()
        # write code here
    def GetMedian(self, num_list):
        length = len(self.num_list)
        if length % 2 == 0:
            return (self.num_list[int(length//2) - 1] + self.num_list[int(length//2)])/2.0
        else:
            return self.num_list[length//2]