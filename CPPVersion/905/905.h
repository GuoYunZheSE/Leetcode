//
// Created by 郭蕴喆 on 2019/12/13.
//

#ifndef CPPVERSION_905_H
#define CPPVERSION_905_H

#endif //CPPVERSION_905_H

#include <vector>
class Solution {
public:
    std::vector<int> sortArrayByParity(std::vector<int>& A) {
        std::vector<int> even;
        std::vector<int> odd;
        for(std::vector<int>::const_iterator it=A.begin();it!=A.end();++it){
            if (*it%2==0){
                even.push_back(*it);
            } else{
                odd.push_back(*it);
            }
        }
        odd.insert(odd.begin(),even.begin(),even.end());
        return odd;
    }
};