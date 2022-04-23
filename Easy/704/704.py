# @Date    : 09:46 04/10/2022
# @Author  : ClassicalPi
# @FileName: 704.py
# @Software: PyCharm

class Solution:
    def search(self, nums: [int], target: int) -> int:
        def binary_search(left:int, right:int):
            if left > right:
                return -1
            mid = int((left - right) / 2 + right)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return binary_search(mid + 1, right)
            if nums[mid] > target:
                return binary_search(left, mid - 1)
        return binary_search(0, len(nums)-1)

if __name__ == '__main__':
    S = Solution()
    print(S.search([1,2,3,4,5],1))
    print(S.search([1, 2, 3, 4, 5], 2))
    print(S.search([1, 2, 3, 4, 5], 3))
    print(S.search([1, 2, 3, 4, 5], 4))
    print(S.search([1, 2, 3, 4, 5], 0))
    print(S.search([-1,0,3,5,9,12],13))