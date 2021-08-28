# @Date    : 17:19 08/21/2021
# @Author  : ClassicalPi
# @FileName: 135.py
# @Software: PyCharm
class Solution:
    def candy(self, ratings: [int]) -> int:
        res = {}
        strike = 0
        base = 1
        for i in range(0,len(ratings)):
            if i == 0:
                res[i] = base
            if ratings[i] > ratings[i-1]:
                strike += 1
            else:
                strike = 0
            res[i] = (base + strike)
        strike = 0
        for j in range(len(ratings)-1,-1,-1):
            if j == len(ratings) - 1:
                res[j] = max(res[j],1)
            if ratings[j] > ratings[j+1]:
                strike += 1
            else:
                strike = 0
            res[j] = max(res[j],base+strike)
        return sum(res.values())