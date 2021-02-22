# @Date    : 16:46 02/22/2021
# @Author  : ClassicalPi
# @FileName: 66.py
# @Software: PyCharm

class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        digits[-1]=digits[-1]+1
        Carry=0
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=Carry
            Carry=0
            if digits[i]>9:
                digits[i]%=10
                Carry+=1
        if Carry>0:
            res=[1]
            res.extend(digits)
            return res
        return digits
if __name__ == '__main__':
    S=Solution()
    print(S.plusOne([4,3,2,1]))
    print(S.plusOne([1]))
    print(S.plusOne([0]))
    print(S.plusOne([9,9,9,9,9,9]))
    print(S.plusOne([1,2]))