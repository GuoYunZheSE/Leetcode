class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        even=0
        odd=1
        while even<len(A)-1 and odd<len(A):
            if A[even]%2==0:
                even+=2
            elif A[even]%2==1:
                while A[odd]%2!=0:
                    odd+=2
                temp=A[even]
                A[even]=A[odd]
                A[odd]=temp
                even+=2
                odd+=2
        return A
if __name__ == '__main__':
    S=Solution()
    S.sortArrayByParityII([4,2,5,7,8,9,11,21,23,3])
