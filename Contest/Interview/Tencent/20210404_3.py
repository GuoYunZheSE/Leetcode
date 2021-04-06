# @Date    : 19:54 04/04/2021
# @Author  : ClassicalPi
# @FileName: 20210404_3.py
# @Software: PyCharm

import collections

class Solution:
    def timp_count(self,n:int,students:[int]):
        if n==1:
            return students[0]
        if n==2:
            return max(students)

        time=0
        students = sorted(students)
        left=collections.deque(students)
        right=collections.deque()

        fast=left.popleft()
        slower=left.popleft()

        right.append(slower)
        left.appendleft(fast)
        time+=(slower+fast)




