class Solution:

    def dicini(self,height:[int]):
        self.dict={}
        for i in range(len(height)):
            if self.dict.__contains__(height[i]):
                self.dict[height[i]].append(i)
            else:
                self.dict.setdefault(height[i],[i])

    def get_area(self,l:[])->int:
        area=0
        begin=l[0]
        for i in l:
            if begin==i:
                continue
            else:
                area+=i-begin-1
                begin=i
        return area

    def trap(self, height: [int]) -> int:
        res=0
        self.dicini(height)
        height_increase = sorted(list(self.dict.keys()),reverse=True)
        f=0
        s=1
        while s<len(height_increase):
            first=height_increase[f]
            second=height_increase[s]
            if len(self.dict[first])==1:
                self.dict[second]+=self.dict[first]
                f+=1
                s+=1
            else:
                area=self.get_area(sorted(self.dict[first]))
                res+=area*(first-second)
                self.dict[second]+=self.dict[first]
                f+=1
                s+=1
        return res