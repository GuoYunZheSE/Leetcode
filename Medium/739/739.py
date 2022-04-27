# @Date    : 11:59 04/27/2022
# @Author  : ClassicalPi
# @FileName: 739.py
# @Software: PyCharm
class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        mono_stack = []
        order_dic = {}
        for index, val in enumerate(temperatures):
            while mono_stack and mono_stack[-1][1] < val:
                order_dic.setdefault(mono_stack[-1][0], index)
                mono_stack.pop()
            mono_stack.append((index,val))
        for index, val in enumerate(temperatures):
            temperatures[index] = order_dic.get(index, index) - index
        return temperatures

if __name__ == '__main__':
    S =Solution()
    print(S.dailyTemperatures([73,74,75,71,69,72,76,73]))