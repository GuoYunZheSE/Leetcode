# @Date    : 16:49 02/26/2020
# @Author  : ClassicalPi
# @FileName: 862.py
# @Software: PyCharm
import typing
import collections
class Solution:
    def shortestSubarray(self, A: typing.List[int], K: int) -> int:
        left,right=0,0
        res,S=len(A)+1,[0]
        Dq=collections.deque()
        for i in A:
            S.append(S[-1]+i)
        for i,s in enumerate(S):
            while Dq and s<S[Dq[-1]]:
                Dq.pop()
            while Dq and s-S[Dq[0]]>=K:
                res=min(res,i-Dq.popleft())
            Dq.append(i)
        return res if res<len(A)+1 else -1
if __name__ == '__main__':
    A=[2,-1,2]
    K=3
    s=Solution()
    print(s.shortestSubarray(A,K))