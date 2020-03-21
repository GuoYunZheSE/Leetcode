# @Date    : 15:40 03/07/2020
# @Author  : ClassicalPi
# @FileName: 1371.py
# @Software: PyCharm
class Solution:

    def check(self,d:dict):
        for each in list(dict.values()):
            if not each%2==0:
               return False
        return True

    def findTheLongestSubstring(self, s: str) -> int:
        dic={
            a:0 for a in "aeiou"
        }
        rest={
            a:s.count(a) for a in "aeiou"
        }
        union={'a','e','i','o','u'}
        left,right=0,0
        res=0
        for right in range(0,len(s)):
            if s[right] in union:
                dic[s[right]]+=1
                rest[s[right]]-=1
            if self.check(dic):
                res=max(res,right-left+1)
            # else:
