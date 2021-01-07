# @Date    : 20:49 01/05/2021
# @Author  : ClassicalPi
# @FileName: 48.py
# @Software: PyCharm
import copy
class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        temp=copy.deepcopy(matrix)
        for row_index,row in enumerate(temp[::-1]):
            for column_index,column in enumerate(row):
                matrix[column_index][row_index]=column
if __name__ == '__main__':
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    S=Solution()
    S.rotate(matrix)
    print(matrix)