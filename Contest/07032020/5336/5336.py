# @Date    : 15:30 03/07/2020
# @Author  : ClassicalPi
# @FileName: 5336.py
# @Software: PyCharm

class Solution:
    def sortString(self, s: str) -> str:
        if len(s)==1:
            return s
        letters=[0 for i in  range(0,26)]
        res=""
        for each in s:
            letters[ord(each)-97]+=1
        while sum(letters)>0:
            for i in range(0,26):
                if letters[i]>0:
                    letters[i]-=1
                    res+=chr(i+97)
            for i in range(25,-1,-1):
                if letters[i]>0:
                    letters[i]-=1
                    res+=chr(i+97)
        return res
if __name__ == '__main__':
    s="spo"
    S=Solution()
    print(S.sortString(s))