# Runtime: 60 ms, faster than 16.22% of Python3 online submissions for Base 7.
class Solution:
    def convertToBase7(self,num):
        """
        :type num: int
        :rtype: str
        """
        mark = False
        A=''
        if num<0:
            num=abs(num)
            mark=True
        while num>=7:
            A=A+str(num%7)
            num=int(num/7)
        A = A +str(num)
        if mark:
            return '-' + A[::-1]
        else:
            return A[::-1]