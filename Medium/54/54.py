# @Date    : 16:23 01/07/2021
# @Author  : ClassicalPi
# @FileName: 54.py
# @Software: PyCharm
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:

        left_border,top_border=0,0
        right_border,bottom_border=len(matrix[0]),len(matrix)

        capacity=len(matrix)*len(matrix[0])
        res=[]

        # TR:to right, TB:to bottom, TL:to left, TT:to top
        direction="TR"
        while len(res)<capacity:
            print(res)
            if direction=="TR":
                for i in range(left_border,right_border):
                    res.append(matrix[top_border][i])
                top_border+=1
                direction="TB"
                continue
            if direction=="TB":
                for eachrow in range(top_border,bottom_border):
                    res.append(matrix[eachrow][right_border-1])
                right_border -= 1
                direction = "TL"
                continue
            if direction=="TL":
                for each in range(right_border-1,left_border-1,-1):
                    res.append(matrix[bottom_border-1][each])
                bottom_border-=1
                direction = "TT"
                continue
            if direction=="TT":
                for each in range(bottom_border-1,top_border-1,-1):
                    res.append(matrix[each][left_border])
                left_border+=1
                direction = "TR"
                continue
        return res
if __name__ == '__main__':
    S=Solution()
    print(S.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))