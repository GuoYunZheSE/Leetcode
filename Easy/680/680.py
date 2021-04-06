# @Date    : 20:59 04/05/2021
# @Author  : ClassicalPi
# @FileName: 680.py
# @Software: PyCharm
import collections
class Solution:
    def validPalindrome(self, s: str) -> bool:
        q=collections.deque()

        for each in s:
            q.append(each)

        while q and q[0]==q[-1]:
            if len(q)>=2:
                q.popleft()
                q.pop()
            else:
                q.pop()

        if len(q)==0:
            return True

        q2=q.copy()

        q.pop()
        q2.popleft()

        while q and q[0]==q[-1]:
            if len(q)>=2:
                q.popleft()
                q.pop()
            else:
                q.pop()
        while q2 and q2[0]==q2[-1]:
            if len(q2)>=2:
                q2.popleft()
                q2.pop()
            else:
                q2.pop()


        return any([len(q)==0,len(q2)==0])