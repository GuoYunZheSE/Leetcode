# @Date    : 11:36 04/16/2021
# @Author  : ClassicalPi
# @FileName: 229.py
# @Software: PyCharm
import collections
class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        # d=collections.Counter(nums)
        # res=[]
        # for k,v in d.items():
        #     if v>len(nums)/3:
        #         res.append(k)
        # return res
        candidate1,candidate2,count1,count2=0,1,0,0
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
            elif count1==0:
                candidate1,count1=num,1
            elif count2==0:
                candidate2,count2=num,1
            else:
                count2-=1
                count1-=1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]
if __name__ == '__main__':
    S=Solution()
    print(S.majorityElement([3,0,3,4]))