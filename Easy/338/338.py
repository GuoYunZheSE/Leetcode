# @Date    : 00:14 08/31/2021
# @Author  : ClassicalPi
# @FileName: 338.py
# @Software: PyCharm
class Solution:
    def countBits(self, n: int) -> [int]:
        res = [0 for i in range(n)]
        for i in range(0,n):
            res[i] = res[i//2] + i%2
        return res
if __name__ == '__main__':
    S = Solution()
    print(S.countBits(10))