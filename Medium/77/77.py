# @Date    : 15:57 08/22/2021
# @Author  : ClassicalPi
# @FileName: 77.py
# @Software: PyCharm
class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        candidatess = [i for i in range(1,n+1)]
        res = []
        def DFS(candidates:[],left:int,cur:[]):
            if left > 0:
                for i in range(0,len(candidates)):
                    DFS(candidates[i+1:],left - 1, cur + [candidates[i]])
            else:
                res.append(cur)
        DFS(candidatess,k,[])
        return res