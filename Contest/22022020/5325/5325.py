class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count={c:0 for c in 'abc'}
        res=i=j=0
        for j in range(0,len(s)):
            count[s[j]]+=1
            while all(count.values()):
                count[s[i]]-=1
                i+=1
            res+=i
        return res


if __name__ == '__main__':
    s = "abcabc"
    s1=Solution()
    print(s1.numberOfSubstrings(s))