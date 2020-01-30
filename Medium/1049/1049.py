import sys
class Solution:
    def lastStoneWeightII(self, A):
        dp = {0}
        sumA = sum(A)
        for a in A:
            dp |= {a + i for i in dp}
        return min(abs(sumA - i - i) for i in dp)


if __name__ == '__main__':
    stones=[2,7,4,1,8,1]
    S=Solution()
    print(S.lastStoneWeightII(stones))
