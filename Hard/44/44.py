# @Date    : 16:37 01/04/2021
# @Author  : ClassicalPi
# @FileName: 44.py
# @Software: PyCharm

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_index,p_index,ss_index=0,0,0
        star=None
        while (s_index < len(s)):
            if p_index<len(p) and p[p_index]=="*":
                star=p_index
                p_index+=1
                ss_index=s_index
                continue
            if p_index<len(p) and (p[p_index]=="?" or p[p_index]==s[s_index]):
                s_index+=1
                p_index+=1
                continue
            if star!=None:
                p_index=star+1
                ss_index+=1
                s_index=ss_index
                continue
            return False
        while (p_index < len(p) and p[p_index]=="*"):
            p_index+=1
        return p_index==len(p)
if __name__ == '__main__':
    S=Solution()
    print(S.isMatch("aa","a"))
    print(S.isMatch("aa", "*"))
    print(S.isMatch("cb", "?a"))
    print(S.isMatch("adceb", "*a*b"))