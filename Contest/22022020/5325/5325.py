class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        check={c:0 for c in "abc"}
        left=0
        res=0
        for right in range(0,len(s)):
            check[s[right]]+=1
            while all(check.values()):
                check[s[left]]-=1
                left+=1
            res+=left
        return res

if __name__ == '__main__':
    s = "aaacb"
    s1=Solution()
    print(s1.numberOfSubstrings(s))