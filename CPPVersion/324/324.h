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
        int m = nums.size();
        if (m%2==0){
            for (int i = 0; i <m/2 ; ++i) {
                res.push_back(nums[i]);
                res.push_back(nums[i+m/2]);
            }
        } else{
            for (int i = 0; i <int(m/2) ; ++i) {
                res.push_back(nums[i]);
                res.push_back(nums[i+int(m/2)+1]);
            }
            res.push_back(nums[int(m/2)]);
        }
        nums=res;
    }
};
#endif //CPPVERSION_324_H
