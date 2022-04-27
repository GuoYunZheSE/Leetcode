# @Date    : 00:03 04/26/2022
# @Author  : ClassicalPi
# @FileName: 752.py
# @Software: PyCharm

import collections
class Solution:
    def openLock(self, deadends: [str], target: str) -> int:
        passed = set()
        deadends = set(deadends)
        queue = collections.deque([(0,0,0,0,0)])
        if "0000" in deadends:
            return -1
        while queue:
            dist, wheel_1, wheel_2, wheel_3, wheel_4 = queue.popleft()
            wheels = [dist, wheel_1, wheel_2, wheel_3, wheel_4]
            if f"{wheel_1}{wheel_2}{wheel_3}{wheel_4}" == target:
                return dist
            for i in range(1,5):
                candidates = []
                new_wheels = wheels.copy()
                new_wheels[0] = dist + 1
                new_wheels[i] = (new_wheels[i] - 1 + 10) % 10
                candidates.append(tuple(new_wheels))
                new_wheels[i] = (new_wheels[i] + 2 + 10) % 10
                candidates.append(tuple(new_wheels))
                for candidate in candidates:
                    candidate_wheels = f"{candidate[1]}{candidate[2]}{candidate[3]}{candidate[4]}"
                    if candidate_wheels not in deadends and candidate_wheels not in passed:
                        passed.add(candidate_wheels)
                        queue.append(candidate)
        return -1

if __name__ == '__main__':
    S = Solution()
    print(S.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))