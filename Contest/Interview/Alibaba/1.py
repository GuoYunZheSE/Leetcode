# @Date    : 16:03 05/06/2020
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm

import sys


# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)

# n<m
# 1 1
# 2 (m-1)+1
# 3 (m-1)(m-1)+(m-1)+1
# 4 (m-1)(m-2)(m-3)+(m-1)(m-2)+(m-1)+1
#n>=m
#1 1
#2
class Solution():
    def helper(self,m,n):
        ans=1
        while n>0:
            ans*=(m-n)
            n-=1
        return ans
    def pingpong(self,n:int,m:int):
        if n==1:
            return 1
        elif n<=m:
            ans=0
            while n>1:
                ans+=self.helper(m,n-1)
                ans=ans%(10**9+7)
                n-=1
            ans+=1
            ans = ans % (10 ** 9 + 7)
            return ans
        else:
            ans=self.pingpong(m,m)
            for i in range(n-m):
                ans=(ans*m)%(10**9+7)
            return ans
if __name__ == '__main__':
    line=sys.stdin.readline().strip()
    a = line.split()
    s=Solution()
    print(s.pingpong(int(a[0]),int(a[1])))
