# @Date    : 12:20 07/02/2020
# @Author  : ClassicalPi
# @FileName: 415.py
# @Software: PyCharm

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1=num1[::-1]
        num2=num2[::-1]
        res=""
        carry=0
        for i in range(max(len(num2),len(num1))):
            if i<len(num1):
                carry+=int(num1[i])
            if i<len(num2):
                carry+=int(num2[i])
            res+=str(carry%10)
            carry=carry//10
        if carry!=0:
            res+=str(carry)
        return res[::-1]

