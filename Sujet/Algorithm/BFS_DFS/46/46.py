class Solution:
    def DFS(self,res:[[]],nums:[],pre:[]):
        if len(nums)==0:
            res.append(pre)
        else:
            for i in range(0,len(nums)):
                temp = nums.copy()
                temp.pop(i)
                self.DFS(res,temp,pre+[nums[i]])
            return res
    def permute(self, nums: []) -> [[int]]:
        res=[]
        self.DFS(res,nums,pre=[])
        return res

if __name__ == '__main__':
    nums=[1,2,3,4,5,6,7,8,9,10]
    s=Solution()
    A=s.permute(nums)
    print(len(A))