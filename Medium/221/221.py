# @Date    : 23:44 08/25/2021
# @Author  : ClassicalPi
# @FileName: 221.py
# @Software: PyCharm
class Solution:
    def maximalSquare_0(self, matrix: [[str]]) -> int:
        res = 0
        for row in range(0,len(matrix)):
            heights = []
            stack = [-1]
            for i in range(0,len(matrix[0])):
                matrix[row][i] = int(matrix[row][i])
                if row > 0 and matrix[row][i] == 1:
                    matrix[row][i] += matrix[row-1][i]
                heights.append(matrix[row][i])
            heights.append(0)
            for i in range(0,len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    if h==w:
                        res = max(res,h*w)
                stack.append(i)
        return res

    def maximalSquare(self, matrix: [[str]]) -> int:
        MaxLength = 0
        dp = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                # print(f"i:{i} j:{j}")
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
                    MaxLength = max(MaxLength, dp[i][j])
        return MaxLength**2

if __name__ == '__main__':
    S = Solution()
    print(S.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))