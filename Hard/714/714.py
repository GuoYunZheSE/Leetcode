# @Date    : 08:45 03/28/2021
# @Author  : ClassicalPi
# @FileName: 714.py
# @Software: PyCharm
# class Solution:
#     def maxProfit(self, prices: [int]) -> int:
#         valley=[]
#         peeks=[]
#         i=0
#         while i <len(prices)-1:
#             while i<len(prices)-1 and prices[i]>=prices[i+1]:
#                 i+=1
#             valley.append(i)
#             while i<len(prices)-1 and prices[i]<=prices[i+1]:
#                 i+=1
#             peeks.append(i)
#         profits=[]
#         for peek in peeks:
#             for valle in valley:
#                 if peek>valle:
#                     profits.append((valle,peek,prices[peek]-prices[valle]))
#         res=[]
#         for i in range(0,len(profits)-1):
#             for j in range(i+1,len(profits)):
#                 temp=profits[i][2]
#                 if profits[i][1]<=profits[j][0]:
#                     temp+=profits[j][2]
#                 res.append(temp)
#         res.sort()
#         if len(res)==0:
#             if len(profits)==1:
#                 return profits[0][2]
#             if len(profits)==0:
#                 return 0
#         else:
#             return max(res)
import sys
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        firstBuyPrice=sys.maxsize
        secondBuyPrice=-sys.maxsize
        firstSellProfit=-sys.maxsize
        secondSellProfit=-sys.maxsize
        for price in prices:
            firstBuyPrice=min(firstBuyPrice,price)
            firstSellProfit=max(firstSellProfit,price-firstBuyPrice)
            secondBuyPrice=max(secondBuyPrice,firstSellProfit-price)
            secondSellProfit=max(secondSellProfit,secondBuyPrice+price)
        return secondSellProfit
if __name__ == '__main__':
    S=Solution()
    print(S.maxProfit([1,2,3,4,5]))
    print(S.maxProfit([3,3,5,0,0,3,1,4]))
    print(S.maxProfit([1,2,4,2,5,7,2,4,9,0]))
    print(S.maxProfit([7,6,4,3,1]))
    print(S.maxProfit([1,4,2]))
