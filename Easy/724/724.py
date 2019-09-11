# 724. Find Pivot Index
# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0
        else:
            sum_left=0
            sum_total=sum(nums)
            sum_right=sum_total
            for pivot in range(0,len(nums)):
                sum_right-=nums[pivot]
                if sum_right==sum_left:
                    return pivot
                sum_left += nums[pivot]
            return -1
# Success
# Details
# Runtime: 164 ms, faster than 98.47% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15 MB, less than 8.33% of Python3 online submissions for Find Pivot Index.
if __name__ == '__main__':
    a=[-1,-1,-1,-1,-1,-1]
    S=Solution()
    S.pivotIndex(a)