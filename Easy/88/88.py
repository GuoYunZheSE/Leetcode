# @Date    : 20:24 03/16/2021
# @Author  : ClassicalPi
# @FileName: 88.py
# @Software: PyCharm
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp=[]
        i,j=0,0
        nums3=nums1[0:m]
        while i < len(nums3) and j < len(nums2):
            if nums3[i]<=nums2[j]:
                temp.append(nums3[i])
                i+=1
            else:
                temp.append(nums2[j])
                j+=1
        if j==len(nums2):
            temp+=nums3[i:]
        else:
            temp+=nums2[j:]
        for i in range(m+n):
            nums1[i]=temp[i]


if __name__ == '__main__':
    S=Solution()
    n1=[1,2,3,0,0,0]
    # S.merge(n1,3,[2,5,6],3)
    # print(n1)
    S.merge([1, 2, 3, 0, 0, 0], 3, [], 0)
    S.merge([1], 1, [], 0)
    S.merge([], 0, [], 0)