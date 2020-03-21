# @Date    : 16:07 03/21/2020
# @Author  : ClassicalPi
# @FileName: 5350.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.checklist={1:0,
                        2:1,
                        3:7}

    def transform(self,n:int)->int:
        res=0
        origin=n
        if n==1:
            return 0
        while n!=1:
            if self.checklist.__contains__(n):
                self.checklist.setdefault(origin,res+self.checklist[n])
                return res+self.checklist[n]
            else:
                if n%2==0:
                    n=n/2
                    res+=1
                else:
                    n=3*n+1
                    res+=1

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res=[]
        for i in range(lo,hi+1):
            trans=self.transform(i)
            res.append([i,trans])
        res=sorted(res,key=lambda x:(x[1],x[0]))
        return res[k-1][0]

if __name__ == '__main__':
    s=Solution()
    lo=1
    hi=1000
    k=777
    print(s.getKth(lo,hi,k))