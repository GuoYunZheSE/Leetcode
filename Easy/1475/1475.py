# @Date    : 23:13 04/26/2022
# @Author  : ClassicalPi
# @FileName: 1475.py
# @Software: PyCharm
class Solution:
    def finalPrices(self, prices: [int]) -> [int]:
        order_dic = {}
        mono_stack = []
        for index, price in enumerate(prices):
            while mono_stack and mono_stack[-1][1] >= price:
                order_dic.setdefault(mono_stack[-1][0], price)
                mono_stack.pop()
            mono_stack.append((index, price))
        for index, price in enumerate(prices):
            prices[index] -= order_dic.get(index, 0)
        return prices

if __name__ == '__main__':
    S = Solution()
    print(S.finalPrices([]))