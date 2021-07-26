# @Date    : 19:49 07/25/2021
# @Author  : ClassicalPi
# @FileName: 3.py
# @Software: PyCharm
import sys
class Solution:
    # A
    # A+B A*C
    # A+2B A*C+B A*C+B*C A*C^2
    # A+3B A*C+2B C(A+B)+B A*C^2+B (A+2B)*C A*C^2+B*C (A+B)*C^2 A*C^3
    def __init__(self,A:int,B:int,C:int,Q:int):
        self.A = A
        self.B = B
        self.C = C
        self.Q = Q
    def NextGeneration(self,s:set)->(set,bool):
        temp = set()
        for each in s:
            res1 = each+self.B
            res2 = each * self.C
            temp.add(each+self.B)
            temp.add(each * self.C)
            if res1 == self.Q or res2 == self.Q:
                return (temp,True)
        return (temp,False)
    def InfCheck(self):
        if self.C == 1:
            if (self.Q-self.A)%self.B == 0:
                print("1")
            else:
                print("0")
            return
        if self.Q==self.A:
            print("1")
            return
        else:
            ori = {self.A}
            s,res = self.NextGeneration(ori)
            while max(s)<self.Q:
                if res:
                    print("1")
                    return
                else:
                    s,res = self.NextGeneration(s)
                    if res:
                        print("1")
                        return
            print("0")
if __name__ == '__main__':
    # S=Solution(1,1,1,99999)
    # S.InfCheck()
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        S=Solution(values[0],values[1],values[2],values[3])
        S.InfCheck()