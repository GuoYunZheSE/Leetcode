# @Date    : 18:25 07/25/2021
# @Author  : ClassicalPi
# @FileName: 283.py
# @Software: PyCharm
class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-i-1):
                if nums[j]==0:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums

if __name__ == '__main__':
    S=Solution()
    print(S.moveZeroes([]))