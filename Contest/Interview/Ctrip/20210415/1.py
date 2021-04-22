# @Date    : 19:04 04/15/2021
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm
import collections
import sys
class Solution:
    def similarity(self,A:str,B:str):
        A=A.strip()
        B=B.strip()
        listA=[a.strip().lower() for a in A.split(" ")]
        listB = [b.strip().lower() for b in B.split(" ")]

        dp=[[0 for b in listB] for a in listA]

        for a in range(0,len(listA)):
            dp[a][0]=a
        for b in range(0,len(listB)):
            dp[0][b]=b

        for a in range(1,len(listA)):
            for b in range(1,len(listB)):
                if listA[a]==listB[b]:
                    dp[a][b]=dp[a-1][b-1]
                else:
                    dp[a][b]=min([dp[a-1][b],dp[a][b-1],dp[a-1][b-1]])+1
        similarity=1-dp[-1][-1]/len(listA)
        if similarity<0:
            print("0.00")
        else:
            print("{:.2f}".format(similarity))

if __name__ == '__main__':
    line=sys.stdin.readline().strip()
    A,B=line.split("<trip>")
    S=Solution()
    S.similarity(A,B)