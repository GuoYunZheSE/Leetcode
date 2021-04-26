# @Date    : 16:20 04/22/2021
# @Author  : ClassicalPi
# @FileName: 202.py
# @Software: PyCharm
class Solution:
    def isHappy(self, n: int) -> bool:
        index=0
        while index<100:
            res=0
            while n // 10 > 0:
                res+=(n%10)**2
                n=n//10
            res+=n**2
            print(res)
            if res ==1:
                return True
            else:
                n=res
                index+=1

if __name__ == '__main__':
    S=Solution()
    print(S.isHappy(19))