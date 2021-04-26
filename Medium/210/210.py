# @Date    : 15:39 04/26/2021
# @Author  : ClassicalPi
# @FileName: 210.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.courseDic={int:[[int],str,0,0]}
        self.time=-1
        self.res=[]
        self.hasCycle=False
    def getTime(self):
        self.time+=1
        return self.time
    def DFS(self,courseID:int):
        currentCourse=self.courseDic[courseID]
        currentCourse[1]="Gray"
        currentCourse[2]=self.getTime()
        for afterCourse in currentCourse[0]:
            if self.courseDic[afterCourse][1]=="White":
                self.DFS(afterCourse)
            elif self.courseDic[afterCourse][1]=="Gray":
                self.hasCycle=True
                return
        currentCourse[3]=self.getTime()
        currentCourse[1]="Black"
        self.res.append(courseID)
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        for i in range(numCourses):
            self.courseDic.setdefault(i,[[],"White",0,0])
        for prerequisite in prerequisites:
            self.courseDic[prerequisite[1]][0].append(prerequisite[0])
        for courseID in range(numCourses):
            if self.hasCycle:
                return []
            if self.courseDic[courseID][1]=="White":
                self.DFS(courseID)
        return self.res[::-1]