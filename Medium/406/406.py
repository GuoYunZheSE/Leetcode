# @Date    : 17:21 04/23/2022
# @Author  : ClassicalPi
# @FileName: 406.py
# @Software: PyCharm

class Solution:
    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        for p in people:
            res.insert(p[1],p)
        return res