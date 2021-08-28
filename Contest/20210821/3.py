# @Date    : 16:05 08/21/2021
# @Author  : ClassicalPi
# @FileName: 3.py
# @Software: PyCharm
# 8 9 11 10 9 7 6 2
# 1 2 3  2

# 1 2 3
# 1 3 2
# 2 1 3
import sys
import collections
def Solution(nums:[int]):
    res = {}
    base = 1
    strike = 0

    for i in range(0,len(nums)):
        if i == 0:
            res[0] = 1
            continue
        if nums[i] > nums[i-1]:
            strike += 1
        else:
            strike = 0
        res[i] = base + strike
    for j in range(len(nums)-1,-1,-1):
        if j == len(nums) - 1:
            res[j] = max(res[j],1)
            continue
        if nums[j] > nums[j+1]:
            strike += 1
        else:
            strike = 0
        res[j] = max(res[j],base+strike)
    return sum(list(res.values()))

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))
    print(Solution(nums))
