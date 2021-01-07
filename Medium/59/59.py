# @Date    : 18:45 01/07/2021
# @Author  : ClassicalPi
# @FileName: 59.py
# @Software: PyCharm
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        matrix=[[0 for a in range(n)] for b in range(n)]

        left_border,top_border=0,0
        right_border,bottom_border=n,n

        count=1
        direction=1

        while count<=n*n:
            if direction==1:
                for i in range(left_border,right_border):
                    matrix[top_border][i]=count
                    count+=1
                top_border+=1
                direction=2

            if direction==2:
                for i in range(top_border,bottom_border):
                    matrix[i][right_border-1]=count
                    count+=1
                right_border-=1
                direction=3

            if direction==3:
                for i in range(right_border-1,left_border-1,-1):
                    matrix[bottom_border-1][i]=count
                    count+=1
                bottom_border-=1
                direction=4

            if direction==4:
                for i in range(bottom_border-1,top_border-1,-1):
                    matrix[i][left_border]=count
                    count+=1
                left_border+=1
                direction=1

        return matrix
if __name__ == '__main__':
    S=Solution()
    print(S.generateMatrix(3))