import sys
class Solution:
    def __init__(self):
        self.rows=0
        self.columns=0
        self.matrix=[[]]

    def BFS(self,r:int,c:int):
        hip=1
        Stop=False
        while not Stop:
            for rowChange in range(-hip,hip+1):
                if r+rowChange>=0 and r+rowChange<self.rows:
                    if c+abs(hip-abs(rowChange))<self.columns:
                        if self.matrix[r+rowChange][c+abs(hip-abs(rowChange))]==0:
                            return hip
                    if c-abs(hip-abs(rowChange))>=0:
                        if self.matrix[r+rowChange][c-abs(hip-abs(rowChange))]==0:
                            return hip
            hip+=1

    def updateMatrix(self, matrix: [[int]]) -> [[int]]:
        self.rows=len(matrix)
        self.columns=len(matrix[0])
        self.matrix=matrix
        res=matrix.copy()
        for eachRow in range(0,self.rows):
            for eachColumn in range(0,self.columns):
                if self.matrix[eachRow][eachColumn]!=0:
                    res[eachRow][eachColumn]=self.BFS(eachRow,eachColumn)
        return res

if __name__ == '__main__':
    nums=[[0,0,0],[0,1,0],[0,0,0]]

    S=Solution()
    print(S.updateMatrix(nums))
