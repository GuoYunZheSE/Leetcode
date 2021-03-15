# @Date    : 11:02 03/15/2021
# @Author  : ClassicalPi
# @FileName: Backtracking.py
# @Software: PyCharm
class Solution:
    def backtracking(self,path:[],nums:[],res:[]):
        res.append(path)
        for i in range(len(nums)):
            self.backtracking(path+[nums[i]],nums[i+1:],res)

    def subsets(self, nums: [int]) -> [[int]]:
        res=[]
        self.backtracking([],nums,res)
        return res

if __name__ == '__main__':
    S=Solution()
    print(S.subsets([1,2,3]))