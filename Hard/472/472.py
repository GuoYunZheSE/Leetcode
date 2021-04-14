# @Date    : 17:28 04/14/2021
# @Author  : ClassicalPi
# @FileName: 472.py
# @Software: PyCharm
class Solution:
    def findAllConcatenatedWordsInADict(self, words: [str]) -> [str]:
        wordSet=set(words)
        res=[False for i in words]
        for s in range(0,len(words)):
            word=words[s]
            temp=[True]
            for i in range(1,len(word)+1):
                temp+=any(temp[j] and word[j:i] in wordSet and word !=word[j:i] for j in range(i)),
            if len(word)<1:
                temp.append(False)
            res[s]=temp[-1]
        return [words[i] for i in range(0,len(words))if res[i]]
if __name__ == '__main__':
    S=Solution()
    print(S.findAllConcatenatedWordsInADict([""]))