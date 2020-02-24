# @Date    : 21:51 02/24/2020
# @Author  : ClassicalPi
# @FileName: 996.py
# @Software: PyCharm

import typing
import math
class Solution:
    def DFS(self,res:typing.List[typing.List[int]],nums: typing.List[int],pre:typing.List[int]):
        if len(nums)==0:
            res.append(pre)
            return res
        else:
            used = set()
            for i in range(0,len(nums)):
                if nums[i] not in used:
                    if pre==[] or ((pow((pre[-1]+nums[i]),0.5)//1)**2==(pre[-1]+nums[i])):
                        used.add(nums[i])

                        temp=nums.copy()
                        temp.pop(i)

                        self.DFS(res,temp,pre+[nums[i]])
            return res
    def numSquarefulPerms(self, A: typing.List[int]) -> int:
        res=[]
        self.DFS(res,nums=A,pre=[])
        return len(res)

if __name__ == '__main__':
    nums=[2,2,2]
    s=Solution()
    print(s.numSquarefulPerms(nums))
