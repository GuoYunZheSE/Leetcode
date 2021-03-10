# @Date    : 14:19 03/10/2021
# @Author  : ClassicalPi
# @FileName: 764.py
# @Software: PyCharm
import sys
class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        memory=[sys.maxsize for i in range(len(cost))]
        if len(cost)<=2:
            return min(cost)
        else:
            res=[]
            memory[0]=cost[0]
            memory[1]=cost[1]
            cost.append(0)
            memory.append(0)
            for i in range(2,len(cost)):
                memory[i]=min(memory[i-1],memory[i-2])+cost[i]
            res.append(memory[-1])

            memory = [sys.maxsize for i in range(len(cost))]
            memory[0]=cost[0]
            memory[1]=cost[1]
            cost.append(0)
            memory.append(0)
            for i in range(3,len(cost)):
                memory[i]=min(memory[i-1],memory[i-2])+cost[i]
            res.append(memory[-1])
            return min(res)
if __name__ == '__main__':
    S=Solution()
    print(S.minCostClimbingStairs( [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))