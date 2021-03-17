# @Date    : 20:48 03/16/2021
# @Author  : ClassicalPi
# @FileName: 91.py
# @Software: PyCharm
class Solution:

    def numDecodings(self, s: str) -> int:

        memo=[0 for i in range(len(s)+1)]
        memo[0]=1
        memo[1]=0 if s[0]=='0' else 1

        if not s:
            return 0

        for i in range(2,len(s)+1):
            if 0<int(s[i-1:i])<=9:
                memo[i]+=memo[i-1]
            if 10<=int(s[i-2:i])<=26:
                memo[i]+=memo[i-2]
        return memo[-1]
if __name__ == '__main__':
    S=Solution()
    print(S.numDecodings("12"))
    print(S.numDecodings("226"))
    print(S.numDecodings("27212"))
    print(S.numDecodings("06"))
    print(S.numDecodings("232335"))