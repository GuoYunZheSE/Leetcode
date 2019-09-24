# 461. Hamming Distance
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xString=bin(x)[2:][::-1]
        yString=bin(y)[2:][::-1]
        if len(xString)>=len(yString):
            res=0
            for i in range(0,len(yString)):
                if xString[i]!=yString[i]:
                    res+=1
            for j in range(len(yString),len(xString)):
                if xString[j]=='1':
                    res+=1
            return res
        else:
            res=0
            for i in range(0,len(xString)):
                if xString[i]!=yString[i]:
                    res+=1
            for j in range(len(xString),len(yString)):
                if yString[j]=='1':
                    res+=1
            return res
        #
        # class Solution:
        #     def hammingDistance(self, x: int, y: int) -> int:
        #         return bin(x ^ y)[2:].count("1")
if __name__ == '__main__':
    X=1
    Y=4
    S=Solution()
    S.hammingDistance(X,Y)