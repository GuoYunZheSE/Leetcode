# @Date    : 15:42 04/22/2021
# @Author  : ClassicalPi
# @FileName: 200.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.res=0
        self.grid=[]
        self.points=set()
    def DFS(self, row:int, column:int):
        if self.grid[row][column]=='1':
            self.points.add((row,column))
            if row-1>=0 and (row-1,column) not in self.points:
                self.DFS(row - 1, column)
            if row+1<=len(self.grid)-1 and (row+1,column) not in self.points:
                self.DFS(row + 1, column)
            if column-1>=0 and (row,column-1) not in self.points:
                self.DFS(row,column-1)
            if column+1<=len(self.grid[0])-1 and (row,column+1) not in self.points:
                self.DFS(row,column+1)
            return True
        else:
            return False
    def numIslands(self, grid: [[str]]) -> int:
        self.grid=grid
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if (row,column) not in self.points:
                    if self.DFS(row,column):
                        self.res+=1
        return self.res

if __name__ == '__main__':
    S=Solution()
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    print(S.numIslands(grid))