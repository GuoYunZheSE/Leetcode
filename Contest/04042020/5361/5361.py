# @Date    : 23:32 04/04/2020
# @Author  : ClassicalPi
# @FileName: 5361.py
# @Software: PyCharm

class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xc=(float((x1+x2)/2))
        yc=(float((y1+y2)/2))
        h=[x2-xc,y2-yc]
        v=[abs(x_center-xc),abs(y_center-yc)]
        u=[0,0]
        for i in range(0,2):
            if v[i]-h[i]>0:
                u[i]=v[i]-h[i]
        return (u[0]**2+u[1]**2)<=(radius**2)

if __name__ == '__main__':
    s=Solution()
    print(s.checkOverlap(1,1,1,1,-3,2,-1))