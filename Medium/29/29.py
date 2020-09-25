# @Date    : 20:25 09/25/2020
# @Author  : ClassicalPi
# @FileName: 29.py
# @Software: PyCharm

class Solution:
    # def divide(self, dividend: int, divisor: int) -> int:
    #     signed = False
    #     if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
    #         signed = True
    #     dividend = abs(dividend)
    #     divisor = abs(divisor)
    #     if dividend==0 or dividend<divisor:
    #         return 0
    #     else:
    #         ans=0
    #         while dividend-divisor>=0:
    #             dividend-=divisor
    #             ans+=1
    #
    #         if signed:
    #             return -ans
    #         else:
    #             return ans
    def divide(self, A, B):
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res

if __name__ == '__main__':
    S=Solution()
    print(S.divide(-7,-2))