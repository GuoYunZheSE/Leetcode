# @Date    : 17:20 04/11/2021
# @Author  : ClassicalPi
# @FileName: 139.py
# @Software: PyCharm
import timeit
class Solution:
    # def __init__(self):
    #     self.res=False
    #     self.wordDict=set()
    # def DFS(self,s:str):
    #     if s=="":
    #         self.res=True
    #     if self.res==True:
    #         return
    #     for i in range(0,len(s)+1):
    #         if s[0:i] in self.wordDict:
    #             self.DFS(s[i:])
    # def wordBreak(self, s: str, wordDict: [str]) -> bool:
    #     self.wordDict=set(wordDict)
    #     self.DFS(s)
    #     return self.res
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        ans=[True]
        self.wordDict = set(wordDict)
        for i in range(1,len(s)+1):
            ans+=any(ans[j] and s[j:i] in self.wordDict for j in range(i)),
        return ans[-1]

if __name__ == '__main__':
    t = timeit.timeit(stmt='''wordBreak(s = "leetcode", wordDict = ["leet","code"])''', setup="from  __main__ import wordBreak", number=1000000)
    print(t)