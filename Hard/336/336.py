# @Date    : 23:32 07/08/2020
# @Author  : ClassicalPi
# @FileName: 336.py
# @Software: PyCharm
class TRIE:
    def __init__(self):
        self.root={}
        self.END=-1

    def insert(self,word:str,index:int)->None:
        curNode=self.root
        for eachchar in word:
            if not curNode.__contains__(eachchar):
                curNode.setdefault(eachchar,{})
            curNode=curNode[eachchar]
        curNode[self.END]=True
        curNode["index"]=index

    def search(self,word:str)->bool:
        curNode=self.root
        for eachchar in word:
            if not curNode.__contains__(eachchar):
                return False
            curNode=curNode[eachchar]

        if curNode[self.END]==True:
            return True
        else:
            return False

class Solution:
    def isPalindrome(self,case:str)->bool:
        left=0
        right=len(case)-1
        while left<=right:
            if case[left]==case[right]:
                left+=1
                right-=1
            else:
                return False
        return True

    def palindromePairs(self, words: [str]) -> [[int]]:
        trie=TRIE()
        for index,eachword in enumerate(words):
            trie.insert(eachword,index)
        res=[]
        for eachword in words:
            for i in range(len(eachword)):
                if 