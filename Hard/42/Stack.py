class Solution:
    def trap(self, height: [int]) -> int:
        stack = []
        res = 0
        for i in range(0,len(height)):
            while stack and height[i] > height[stack[-1]]:
                base = height[stack.pop()]
                if stack:
                    h = min(height[i],height[stack[-1]]) - base
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res
if __name__ == '__main__':
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    S=Solution()
    print(S.trap(height))