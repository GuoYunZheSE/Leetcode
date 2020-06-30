# @Date    : 13:39 06/30/2020
# @Author  : ClassicalPi
# @FileName: 43.py
# @Software: PyCharm

# Input: num1 = "123", num2 = "456"
# Output: "56088"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Longer=num1
        # Shorter=num2
        # if len(num1)<len(num2):
        #     Longer=num2
        #     Shorter=num1
        if num2==0 or num1==0:
            return 0
        Product={}
        for key1,Multiplier1 in enumerate(num1[::-1]):
            for key2,Multiplier2 in enumerate(num2[::-1]):
                index=key2+key1+1
                value=int(Multiplier1)*int(Multiplier2)
                carrier=value//10
                rest=value%10
                if Product.__contains__(index):
                    Product[index]+=rest
                    if Product[index]>=10:
                        if Product.__contains__(index + 1):
                            Product[index + 1] += 1
                        else:
                            Product.setdefault(index + 1, 1)
                        Product[index]-=10
                else:
                    Product.setdefault(index,rest)
                if Product.__contains__(index+1):
                    Product[index+1]+=carrier
                    if Product[index+1]>=10:
                        if Product.__contains__(index + 2):
                            Product[index + 2] += 1
                        else:
                            Product.setdefault(index + 2, 1)
                        Product[index+1]-=10
                else:
                    Product.setdefault(index+1,carrier)
        res=""
        for i in range(max(list(Product.keys())),0,-1):
            if not (i==max(list(Product.keys())) and Product[i]==0):
                res+=str(Product[i])
        return res
if __name__ == '__main__':
    s1="213234243243242343242343212"
    s2="10223432432423432423442343211"
    S=Solution()
    print(213234243243242343242343212*10223432432423432423442343211)
    print(S.multiply(s1,s2))