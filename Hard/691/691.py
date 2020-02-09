class Solution:
    def __init__(self):
        self.dic={}

    def dictIni(self,stickers: [str], target: str)->None:
        self.dic.fromkeys(stickers)
        for eachSticker in stickers:
            temp=dict.fromkeys(eachSticker)
            for eachLetter in eachSticker:
                temp[eachLetter]=eachSticker.count(eachLetter)
            self.dic[eachSticker]=temp
        temp = dict.fromkeys(target)
        for eachLetter in target:
            temp[eachLetter] = target.count(eachLetter)
        self.dic[target] = temp

    def findLetter(self,target)->[str,int]:
        # Find the most usage sticker now.
        # Use grady to find it.
        maximum=["",-1]
        for sticker in self.dic.keys():
            temp=[sticker,0]
            if sticker!=target:
                for k, v in self.dic[target].items():
                    if self.dic[sticker].__contains__(k) and self.dic[target][k]>0:
                        temp[1]+=min(self.dic[sticker][k],v)
                        # temp[1]+=1
            if temp[1]>maximum[1]:
                maximum=temp
        return maximum

    def updateDic(self,maximum:[str,int],targer:str):
        # Update the system dictionary using the most helpful sticker.
        for k,v in self.dic[maximum[0]].items():
            if self.dic[targer].__contains__(k):
                if self.dic[targer][k]-v>=0:
                    self.dic[targer][k]-=v
                else:
                    self.dic[targer][k]=0

    def minStickers(self, stickers: [str], target: str) -> int:
        self.dictIni(stickers,target)
        ans=0
        while sum(self.dic[target].values())>0:
            ans+=1
            maximum=self.findLetter(target)
            if maximum[1]==0:
                return -1
            self.updateDic(maximum,target)
        return ans

if __name__ == '__main__':
    stickers,target=["these","guess","about","garden","him"],"atomher"
    s=Solution()
    print(s.minStickers(stickers,target))