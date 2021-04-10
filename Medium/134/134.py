# @Date    : 14:38 04/10/2021
# @Author  : ClassicalPi
# @FileName: 134.py
# @Software: PyCharm
class Solution:
    def check(self,index:int,remain:[])->bool:
        now=0
        for i in range(index,len(remain)):
            now+=remain[i]
            if not now>=0:
                return False
        for j in range(0,index):
            now+=remain[j]
            if not now>=0:
                return False
        return True
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        remain=[gas[a]-cost[a] for a in range(len(gas))]
        for index,val in enumerate(remain):
            if val>=0:
                valid=self.check(index,remain)
                if valid:
                    return index
        return -1