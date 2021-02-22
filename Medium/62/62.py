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
        if m==1 or n==1:
            return 1
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        dp[1][1],dp[2][1],dp[1][2]=1,1,1
        for row in range(1,m+1):
            for column in range(1,n+1):
                if not(row==1 and column==1):
                    dp[row][column]=dp[row-1][column]+dp[row][column-1]
        return dp[m][n]


if __name__ == '__main__':
    S=Solution()
    print(S.uniquePaths(3,7))
    print(S.uniquePaths(3, 2))
    print(S.uniquePaths(3,3))