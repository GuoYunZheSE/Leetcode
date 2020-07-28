# @Date    : 20:21 07/22/2020
# @Author  : ClassicalPi
# @FileName: find_path.py
# @Software: PyCharm

# 你是一位系统管理员，手里有一份包含合法文件夹
# 列表，你的任务是找出该列表中包含文件数目最多的文件夹
import sys
class Solution:
    def findPath(self):
        n = int(sys.stdin.readline())
        Pathes=[]
        dic={}
        for i in range(n):
            line = sys.stdin.readline().strip('\n')
            if line !="" or " ":
                Pathes.append(line)

        for eachpath in Pathes:
            stack=[]
            temp=eachpath.split("/")
            if eachpath[0]!='/' or temp.count("")>1:
                continue
            for val in temp[1:]:
                if val==".":
                    continue
                elif val=="..":
                    stack.pop()
                else:
                    stack.append(val)
            for index,val in enumerate(stack):
                if index==len(stack)-1:
                    if not val.endswith(".txt"):
                        if not dic.__contains__(val):
                            dic.setdefault(val, {"Count": 0, "Exist": True})
                        else:
                            dic[val]["Exist"] = True
                else:
                    if not dic.__contains__(val):
                        dic.setdefault(val,{"Count": 0, "Exist": False})
                    if stack[-1].endswith(".txt"):
                        dic[val]["Count"]+=1
        res=[["null",0]]
        for key in list(dic.keys()):
            if dic[key]["Exist"]:
                if dic[key]["Count"]>res[0][1]:
                    res=[[key,dic[key]["Count"]]]
                elif dic[key]["Count"]==res[0][1]:
                    res.append([key,dic[key]["Count"]])

        RES=[]
        for each in res:
            for p in Pathes:
                if p[-1]==each[0] and not p.endswith(".txt"):
                    RES.append(p)
        RES.sort()
        if not RES:
            return "null"
        else:
            for each in RES:
                print(each)
if __name__ == '__main__':
    S=Solution()
    S.findPath()