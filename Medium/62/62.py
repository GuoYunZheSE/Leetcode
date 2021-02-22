# @Date    : 17:52 02/19/2021
# @Author  : ClassicalPi
# @FileName: 62.py
# @Software: PyCharm
import math
# class Solution:
#     # 2*2: Down:1 Right:1->2
#     # 3*2: Donw:2 Right:1->3
#     # 3*3: Down:2 Right:2->6
#     # C(n,m)
#     def uniquePaths(self, m: int, n: int) -> int:
#         if m==1 or n==1:
#             return 1
#         m = m - 1
#         n = n - 1
#         Numerator = m+n
#         total=Numerator
#         for i in range(m-1):
#             total-=1
#             Numerator*=total
#         return int(Numerator/(math.factorial(m)))

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n]*m
        dp[0][0]=0
        dp[0][1],dp[1][0]=1,1


if __name__ == '__main__':
    S=Solution()
    print(S.uniquePaths(3,7))
    print(S.uniquePaths(3, 2))
    print(S.uniquePaths(3,3))