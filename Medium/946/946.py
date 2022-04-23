# @Date    : 00:07 04/24/2022
# @Author  : ClassicalPi
# @FileName: 946.py
# @Software: PyCharm

import collections
class Solution:
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        pushed_deque = collections.deque(pushed)
        popped_deque = collections.deque(popped)
        cur = collections.deque([])

        while popped_deque:
            if cur and (cur[-1] != popped_deque[0] and len(pushed_deque) == 0):
                return False
            while not cur or cur[-1] != popped_deque[0] and pushed_deque:
                cur.append(pushed_deque.popleft())
            cur.pop()
            popped_deque.popleft()
        return True

if __name__ == '__main__':
    S = Solution()
    print(S.validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))
    print(S.validateStackSequences([1,2,3,4,5,6,7],[1,2,5,3,6,7,4]))