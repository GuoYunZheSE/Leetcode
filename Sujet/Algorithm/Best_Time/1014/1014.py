class Solution:
    def maxScoreSightseeingPair(self, A):
        preSpotValue=0
        preSpotIndex=0
        ans=0
        for i in range(0,len(A)):
            ans=max(ans,preSpotValue+A[i]+preSpotIndex-i)
            if (preSpotIndex+preSpotValue<i+A[i]):
                preSpotValue=A[i]
                preSpotIndex=i
        return ans

if __name__ == '__main__':
    nums=[8,1,5,2,6]
    s=Solution()
    print(s.maxScoreSightseeingPair(nums))