//
// Created by 郭蕴喆 on 2020/2/14.
//

#ifndef CPPVERSION_42_H
#define CPPVERSION_42_H

#include <vector>
#include <stack>

class Solution {
public:
    int trap(std::vector<int>& height) {
        std::stack<int> s;
        int res=0;
        s.push(0);
        for (int i = 1; i < height.size(); ++i) {
            while (!s.empty() && height[i]>height[s.top()]){
                int top=s.top();
                s.pop();
                if (s.empty()){
                    break;
                }
                res+=(std::min(height[i],height[s.top()])-height[top])*(i-s.top()-1);
            }
            s.push(i);
        }
        return res;
    }
};
#endif //CPPVERSION_42_H
