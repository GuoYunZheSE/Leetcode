import math
class Solution:
    def __init__(self):
        self.prims=0
    def numPrimeArrangements(self, n: int) -> int:
        for each in range(0,n+1):
            if self.isPrime(each):
                self.prims+=1
        return int((math.factorial(self.prims)*math.factorial(n-self.prims))%int(1e9+7))

    @staticmethod
    def isPrime( n: int) -> bool:
        if n <= 3:
            if n == 3 or n==2:
                return True
            else:
                return False
        else:
            sqrt = int(math.sqrt(n))
            for i in range(2, sqrt + 1):
                if n % i == 0:
                    return False
            return True
if __name__ == '__main__':
    S=Solution()
    print(S.numPrimeArrangements(100))
