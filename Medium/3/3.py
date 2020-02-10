class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        cur=set()
        i,j=0,0
        while j<len(s):
            if not cur.__contains__(s[j]):
                cur.add(s[j])
                j+=1
            else:
                res=max(res,len(cur))
                cur.remove(s[i])
                i+=1
        res = max(res, len(cur))
        return res

if __name__ == '__main__':
    s=" "
    sol=Solution()
    print(sol.lengthOfLongestSubstring(s))