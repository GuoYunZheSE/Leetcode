class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        ans=0
        if n==0:
            return True
        if len(flowerbed)==1:
            return flowerbed[0]==0 and n==1
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if i==0:
                    if flowerbed[i+1]==0:
                        flowerbed[i]=1
                        ans+=1
                elif i==len(flowerbed)-1:
                    if flowerbed[i-1]==0:
                        flowerbed[i] = 1
                        ans+=1
                else:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        flowerbed[i] = 1
                        ans+=1
        return ans>=n
if __name__ == '__main__':
    s=Solution()
    print(s.canPlaceFlowers([1,0,0,0,0,1],2))