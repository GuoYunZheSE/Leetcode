# @Date    : 19:54 04/04/2021
# @Author  : ClassicalPi
# @FileName: 20210404_5.py
# @Software: PyCharm
import sys
class Solution:
    def physical_class(self,n:int,m:int,w:[int]):
        for i in range(2**n,2**(n+1)):
            sum=0
            count=0
            for index,val in enumerate(bin(i)[3:]):
                if val=='1':
                    sum+=w[index]
                    count+=1
            if sum!=0 and sum%m==0:
                return count
        return -1

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    S = Solution()
    for i in range(n):
        nn,m = sys.stdin.readline().strip().split(" ")
        nn=int(nn)
        m=int(m)
        line = sys.stdin.readline().strip()
        w = list(map(int, line.split(" ")))
        print(S.physical_class(nn,m,w))