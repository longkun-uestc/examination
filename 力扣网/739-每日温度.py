from typing import List
class Solution:
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)-1):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
                if j == len(temperatures)-1:
                    res.append(0)
        res.append(0)
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        stack = [0]
        res = [0 for i in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            if not stack or temperatures[i] < temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop(-1)
                stack.append(i)
        return res


if __name__ == '__main__':
    tem = [73]
    s = Solution()
    r = s.dailyTemperatures(tem)
    print(r)