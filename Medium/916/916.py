# @Date    : 23:33 02/26/2020
# @Author  : ClassicalPi
# @FileName: 916.py
# @Software: PyCharm

import typing
import collections
class Solution:
    # def wordSubsets(self, A: typing.List[str], B: typing.List[str]) -> typing.List[str]:
    #     UnionB={}
    #     res=[]
    #     for b in B:
    #         temp=collections.Counter(b)
    #         for key,val in temp.items():
    #             if UnionB.__contains__(key):
    #                 UnionB[key]=max(UnionB[key],val)
    #             else:
    #                 UnionB.setdefault(key,val)
    #     for a in A:
    #         temp=collections.Counter(a)
    #         univer=True
    #         for key,val in UnionB.items():
    #             if (not temp.__contains__(key) ) or (temp[key]<val):
    #                 univer=False
    #         if univer:
    #             res.append(a)
    #     return res
    def wordSubsets(self, A, B):
        count = collections.Counter()
        for b in B:
            count = count | collections.Counter(b)
        return [a for a in A if collections.Counter(a) & count == count]
    def test(self,A: typing.List[str], B: typing.List[str],res:typing.List[str])->None:
        temp=self.wordSubsets(A, B)
        if temp==res:
            print(temp)
            print("Test Pass")
        else:
            print(temp)
            print("Test Failed")
if __name__ == '__main__':
    s=Solution()
    s.test(["amazon","apple","facebook","google","leetcode"],["e","o"],["facebook","google","leetcode"])
    s.test(["amazon","apple","facebook","google","leetcode"],["l","e"],["apple","google","leetcode"])
    s.test(["amazon","apple","facebook","google","leetcode"],["e","oo"],["facebook","google"])
    s.test(["amazon","apple","facebook","google","leetcode"],["lo","eo"],["google","leetcode"])
    s.test(["amazon","apple","facebook","google","leetcode"],["ec","oc","ceo"],["facebook","leetcode"])