# @Date    : 20:10 04/23/2021
# @Author  : ClassicalPi
# @FileName: 207.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.hasCycle=False
        self.time=0
        self.courseDict={int:[[],int,int,int]}
    def getTime(self):
        self.time+=1
        return self.time-1
    def DFS(self,courseID:int):
        if self.hasCycle:
            return
        currentCourse=self.courseDict[courseID]
        currentCourse[1]=1
        currentCourse[2]=self.getTime()
        for eachcourse in currentCourse[0]:
            if self.courseDict[eachcourse][1]==0:
                self.DFS(eachcourse)
            elif self.courseDict[eachcourse][1]==1:
                self.hasCycle=True
        currentCourse[3]=self.getTime()
        currentCourse[1]=3
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        for courseID in range(numCourses):
            self.courseDict.setdefault(courseID,[[],0,0,0])
        for prerequisite in prerequisites:
            self.courseDict[prerequisite[1]][0].append(prerequisite[0])
        for courseID in range(numCourses):
            self.DFS(courseID)
        return not self.hasCycle
if __name__ == '__main__':
    S=Solution()
    print(S.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))