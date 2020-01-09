class Solution:
    def longestMountain(self, A: [int]) -> int:
        res=[]
        count=1
        up=True
        noHead=False
        i=0
        while i<len(A):
            if up:
                if i==len(A)-1:
                    i += 1
                else:
                    if A[i]<A[i+1]:
                        noHead=False
                        count+=1
                        i+=1
                    else:
                        if i==0 or noHead:
                            i+=1
                            noHead=True
                        else:
                            up=False
            else:
                if i==len(A)-1:
                    i+=1
                    res.append(count)
                else:
                    if A[i]>A[i+1]:
                        noHead = False
                        count+=1
                        i+=1
                    else:
                        if A[i]==A[i+1]:
                            res.append(count)
                            count=1
                            i+=1
                            up=True
                            noHead=True
                        else:
                            up=True
                            noHead = False
                            res.append(count)
                            count=1
        if len(res)>0:
            return max(res)
        else:
            return 0
if __name__ == '__main__':
    A=[2,3,3,2,0,2]
    S=Solution()
    print(S.longestMountain(A))