# @Date    : 15:01 01/08/2021
# @Author  : ClassicalPi
# @FileName: 55.py
# @Software: PyCharm

# Time OUT
# class Solution:
#     def __init__(self):
#         self.res_map=[]
#     def canJump(self, nums: [int]) -> bool:
#         self.res_map=[0]*len(nums)
#         self.last_index=len(nums)-1
#         if len(nums)<=1:
#             return True
#         def jump(index:int):
#             if nums[index]==0:
#                 if self.res_map[index]==1:
#                     return True
#                 else:
#                     self.res_map[index]=-1
#                     return False
#             temp=[]
#             for i in range(1,nums[index]+1):
#                 if self.res_map[index+i]==1 or index+i==self.last_index:
#                     self.res_map[index]=1
#                     temp.append(True)
#                     return True
#                 elif self.res_map[index+i]==-1:
#                     temp.append(False)
#                 else:
#                     s=jump(index+i)
#                     if s:
#                         return True
#                     temp.append(s)
#             return any(temp)
#         return jump(0)

# Backtracking-2
class Solution:
    def canJump(self, nums: [int]) -> bool:
        def subJump(position:int, nums:[int]):
            if position==len(nums)-1:
                return True
            furthest=min(len(nums)-1,position+nums[position])
            for nextPosition in range(furthest,position-1,-1):
                if subJump(nextPosition,nums):
                    return True
            return False
        return subJump(0,nums)
if __name__ == '__main__':
    S=Solution()
    print(S.canJump([2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,3,1,2,2,1,5,2,4]))
