# @Date    : 15:06 03/15/2021
# @Author  : ClassicalPi
# @FileName: 79.py
# @Software: PyCharm
class Solution:
    def find(self,row:int,column:int,target:[str],used:[],board: [[str]],res:[]):
        points=[[row,column-1],[row,column+1],[row-1,column],[row+1,column],[row,column]]
        points=[point for point in points if 0<=point[0]<len(board) and 0<=point[1]<len(board[0])]
        for point in points:
            temp=target.copy()
            if point not in used and board[point[0]][point[1]]==target[-1] and not res:
                temp.pop()
                if not temp:
                    res.append(point)
                    return True
                self.find(point[0],point[1],temp,used+[point],board,res)
        return False
    def exist(self, board: [[str]], word: str) -> bool:
        def preCheck():
            preDict = {}

            for i in word:
                if i in preDict: preDict[i]+=1
                else: preDict[i] = 1

            for i in board:
                for j in i:
                    if j in preDict and preDict[j]>0: preDict[j]-=1
            for i in preDict.values():
                if i>0: return False
            return True
        # if not preCheck(): return False
        res=[]
        for row in range(len(board)):
            for column in range(len(board[row])):
                used = []
                targets = list(word)
                targets.reverse()
                self.find(row,column,targets,used,board,res)
                if res:
                    return True
        return False
if __name__ == '__main__':
    S=Solution()
    print(S.exist([["a","b"],["c","d"]],"abcd")==False)
    print(S.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")==True)
    print(S.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")==True)
    print(S.exist([["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]],"AAAAAAAAAAAAAAB"))
