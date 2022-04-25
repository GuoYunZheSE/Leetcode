# @Date    : 16:27 04/24/2022
# @Author  : ClassicalPi
# @FileName: 494.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.res = 0
        self.cache = {}
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        def DFS(index:int, sum:int):
            if (index,sum) not in self.cache:
                res = 0
                if index == len(nums):
                    if sum == 0:
                        res = 1
                else:
                    res = DFS(index + 1, sum - nums[index]) + DFS(index + 1, sum + nums[index])
                self.cache[(index,sum)] = res
            return self.cache[(index,sum)]
        return DFS(0, target)

if __name__ == '__main__':
    S = Solution()
    print(S.findTargetSumWays([1,1,1,1,1], 3))
    # print(S.findTargetSumWays([1], 1))