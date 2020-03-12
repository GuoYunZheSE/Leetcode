# @Date    : 13:41 03/12/2020
# @Author  : ClassicalPi
# @FileName: Divide.py
# @Software: PyCharm

# 整除的数组
# 时间限制：C/C++语言 3000MS；其他语言 5000MS
# 内存限制：C/C++语言 131072KB；其他语言 655360KB
# 题目描述：
# 小美曾经有一个特殊的数组，这个数组的长度为n。但是她在打恐怖游戏的时候被吓得忘记了这个数组长什么样了。不过她还记得这个数组满足一些条件。
#
# 首先这个数组的每个数的范围都在L和R之间。包括端点。
#
# 除此之外，这个数组满足数组中的所有元素的和是k的倍数。
#
# 但是这样的数组太多了，小美想知道有多少个这样的数组。你只需要告诉她在模1e9+7意义下的答案就行了。

def find(l:int,r:int,k:int,num:int,equal:int,cur:int):
    if num*r<k:
        return
    while num*r>k:
        find(l,r,k,num,equal+k,cur)