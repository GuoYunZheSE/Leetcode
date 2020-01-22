import math
class Solution:
    def __init__(self):
        self.combination=set()
        self.pathNums=0
        self.n=0

    def addTest(self,num:int)->int:
        count=0
        temp=self.combination.copy()
        if num not in self.combination:
            count+=1
        for i in self.combination:
            if (i+num) not in temp and (i+num)<=self.n:
                count+=1
                temp.add(i+num)
        return count

    def add(self,num:int):
        print("Add {}".format(num))
        temp=self.combination.copy()
        self.combination.add(num)
        for i in temp:
            self.combination.add(i+num)
        print("ADD FINISH")
        # print(self.combination)

    def check(self)->bool:
        for i in range(1,self.n+1):
            if i not in self.combination:
                return False
        return True

    def bisearch(self,l,r)->int:
        mid=int((l+r)/2)
        aTmid=self.addTest(mid)
        aTmidm1=self.addTest(mid-1)
        if r-l==1 or l==r:
            if aTmid>aTmidm1:
                return mid
            else:
                return mid-1
        if aTmid-aTmidm1>0:
            return self.bisearch(mid+1,r)
        elif aTmid-aTmidm1<0:
            return self.bisearch(l,mid-1)
        else:
            print("Find:{}".format(mid))
            return mid

    def minPatches(self, nums: [int], n: int) -> int:
        self.n=n
        for i in nums:
            if len(self.combination)==0:
                self.combination.add(i)
            else:
                temp=self.combination.copy()
                for t in temp:
                    self.combination.add(t+i)
                self.combination.add(i)
        print('Initial combination:{}'.format(self.combination))
        if self.check():
            return 0
        else:
            if self.n<=64:
                while not self.check():
                    temp={}
                    for i in range(1,abs(n)+1):
                        aT = self.addTest(i)
                        if len(temp)>1:
                            if aT<=max(temp.values()):
                                break
                            temp.update({i: aT})
                        else:
                            temp.update({i:aT})
                    print(temp)
                    for k,v in temp.items():
                        if v==max(temp.values()):
                            self.add(k)
                            self.pathNums+=1
                            break
            else:
                while not self.check():
                    path=self.bisearch(1,n)
                    self.add(path)
                    self.pathNums += 1
                    print(self.pathNums)
            return self.pathNums

if __name__ == '__main__':
    S=Solution()
    print(S.minPatches([1,2,31,33],2147483647))