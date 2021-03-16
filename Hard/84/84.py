# @Date    : 19:37 03/16/2021
# @Author  : ClassicalPi
# @FileName: 84.py
# @Software: PyCharm
import sys
class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
if __name__ == '__main__':
    S=Solution()
    print(S.largestRectangleArea([2,1,5,6,2,3]))
    print(S.largestRectangleArea([2, 4]))
    print(S.largestRectangleArea([2,1,2]))
    print(S.largestRectangleArea([1,1]))