# @Date    : 11:56 09/22/2020
# @Author  : ClassicalPi
# @FileName: 28.py
# @Software: PyCharm

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        if haystack==needle=='':
            return 0
        for start in range(0,len(haystack)-len(needle)+1):
            for i in range(len(needle)):
                if haystack[start+i]!=needle[i]:
                    break
                else:
                    if i==len(needle)-1:
                        return start
        return -1

if __name__ == '__main__':
    haystack = "abcabcdabcde"
    needle = "de"
    S=Solution()
    print(S.strStr(haystack,needle))