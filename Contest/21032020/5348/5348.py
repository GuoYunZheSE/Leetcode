# @Date    : 15:30 03/21/2020
# @Author  : ClassicalPi
# @FileName: 5348.py
# @Software: PyCharm

class Solution:
    def findTheDistanceValue(self, arr1: [int], arr2: [int], d: int) -> int:
        res=0
        for i in arr1:
            mark=True
            for j in arr2:
                if abs(i-j)<=d:
                    mark=False
                    break
            if mark:
                res+=1
        return res

if __name__ == '__main__':
    S=Solution()
    a1=[2,1,100,3]
    a2=[-5,-2,10,-3,7]
    d = 6
    print(S.findTheDistanceValue(a1,a2,d))