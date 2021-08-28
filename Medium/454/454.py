# @Date    : 15:56 08/15/2021
# @Author  : ClassicalPi
# @FileName: 454.py
# @Software: PyCharm
class Solution:
    def fourSumCount(self, A: [int], B: [int], C: [int], D: [int]) -> int:
        res = 0
        tableAB = {}
        tableCD = {}
        for numA in A:
            for numB in B:
                tableAB[numA+numB] = tableAB.get(numA+numB,0) + 1
        for numC in C:
            for numD in D:
                tableCD[numC+numD] = tableCD.get(numC+numD,0) + 1
        for key,val in tableAB.items():
            if (0-key) in tableCD:
                res += (val * tableCD[0-key])
        return res

if __name__ == '__main__':
    S = Solution()
    print(S.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))