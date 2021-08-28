# @Date    : 19:49 08/17/2021
# @Author  : ClassicalPi
# @FileName: 32.py
# @Software: PyCharm
import collections
class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = collections.deque([0])
    #     res = 0
    #     for c in s:
    #         if c == "(":
    #             stack.append(0)
    #         else:
    #             if len(stack) > 1:
    #                 val = stack.pop()
    #                 stack[-1] += val + 2
    #                 res = max(res,stack[-1])
    #             else:
    #                 stack = [0]
    #     return res
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        res = 0
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    res = max(res,stack[-1])
                else:
                    stack.append(0)
        return res