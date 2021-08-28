# @Date    : 15:09 08/21/2021
# @Author  : ClassicalPi
# @FileName: 4.py
# @Software: PyCharm
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算最小航行费用
# @param input int整型二维数组 二维网格
# @return int整型
#
import sys
class Solution:
    def minSailCost(self , input ):
        cache = {}
        costMap = {
            0:2,
            1:1,
            2:sys.maxsize
        }
        def recur(cur_row:int,cur_column:int,row:int,column:int):
            if cur_row == row - 1 and cur_column == column - 1:
                return costMap[input[cur_row][cur_column]]
            if input[cur_row][cur_column] == 2 and not(cur_row == 0 and cur_column ==0):
                return sys.maxsize
            temp = 1
            if input[cur_row][cur_column] == 0:
                temp = 2
            if cur_row == 0 and cur_column ==0:
                temp = 0
            ret = [sys.maxsize]
            if cur_row + 1 < row:
                if cache.get((cur_row+1,cur_column),-1) == -1:
                    res = recur(cur_row+1,cur_column,row,column)
                    cache[(cur_row+1,cur_column)] = res
                    ret.append(res)
                else:
                    ret.append(cache[(cur_row+1,cur_column)])
            if cur_column + 1 < column:
                if cache.get((cur_row,cur_column+1),-1) == -1:
                    res = recur(cur_row,cur_column+1,row,column)
                    cache[(cur_row,cur_column+1)] = res
                    ret.append(res)
                else:
                    ret.append(cache[(cur_row,cur_column+1)])
            return min(ret) + temp
        res = recur(0,0,len(input),len(input[0]))
        if res >= sys.maxsize:
            return -1
        # res -= costMap[input[0][0]]
        return res

if __name__ == '__main__':
    S = Solution()
    print(S.minSailCost([[2,1,1,1,0],[0,1,0,1,0],[1,1,2,1,1],[0,2,0,0,1]]))