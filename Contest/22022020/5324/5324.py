import typing
class Cashier:

    def __init__(self, n: int, discount: int, products: typing.List[int], prices: typing.List[int]):
        self.n=n
        self.discount=discount
        self.products=products
        self.prices=prices
        self.dic={}
        for i in range(0,len(products)):
            self.dic.setdefault(products[i],prices[i])
        self.curr=0

    def getBill(self, product: typing.List[int], amount: typing.List[int]) -> float:
        self.curr+=1
        bill=0.0
        for i in range(0,len(product)):
            bill+=(amount[i]*self.dic[product[i]])
        if self.curr==self.n:
            self.curr=0
            bill-=(self.discount*bill)/100
        return bill

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)