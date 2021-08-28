# @Date    : 17:38 08/21/2021
# @Author  : ClassicalPi
# @FileName: 39.py
# @Software: PyCharm
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def DFS(target:int,candidates:[],combination:[]):
            if target < 0:
                return
            if target == 0:
                res.append(combination)
                return
            for i in range(len(candidates)):
                DFS(target - candidates[i],candidates[i:],combination + [candidates[i]])
        DFS(target,candidates,[])
        return res
if __name__ == '__main__':
    S = Solution()
    print(S.combinationSum( [2,3,5], target = 8))