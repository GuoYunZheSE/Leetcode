# @Date    : 13:09 03/15/2021
# @Author  : ClassicalPi
# @FileName: 90.py
# @Software: PyCharm
class Solution:
    def BFS(self, path: [], nums: [], res: []):
        res.append(path)
        pasted = []
        for i in range(len(nums)):
            if nums[i] not in pasted:
                pasted.append(nums[i])
                self.BFS(path + [nums[i]], nums[i + 1:], res)

    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        res = []
        nums.sort()
        self.BFS([], nums, res)
        return res
