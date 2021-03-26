# @Date    : 11:28 03/26/2021
# @Author  : ClassicalPi
# @FileName: 118.py
# @Software: PyCharm
class Solution:
    def generate(self, numRows: int) -> [[int]]:
        res=[]
        for i in range(0,numRows):
            temp=[]
            for index in range(i+1):
                if index==0 or index==i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][index-1]+res[i-1][index])
            res.append(temp)
        return res
if __name__ == '__main__':
    S=Solution()
    print(S.generate(1000))