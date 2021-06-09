from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        flag = -1
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                flag = -1
            else:
                x = students.pop(0)
                students.append(x)
                flag = flag - 1 if flag != -1 else len(students)-1
            if flag == 0:
                break
        return len(students)

if __name__ == '__main__':
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]
    s = Solution()
    x = s.countStudents(students, sandwiches)
    print(x)