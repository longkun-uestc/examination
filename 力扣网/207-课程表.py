from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = {}
        for i in range(numCourses):
            course_dict[i] = {'count': 0, 'arrive': []}
        for pair in prerequisites:
            # if pair[1] not in course_dict:
            #     course_dict[pair[1]] = {'count': 0, 'arrive': [pair[0]]}
            # else:
            #     course_dict[pair[1]]['arrive'].append(pair[0])
            # if pair[0] not in course_dict:
            #     course_dict[pair[0]] = {'count': 1, 'arrive': []}
            # else:
            #     course_dict[pair[0]]['count'] += 1
            course_dict[pair[1]]['arrive'].append(pair[0])
            course_dict[pair[0]]['count'] += 1

        stack = [key for key, val in course_dict.items() if val['count'] == 0]
        while stack:
            now = stack.pop()
            arrive = course_dict[now]['arrive']
            for item in arrive:
                course_dict[item]['count'] -= 1
                if course_dict[item]['count'] == 0:
                    stack.append(item)
            course_dict.pop(now)
        if not course_dict:
            return True
        else:
            return False


if __name__ == '__main__':
    n = 2
    arr = [[0,1]]
    s = Solution()
    res = s.canFinish(n, arr)
    print(res)



