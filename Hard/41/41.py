# @Date    : 11:06 10/07/2020
# @Author  : ClassicalPi
# @FileName: 41.py
# @Software: PyCharm

class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        nums.append(0)
        for i in range(len(nums)):
            if nums[i]<0 or nums[i]>=len(nums):
                nums[i]=0
        for i in range(len(nums)):
            nums[nums[i]%len(nums)]+=len(nums)
        for i in range(1,len(nums)):
            if nums[i]//len(nums)==0:
                return i
        return len(nums)
if __name__ == '__main__':
    S=Solution()
    print(S.firstMissingPositive([1,2,3,6,7,8,20,23]))