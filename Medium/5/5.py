# @Date    : 12:57 07/03/2020
# @Author  : ClassicalPi
# @FileName: 5.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.s= ""
        self.res=0
        self.index=[]

    def findPalindromicByIndex(self,i):
        #Length is the product of 2
        if i<len(self.s)-1:
            if self.s[i]==self.s[i + 1]:
                left=i
                right=i+1
                while left>=0 and right<len(self.s):
                    if self.s[left]==self.s[right]:
                        if self.res < right - left + 1:
                            self.res = right - left + 1
                            self.index = [left, right]
                        left-=1
                        right+=1
                    else:
                        break
                # Single
            if i>0 and self.s[i-1]==self.s[i+1]:
                left=i-1
                right=i+1
                while left>=0 and right<len(self.s):
                    if self.s[left]==self.s[right]:
                        if self.res < right - left + 1:
                            self.res = right - left + 1
                            self.index = [left, right]
                        left-=1
                        right+=1
                    else:
                        break
        else:
            if self.res==0:
                self.res=1
                self.index=[i,i]

    def longestPalindrome(self, s: str) -> str:
        if s=="":
            return ""
        self.s=s
        for i in range(len(s)):
            self.findPalindromicByIndex(i)
        res=""
        for i in range(self.index[0],self.index[1]+1):
            res+=self.s[i]
        return res

if __name__ == '__main__':
    s="asdasdasdasdasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvasdasdasdasdasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvvdvdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvasdasdasdasdvdvdvvdvdv"
    S=Solution()
    print(S.longestPalindrome(s))