# @Date    : 22:30 08/21/2021
# @Author  : ClassicalPi
# @FileName: 5834.py
# @Software: PyCharm
class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        if not word:
            return res
        cur = 'a'
        for c in word:
            if ord(c) == ord(cur):
                res += 0
            if ord(c) > ord(cur):
                res += min(ord(c)-ord(cur),ord(cur)-ord(c)+26)
            if ord(cur) > ord(c):
                res += min(ord(cur) - ord(c), ord(c) - ord(cur) + 26)
            cur = c
        return res + len(word)
if __name__ == '__main__':
    S = Solution()
    print(S.minTimeToType("bza"))