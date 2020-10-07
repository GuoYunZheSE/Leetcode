# @Date    : 10:51 09/27/2020
# @Author  : ClassicalPi
# @FileName: 5524.py
# @Software: PyCharm

class Solution:
    def minOperationsMaxProfit(self, customers: [int], boardingCost: int, runningCost: int) -> int:
        waiting=0
        profits=[0]

        if 4*boardingCost<runningCost:
            return -1

        for customer in customers:
            if customer+waiting>=4:
                profit=4*boardingCost-runningCost
                waiting=waiting+customer-4
            else:
                profit = (waiting+customer) * boardingCost - runningCost
                waiting=0
            last=profits[-1]
            profits.append(profit+last)

        while waiting>0:
            if waiting>=4:
                profit = 4 * boardingCost - runningCost
                last = profits[-1]
                profits.append(profit + last)
                waiting-=4
            else:
                profit = waiting * boardingCost - runningCost
                last = profits[-1]
                profits.append(profit + last)
                waiting=0
        return profits.index(max(profits))

if __name__ == '__main__':
    S=Solution()
    print(S.minOperationsMaxProfit([8,3],5,6))
