# https://web.stanford.edu/class/cs124/lec/med.pdf
class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    # if not word1 or not word2:
    #     return max(len(word1),len(word2))
    # row,column = len(word1),len(word2)
    # dp = [[0 for c2 in range(0,column+1)] for c1 in range(0,row+1)]
    #
    # for i in range(0,row+1):
    #     dp[i][0] = i
    # for j in range(0,column+1):
    #     dp[0][j] = j
    #
    # for i in range(1,row+1):
    #     for j in range(1,column+1):
    #         if word1[i-1] == word2[j-1]:
    #             dp[i][j] = dp[i-1][j-1]
    #         else:
    #             dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
    # return dp[-1][-1]
    def minDistance2(self, word1, word2, i, j, memo):
        """Memoized solution"""
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.minDistance2(word1, word2, i + 1, j + 1, memo)
            else:
                insert = 1 + self.minDistance2(word1, word2, i, j + 1, memo)
                delete = 1 + self.minDistance2(word1, word2, i + 1, j, memo)
                replace = 1 + self.minDistance2(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]

    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def TopDownDP(word1: str, word2: str, i: int, j: int):
            if not word1 or not word2:
                return max(len(word1), len(word2))
            if (i, j) in cache:
                return cache[(i, j)]
            else:
                if word1[0] == word2[0]:
                    return TopDownDP(word1[1:], word2[1:], i + 1, j + 1)
                insert = TopDownDP(word1, word2[1:], i, j + 1) + 1
                delete = TopDownDP(word1[1:], word2, i + 1, j) + 1
                replace = TopDownDP(word1[1:], word2[1:], i + 1, j + 1) + 1
                temp = min(insert,delete,replace)
                cache[(i,j)] = temp
                return temp
        return TopDownDP(word1,word2,0,0)
if __name__ == '__main__':
    S = Solution()
    memo = {}
    print(S.minDistance("horse", "ros"))
