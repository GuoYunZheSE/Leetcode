# @Date    : 13:09 04/10/2021
# @Author  : ClassicalPi
# @FileName: 131.py
# @Software: PyCharm
import collections
class Solution:
    def __init__(self):
        self.res=[]
    def DFS(self,start:int,s:str,path:[]):
        if start>=len(s):
            self.res.append(path)
            return
        for step in range(0,len(s)-start+1):
            if self.isPalindrome(start,start+step,s):
                self.DFS(start+step+1,s,path+[s[start:start+step+1]])
    def partition(self, s: str) -> [[str]]:
        self.DFS(0,s,[])
        return self.res
    def isPalindrome(self,start:int,end:int,s:str)->bool:
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True

if __name__ == '__main__':
    S=Solution()
    print(S.partition("aab"))