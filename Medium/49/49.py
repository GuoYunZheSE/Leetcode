# @Date    : 12:24 01/06/2021
# @Author  : ClassicalPi
# @FileName: 49.py
# @Software: PyCharm

import collections
# # Time Limit Exceeded
# class Solution:
#     def groupAnagrams(self, strs: [str]) -> [[str]]:
#         dic={}
#         for eachstr in strs:
#             modify=False
#             for key,val in dic.items():
#                 if collections.Counter(eachstr)==collections.Counter(key):
#                     val=val.append(eachstr)
#                     modify=True
#             if not modify:
#                 dic.setdefault(eachstr,[eachstr])
#         return dic.values()

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

if __name__ == '__main__':
    S=Solution()
    print(S.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(S.groupAnagrams([""]))
    print(S.groupAnagrams(
["ddddddddddg","dgggggggggg"]))