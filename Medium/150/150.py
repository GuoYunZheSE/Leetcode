# @Date    : 20:12 04/14/2021
# @Author  : ClassicalPi
# @FileName: 150.py
# @Software: PyCharm
class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        s=[]
        for token in tokens:
            s.append(token)
            if token in ['+','-','*','/']:
                num1=s.pop()
                num2=s.pop()
                if token == '+':
                    temp=(num1+num2)
                if token == '-':
                    temp=(num1-num2)
                if token == '*':
                    temp=(num1*num2)
                if token == '/':
                    temp=(num1/num2)
            s.append(temp)
        return s[0]