# @Date    : 09:09 03/12/2020
# @Author  : ClassicalPi
# @FileName: 1287.py
# @Software: PyCharm
import collections
class Solution:
    def findSpecialInteger(self, arr: [int]) -> int:
        for key,val in (collections.Counter(arr)).items():
            if val>=len(arr)//4:
                return key
        return -1
