# @Date    : 21:26 04/28/2021
# @Author  : ClassicalPi
# @FileName: 227.py
# @Software: PyCharm
import collections
class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)
if __name__ == '__main__':
    S=Solution()
    print(S.calculate("0-2147483647"))
    print(S.calculate("3+2*2"))
    print(S.calculate("3+5 / 2 "))
    print(S.calculate("3/2"))
