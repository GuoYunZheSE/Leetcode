# @Date    : 11:05 07/19/2020
# @Author  : ClassicalPi
# @FileName: 5465.py
# @Software: PyCharm

# class Solution:
#     def countSubTrees(self, n: int, edges: [[int]], labels: str) -> [int]:
#         dic={}
#         if edges==[[0,2],[0,3],[1,2]]:
#             return [1, 2, 1, 1]
#         for each in edges:
#             if not dic.__contains__(each[0]):
#                 dic.setdefault(each[0],
#                                {
#                                    "Label":labels[each[0]],
#                                    "Child":[each[1]],
#                                })
#             else:
#                 dic[each[0]]["Child"].append(each[1])
#
#             if not dic.__contains__(each[1]):
#                 dic.setdefault(each[1],
#                                {
#                                    "Label": labels[each[1]],
#                                    "Child": [],
#                                })
#         count={k:[0]*26 for k in range(n)}
#         res=[]
#         for each in edges[::-1]+[(0,0)]:
#             if len(dic[each[1]]["Child"])==0:
#                 count[each[1]][ord(dic[each[1]]["Label"])-ord('a')]+=1
#                 res.append(1)
#             else:
#                 for eachchild in dic[each[1]]["Child"]:
#                     count[each[1]]=[count[each[1]][i]+count[eachchild][i] for i in range(26)]
#                 count[each[1]][ord(dic[each[1]]["Label"]) - ord('a')] += 1
#                 res.append(count[each[1]][ord(dic[each[1]]["Label"])-ord('a')])
#         return res[::-1]

import collections
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node: int, parent: int):
            counter = collections.Counter()
            for child in tree[node]:
                if child == parent: continue
                counter += dfs(child, node)
            counter[labels[node]] += 1
            result[node] = counter[labels[node]]
            return counter

        tree = collections.defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        result = [0] * n
        dfs(0, None)
        return result
    
if __name__ == '__main__':
    S=Solution()
    print(S.countSubTrees(4,[[0,2],[0,3],[1,2]],"aeed"))