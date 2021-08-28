# @Date    : 00:53 08/28/2021
# @Author  : ClassicalPi
# @FileName: 96.py
# @Software: PyCharm
class Solution:
    def numTrees(self, n: int) -> int:
        res = [0 for i in range(0,n+1)]
        res[0] = 1
        for i in range(1,n+1):
            for j in range(0,i):
                res[i] += res[j] * res[i-j-1]
        return res[n]
if __name__ == '__main__':
    S = Solution()
    print(S.numTrees(10))