# Runtime: 240 ms, faster than 65.73% of Python3 online submissions for Advantage Shuffle.
# Memory Usage: 16.1 MB, less than 9.09% of Python3 online submissions for Advantage Shuffle.
class Solution:
    # def advantageCount(self, A:[int], B: [int]) -> [int]:
    #     if A==None or B==None:
    #         return None
    #     result = []
    #     for b in B:
    #         negitive=[]
    #         positive=[]
    #         for index, value in enumerate(A):
    #             if value-b>0:
    #                 positive.append([index, value - b])
    #             else:
    #                 negitive.append([index, value - b])
    #         min=[0,0]
    #         if  positive.__len__()==0:
    #             min=negitive[0]
    #             for i in negitive:
    #                 if i[1]<min[1]:
    #                     min=i
    #         else:
    #             min=positive[0]
    #             for j in positive:
    #                 if j[1]<min[1]:
    #                     min=j
    #         result.append(A[min[0]])
    #         A.remove(A[min[0]])
    #     return result
    def advantageCount(self, A:[int], B: [int]) -> [int]:
        A=sorted(A)
        import collections
        take=collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b<A[-1]:
                take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]
if __name__ == '__main__':
    A=[2,7,11,15]
    B=[1,10,4,11]
    S=Solution()
    S.advantageCount(A,B)
