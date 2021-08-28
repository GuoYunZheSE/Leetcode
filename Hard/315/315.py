# @Date    : 22:10 07/26/2021
# @Author  : ClassicalPi
# @FileName: 315.py
# @Software: PyCharm

class Solution:
    def countSmaller(self, nums: [int]) -> [int]:
        res = [0 for i in range(len(nums))]
        def sort(index:[]):
            mid = len(index)//2
            if mid:
                left,right = sort(index[0:mid]),sort(index[mid:])
                for i in range(len(index)-1,-1,-1):
                    if not right or (left and nums[left[-1]] > nums[right[-1]]):
                        res[left[-1]] += len(right)
                        index[i] = left.pop()
                    else:
                        index[i] = right.pop()
            return index
        sort(list(range(len(nums))))
        return res

if __name__ == '__main__':
    S = Solution()
    print(S.countSmaller([5,2,6,1]))
    print(S.countSmaller([-1,-1]))