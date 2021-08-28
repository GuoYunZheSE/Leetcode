# @Date    : 17:05 08/14/2021
# @Author  : ClassicalPi
# @FileName: 395.py
# @Software: PyCharm
import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        uniqueLetterNumber = len(set(s))
        res = 0
        for selectedUniqueNumber in range(1,uniqueLetterNumber+1):
            window = collections.deque([])
            windowMap = {}
            curK = 0
            curUniqueLetterNumber = 0
            right = 0
            while right < len(s):
                c = s[right]
                if curUniqueLetterNumber <= selectedUniqueNumber:
                    if windowMap.get(c,0) == 0:
                        curUniqueLetterNumber += 1
                    windowMap[c] = windowMap.get(c,0) + 1
                    window.append(c)
                    if windowMap[c] == k:
                        curK += 1
                    right += 1
                else:
                    popTemp = window.popleft()
                    if windowMap[popTemp]==1:
                        curUniqueLetterNumber -= 1
                    if windowMap[popTemp]==k:
                        curK -= 1
                    windowMap[popTemp] -= 1
                if curUniqueLetterNumber == selectedUniqueNumber and curK == curUniqueLetterNumber:
                    res = max(res,len(window))
        return res

if __name__ == '__main__':
    S = Solution()
    print(S.longestSubstring("bbaaacbd",3))