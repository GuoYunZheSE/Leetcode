class Solution:
    def __init__(self):
        self.trace={
            'N':0,
            'S':0,
            'E':0,
            'W':0
        }

    def changeDirection(self,curr:chr,direction:chr)->chr:
        temp={
            0:'N',
            1:'E',
            2:'S',
            3:'W'
        }
        if curr=='N':
            curr=0
        elif curr=='E':
            curr=1
        elif curr=='S':
            curr=2
        else:
            curr=3
        if direction=='R':
            return temp.get((curr+1)%4)
        else:
            return temp.get((curr-1)%4)

    def check(self)->bool:
        if self.trace['N']==self.trace['S']:
            if self.trace['W']==self.trace['E']:
                return True
            return False
        return False

    def draw(self,coordinate:[[]],direction:chr):
        temp=''
        if direction=='N':
            self.row-=1
            temp='^'
        if direction=='S':
            self.row+=1
            temp = 'v'
        if direction=='E':
            self.col+=1
            temp = '>'
        if direction == 'W':
            self.col-=1
            temp = '<'
        coordinate[self.row][self.col]=temp
        for r in coordinate:
            print(r)
        print("**********************************************************")


    def isRobotBounded(self, instructions: str) -> bool:
        current='N'
        # coordinate=[['0' for col in range(10)] for row in range(10)]
        # self.row=int(len(coordinate)/2)
        # self.col=int(len(coordinate[0])/2)
        # coordinate[self.row][self.col] = '$'
        for i in range(0,4):
            for each in instructions:
                if each=='G':
                    self.trace[current]+=1
                    # self.draw(coordinate,current)
                    continue
                if each=='L' or each=='R':
                    current=self.changeDirection(current,each)
                    continue
            if self.check():
                return True
        return False

if __name__ == '__main__':
    s=Solution()
    ins="RLLGGLRGLGLLLGRLRLRLRRRRLRLGRLLLGGL"
    print(s.isRobotBounded(ins))


