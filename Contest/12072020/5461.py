# @Date    : 10:39 07/12/2020
# @Author  : ClassicalPi
# @FileName: 5461.py
# @Software: PyCharm
# 1：1
# 11：3
# 111: 6
# 1111:10
# 11111:15
# 111111:21
class Solution:
    def getNum(self,length):
        if length==1:
            return 1
        else:
            sum=0
            add=1
            while length>0:
                sum+=add
                add+=1
                length-=1
            return sum

    def numSub(self, s: str) -> int:
        if len(s)==1:
            if s[0]=="1":
                return 1
            return 0
        else:
            left=0
            while left<len(s):
                if s[left]=="0":
                    left+=1
                else:
                    break
            if left==(len(s)-1):
                if s[left]=="0":
                    return 1
                return 0
            else:
                res = 0
                right=left
                while right<len(s):
                    if s[right]=="1":
                        right+=1
                    else:
                        res+=self.getNum(right-left)
                        left=right
                        while left < len(s):
                            if s[left] == "0":
                                left += 1
                            else:
                                break
                        right=left
                if  right==len(s):
                    res+=self.getNum(right-left)
                return res%(10**9+7)

if __name__ == '__main__':
    S=Solution()
    print(S.numSub("0110111"))
    print(S.numSub("101"))
    print(S.numSub("0"))
    print(S.numSub("1"))