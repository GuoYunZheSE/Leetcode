class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        i=0
        while i<len(strs[0]):
            Same=True
            for s in strs:
                if i < len(s):
                    if strs[0][i]!=s[i]:
                        Same=False
                else:
                    return strs[0][:i]
            if Same:
                i+=1
            else:
                return strs[0][:i]
        return strs[0][:i]