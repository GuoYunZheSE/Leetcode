# @Date    : 15:37 03/21/2020
# @Author  : ClassicalPi
# @FileName: 5349.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.reservedSeats=[]
        self.last=0
    def checkRow(self,rowID:int)->int:
        res=0
        row=[0 for i in range(10)]
        for i in range(self.last,len(self.reservedSeats)):
            if self.reservedSeats[i][0]-1==rowID:
                row[self.reservedSeats[i][1]-1]=1
                self.last+=1
            else:
                break
        if sum(row)==0:
            return 2
        if sum(row[1:5])==0:
            row[4]=1
            res+=1
        if sum(row[3:7])==0:
            row[6]=1
            res+=1
        if sum(row[5:9])==0:
            res+=1
        return res
    #
    # def checkRow_2(self,rowID:int)->int:
    #

    def maxNumberOfFamilies(self, n: int, reservedSeats: [[int]]) -> int:
        res=0
        self.reservedSeats=sorted(reservedSeats,key=lambda  x:x[0])
        for i in range(0,n):
            if self.last==len(self.reservedSeats):
                res+=(n-1)*2
                return res
            res+=self.checkRow(i)
        return res

if __name__ == '__main__':
    s=Solution()
    n = 10**6
    reservedSeats =  [[4,3],[1,4],[4,6],[1,7]]
    print(s.maxNumberOfFamilies(n,reservedSeats))