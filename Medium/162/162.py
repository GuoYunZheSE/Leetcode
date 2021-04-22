# @Date    : 09:57 04/16/2021
# @Author  : ClassicalPi
# @FileName: 162.py
# @Software: PyCharm
class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        peaks=[]
        valley=[]
        if len(nums)==0:
            return nums[0]
        index=0
        while index<len(nums)-1:
            while index<len(nums)-1 and nums[index]<nums[index+1]:
                index+=1
            peaks.append(index)
            while index<len(nums)-1 and nums[index]>nums[index+1]:
                index+=1
            valley.append(index)
        return peaks[0]
if __name__ == '__main__':
    S=Solution()
    print(S.findPeakElement([2]))