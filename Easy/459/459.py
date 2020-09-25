# @Date    : 19:16 09/25/2020
# @Author  : ClassicalPi
# @FileName: 459.py
# @Software: PyCharm

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)<=1:
            return False
        for jump in range(1,len(s)//2+1):
            if len(s)%jump==0:
                before=s[0:jump]
                start=jump
                same=True
                while start<=len(s)-jump:
                    if s[start:start+jump]!=before:
                        same=False
                        break
                    start+=jump
                if same:
                    return True
        return False

if __name__ == '__main__':
    S=Solution()
    print(S.repeatedSubstringPattern("abcdeabcde"))