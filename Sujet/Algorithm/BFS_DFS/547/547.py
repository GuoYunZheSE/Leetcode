class Solution:
    def __init__(self):
        self.passed=set()
        self.rows=0
        self.columns=0
        self.matrix=[[]]

    def DFS(self,r:int,c:int):

        if r not in self.passed:
            self.passed.add(r)

        if c<self.columns-1:
            self.DFS(r,c+1)

        if self.matrix[r][c]==1:
            if c not in self.passed:
                self.DFS(c,0)



    def findCircleNum(self, M: [[int]]) -> int:
        self.rows=len(M)
        self.columns=len(M[0])
        self.matrix=M
        count = 0
        for eachRow in range(0,len(M)):
            if eachRow not in self.passed:
                count+=1
                self.passed.add(eachRow)
                self.DFS(eachRow,eachRow)
        return count

if __name__ == '__main__':
    M=[[1,1,0],[1,1,1],[0,1,1]]
    S=Solution()
    print(S.findCircleNum(M))