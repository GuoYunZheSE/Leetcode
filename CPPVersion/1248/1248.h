//
// Created by 郭蕴喆 on 2020/2/10.
//

#ifndef CPPVERSION_1248_H
#define CPPVERSION_1248_H

#include <vector>
class Solution {
public:
    int numberOfSubarrays(std::vector<int>& nums, int k) {
        int res=0;
        int curr=0;
        int i=0;
        int j=0;
        while (j<nums.size() or i<j){
            if (curr<k){
                if (nums[j]%2==1){
                    curr+=1;
                    j+=1;
                } else{
                    j+=1;
                }
            } else{
                if (nums[i]%2==0){
                    res+=1;
                    i+=1;
                } else{
                    if (j==nums.size()-1){
                        break;
                    }
                    if (nums[j]%2==1){
                        res+=1;
                        i+=1;
                        j+=1;
                    } else{
                        res+=1;
                        j+=1;
                    }
                }
            }
        }
        return res;
    }
};
#endif //CPPVERSION_1248_H
