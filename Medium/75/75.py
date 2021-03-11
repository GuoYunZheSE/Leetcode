# @Date    : 10:14 03/11/2021
# @Author  : ClassicalPi
# @FileName: 75.py
# @Software: PyCharm
import collections
class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter=collections.Counter(nums)
        index=0
        for i in [0,1,2]:
            if counter[i]:
                for j in range(counter[i]):
                    nums[index]=i
                    index+=1
