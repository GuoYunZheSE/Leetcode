
#ifndef CPPVERSION_11_H
#define CPPVERSION_11_H

#endif //CPPVERSION_11_H

#include <vector>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int res=0;
        int left=0;
        int right=height.size()-1;
        while (left<right){
            res=std::max(res,std::min(height[left],height[right])*(right-left));
            if (height[left]<height[right]){
                left+=1;
            } else{
                right-=1;
            }
        }
        return res;
    }
};