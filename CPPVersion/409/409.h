//
// Created by 郭蕴喆 on 2019/12/13.
//

#ifndef CPPVERSION_409_H
#define CPPVERSION_409_H

#endif //CPPVERSION_409_H

#include <string>
#include <unordered_map>

class Solution {
public:
    std::unordered_map<char,int> dict;
    int longestPalindrome(std::string s) {
        for(std::string::iterator it=s.begin();it!=s.end();++it){
            std::unordered_map<char,int>::const_iterator got=this->dict.find(*it);
            if(got==this->dict.end()){
                this->dict.emplace(*it,1);
            } else{
                int temp=got->second;
                char key=got->first;
                this->dict.erase(got);
                this->dict.emplace(key,temp+1);
            }
        }
        int odd=0;
        int even=0;
        for(std::unordered_map<char,int>::const_iterator it=this->dict.begin();it!=this->dict.end();++it){
            if (it->second%2!=0){
                if (odd==0){
                    odd+=1;
                    even+=it->second-1;
                } else{
                    even+=it->second-1;
                }
            } else{
                even+=it->second;
            }
        }
        return odd+even;
    }
};