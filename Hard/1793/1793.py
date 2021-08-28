# @Date    : 01:00 08/26/2021
# @Author  : ClassicalPi
# @FileName: 1793.py
# @Software: PyCharm
import sys
class Solution:
    # 1, 4, 3, 7, 4, 5
    def maximumScore(self, nums: [int], k: int) -> int:
        nums.append(0)
        stack = [-1]
        res = 0
        for l in range(0,len(nums)):
            j = l - 1
            while nums[l] < nums[stack[-1]]:
                h = nums[stack.pop()]
                w = j - stack[-1]
                if stack[-1] < k <= j:
                    print(f"i:{stack[-1]} j:{j} h:{h} w:{w} res:{h*w}")
                    res = max(res,h*w)
            stack.append(l)
        return res
if __name__ == '__main__':
    S = Solution()
    print(S.maximumScore([8407,5626,9236,4362,9678,6568,4170,5691,7865,4067,2094,9451,9667,1400,5093,6191,7286,7368,6461,4309,9751,3672,4165,4940,3726,7003,6263,4250,1950,9536,61,1486,6009,6977,7084,2472,7921,1913,117,3543,5075,1582,7987,6710,1331,3023,6856,1125,1475,4158,3422,7864,9178,7255,4997,2128,5441,5910,6719,1308,4444,9746],30))