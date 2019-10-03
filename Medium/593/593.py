# 593. Valid Square
# Medium
#
# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
# The coordinate (x,y) of a point is represented by an integer array with two integers.
import math
class Solution:
    def validSquare(self, p1: [int], p2: [int], p3: [int], p4: [int]) -> bool:
        dict={1:p1,2:p2,3:p3,4:p4}
        if p1==p2 or p1==p3 or p1==p4 or p2==p3 or p2==p4 or p3==p4:
            return False
        maxdis=-1
        farpoint=1
        diss2=pow(p2[0]-p1[0],2)+pow(p2[1]-p1[1],2)
        if diss2>=maxdis:
            maxdis=diss2
            farpoint=2
        diss3=pow(p3[0]-p1[0],2)+pow(p3[1]-p1[1],2)
        if diss3>=maxdis:
            maxdis=diss3
            farpoint=3
        diss4=pow(p4[0]-p1[0],2)+pow(p4[1]-p1[1],2)
        if diss4>=maxdis:
            maxdis=diss4
            farpoint=4
        slope1_numerator=(dict[farpoint][1]-p1[1])
        slope1_denominator=(dict[farpoint][0]-p1[0])
        if slope1_denominator==0:
            slope1="INF"
        if slope1_numerator==0:
            slope1=0
        else:
            if slope1_denominator!=0:
                slope1=slope1_numerator/slope1_denominator
        rest=[2,3,4]
        rest.remove(farpoint)
        maxdis2=pow(dict[rest[0]][0]-dict[rest[1]][0],2)+pow(dict[rest[0]][1]-dict[rest[1]][1],2)

        slope2_numerator=(dict[rest[0]][1]-dict[rest[1]][1])
        slope2_denominator=(dict[rest[0]][0]-dict[rest[1]][0])
        if slope2_denominator==0:
            slope2="INF"
            if (slope1==0 and maxdis2==maxdis) and pow(dict[rest[0]][0]-p1[0],2)+pow(dict[rest[0]][1]-p1[1],2)==pow(dict[rest[0]][0]-dict[farpoint][0],2)+pow(dict[rest[0]][1]-dict[farpoint][1],2):
                return True
            else:
                return False
        if slope2_numerator==0:
            slope2=0
            if (slope1=="INF" and maxdis2==maxdis) and pow(dict[rest[0]][0]-p1[0],2)+pow(dict[rest[0]][1]-p1[1],2)==pow(dict[rest[0]][0]-dict[farpoint][0],2)+pow(dict[rest[0]][1]-dict[farpoint][1],2):
                return True
            else:
                return False
        if (slope1=="INF" or slope1==0):
            return False
        return(((slope1_numerator*slope2_numerator)/(slope2_denominator*slope1_denominator))==-1) and maxdis==maxdis2 and pow(dict[rest[0]][0]-p1[0],2)+pow(dict[rest[0]][1]-p1[1],2)==pow(dict[rest[0]][0]-dict[farpoint][0],2)+pow(dict[rest[0]][1]-dict[farpoint][1],2)

if __name__ == '__main__':

    p1 =[2, 1]
    p2 =[2, 2]
    p3 =[2, 0]
    p4=[0, 1]
    S=Solution()
    print(S.validSquare(p1,p2,p3,p4))
