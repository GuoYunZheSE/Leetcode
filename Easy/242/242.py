# @Date    : 16:43 01/06/2021
# @Author  : ClassicalPi
# @FileName: 242.py
# @Software: PyCharm
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count,t_count=[0]*26,[0]*26
        for each in s:
            s_count[ord(each)-ord('a')]+=1
        for each in t:
            t_count[ord(each)-ord('a')]+=1
        return s_count==t_count

if __name__ == '__main__':
    S=Solution()
    print(S.isAnagram("rat","yat"))
    print(S.isAnagram("rat", "atr"))
