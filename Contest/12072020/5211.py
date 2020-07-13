# @Date    : 11:09 07/12/2020
# @Author  : ClassicalPi
# @FileName: 5211.py
# @Software: PyCharm
import heapq
class Solution:
    def maxProbability(self, n: int, edges: [[int]], succProb: [float], start: int, end: int) -> float:
        S=set()

        Dict={}
        for index,val in enumerate(edges):
            if Dict.__contains__(val[0]):
                Dict[val[0]].setdefault(val[1],succProb[index])
            else:
                Dict.setdefault(val[0],{val[1]:succProb[index]})
            if Dict.__contains__(val[1]):
                Dict[val[1]].setdefault(val[0],succProb[index])
            else:
                Dict.setdefault(val[1],{val[0]:succProb[index]})
        h = [(-1, start)]  # Dijkstra's algo
        while h:
            p,n=heapq.heappop(h)
            if n==end:return -p
            S.add(n)
            for eachnode in Dict[n]:
                if eachnode in S:
                    continue
                else:
                    heapq.heappush(h,(p*Dict[n][eachnode],eachnode))
        return 0

if __name__ == '__main__':
    S=Solution()
    print(S.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))
    print(S.maxProbability( n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))
    print(S.maxProbability(5,[[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]],[0.37,0.17,0.93,0.23,0.39,0.04],3,4))