# @Date    : 20:43 04/05/2021
# @Author  : ClassicalPi
# @FileName: 125.py
# @Software: PyCharm
class Solution:
    def isPalindrome(self, s: str) -> bool:
        S=[]
        for each in s:
            if 65<=ord(each)<=90 or 97<=ord(each)<=122 or 48<=ord(each)<=57:
                S.append(each.upper())
        for i in range(0,len(S)//2):
            if S[i]!=S[len(S)-i-1]:
                return False
        return True

if __name__ == '__main__':
    S=Solution()
    print(S.isPalindrome("Zeus was deified, saw Suez."))