import typing
class Solution:
    def DFS(self,res:typing.List[typing.List[int]],nums: typing.List[int],pre:typing.List[int]):
        if len(nums)==0:
            res.append(pre)
            return res
        else:
            used = set()
            for i in range(0,len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])

                    temp=nums.copy()
                    temp.pop(i)

                    self.DFS(res,temp,pre+[nums[i]])
            return res

    def permuteUnique(self, nums: typing.List[int]) -> typing.List[typing.List[int]]:
        res=[]
        self.DFS(res,nums,[])
        return res

if __name__ == '__main__':
    nums=[1,2,3,4,5,1,2,4,2,3]
    s=Solution()
    print(s.permuteUnique(nums))