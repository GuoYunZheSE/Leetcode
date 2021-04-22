# @Date    : 11:13 04/16/2021
# @Author  : ClassicalPi
# @FileName: 169.py
# @Software: PyCharm
import collections
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        d=collections.Counter(nums)
        for k,v in d.items():
            if v>=len(nums)//2:
                return k
        return -1