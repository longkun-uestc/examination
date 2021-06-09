from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x[0], x[1]))
        merges = []
        for interval in intervals:
            if not merges or merges[-1][1]<interval[0]:
                merges.append(interval)
            else:
                merges[-1][1] = max(merges[-1][1], interval[1])
        return merges