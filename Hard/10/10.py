# @Date    : 21:17 07/28/2020
# @Author  : ClassicalPi
# @FileName: 10.py
# @Software: PyCharm
import collections
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])



if __name__ == '__main__':
    S=Solution()
    print(S.isMatch("aa","a"))
    print(S.isMatch("aa", "a*"))
    print(S.isMatch("ab", ".*"))
    print(S.isMatch("aa", "a"))