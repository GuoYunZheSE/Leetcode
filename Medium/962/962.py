class Solution:
    def maxWidthRamp(self, A: [int]) -> int:
        res=0
        stack=[]
        for index,val in enumerate(A):
            if not stack or val<A[stack[-1]]:
                stack.append(index)
        if len(stack)>=len(A)/2:
            for i in range(len(A))[::-1]:
                while stack and A[i]>=A[stack[-1]]:
                    res=max(res,i-stack.pop())
        else:
            B=A[::-1]
            for index,val in enumerate(A):
                for index2,val2 in enumerate(B):
                    true_index=abs(index2+1-len(A))
                    if true_index-index<=res:
                        break
                    else:
                        if val2>=val:
                            res=max(res,true_index-index)
                            break
        return res
if __name__ == '__main__':
    S=Solution()
    print(S.maxWidthRamp(
[29,28,27,27,22,22,20,16,16,13,13,12,10,8,8,8,8,6,5,4,4,3,3,2,2,2,1,1,1,0]))