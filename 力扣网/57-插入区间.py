from  typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        res = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                i += 1
            else:
                break
        left = min(intervals[i][0], newInterval[0])
        right = newInterval[1]
        while i < len(intervals):
            if intervals[i][0] <= newInterval[1]:
                right = max(intervals[i][1], right)
                i += 1
            else:
                break
        res.append([left, right])
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    intervals = [[1, 5]]
    newInterval = [2, 3]
    s = Solution()
    r = s.insert(intervals, newInterval)
    print(r)





