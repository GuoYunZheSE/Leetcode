class Solution:
    def __init__(self):
        self.dic={}
        self.memo={}
        self.word=[]
        self.res=[]

    def decomposition(self):
        for i in self.word:
            if self.dic.__contains__(len(i)):
                temp=self.dic.get(len(i))
                temp.append(i)
                self.dic.update({len(i):temp})
            else:
                self.dic.setdefault(len(i),[i])

    def connected(self,small:str,big:str):
        for each in small:
            if not big.__contains__(each):
                return False
        return True

    def next(self,orign:str,s:str,curr:int):
        if s in self.dic.get(max(self.dic.keys())):
            self.res.append(curr)
            self.memo.setdefault(orign,curr)
            return True
        count=1
        if self.dic.get(len(s)+count)==None:
            self.res.append(curr)
            self.memo.setdefault(orign, curr)
            while self.dic.get(len(s)+count)==None:
                count+=1
            strs=self.dic.get(len(s)+count)
            for each in strs:
                if not self.memo.keys().__contains__(each):
                    self.next(each,each,1)
        else:
            strs = self.dic.get(len(s) + count)
            for each in strs:
                if self.connected(s,each):
                    self.next(orign,each,curr+1)
                else:
                    self.res.append(curr)
                    if not self.memo.keys().__contains__(each):
                        self.next(each,each,1)

    def longestStrChain(self, words: [str]) -> int:
        if len(words)==1:
            return 1
        else:
            self.word=words
            self.decomposition()
            minLength=min(self.dic.keys())
            for each in self.dic.get(minLength):
                self.next(each,each,1)
        return max(self.res)

if __name__ == '__main__':
    S=Solution()
    print(S.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))