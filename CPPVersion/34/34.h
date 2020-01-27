//
// Created by 郭蕴喆 on 2020/1/27.
//

#ifndef CPPVERSION_34_H
#define CPPVERSION_34_H

#include <vector>
class Solution {
public:
    std::vector<int> searchRange(std::vector<int>& nums, int target) {
        int begin=-1;
        if (nums.empty()){
            std::vector<int> temp ({-1,-1});
            return temp;
        }
        int end=nums.size()+1;
        int count=0;
        for(std::vector<int>::const_iterator it=nums.begin();it!=nums.end();it++){
            if(*it==target){
                begin=count;
                break;
            }
            count+=1;
        }
        count=nums.size()-1;
        for(std::vector<int>::const_iterator it=nums.end()-1;it>=nums.begin();it--){
            if(*it==target){
                end=count;
                break;
            }
            count-=1;
        }
        if(begin==-1 || end==nums.size()){
            std::vector<int> temp ({-1,-1});
            return temp;
        } else{
            std::vector<int> temp ({begin,end});
            return temp;
        }
    }
};
#endif //CPPVERSION_34_H
