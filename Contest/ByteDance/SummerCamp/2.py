# @Date    : 10:35 08/01/2020
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm
import sys
class Solution():
    def whereIsMachine(self):
        def find_ip(net:str):

        n = int(sys.stdin.readline().strip())
        m = int(sys.stdin.readline().strip())
        server_room={}
        for i in range(n):
            ro