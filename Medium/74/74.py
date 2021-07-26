# @Date    : 00:48 07/23/2021
# @Author  : ClassicalPi
# @FileName: 74.py
# @Software: PyCharm
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        def biSearch(matrix:[[int]],l:int,r:int,target:int):

            mid =int(l+(r-l)/2)
            mid_row = mid // len(matrix[0])
            mid_column = mid % len(matrix[0])
            if l > r:
                return -1
            if matrix[mid_row][mid_column] < target:
                return biSearch(matrix,mid+1,r,target)
            if matrix[mid_row][mid_column] > target:
                return biSearch(matrix,l,mid-1,target)
            if matrix[mid_row][mid_column] == target:
                return mid
            return -1

        if biSearch(matrix,0,len(matrix)*len(matrix[0])-1,target)!=-1:
            return True
        return False

if __name__ == '__main__':
    S=Solution()
    print(S.searchMatrix([[1]],2))