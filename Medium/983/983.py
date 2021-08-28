# @Date    : 16:03 08/01/2021
# @Author  : ClassicalPi
# @FileName: 983.py
# @Software: PyCharm

import sys
class Solution:
    def mincostTickets(self, days: [int], costs: [int]) -> int:
        res = [0 for i in range(0, days[-1]+1)]
        daySet = set(days)
        for day in range(1,days[-1]+1):
            if day in daySet:
                res[day] = min(res[max(day-1),0]+costs[0],res[max(day-7),0]+costs[1],res[max(day-30),0]+costs[2])
            else:
                res[day] = res[day-1]
        return res[-1]
if __name__ == '__main__':
    S=Solution()
    print(S.mincostTickets([1,4,6,7,8,20],[2,7,15]))