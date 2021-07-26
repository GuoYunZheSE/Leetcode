# @Date    : 19:03 04/27/2021
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm
# 1 2 4 8 16
#   1 2 4 8
#     1 2 4
#       1 2
#         1
import sys
class Solution:
    def cellNum(self,N)->(int,[]):
        res=[]
        for i in range(0,2**32+1):
            if i==N:
                binary=bin(i)[2:]
                day=len(binary)
                for j in range(len(binary)):
                    if binary[j]=="1":
                        res.append(j+1)
                return (day,res)

if __name__ == '__main__':
    S=Solution()
    case = int(sys.stdin.readline().strip())
    for i in range(case):
        N = int(sys.stdin.readline().strip())
        day,res=S.cellNum(N)
        print(day)
        s=""
        for each in res:
            s=s+f"{each} "
        s=s.strip()
        print(s)
