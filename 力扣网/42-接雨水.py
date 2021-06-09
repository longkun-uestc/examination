from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        i = 1
        while i < len(height) and height[i] >= height[i-1]:
            i += 1
        feng = [i-1]
        flag = 'B'
        while i < len(height):
            if flag == "B":
                while i < len(height) and height[i] <= height[i-1]:
                    i += 1
                flag = 'T'
            elif flag == 'T':
                while i < len(height) and height[i] >= height[i-1]:
                    i += 1
                feng.append(i-1)
                flag = "B"
        print(feng)
        f1 = 0
        total = 0
        while f1 < len(feng):
            next = f1 + 1
            while next < len(feng) and height[feng[next]] < height[feng[f1]]:
                next += 1
            if next < len(feng):
                # s = [height[feng[f1]] - height[x] for x in range(feng[f1], feng[next]) if height[x] < height[feng[f1]]]
                # total += sum(s)
                s = 0
                for x in range(feng[f1], feng[next]):
                    if height[x] < height[feng[f1]]:
                        s += height[feng[f1]] - height[x]
                total += s
                f1 = next
            else:
                if f1 < len(feng) - 1:
                    max_f = f1 + 1
                    max_h = height[feng[max_f]]
                    for idx in range(max_f+1, len(feng)):
                        if height[feng[idx]] > max_h:
                            max_h = height[feng[idx]]
                            max_f = idx

                    minh = min(height[feng[f1]], height[feng[max_f]])
                    # s = [minh - height[x] for x in range(feng[f1], feng[max_f]) if height[x] <= minh]
                    # total += sum(s)
                    s = 0
                    for x in range(feng[f1], feng[max_f]):
                        if height[x] <= minh:
                            s += minh - height[x]
                    total += s
                    f1 = max_f
                else:
                    f1 += 1

                # if f1 < len(feng) - 1:
                #     minf = min(height[feng[f1]], height[feng[f1+1]])
                #     s = [minf - height[x] for x in range(feng[f1], feng[f1+1]) if height[x] <= minf]
                #     total += sum(s)
                # f1 += 1
        print(total)
        return total



if __name__ == '__main__':
    s = Solution()
    x = [2,2,0,1,0,2,1,0,1,3,2,1,2,1]
    x = [0,1,0,2,1,0,1,3,2,1,2,1]
    x = [5,2,1,2,1,5]
    # x = [5,5,4,7,8,2,6,9,4,5]
    # x = [2,8,5,5,6,1,7,4,5]
    s.trap(x)