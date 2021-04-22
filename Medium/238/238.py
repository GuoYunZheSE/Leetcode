# @Date    : 15:50 04/15/2021
# @Author  : ClassicalPi
# @FileName: 238.py
# @Software: PyCharm
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        countZero=0
        product=1
        for num in nums:
            if num!=0:
                product*=num
            else:
                countZero+=1
        if countZero==0:
            return [int(product/num) for num in nums]
        else:
            res=[]
            for num in nums:
                if num!=0:
                    res.append(0)
                else:
                    if countZero==1:
                        res.append(product)
                    else:
                        res.append(0)
        return res