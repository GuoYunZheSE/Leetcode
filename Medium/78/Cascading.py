# @Date    : 21:42 03/14/2021
# @Author  : ClassicalPi
# @FileName: Cascading.py
# @Software: PyCharm
import timeit
class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        res=[[]]
        for num in nums:
            res+=[a+[num] for a in res]
        return res

if __name__ == '__main__':
    S=Solution()
    print(S.subsets([1,2,3]))