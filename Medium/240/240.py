# @Date    : 23:38 07/19/2021
# @Author  : ClassicalPi
# @FileName: 240.py
# @Software: PyCharm
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        r,c = 0,n-1
        while r < m and c >= 0:
            if matrix[r][c]>target:
                c -= 1
            elif matrix[r][c]<target:
                r += 1
            else:
                return True
        return False