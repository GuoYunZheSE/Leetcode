import sys
class Solution:
    def findBestValue(self, arr: [int], target: int) -> int:
        arr.sort()
        sumption=0
        length=len(arr)
        for i in range(length):
            ans=round((target-sumption)/length)
            if ans<=arr[i]: return ans
            sumption+=arr[i]
            length-=1
        return arr[-1]

if __name__ == '__main__':
    nums=[2,3,5]
    s=Solution()
    print(s.findBestValue(nums,10))