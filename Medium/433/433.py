# @Date    : 16:27 04/06/2021
# @Author  : ClassicalPi
# @FileName: 433.py
# @Software: PyCharm
import collections
import sys
class Solution:
    def minMutation(self, start: str, end: str, bank: [str]) -> int:
        currLayer=collections.deque([[start,0]])
        nextLayer=collections.deque()
        bankSet=set(bank)
        res=sys.maxsize
        if not end in bankSet:
            return -1
        while currLayer:
            currGene,depth=currLayer.popleft()
            for i in range(len(currGene)):
                for c in "ATCG":
                    mutedGene=currGene[0:i]+c+currGene[i+1:]
                    if mutedGene==end:
                        res=min(res,depth+1)
                        return res
                    if mutedGene in bankSet:
                        bankSet-=set(mutedGene)
                        nextLayer.append([mutedGene,depth+1])
            if not currLayer:
                currLayer,nextLayer=nextLayer,collections.deque()
                bankSet=set(bank)-set([a[0] for a in currLayer])
        return -1 if res==sys.maxsize else res

if __name__ == '__main__':
    S=Solution()
    print(S.minMutation("AACCGGTT","AAACGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"]))