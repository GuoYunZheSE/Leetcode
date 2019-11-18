# import sys
# class ExamRoom:
#
#     def __init__(self, N: int):
#         self.N=N
#         self.dic={}
#
#     def seat(self) -> int:
#
#         if self.dic=={}:
#             self.dic.setdefault({(self.N-1)*2:1})
#             return 0
#
#         maxDisstance=max(self.dic.keys())
#         MDpossitions = self.dic.get(maxDisstance)
#         LastMDP=-1
#
#         if maxDisstance%2==0 and self.dic.__contains__(maxDisstance-1):
#             MDpossitions2=[]
#             MDpossitions2+=self.dic.get(maxDisstance-1)
#             LastMDP1=min(MDpossitions)
#             LastMDP2=min(MDpossitions2)
#             if LastMDP1<=LastMDP2:
#                 LastMDP=LastMDP1
#             else:
#                 LastMDP=LastMDP2
#                 maxDisstance-=1
#
#         if LastMDP+(maxDisstance)/2==self.N:
#
#             if self.dic.__contains__((maxDisstance/2)-1):
#                 temp=self.dic.get((maxDisstance/2)-1)
#                 temp+=[LastMDP]
#                 self.dic.update({(maxDisstance/2)-1:temp})
#             else:
#                 self.dic.setdefault({(maxDisstance/2)-1:[LastMDP]})
#         else:
#             dis=int(maxDisstance/2)
#             if self.dic.__contains__(dis):
#                 temp=self.dic.get(dis)
#                 temp.append(LastMDP+dis)
#                 self.dic.update({dis:temp})
#             else:
#                 self.dic.setdefault({dis:[LastMDP+dis]})
#
#             if self.dic.__contains__(dis - 1):
#                 temp = self.dic.get(dis - 1)
#                 temp += [LastMDP]
#                 self.dic.update({dis - 1: temp})
#             else:
#                 self.dic.setdefault({dis - 1: [LastMDP]})
#
#         temp2=self.dic.get(maxDisstance)
#         temp2.remove(LastMDP)
#         if temp2==[]:
#             self.dic.pop(maxDisstance)
#         else:
#             self.dic.update({ maxDisstance:temp2})
#         return LastMDP
#
#     def leave(self, p: int) -> None:
#
#
# # Your ExamRoom object will be instantiated and called as such:
# # obj = ExamRoom(N)
# # param_1 = obj.seat()
# # obj.leave(p)
#
#
# # 1 0 0 1 0 1 0 0 0 0
# # 1 1 0 1 0 1 0 0 0 0
# # 1 0 0 0 0 0 0 0 0 1
# # 1 0 0 0 1 0 0 0 0 1
# # 1 0 1 0 1 0 0 0 0 1
# # 1 0 1 0 0 0 0 0 0 1
# # 1 0 1 0 0 1 0 0 0 1
