# @Date    : 15:01 08/21/2021
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm
import sys

def sumCheck(nums:[],M:int):
    dic = {}
    res = 0
    for i in range(0,len(nums) - 1):
        for j in range(i+1,len(nums)):
            dic[nums[i]+nums[j]] = dic.get(nums[i]+nums[j],0) + 1
    for key,val in dic.items():
        if key <= M:
            res += val
    return res
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    nums = list(map(int, line.split()))
    M = int(sys.stdin.readline().strip())
    print(sumCheck(nums,M))