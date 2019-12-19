//
// Created by 郭蕴喆 on 2019/12/18.
//

#ifndef CPPVERSION_349_H
#define CPPVERSION_349_H

#endif //CPPVERSION_349_H

#include <vector>
#include <unordered_set>
class Solution {
public:
    std::vector<int> intersection(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::vector<int> res;
        std::unordered_set<int> temp;
        std::vector<int> smaller=nums1;
        std::vector<int> bigger=nums2;

        if(nums1.size()>=nums2.size()){
            smaller=nums2;
            bigger=nums1;
        }

        for(std::vector<int>::iterator it=smaller.begin();it!=smaller.end();it++){
            std::vector<int>::iterator find=bigger.begin();
            while (find!=bigger.end()&&*find!=*it){
                find++;
            }
            if (find!=bigger.end()){
                if (temp.find(*it)==temp.end()){
                    temp.insert(*it);
                }
            }
        }

        for (std::unordered_set<int>::const_iterator it=temp.begin();it!=temp.end();it++) {
            res.push_back(*it);
        }
        return res;
    }
};