# @Date    : 20:03 03/13/2021
# @Author  : ClassicalPi
# @FileName: 76.py
# @Software: PyCharm
import collections
class Solution:
    def find_res(self, window_dict:dict, t_dict:dict):
        for key,val in t_dict.items():
            if not (window_dict.get(key) is not None and window_dict.get(key) >= val):
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        res=[]
        t_dict=dict(collections.Counter(t))
        window=collections.deque()
        window_dict={}
        start,end=0,0
        while start<len(s) or end<len(s):
            if not self.find_res(window_dict,t_dict):
                if end==len(s):
                    break
                window.append(s[end])
                if window_dict.get(s[end]):
                    window_dict[s[end]]+=1
                else:
                    window_dict[s[end]] = 1
                end+=1
            else:
                if not res or len(res)>=len(window):
                    res=window.copy()
                window.popleft()
                if window_dict[s[start]]>1:
                    window_dict[s[start]]-=1
                else:
                    window_dict.pop(s[start])
                start+=1
        return "".join(res)

if __name__ == '__main__':
    S=Solution()
    print(S.minWindow(s = "ADOBECODEBANC", t = "ABC"))
    print(S.minWindow(s="a", t="a"))
    print(S.minWindow(s="aasdasda", t="c"))