# @Date    : 12:08 07/02/2020
# @Author  : ClassicalPi
# @FileName: 67.py
# @Software: PyCharm

# Input: a = "11", b = "1"
# Output: "100"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        a=a[::-1]
        b=b[::-1]
        c=""
        for i in range(max(len(a),len(b))):
            if i <len(a):
                carry+=int(a[i])
            if i <len(b):
                carry+=int(b[i])
            c+=str(carry%2)
            carry=carry//2
        if carry!=0:
            c+="1"
        return c[::-1]
if __name__ == '__main__':
    S=Solution()
    print(S.addBinary("11","1"))
    print(S.addBinary("10","1"))
    print(S.addBinary("1","1000"))
    print(S.addBinary("1010","1011"))
