class Solution:
    def maximum69Number (self, num: int) -> int:
        temp=num
        count=0
        maxPosition=-1
        while num>=1:
            if num%10==6:
                maxPosition=count
            count+=1
            num=int(num/10)
        if maxPosition==-1:
            return temp
        else:
            return 3*10**maxPosition+temp
if __name__ == '__main__':
    S=Solution()
    print(S.maximum69Number(6669))
    print(S.maximum69Number(9969))
    print(S.maximum69Number(9699))
    print(S.maximum69Number(9666))
    print(S.maximum69Number(9969))