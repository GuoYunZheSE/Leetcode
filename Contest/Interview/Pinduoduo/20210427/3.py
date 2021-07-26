# @Date    : 20:00 04/27/2021
# @Author  : ClassicalPi
# @FileName: 3.py
# @Software: PyCharm
import sys
import collections
class Solution:
    def minBinNum(self,x:str,k:int):
        nums=collections.deque([c for c in x])

        while nums and nums[-1]=='1':
            nums.pop()
        if nums:
            nums.pop()
        else:
            x+="0"
        nums.append("1")

        while len(nums)<len(x):
            nums.append("0")

        one=nums.count("1")
        while one > k:
            for i in range(len(nums)-1,-1,-1):
                if nums[i]=="1":
                    nums[i]="0"
                    one-=1
                if one == k:
                    break
        while one < k:
            for i in range(len(nums)-1,-1,-1):
                if nums[i]=="0":
                    nums[i]="1"
                    one+=1
                if one == k:
                    break
        return nums

if __name__ == '__main__':
    S=Solution()
    x = str(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    res=S.minBinNum(x,k)
    s=""
    for each in  res:
        s+=f"{each}"
    print(s.strip())