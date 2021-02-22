# @Date    : 15:44 02/22/2021
# @Author  : ClassicalPi
# @FileName: 63.py
# @Software: PyCharm
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        rows=len(obstacleGrid)
        columns=len(obstacleGrid[0])
        if rows==1:
            if 1 in obstacleGrid[0]:
                return 0
            else:
                return 1
        if columns==1:
            for each in obstacleGrid:
                if each[0]==1:
                    return 0
            return 1
        dp=[[0 for i in range(columns+1)] for j in range(rows+1)]
        dp[1][1],dp[2][1],dp[1][2]=dp[0][0]^1,dp[1][0]^1,dp[0][1]^1
        if dp[1][1]==1:
            return 0
        for row in range(1,rows+1):
            for column in range(1,columns+1):
                if not(row==1 and column==1):
                    if obstacleGrid[row-1][column-1]==1:
                        dp[row][column]=0
                    else:
                        dp[row][column]=dp[row - 1][column] + dp[row][column - 1]
        return dp[rows][columns]

if __name__ == '__main__':
    S=Solution()
    print(S.uniquePathsWithObstacles([[0,1],[0,0]]))