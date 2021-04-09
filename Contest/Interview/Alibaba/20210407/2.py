# @Date    : 09:06 04/07/2021
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm
import collections
class Solution:
    def maxSum(self,l:[],n:int):
        window1 = collections.deque()
        for index,val in enumerate(l):
            if len(window1)<n:
                window1.append(val)