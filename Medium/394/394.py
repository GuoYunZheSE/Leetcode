# @Date    : 21:58 09/01/2021
# @Author  : ClassicalPi
# @FileName: 394.py
# @Software: PyCharm
class Solution:
    def decodeString(self, s: str) -> str:
        stack,curNum,curString = [], 0, ""
        for c in s:
            if c == "[":
                stack.extend([curNum,curString])
                curNum, curString = 0, ""
            elif c == "]":
                curString = stack.pop() + curString * stack.pop()
            elif c.isdigit():
                curNum = 10*curNum + int(c)
            else:
                curString += c
        return curString