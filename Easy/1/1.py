class Solution:
    def __init__(self):
        self.dic={}
        self.duplicate={}
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(0,len(nums)):
            if self.dic.__contains__(nums[i]):
                self.duplicate.setdefault(nums[i],i)
            else:
                self.dic.setdefault(nums[i],i)
        for each in nums:
            remain=target-each
            if self.dic.__contains__(remain):
                if remain==each:
                    if remain in self.duplicate:
                        return [self.dic.get(each), self.duplicate.get(each)]
                else:
                    return [self.dic.get(each),self.dic.get(remain)]
if __name__ == '__main__':
    nums=[3,2,4]
    target = 6
    S=Solution()
    print(S.twoSum(nums,target))