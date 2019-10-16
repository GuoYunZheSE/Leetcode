class Solution:
    def reverse(self, x: int) -> int:
        result=0
        length=0
        if x==0:
            return 0
        if x>=0:
            mark=1
        else:
            mark=-1
            x=abs(x)

        while x%10==0:
            x=x/10
        while x/pow(10,length)>=10:
            length+=1
        while x>=10:
            remainder=x%10
            x=x//10
            result+=pow(10,length)*remainder
            length-=1
        result+=x
        if mark==-1:
            result=result*-1

        if abs(result)>= 2147483647:
            return 0
        else:
            return int(result)

if __name__ == '__main__':
    S=Solution()
    print(S.reverse(123))
