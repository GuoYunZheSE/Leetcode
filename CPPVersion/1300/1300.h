//
// Created by 郭蕴喆 on 2020/2/4.
//

#ifndef CPPVERSION_1300_H
#define CPPVERSION_1300_H

#include <vector>
#include <algorithm>
#include <cmath>

class Solution {
public:
    int findBestValue(std::vector<int>& arr, int target) {
        std::sort(arr.begin(),arr.end());
        int sumption=0;
        int length=arr.size();
        for (int i = 0; i < arr.size(); ++i) {
            int ans=round((double(target)-double(sumption))/length);
            if (ans<=arr[i]){
                if (target-((ans-1)*length+sumption)==((ans*length+sumption)-target))
                {
                    return ans-1;
                }
                return ans;
            }
            sumption+=arr[i];
            length-=1;
        }
        return arr[-1];
    }
};
#endif //CPPVERSION_1300_H
