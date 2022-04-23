# @Date    : 11:03 04/23/2022
# @Author  : ClassicalPi
# @FileName: 30.py
# @Software: PyCharm

import collections
class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        word_length = len(words[0])
        window_size = len(words) * word_length
        words_dic = dict(collections.Counter(words))
        res = []

        if window_size > len(s):
            return []
        for i in range(0, len(s) - window_size + 1):
            substring = s[i:i + window_size]
            subwords_dic = collections.defaultdict(int)
            for j in range(0, len(substring) - word_length + 1, word_length):
                subwords_dic[substring[j:j + word_length]] += 1
            if subwords_dic == words_dic:
                res.append(i)

        return res

if __name__ == '__main__':
    S = Solution()
    print(S.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))