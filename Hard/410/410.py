import sys
class Solution:
    def __init__(self):
        self.nums=[]
        self.table=[]
        self.sum=[]

    def dp(self,row:int,column:int):
        if row==1:
            return self.sum[column-1]
        maxes=[sys.maxsize]
        for c in range(column+1,len(self.nums)):
            DP=0
            if self.table[row-1][c]!=-1:
                DP=self.table[row-1][c]
            else:
                DP=self.dp(row-1,c)
                self.table[row - 1][c]=DP
            maxes.append(max(self.sum[len(self.nums)-1]-self.sum[c-1],DP))
        return min(maxes)

    def splitArray(self, nums: [int], m: int) -> int:
        self.nums=nums
        self.table=[[-1 for i in range(len(nums))]for j in range(m)]

        self.sum=[0 for i in range(len(nums))]
        self.sum[0]=nums[0]

        for i in range(1,len(nums)):
            self.sum[i]+=self.sum[i-1]+nums[i]

        return self.dp(m,0)

if __name__ == '__main__':
    S=Solution()
    nums=[7,2,5,10,8]
    m=2
    print(S.splitArray(nums,m))