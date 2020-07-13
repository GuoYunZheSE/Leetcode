#Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

#Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

class Solution:
    def __init__(self):
        self.squares=set()
        self.n=0
    def getSquare(self):
        for i in range(1,(self.n+1)//2):
            if i**2<=self.n:
                self.squares.add(i**2)
    def winnerSquareGame(self, n: int) -> bool:
        res=self.squares
        while
