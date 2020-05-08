# @Date    : 21:08 04/26/2020
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm
import sys
import math
class Area():
    def solution(self):
        testcases=int(sys.stdin.readline().strip())
        for i in range(testcases):
            line = sys.stdin.readline().strip()
            values = list(map(int, line.split()))
            A,B,C=values[0],values[1],values[2]
            delta=(2*B*C-2*A)**2-4*B**2*C**2
            if delta<=0:
                print(0)
            else:
                x1=0
                y1=0
                y2=(-(2*B*C-2*A)+math.sqrt(delta))/(2*B**2)
                y3=(-(2*B*C-2*A)-math.sqrt(delta))/(2*B**2)
                x2=B*y2+C
                x3=B*y3+C
                area=-(y2-y1)/((x2-x1)*(x2-x1))*((x3-x2)*(x3-x2)*(x3-x2))/6
                print(abs(area))
if __name__ == '__main__':
    a=Area()
    a.solution()