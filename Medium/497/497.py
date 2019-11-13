import random
class Solution:

    def __init__(self, rects: [[int]]):
        self.rec=[]
        self.used={}
        self.x=0
        self.y=0
        self.index=-1
        for eachRect in rects:
            self.rec.append([[eachRect[0],eachRect[2]],[eachRect[1],eachRect[3]]])

    def pick(self) -> [int]:
        if self.index==-1:
            self.index=0
            self.x=self.rec[self.index][0][0]
            self.y=self.rec[self.index][1][0]
        if self.index<len(self.rec):
            if self.y<=self.rec[self.index][1][1]:
                self.y=self.y+1
                return [self.x,self.y-1]
            else:
                if self.x<self.rec[self.index ][0][1]:
                    self.x=self.x+1
                    self.y=self.rec[self.index][1][0]+1
                    return [self.x,self.y-1]
                else:
                    if self.index!=len(self.rec)-1:
                        self.index+=1
                        self.x=self.rec[self.index][0][0]
                        self.y=self.rec[self.index][1][0]
                        return self.pick()
                    else:
                        self.index = -1
                        return self.pick()
        else:
            self.index=-1
            return self.pick()

if __name__ == '__main__':
    S=Solution([[82918473, -57180867, 82918476, -57180863], [83793579, 18088559, 83793580, 18088560], [66574245, 26243152, 66574246, 26243153], [72983930, 11921716, 72983934, 11921720]])
    i=0
    while i <10000:
        i+=1
        print("{}:{}".format(i,S.pick()))
