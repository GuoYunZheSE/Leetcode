import sys
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices)==0:
            return 0
        buyPrice=prices[0]
        ans=0
        for i in range(0,len(prices)):
            ans=max(ans,prices[i]-buyPrice)
            if prices[i]<buyPrice:
                buyPrice=prices[i]
        return ans

if __name__ == '__main__':
    nums=[7,6,4,3,1]
    s=Solution()
    print(s.maxProfit(nums))