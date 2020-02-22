import typing
class bigger(int):
    def __lt__(self, other):
        ca=bin(self).count('1')
        co=bin(other).count('1')
        return (ca<co or (ca==co and int(self)<int(other)))
class Solution:
    def sortByBits(self, arr: typing.List[int]) -> []:
        arr.sort(key=bigger)
        return arr

if __name__ == '__main__':
    nums=[10]
    s=Solution()
    print(s.sortByBits(nums))