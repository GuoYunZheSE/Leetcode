# @Date    : 10:23 03/04/2020
# @Author  : ClassicalPi
# @FileName: Presum.py
# @Software: PyCharm

import typing
class Solution(object):
    def numSubarraysWithSum(self, A:typing.List[int], S)->int:
        presum=[0]
        res=0
        for each in A:
            presum.append(presum[-1]+each)
        # [0,1,1,2,2,3]
        left,right=0,0
        for right in range(0,len(presum)):
            if presum[right]-presum[left]==S:
                res+=1
            while presum[right]-presum[left]>S:
                if presum[right] - presum[left] == S:
                    res += 1
                left+=1

        return res
if __name__ == '__main__':
    A=[1,0,1,0,1]
    S=2
    s=Solution()
    print(s.numSubarraysWithSum(A,S))