# @Date    : 12:32 03/12/2020
# @Author  : ClassicalPi
# @FileName: DoubleWay.py
# @Software: PyCharm
import sys
class solution:
    def __init__(self):
        self.res=0
        self.first=[]
        self.length=0
    def DFS(self,x: int, y: int):
        if x == 1 and y == self.length - 1:
            self.res += 1
            return self.res
        if y < self.length - 1 and self.first[x][y + 1] != 'X':
            self.DFS(x, y + 1)
        if x == 1 and y < self.length - 1 and self.first[x - 1][y + 1] != 'X':
            self.DFS(x - 1, y + 1)
        if x == 0 and y < self.length - 1 and self.first[x + 1][y + 1] != 'X':
            self.DFS(x + 1, y + 1)


if __name__ == '__main__':
    N=int(input())
    first=[[],[]]
    first[0]=input()
    first[1]=input()
    # N=5
    # first=["..X.X","XX..."]

    s=solution()
    s.first=first
    s.length=N
    s.DFS(0,0)
    print(s.res)