# @Date    : 19:26 04/15/2021
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm
import collections
import sys
class Solution:
    def game_number(self,nums:[],k:int):
        status=[i for i in nums]
        dividable=0 if status[0]%k!=0 else 1
        for i in range(1,len(nums)):
            status[i]+=status[i-1]
            if status[i]%k==0:
                dividable+=1
        res=dividable
        for i in range(1,len(status)):
            if status[i-1]%k==0:
                dividable-=1
                res+=dividable
            else:
                for num in status[i:]:
                    if (num-status[i-1])%k==0:
                        res+=1
        return res
        # res=0
        # for i in range(0,len(nums)):
        #     SUM=nums[i]
        #     if SUM % k == 0:
        #         res += 1
        #     for num in nums[i+1:]:
        #         SUM+=num
        #         if SUM%k==0:
        #             res+=1
        # return res

if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    nums=[int(i) for i in line.split(" ")]
    S=Solution()
    print(S.game_number(nums,k))