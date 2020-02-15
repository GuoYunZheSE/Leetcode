class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        if not nums:
            return []
        m=[False for i in range(0,len(nums))]
        res=[]
        for n in nums:
            m[n-1]=True
        for j in range(0,len(m)):
            if not m[j]:
                res.append(j+1)
        return res
if __name__ == '__main__':
    nums=[4,3,2,7,8,2,3,1]
    S=Solution()
    print(S.findDisappearedNumbers(nums))