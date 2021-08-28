# @Date    : 22:55 08/21/2021
# @Author  : ClassicalPi
# @FileName: 5837.py
# @Software: PyCharm
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        dp = [[0 for i in range(3600)] for j in range(3600)]
        prefix = [[0 for i in range(3600)] for j in range(3600)]
        for i in range(1,len(num)+1):
            dp[1][i] = 1
        for i in range(1,len(num)):
            for j in range(i,0,-1):
                if num[j] == '0':
                    dp[j][i] = 0
                else:
                    dp[j][i] = (dp[j][i]+prefix[j-1][min(i-j,j-i)])%(10**9+7)
                    if 2*j-i-1> 0 and (num[j:i-j+1])>(num[2*j-i-1:i-j+1]):
                        dp[j][i] = (dp[j][i]+dp[2*j-1][j-1])%(10**9+7)
                prefix[i][i-j+1] = (prefix[i][i-j]+dp[j][i])%(10**9+7)
        res = 0
        for i in range(1,len(num)+1):
            res = (res + dp[i][len(num)])%(10**9+7)
        return res
if __name__ == '__main__':
    S = Solution()
    print(S.numberOfCombinations("327"))