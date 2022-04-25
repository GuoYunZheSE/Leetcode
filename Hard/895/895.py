# @Date    : 10:12 04/24/2022
# @Author  : ClassicalPi
# @FileName: 895.py
# @Software: PyCharm

import collections
class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(val)
    def pop(self) -> int:
        res = self.group[self.max_freq].pop()
        self.freq[res] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return res
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()