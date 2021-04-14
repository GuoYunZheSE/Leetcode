# @Date    : 11:51 04/14/2021
# @Author  : ClassicalPi
# @FileName: 140.py
# @Software: PyCharm
import collections
class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        ok=[False for i in range(len(s)+1)]
        ok[0]=True
        d={}
        for i in range(1,len(s)+1):
            d.setdefault(i,[])

        self.wordSet=set(wordDict)
        for i in range(1,len(s)+1):
            for j in range(i):
                if ok[j] and s[j:i] in self.wordSet:
                    ok[i]=True
                    if j==0:
                        d[i].append(s[j:i]+" ")
                    else:
                        d[i].extend([a+s[j:i]+" " for a in  d[j]])
        if not ok[-1]:
            return []
        return [a.strip() for a in d[len(s)]]