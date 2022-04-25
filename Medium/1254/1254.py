# @Date    : 17:47 04/24/2022
# @Author  : ClassicalPi
# @FileName: 1254.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.passed = set()
    def closedIsland(self, grid: [[int]]) -> int:
        width, length = len(grid), len(grid[0])
        def check(row:int, column:int):
            self.passed.add((row, column))
            if (row == 0 or row == width - 1) or (column == 0 or column == length - 1):
                if grid[row][column] == 1:
                    return True
                else:
                    return False
            res = []
            if (row + 1, column) not in self.passed and grid[row + 1][column] == 0:
                res.append(check(row + 1, column))
            if (row - 1, column) not in self.passed and grid[row - 1][column] == 0:
                res.append(check(row - 1, column))
            if (row, column + 1) not in self.passed and grid[row][column + 1] == 0:
                res.append(check(row, column + 1))
            if (row, column - 1) not in self.passed and grid[row][column - 1] == 0:
                res.append(check(row, column - 1))
            return all(res)

        ret = 0
        if width <= 2 or length <= 2:
            return ret
        for row in range(1,width - 1):
            for column in range(1, length - 1):
                if (row,column) not in self.passed and grid[row][column] == 0:
                    if check(row,column):
                        ret += 1
        return ret

if __name__ == '__main__':
    S = Solution()
    print(S.closedIsland([[0,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,1],[1,0,1,0,0,1,0,1],[1,0,0,0,0,1,0,1],[1,0,0,1,0,1,0,1],[1,1,0,1,0,0,0,1],[1,0,0,0,0,0,0,1],[0,1,1,1,1,1,1,1]]))
