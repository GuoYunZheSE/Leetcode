# @Date    : 21:41 02/28/2020
# @Author  : ClassicalPi
# @FileName: 904.py
# @Software: PyCharm
import typing
class Solution:
    def totalFruit(self, tree: typing.List[int]) -> int:
        basket={}
        left,right=0,0
        res=0
        for right in range(0,len(tree)):
            if basket.__contains__(tree[right]):
                basket[tree[right]]+=1
            else:
                basket.setdefault(tree[right],1)
            while len(basket)>2:
                basket[tree[left]]-=1
                if basket[tree[left]]==0:
                     basket.pop(tree[left])
                left+=1
            res=max(res,right-left+1)
        return res
if __name__ == '__main__':
    tree=[1,2,1]
    s=Solution()
    print(s.totalFruit(tree))