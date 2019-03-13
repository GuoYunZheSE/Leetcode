# Runtime: 40 ms, faster than 79.32% of Python3 online submissions for Range Addition II.
# Memory Usage: 14.2 MB, less than 16.67% of Python3 online submissions for Range Addition II.
class Solution:
    def maxCount(self, m: int, n: int, ops: [[int]]):
        if not ops:
            return m*n
        return min(op[0] for op in ops)*min(op[1] for op in ops)