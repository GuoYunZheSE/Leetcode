# @Date    : 21:58 07/24/2021
# @Author  : ClassicalPi
# @FileName: 279.py
# @Software: PyCharm
import math
import sys
class Solution:
    def numSquares(self, n: int) -> int:
        resMap = [0,1]+[sys.maxsize]*(n)
        for i in range(1,n+1):
            Min = sys.maxsize
            for j in range(1,int(math.sqrt(i))+1):
                Min = min(Min,resMap[i-j**2]+1)
            resMap[i]=Min
        return resMap[n]
if __name__ == '__main__':
    S=Solution()
    print(S.numSquares(1))
    print(S.numSquares(2))
    print(S.numSquares(3))
    print(S.numSquares(4))
    print(S.numSquares(5))
    print(S.numSquares(6))
    print(S.numSquares(7))
    print(S.numSquares(8))
    print(S.numSquares(9))
    print(S.numSquares(12))
    print(S.numSquares(9999))
