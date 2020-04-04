# @Date    : 23:12 04/04/2020
# @Author  : ClassicalPi
# @FileName: 5362.py
# @Software: PyCharm
import collections
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        elif k==len(s):
            return True
        else:
            dic=collections.Counter(s)
            odd=0
            even=0
            for i in dic.values():
                if i%2==0:
                    even+=1
                else:
                    odd+=1
            while k>1:
                if odd>0:
                    k-=1
                    odd-=1
                    continue
                else:
                    k-=1
                    even-=1
                    odd+=1
            return (odd==0 or odd==1)

if __name__ == '__main__':
    s=Solution()
    print(s.canConstruct("hdafhdajskdajsfbajhfawkfhawdhaiw",20))