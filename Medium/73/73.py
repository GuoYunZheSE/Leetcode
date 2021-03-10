# @Date    : 15:35 03/10/2021
# @Author  : ClassicalPi
# @FileName: 73.py
# @Software: PyCharm
class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        columns=len(matrix[0])
        zero_rows=set()
        zero_columns=set()
        for row in range(rows):
            for column in range(columns):
                if matrix[row][column]==0:
                    zero_rows.add(row)
                    zero_columns.add(column)
        for row in range(rows):
            for column in range(columns):
                if row in zero_rows or column in zero_columns:
                    matrix[row][column]=0
