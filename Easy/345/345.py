class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s)<=1:
            return s
        s=list(s)
        begin=0
        end=len(s)-1
        vowel={'a','e','i','o','u','A','E','I','O','U'}
        while begin<=end:
            if s[begin] in vowel:
                if s[end] in vowel:
                    temp=s[end]
                    s[end]=s[begin]
                    s[begin]=temp
                    begin+=1
                    end-=1
                else:
                    end-=1
            else:
                begin+=1
        return ''.join(s)

if __name__ == '__main__':
    s="leetcode"
    sol =Solution()
    print(sol.reverseVowels(s))