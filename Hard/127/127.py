# @Date    : 21:20 04/05/2021
# @Author  : ClassicalPi
# @FileName: 127.py
# @Software: PyCharm
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        wordSet=set(wordList)
        queue=collections.deque([[beginWord,1]])
        while queue:
            word,path=queue.popleft()
            if word == endWord:
                return path
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    temp=word[0:i]+c+word[i+1:]
                    if temp in wordSet:
                        queue.append([temp,path+1])
                        wordSet.remove(temp)
        return 0
if __name__ == '__main__':
    S=Solution()
    endword='cog'
    beginword='hit'
    wl=["hot","dot","dog","lot","log","cog"]
    print(S.ladderLength(beginword,endword,wl))