# @Date    : 10:32 07/19/2020
# @Author  : ClassicalPi
# @FileName: 5464.py
# @Software: PyCharm

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk=numBottles
        emptyBottles=numBottles

        while emptyBottles>=numExchange:
            numBottles=emptyBottles//numExchange

            emptyBottles=emptyBottles%numExchange
            emptyBottles+=numBottles

            drunk+=numBottles
        return drunk
if __name__ == '__main__':
    S=Solution()
    print(S.numWaterBottles(9,3))
    print(S.numWaterBottles(15,4))
    print(S.numWaterBottles(5,5))
    print(S.numWaterBottles(1, 2))