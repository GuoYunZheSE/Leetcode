# topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/
# The Python Solution of Problem:Smallest Number of Coins for Specified Value.
import sys
class SNC:
    def __init__(self,coins:list,value:int):
        self.Coin=coins
        self.Value=value
        self.Mins=[sys.maxsize]*(value+1)
    def findNumber(self)->int:
        self.Mins[0]=0
        for value in range(1,self.Value+1):
            for coin in self.Coin:
                if value>=coin:
                    self.Mins[value]=min(self.Mins[value],self.Mins[value-coin]+1)
        print(self.Mins)
        return self.Mins[self.Value]

if __name__ == '__main__':
    Coins=[1,3,5]
    Value=29
    S=SNC(Coins,Value)
    print(S.findNumber())

