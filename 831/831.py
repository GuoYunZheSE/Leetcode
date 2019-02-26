# Class:Medium
# Data:Friday, 26/02/2019
# Runtime: 52 ms, faster than 28.23% of Python3 online submissions for Masking Personal Information.
# Memory Usage: 12.9 MB, less than 16.67% of Python3 online submissions for Masking Personal Information.
class Solution:
    def maskAddr(self,S:str):
        name1,name2=S.split('@')
        name2,name3=name2.split('.')
        name1=""+name1[0]+"*****"+name1[-1]
        return name1.lower()+"@"+name2.lower()+"."+name3.lower()
    def maskPhone(self,S:str):
        Reserve = ['+', '-', '(', ')', ' ']
        numbers = []
        for eachchar in S:
            if eachchar not in Reserve:
                numbers.append(eachchar)
        code_length = numbers.__len__() - 10
        pre = ""
        for i in range(0, code_length):
            if i == 0:
                pre += "+"
            pre += "*"
            if i == code_length - 1:
                pre += "-"
        return pre + "***-" + "***-"+''.join(numbers[-4:])
    def maskPII(self, S: str) -> str:
        if '@' in S:
            return self.maskAddr(S)
        else:
            return self.maskPhone(S)
#         正则化方法
#         def maskPII(self, S):
#         S = S.lower()
#         S = re.sub(r"[\+\-\(\)\s]", r"", S)
#
#         m = re.search(r"(\d*)(\d{6})(\d{4})", S)
#         if m:
#             pref = ""
#             if m.group(1):
#                 pref = "+" + "*" * len(m.group(1)) + "-"
#
#             S = pref + "***-***-" + m.group(3)
#         else:
#             S = re.sub(r"([a-z])([a-z]*)([a-z])(@.*)", r"\1*****\3\4", S)
#             S = re.sub(r"[\+\-\(\)\s]", r"", S)
#
#         return S
if __name__ == '__main__':
    S="86-(10)12345678"
    def maskPhone(S: str):
        Reserve = ['+', '-', '(', ')', ' ']
        numbers = []
        for eachchar in S:
            if eachchar not in Reserve:
                numbers.append(eachchar)
        code_length = numbers.__len__() - 10
        pre = ""
        for i in range(0, code_length):
            if i == 0:
                pre += "+"
            pre += "*"
            if i == code_length - 1:
                pre += "-"
        numbers.reverse()
        numbers=numbers[0:4]
        numbers.reverse()
        return pre + "***-" + "***-".join(numbers)
    maskPhone(S)