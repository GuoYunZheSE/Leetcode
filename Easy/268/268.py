# @Date    : 12:21 10/07/2020
# @Author  : ClassicalPi
# @FileName: 268.py
# @Software: PyCharm

class Solution:
    def missingNumber(self, nums: [int]) -> int:
        if not nums:
            return 0
        nums_set=set(nums)
        for i in range(len(nums)):
            if i not in nums_set:
                return i
        return len(nums)

if __name__ == '__main__':
    S=Solution()
    print(S.missingNumber([1]))