# @Date    : 17:20 04/11/2021
# @Author  : ClassicalPi
# @FileName: 139.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.res=False
        self.wordDict=set()
    def DFS(self,s:str):
        if s=="":
            self.res=True
        if self.res==True:
            return
        for i in range(0,len(s)+1):
            if s[0:i] in self.wordDict:
                self.DFS(s[i:])
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        self.wordDict=set(wordDict)
        self.DFS(s)
        return self.res

if __name__ == '__main__':
    s=["leet", "code"]
    S=Solution()
    print(S.wordBreak("leetcode",s))