class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""
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
if __name__ == '__main__':
    strs=["dog","racecar","car"]
    S=Solution()
    print(S.longestCommonPrefix(strs))