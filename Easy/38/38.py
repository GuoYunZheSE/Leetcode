# @Date    : 15:15 10/06/2020
# @Author  : ClassicalPi
# @FileName: 38.py
# @Software: PyCharm
import re
class Solution:
    def countAndSay(self, n: int) -> str:
        start="1"
        for i in range(n-1):
            p = re.compile(r"([0-9])(\1*)")
            start=p.sub(lambda m: str(1 + len(m.group(2)))+str(m.group(1)), start)
        return start
if __name__ == '__main__':
    S=Solution()
    print(S.countAndSay(1))