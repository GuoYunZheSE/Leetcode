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

# # Backtracking-2
# class Solution:
#     def canJump(self, nums: [int]) -> bool:
#         def subJump(position:int, nums:[int]):
#             if position==len(nums)-1:
#                 return True
#             furthest=min(len(nums)-1,position+nums[position])
#             for nextPosition in range(furthest,position-1,-1):
#                 if subJump(nextPosition,nums):
#                     return True
#             return False
#         return subJump(0,nums)

# # DP: Top-Down
# class Solution:
#     def canJump(self, nums: [int]) -> bool:
#         self.memo=[0]*len(nums)
#         self.memo[-1]=1
#         def subJump(position:int, nums:[int]):
#             if self.memo[position]!=0:
#                 return self.memo[position]==1
#             furthest=min(len(nums)-1,position+nums[position])
#             for nextPosition in range(position+1,furthest+1):
#                 if subJump(nextPosition,nums):
#                     self.memo[position]=1
#
#                     return True
#             return False
#         return subJump(0,nums)

# DP: Bottom-Up
class Solution:
    def canJump(self, nums: [int]) -> bool:
        self.memo=[0]*len(nums)
        self.memo[-1]=1
        for position in range(len(nums)-1,-1,-1):
            furthest = min(len(nums) - 1, position + nums[position])
            if self.memo[position] != 0:
                return self.memo[position] == 1
            if subJump(nextPosition,nums):
                self.memo[position]=1

                return True
            return False
        return self.memo[0]==1
if __name__ == '__main__':
    S=Solution()
    print(S.canJump([4,2,1,0,9,2,1,4,3,2,5,3,1]))
