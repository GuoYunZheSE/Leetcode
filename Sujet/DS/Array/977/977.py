# 977. Squares of a Sorted Array
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        if len(A)==0:
            return []
        else:
            if A[0]>=0:
                for i in range(0,len(A)):
                    A[i]=A[i]*A[i]
                return A
            if A[len(A)-1]<=0:
                A.reverse()
                for i in range(0,len(A)):
                    A[i]=A[i]*A[i]
                return A
            else:
                minus=[]
                plus=[]
                ordered=[]
                first=True
                mark=0
                for i in range(0,len(A)):
                    if A[i]>=0:
                        plus.append(A[i])
                        if first:
                            mark=i
                        first=False
                for j in range(0,mark):
                    minus.append(A[mark-1-j]*-1)
                cursorMinus=0
                cursorPlus=0
                while cursorMinus<len(minus) and cursorPlus<len(plus):
                    while cursorPlus<len(plus):
                        if minus[cursorMinus]>=plus[cursorPlus]:
                            ordered.append(plus[cursorPlus]*plus[cursorPlus])
                            cursorPlus+=1
                            break
                        else:
                            ordered.append(minus[cursorMinus]*minus[cursorMinus])
                            cursorMinus+=1
                            break
                while cursorMinus < len(minus):
                    ordered.append(minus[cursorMinus] * minus[cursorMinus])
                    cursorMinus += 1
                while cursorPlus<len(plus):
                    ordered.append(plus[cursorPlus] * plus[cursorPlus])
                    cursorPlus += 1
                return ordered

if __name__ == '__main__':
    A=[-4,-1,0,3,10]
    S=Solution()
    print(S.sortedSquares(A))