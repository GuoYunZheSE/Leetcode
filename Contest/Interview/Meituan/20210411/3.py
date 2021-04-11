# @Date    : 11:10 04/11/2021
# @Author  : ClassicalPi
# @FileName: 3.py
# @Software: PyCharm
import sys
class Solution:
    def reduce_(self,s:str):
        s=s.replace("111","")
        stack=[]
        for c in s:
            if len(stack)<3:
                stack.append(c)
            else:
                if stack[len(stack)-3:len(stack)].count("1")>=2:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                stack.append(c)
        zero=stack.count("0")
        return zero-(len(stack)-zero)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    S = Solution()
    line = sys.stdin.readline().strip()
    print(S.reduce_(line))