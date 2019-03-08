# Class:Medium
# Data:07/03/2019
# Runtime: 36 ms, faster than 78.63% of Python3 online submissions for Combination Sum III.
# Memory Usage: 13.3 MB, less than 5.68% of Python3 online submissions for Combination Sum III.
class Solution:
    def combinationSum3(self, k, n):
        res = []
        self.dfs(range(1, 10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:  # backtracking
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], res)
if __name__ == '__main__':
    K=8
    N=40
    S=Solution()
    S.combinationSum3(K,N)