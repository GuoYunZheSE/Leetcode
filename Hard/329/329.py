# @Date    : 23:20 08/09/2021
# @Author  : ClassicalPi
# @FileName: 329.py
# @Software: PyCharm
class Solution:
    def longestIncreasingPath(self, matrix: [[int]]) -> int:
        cache = {}
        def recur (row:int,column:int):
            res = [1]
            passed = set()
            nextRows = [row - 1, row + 1]
            nextColumns = [column - 1, column + 1]
            for nextRow in nextRows:
                if nextRow >= 0 and nextRow < len(matrix) and (nextRow,column) not in passed:
                    if matrix[nextRow][column] > matrix[row][column]:
                        if (nextRow, column) in cache:
                            res.append(cache[(nextRow, column)]+1)
                        else:
                            temp = recur(nextRow,column)
                            res.append(temp+1)
                            cache.setdefault((nextRow,column),temp)
                        passed.add(cache[(nextRow, column)])
            for nextColumn in nextColumns:
                if nextColumn >= 0 and nextColumn < len(matrix[0]) and (row,nextColumn) not in passed:
                    if matrix[row][nextColumn] > matrix[row][column]:
                        if (row,nextColumn) in cache:
                            res.append(cache[(row,nextColumn)]+1)
                        else:
                            temp = recur(row,nextColumn)
                            res.append(temp+1)
                            cache.setdefault((row,nextColumn),temp)
                        passed.add(cache[(row,nextColumn)])
            return max(res)
        ret = -1
        for row in range(0,len(matrix)):
            for column in range(0,len(matrix[0])):
                ret = max(ret,recur(row,column))
        return ret

if __name__ == '__main__':
    S = Solution()
    print(S.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))