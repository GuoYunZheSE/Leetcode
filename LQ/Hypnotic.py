# @Date    : 23:24 03/04/2020
# @Author  : ClassicalPi
# @FileName: Hypnotic.py
# @Software: PyCharm

import time


# 避免天天服用安眠药，防止身体和心理产生一定的瘾性和耐药性。安眠药尽可能短期服用，最长周期不要超过四个星期。
# 也不能突然停药，否则会引起强烈的戒断反应，出现恶心、焦虑、烦躁和反弹性失眠

# 如有安眠药戒断需求，一定要采取日渐递减法减量，好眠君建议，第一周先减1/4药量，当睡眠良好稳定后，第二周方可再减1/4药量，
# 如果同时服用多种安眠药，要选择一种药物，再采用递减法减量。

def getSchedule(medicine:int)->[]:
    schedule=[]

    ticks = time.time()
    count=0
    day=0
    circle=0
    while medicine>0:
        while (count==0 and day<7) or (count==1 and day<12) or (count==2 and day<20) or (count==3 and day<10):
            dt = time.strftime("%Y-%m-%d", time.localtime(ticks+circle*86400))
            schedule.append(["{}:{}".format(dt,1-count*0.25)])
            medicine-=(1-count*0.25)
            day+=1
            circle+=1
        day=0
        if count<3:
            count+=1
    return schedule

if __name__ == '__main__':
    s=getSchedule(29)
    for each in s:
        print(each)