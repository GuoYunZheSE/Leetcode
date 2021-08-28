# @Date    : 19:47 08/01/2021
# @Author  : ClassicalPi
# @FileName: 1011.py
# @Software: PyCharm
class Solution:
    def shipWithinDays(self, weights: [int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            cur, need, mid  = 0, 1, (left+right)//2
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight
            if need > days:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    S = Solution()
    print(S.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))