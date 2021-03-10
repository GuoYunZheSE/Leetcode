# @Date    : 13:47 03/10/2021
# @Author  : ClassicalPi
# @FileName: 70.py
# @Software: PyCharm
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            memory=[0 for i in range(n)]
            memory[0]=1
            memory[1]=2
            for i in range(2,n):
                memory[i]=memory[i-1]+memory[i-2]
            return memory[n-1]
if __name__ == '__main__':
    S=Solution()
    print(S.climbStairs(3))