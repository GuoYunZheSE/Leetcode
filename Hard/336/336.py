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

    def search(self,word:str)->[bool,int]:
        curNode=self.root
        for eachchar in word:
            if not curNode.__contains__(eachchar):
                return [False,0]
            curNode=curNode[eachchar]

        if curNode.__contains__(self.END):
            return [True,curNode["index"]]
        else:
            return [False,0]

class Solution:
    def isPalindrome(self,case:str)->bool:
        if case=="" or len(case)==1:
            return True
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
        for index,eachword in enumerate(words):
            for i in range(len(eachword)):
                if self.isPalindrome(eachword[0:i]):
                    result=trie.search(eachword[i:][::-1])
                    if result[0] and result[1]!=index:
                        res.append([result[1],index])
            if eachword=="":
                for index2,eachword in enumerate(words):
                    if self.isPalindrome(eachword):
                        if index!=index2:
                            res.append([index2,index])
                            res.append([index,index2])
        return res
if __name__ == '__main__':
    S=Solution()
    words=["abcd","dcba","lls","s","sssll",""," "]
    print(S.palindromePairs(words))