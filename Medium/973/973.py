# @Date    : 16:34 04/26/2021
# @Author  : ClassicalPi
# @FileName: 973.py
# @Software: PyCharm
import math
import random
import collections
class Solution:
    def QuickSelect(self,nums:[int],k:int):
        if not nums:
            return
        pivot=random.choice(nums)
        left=[]
        mid=[]
        right=[]
        for num in nums:
            if num<pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)
        if k<=len(left):
            self.QuickSelect(left,k)
        elif k>len(left)+len(mid):
            self.QuickSelect(right,k-len(left)-len(mid))
        else:
            return mid[0]
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        self.dic=collections.defaultdict(list)
        for point in points:
            self.dic[pow(point[0],2)+pow(point[1],2)].append(point)
        nums=list(self.dic.keys())
        # minDistance=self.QuickSelect(nums,k)
        # return self.dic[minDistance]
        count=0
        res=[]
        for num in sorted(nums):
            if count+len(self.dic[num])<=k:
                res.extend(self.dic[num])
                count+=len(self.dic[num])
        return res


if __name__ == '__main__':
    S=Solution()
    print(S.kClosest([[1,3],[-2,2]],1))
