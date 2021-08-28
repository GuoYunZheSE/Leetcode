# @Date    : 21:52 08/16/2021
# @Author  : ClassicalPi
# @FileName: 64.py
# @Software: PyCharm
import sys
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        cache  = {}
        def recur(cur_row:int,cur_column:int,row:int,column:int):
            if cache.get((cur_row,cur_column),-1) != -1:
                return cache[(cur_row,cur_column)]
            if cur_row == row - 1 and cur_column == column - 1:
                return grid[cur_row][cur_column]
            else:
                ret = []
                cur_val = grid[cur_row][cur_column]
                if cur_column + 1 < column:
                    ret.append(recur(cur_row,cur_column+1,row,column)+ cur_val)
                if cur_row + 1 < row:
                    ret.append(recur(cur_row+1,cur_column,row,column)+ cur_val)
                # if cur_row + 1 < row and cur_column + 1 < column:
                #     ret.append(recur(cur_row + 1, cur_column + 1, row, column)+ cur_val)
                cache[(cur_row,cur_column)] = min(ret)
                return min(ret)
        return recur(0,0,len(grid),len(grid[0]))
if __name__ == '__main__':
    S = Solution()
    print(S.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
