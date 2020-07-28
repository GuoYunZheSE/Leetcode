# @Date    : 20:40 07/28/2020
# @Author  : ClassicalPi
# @FileName: 8.py
# @Software: PyCharm
import collections
class Solution:
    def myAtoi(self, str: str) -> int:
        def compare_with_ultr(res,ultr,Positive):
            if len(res)<len(ultr):
                sum=0
                for index,val in enumerate(res[::-1]):
                    sum+=(int(val)*(10**index))
                if Positive:return sum
                else:return -sum
            elif len(res)==len(ultr):
                for i in range(len(res)):
                    if ultr[i]>res[i]:
                        break
                    if res[i]>ultr[i]:
                        if Positive:
                            return 2**31-1
                        else:
                            return -2147483648
                sum=0
                for index,val in enumerate(res[::-1]):
                    sum+=(int(val)*(10**index))
                if Positive:return sum
                else:return -sum
            else:
                if Positive:
                    return 2 ** 31 - 1
                else:
                    return -2147483648

        str=str.strip(" ")
        Positive=True
        if not str:
            return 0
        if not str[0].isdigit():
            if str[0]=="-":
                Positive=False
                str=str[1:]
            elif  str[0]=="+":
                str=str[1:]
            else:
                return 0
        res=[]
        BeginwithZero=True
        for each in str:
            if not each.isdigit():
                break
            else:
                if each=="0" and BeginwithZero:
                    continue
                else:
                    BeginwithZero=False
                    res.append(each)
        if Positive:
            return compare_with_ultr(res,[a for a in "2147483647"],Positive)
        else:
            return compare_with_ultr(res,[a for a in "2147483648"],Positive)
if __name__ == '__main__':
    S=Solution()
    print(S.myAtoi("42"))
    print(S.myAtoi("1095502006p8"))
    print(S.myAtoi("4193 with words"))
    print(S.myAtoi("words and 987"))
    print(S.myAtoi("-91283472332"))
    print(S.myAtoi("  0000000000012345678"))