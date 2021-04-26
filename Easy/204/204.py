# @Date    : 19:06 04/23/2021
# @Author  : ClassicalPi
# @FileName: 204.py
# @Software: PyCharm
class Solution:
    def countPrimes(self, n: int) -> int:
        res=[0 for i in range(n+1)]
        res[2]=1
        if n <= 2:
            return res[n]
        else:
            for i in range(3,n+1):
                isPrime=True
                for j in range(2,i):
                    if i%j==0:
                        isPrime=False
                        break
                if isPrime:
                    res[i]=res[i-1]+1
                else:
                    res[i]=res[i-1]
        return res[n]
if __name__ == '__main__':
    S=Solution()
    print(S.countPrimes(10))