# @Date    : 16:43 08/22/2021
# @Author  : ClassicalPi
# @FileName: 85.py
# @Software: PyCharm
class Solution:
    def maximalRectangle(self, matrix: [[str]]) -> int:
        res = 0
        for row in range(0, len(matrix)):
            stack = [-1]
            heights = []
            for i in range(0, len(matrix[0])):
                matrix[row][i] = int(matrix[row][i])
                if row > 0 and matrix[row][i] == 1:
                    matrix[row][i] += matrix[row - 1][i]
                heights.append(matrix[row][i])
            heights.append(0)
            for i in range(0, len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res
if __name__ == '__main__':
    S = Solution()
    print(S.maximalRectangle([["0","1"],["1","0"]]))