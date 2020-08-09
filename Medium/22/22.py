# @Date    : 23:10 08/06/2020
# @Author  : ClassicalPi
# @FileName: 22.py
# @Software: PyCharm

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

if __name__ == '__main__':
    S=Solution()
    print(S.generateParenthesis(3))