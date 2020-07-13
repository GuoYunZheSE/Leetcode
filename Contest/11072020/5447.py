# @Date    : 23:38 07/11/2020
# @Author  : ClassicalPi
# @FileName: 5447.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.squares=set()
        self.n=0
    def getSquare(self):
        for i in range(0,10000):
            if i**2<=self.n:
                self.squares.add(i**2)
    def winnerSquareGame(self,n: int):
        self.n=n
        self.getSquare()
        for i in range(0,self.n):
            self.addSquare(i)
        return self.addSquare(self.n)
    def addSquare(self,n) -> bool:
        res=list(self.squares)

        if n in self.squares:
            return True
        else:
            for i in res:
                if i<=n:
                    if (n-i) in self.squares:
                        return False
                else:
                    break
            self.squares.add(n)
            return True

if __name__ == '__main__':
    S=Solution()
    print(S.winnerSquareGame(6))
    print(S.winnerSquareGame(2))
    print(S.winnerSquareGame(3))
    print(S.winnerSquareGame(4))
    print(S.winnerSquareGame(7))
    print(S.winnerSquareGame(10000))
