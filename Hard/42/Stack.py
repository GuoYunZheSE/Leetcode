class Solution:
    def trap(self, height: [int]) -> int:

        if not height:
            return 0

        stack=[0]
        res=0

        for i in range(1,len(height)):

            while stack and height[i]>height[stack[-1]]:
                top=stack[-1]
                stack.pop(-1)
                if not stack:
                    break
                res+=(i-stack[-1]-1)*(min(height[i],height[stack[-1]])-height[top])

            stack.append(i)


        return res

if __name__ == '__main__':
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    S=Solution()
    print(S.trap(height))