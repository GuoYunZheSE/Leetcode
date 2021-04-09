# @Date    : 20:00 04/09/2021
# @Author  : ClassicalPi
# @FileName: 130.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.captured=set()
        self.escaped=set()
        self.escape=False
    def DFS(self,row:int,column:int,path:set,board: [[str]]):
        if board[row][column]=="O":
            path.add((row,column))
            if row in [0,len(board)-1] or column in [0,len(board[0])-1]:
                self.escape=True
            if row-1>=0:
                if (row-1,column) not in path:
                    self.DFS(row-1,column,path,board)
            if row+1<=len(board)-1:
                if (row + 1, column) not in path:
                    self.DFS(row+1,column,path,board)
            if column-1>=0:
                if (row , column-1) not in path:
                    self.DFS(row,column-1,path,board)
            if column+1<=len(board[0])-1:
                if (row , column+1) not in path:
                    self.DFS(row,column+1,path,board)
        return path

    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(0,len(board)):
            for column in range(0,len(board[0])):
                if not((row,column) in self.escaped or (row,column) in self.captured):
                    path=self.DFS(row,column,set(),board)
                    if self.escape:
                        self.escaped.update(path)
                        self.escape=False
                    else:
                        self.captured.update(path)
        for each in self.captured:
            board[each[0]][each[1]]='X'

if __name__ == '__main__':
    S=Solution()
    d=[["O","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    S.solve(d)
    print(d)