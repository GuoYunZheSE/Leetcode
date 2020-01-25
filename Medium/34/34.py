class Solution:
    def __init__(self):
        self.nums=[]

    def bisearch(self,target:int,mode):
        begin=0
        end=len(self.nums)
        while begin<end:
            mid=(begin+end)//2
            if self.nums[mid]>target or (mode=="Left" and target==self.nums[mid]):
                end=mid
            else:
                begin=mid+1
        return begin


    def searchRange(self, nums: [int], target: int) -> [int]:
        self.nums=nums
        left_idx = self.bisearch(target, "Left")

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, self.bisearch(target, False)-1]

if __name__ == '__main__':
    cnums=[5, 7, 7, 8, 8, 10]
    S=Solution()
    print(S.searchRange(cnums,8))