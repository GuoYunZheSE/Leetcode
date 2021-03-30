# @Date    : 14:57 03/26/2021
# @Author  : ClassicalPi
# @FileName: 122.py
# @Software: PyCharm

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit=0
        for i in range(1,len(prices)):
            max_profit=(max_profit,max_profit+prices[i]-prices[i-1])
        return max_profit