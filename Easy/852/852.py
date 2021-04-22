# @Date    : 10:44 04/16/2021
# @Author  : ClassicalPi
# @FileName: 852.py
# @Software: PyCharm
class Solution:
    def peakIndexInMountainArray(self, arr: [int]) -> int:
        index=0
        while index < len(arr)-1:
            while index < len(arr)-1 and arr[index]<arr[index+1]:
                index+=1
            return index