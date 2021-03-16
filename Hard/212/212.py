# @Date    : 15:49 03/16/2021
# @Author  : ClassicalPi
# @FileName: 212.py
# @Software: PyCharm
class Solution(object):
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        def preCheck(word:str):
            preDict = {}

            for i in word:
                if i in preDict:
                    preDict[i] += 1
                else:
                    preDict[i] = 1

            for i in board:
                for j in i:
                    if j in preDict and preDict[j] > 0: preDict[j] -= 1
            for i in preDict.values():
                if i > 0: return False
            return True
        res=[]
        for word in words:
            if not preCheck(word): continue
            self.word = word
            self.found = False
            for row in range(len(board)):
                for col in range(len(board[0])):
                    self.visited = []
                    self.visitedSet = set()
                    self.dfs(board, row, col, 0)
                    if self.found:
                        res.append(word)
                        break
                if self.found:
                    break
            continue
        return res

    def dfs(self, board, row, col, i):

        if i == len(self.word):
            self.found = True

        if not self.found and row >= 0 and col >= 0 and row < len(board) and col < len(board[0]) and board[row][col] == \
                self.word[i] and (row, col) not in self.visitedSet:
            self.visited += [(row, col)]
            self.visitedSet.add((row, col))
            self.dfs(board, row + 1, col, i + 1)
            self.dfs(board, row - 1, col, i + 1)
            self.dfs(board, row, col + 1, i + 1)
            self.dfs(board, row, col - 1, i + 1)

            if not self.found:
                self.visitedSet.remove(self.visited.pop())
if __name__ == '__main__':
    S=Solution()
    print(S.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))
