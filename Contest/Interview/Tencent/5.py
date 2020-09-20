# @Date    : 21:21 08/23/2020
# @Author  : ClassicalPi
# @FileName: 5.py
# @Software: PyCharm

#n选 任意个组员 其中一个是leader

if __name__ == '__main__':

    import sys

    n = int(sys.stdin.readline().strip())

    if 1 <= n and n <= 10 ** 9:
        sum1 = 0
        temp1 = n
        temp = 1
        for i in range(1, n + 1):
            print(i)
            temp = int(temp * temp1 // i) % (10 ** 9 + 7)
            sum1 += (temp * i)%(10 ** 9 + 7)
            temp1 -= 1
        print(sum1 % (10 ** 9 + 7))