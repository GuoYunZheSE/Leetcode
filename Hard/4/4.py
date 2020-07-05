# @Date    : 20:42 07/05/2020
# @Author  : ClassicalPi
# @FileName: 4.py
# @Software: PyCharm

# Index: 0 1 2 3 4 5 6
# Num1:  1 3 4 5 6
# Divi: 0 1 2 3 4 5 6
# Num1:  2 4 5 6 9 8

import sys
class Solution:
    def findMedianSortedArrays(self, nums1:[int], nums2:[int]) -> float:
        Longer=nums1
        Shorter=nums2
        if len(Longer)<len(Shorter):
            Longer,Shorter=Shorter,Longer
        Left=0
        Right=len(Shorter)
        while Left<=Right:
            DividePosition_Shorter=(Left+Right)//2
            DividePosition_Longer=(len(Longer)+len(Shorter)+1)//2-DividePosition_Shorter
            Shorter_Max = 0
            Longer_Max = 0
            Shorter_Min = 0
            Longer_Min = 0
            if DividePosition_Shorter==0:
                Shorter_Max=-sys.maxsize
                Longer_Max=Longer[-1]
                Shorter_Min=Shorter[0]
                Longer_Min=Longer[0]
            elif DividePosition_Shorter==len(Shorter):
                Shorter_Max=Shorter[-1]
                Longer_Max=Longer[DividePosition_Longer-1]
                Shorter_Min=sys.maxsize
                Longer_Min=Longer[DividePosition_Longer]
            else:
                Shorter_Max=Shorter[DividePosition_Shorter-1]
                Longer_Max=Longer[DividePosition_Longer-1]
                Shorter_Min=Shorter[DividePosition_Shorter]
                Longer_Min=Longer[DividePosition_Longer]

            if Shorter_Max<=Longer_Min and Longer_Max<=Shorter_Min:
                left_max=max(Shorter_Max,Longer_Max)
                right_min=min(Shorter_Min,Longer_Min)
                if (len(Shorter)+len(Longer))%2==0:
                    return (left_max+right_min)/2
                else:
                    return left_max
            elif Shorter_Max>Longer_Min:
                Right=DividePosition_Shorter-1
            else:
                Left=DividePosition_Shorter+1
if __name__ == '__main__':
    S=Solution()
    nums1 = [1, 2]
    nums2 = [3,4]
    print(S.findMedianSortedArrays(nums1,nums2))


