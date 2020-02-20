//
// Created by 郭蕴喆 on 2020/2/20.
//

#ifndef CPPVERSION_324_H
#define CPPVERSION_324_H

#include <vector>
#include <algorithm>
//class Solution {
//public:
//    void wiggleSort(std::vector<int>& nums) {
//        int size = nums.size();
//        nth_element(begin(nums), begin(nums) + size / 2, end(nums));
//        int m = *(begin(nums) + size / 2);
//
//#define A(i) nums[(1 + 2*(i)) % (size | 1)]
//
//        int l = 0, r = size - 1;
//        for (int i = 0; i <= r;)
//            if (A(i) > m) std::swap(A(i++), A(l++));
//            else if (A(i) < m) std::swap(A(i), A(r--));
//            else i++;
//    }
//};
class Solution {
public:
    void wiggleSort(std::vector<int>& nums) {
        if (nums.size()==1){
            return;
        }
        std::sort(nums.begin(),nums.end());
        std::vector<int> res;
        int m = (nums.size()-1)>>1;
        int left=m;
        int right=nums.size()-1;
        while (left>=0 && right>m){
            res.push_back(nums[left--]);
            res.push_back(nums[right--]);
        }
        while (left>=0){
            res.push_back(nums[left--]);
        }
        while (right>m){
            res.push_back(nums[right--]);
        }
        nums=res;
    }
};
#endif //CPPVERSION_324_H
