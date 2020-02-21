import typing
import sys
class Solution:
    def nextPermutation(self, nums: typing.List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        find=False
        minDisstance=sys.maxsize
        minI=0
        minJ=0
        for i in range(len(nums)-1,0,-1):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    cur=(nums[i]-nums[j])*(10**(len(nums)-1-j))+(nums[j]-nums[i])*(10**(len(nums)-1-i))
                    if cur<minDisstance:
                        minDisstance=cur
                        minI=i
                        minJ=j
                    find=True
        if not find:
            nums.sort()
        else:
            nums[minI], nums[minJ] = nums[minJ], nums[minI]
            aps = sorted(nums[minJ + 1:])
            nums[minJ + 1:] = aps
            return
if __name__ == '__main__':
    nums=[20,28,29,10,21,13,24,18,25,28,12,2,20,16,13,6,21,20,25,17,24,2,10,0,13,13,19,10,4,3,13,24,2,4,5,23,18,21,11,13,11,15,8,1,23,13,29,7,25,24,24]
    s=Solution()
    s.nextPermutation(nums)
    print(nums)