# @Date    : 09:06 04/07/2021
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm
import sys
class Solution:
    def __init__(self):
        self.map={}
        self.map2 = {}
        s=")!@#$%^&*("
        for index,val in enumerate(s):
            self.map.setdefault(val,str(index))
        for index,val in enumerate(s):
            self.map2.setdefault(str(index),val)
        self.map.setdefault('-','-')
        self.map2.setdefault('-', '-')
    def alien_language(self,a:str,b:str):
        n_a,n_b="",""

        for c in a:
            n_a+=self.map[c]
        for c in b:
            n_b+=self.map[b]

        res1,res2,res="","",""

        carry=0
        sign=False
        for i in range(len(n_a)-1,-1,-1):

            temp=int(n_a[i])+int(n_b[i])+carry
            carry = 1 if temp>=10 else 0
            temp=temp%10
            res1+=str(temp)

        res=[n_a+n_b,n_a-n_b,n_b-n_a]
        for each in res:
            each=str(each)
            temp=""
            for c in each:
                temp+=self.map2[c]
            print(temp)

if __name__ == "__main__":
    S=Solution()
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip()
        a,b=line.split(" ")
        S.alien_language(a,b)