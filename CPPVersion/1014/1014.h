//
// Created by 郭蕴喆 on 2020/2/6.
//

#ifndef CPPVERSION_1014_H
#define CPPVERSION_1014_H

#include <vector>
class Solution {
public:
    int maxScoreSightseeingPair(std::vector<int>& A) {
        int previousSpotValue=0;
        int previousSpotIndex=0;
        int count=0;
        int ans=0;
        for (int a:A){
            ans=std::max(ans,previousSpotIndex+previousSpotValue+a-count);
            if (a+count>previousSpotIndex+previousSpotValue){
                previousSpotIndex=count;
                previousSpotValue=a;
            }
            count+=1;
        }
        return ans;
    }
};
#endif //CPPVERSION_1014_H
