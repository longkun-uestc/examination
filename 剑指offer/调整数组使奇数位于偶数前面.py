class Solution:
    def reOrderArray(self, array):
        ji = []
        ou = []
        for a in array:
            if a % 2 == 0:
                ou.append(a)
            else:
                ji.append(a)
        ji.extend(ou)
        return ji
        # left = 0
        # right = len(array) - 1
        # while left < right:
        #     if array[left] % 2 == 0 and array[right] % 2 == 0:
        #         right -= 1
        #     elif array[left] % 2 == 0 and array[right] % 2 != 0:
        #         tmp = array[left]
        #         array[left] = array[right]
        #         array[right] = tmp
        #         left += 1
        #         right -= 1
        #     elif array[left] % 2 != 0 and array[right] % 2 == 0:
        #         left += 1
        #         right -= 1
        #     elif array[left] % 2 != 0 and array[right] % 2 != 0:
        #         left += 1
        # return array


if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 3, 4, 5, 6, 7]
    a = s.reOrderArray(x)
    print(a)
