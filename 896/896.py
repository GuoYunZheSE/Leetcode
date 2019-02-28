# Class:Easy
# Data:Thursday, 28/02/2019

# Runtime: 96 ms, faster than 84.91% of Python3 online submissions for Monotonic Array.
# Memory Usage: 17.2 MB, less than 5.11% of Python3 online submissions for Monotonic Array.
class Solution:
    def isMonotonic(self, A) -> bool:
        if len(A)<=2:
            return True
        else:
            trend=0
            for j in range(0,len(A)-1):
                if (A[j+1]-A[j])!=0:
                    trend=A[j+1]-A[j]
                    break
            for i in range(1,len(A)-1):
                if trend*(A[i+1]-A[i])<0:
                    return False
            return True