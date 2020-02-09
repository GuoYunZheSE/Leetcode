import collections
class Solution:
    def numberOfSubarrays(self, A, k):
        def atMost(k):
            res = i = 0
            for j in range(len(A)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)
if __name__ == '__main__':
    nums = [1, 1, 2, 1, 1]
    k = 3
    s=Solution()
    s.numberOfSubarrays(nums,k)