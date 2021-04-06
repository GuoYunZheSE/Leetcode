# @Date    : 11:46 04/06/2021
# @Author  : ClassicalPi
# @FileName: 126.py
# @Software: PyCharm
import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        wordSet=set(wordList)
        queue=collections.deque([[beginWord,{beginWord}]])

        charSet=set()
        for word in wordList:
            for c in word:
                charSet.add(c)

        res=[]
        while queue:
            word,paths=queue.popleft()
            if word==endWord:
                if res is []:
                    res.append(paths)
                else:
                    if len(paths)<=len(res[0]):
                        res.append(paths)
                continue
            for i in range(len(word)):
                for c in charSet:
                    temp=word[0:i]+c+word[i+1:]
                    if temp in wordSet and temp not in paths:
                        queue.append([temp,paths+{temp}])
        return res