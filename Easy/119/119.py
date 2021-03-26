# @Date    : 14:25 03/26/2021
# @Author  : ClassicalPi
# @FileName: 119.py
# @Software: PyCharm
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        res=[]
        for i in range(0,rowIndex+1):
            temp=[]
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j-1]+res[i-1][j])
            res.append(temp)
        return res[-1]
if __name__ == '__main__':
    S=Solution()
    print(S.getRow(3))