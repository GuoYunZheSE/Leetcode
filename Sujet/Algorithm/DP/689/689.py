class Solution:
    def maxSumOfThreeSubarrays(self, nums, k: int):
        s,temp = [],sum(nums[:k])
        nums.append(0)
        for i in range(len(nums)-k):
            s.append(temp)
            temp -= nums[i]-nums[i+k]
        nums.pop(-1)
        l,r = [0]*len(s),[0]*len(s)
        best = 0
        for i in range(len(s)):
            if s[i] > s[best]:
                best = i
            l[i] = best
        best = len(s)-1
        for i in range(len(s)-1, -1,-1):
            if s[i] >= s[best]:
                best = i
            r[i] = best
        ans = []
        for j in range(k,len(s)-k):
            i, p = l[j-k], r[j+k]
            if ans == [] or (s[i]+s[j]+s[p] > s[ans[0]]+s[ans[1]]+s[ans[2]]):
                ans = [i,j,p]
        return ans
if __name__ == '__main__':
    A=[1,2,1,2,6,7,5,1]
    K=2
    S=Solution()
    S.maxSumOfThreeSubarrays(A,K)