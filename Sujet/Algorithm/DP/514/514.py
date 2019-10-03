import sys
import numpy as np
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        res=np.zeros((len(key)+1, len(ring)), dtype=np.int)
        for k in range(0,len(ring)):
            res[len(key)][k]=0
        for i in range(len(key)-1,-1,-1):
            for j in range(0,len(ring)):
                res[i][j]=sys.maxsize
                for k in range(0,len(ring)):
                    if ring[k]==key[i]:
                        diff=min(abs(k-j),abs(len(ring)-abs(k-j)))
                        res[i][j]=min(res[i][j],diff+res[i+1][k])
        return res[0][0]+len(key)
if __name__ == '__main__':
    ring="ABDEFCBG"
    key="CB"
    S=Solution()
    print(S.findRotateSteps(ring,key))