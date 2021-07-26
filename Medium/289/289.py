# @Date    : 18:40 07/25/2021
# @Author  : ClassicalPi
# @FileName: 289.py
# @Software: PyCharm
class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Any live cell with fewer than two live neighbors dies as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        """
        temp = [[0 for i in range(len(board[0]) + 2)]]
        for row in board:
            temp.append([0] + row + [0])
        temp.append([0 for i in range(len(board[0]) + 2)])

        for row in range(1, len(temp) - 1):
            for column in range(1, len(temp[0]) - 1):
                res = sum([temp[row - 1][column - 1], temp[row - 1][column], temp[row - 1][column + 1],
                           temp[row][column - 1], temp[row][column + 1],
                           temp[row + 1][column - 1], temp[row + 1][column], temp[row + 1][column + 1]])
                if board[row - 1][column - 1] == 0:
                    if res == 3:
                        board[row - 1][column - 1] = 1
                else:
                    if res < 2:
                        board[row - 1][column - 1] = 0
                    elif res > 3:
                        board[row - 1][column - 1] = 0

if __name__ == '__main__':
    S=Solution()
    b = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    S.gameOfLife(b)
    print(b)