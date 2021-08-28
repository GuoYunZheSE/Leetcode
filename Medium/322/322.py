# @Date    : 23:15 07/31/2021
# @Author  : ClassicalPi
# @FileName: 322.py
# @Software: PyCharm
import sys
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:

        if amount == 0 :
            return 0
        if amount < min(coins):
            return -1

        res = {0:0}
        for coin in  coins:
            res[coin] = 1

        for i in range(1,amount+1):
            res[i] = sys.maxsize
            for coin in coins:
                if i - coin >= 0:
                    if res.get(i-coin, -1) != -1:
                        res[i] = min(res[i],res[i-coin] + 1)

        if res[amount] == sys.maxsize:
            return -1
        return res[amount]
if __name__ == '__main__':
    S=Solution()
    print(S.coinChange([1,2,5],11))
    print(S.coinChange([1],0))
    print(S.coinChange([2147483647],2))
    print(S.coinChange([1,2147483647],2))