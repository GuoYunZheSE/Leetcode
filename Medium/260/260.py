class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        temp=sorted(nums)
        res=[]
        index=0
        while index<len(nums):
            if len(res)==2:
                return res
            if index==len(nums)-1:
                res.append(temp[index])
                index+=1
            else:
                if temp[index]!=temp[index+1]:
                    res.append(temp[index])
                    index+=1
                else:
                    index+=2
        return res
if __name__ == '__main__':
    nums=[1,2,1,3,2,5]
    s=Solution()
    print(s.singleNumber(nums))