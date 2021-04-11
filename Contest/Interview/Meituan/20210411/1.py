# @Date    : 10:03 04/11/2021
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm
import sys
class Solution:
    def buyHouse(self,houses:list,k:int):
        location=houses.index(0)
        prices={}
        for i in range(location+1,len(houses)):
            if houses[i]<=k:
                prices.setdefault(i-location,(houses[i],i))
        for i in range(1,location):
            if houses[i]<=k:
                if prices.get(location-i,(-1,-1))!=(-1,-1):
                    if houses[i]<prices[location-i][0]:
                        prices[location-i]=(houses[i],i)
                else:
                    prices.setdefault(location-i, (houses[i],i))
        k=sorted(list(prices.keys()))
        return prices[k[0]][1]+1
if __name__ == "__main__":
    n,k = sys.stdin.readline().strip().split(" ")
    n,k=int(n),int(k)
    S = Solution()
    line = sys.stdin.readline().strip()
    houses = list(map(int, line.split(" ")))
    print(S.buyHouse(houses,k))