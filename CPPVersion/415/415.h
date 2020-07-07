//
// Created by 郭蕴喆 on 2020/7/7.
//

#ifndef CPPVERSION_415_H
#define CPPVERSION_415_H
#include <string>

class Solution {
public:
    std::string reverseString(std::string s){
        std::string res="";
        for (int i = s.size()-1; i >=0; --i) {
            res+=s[i];
        }
        return res;
    }

    std::string addStrings(std::string a, std::string b) {
        int carry=0;
        std::string res="";
        a= this->reverseString(a);
        b= this->reverseString(b);
        for (int i = 0; i <std::max(a.size(),b.size()); ++i) {
            if(i<a.size()){
                carry+=(a[i]-'0');
            }
            if (i<b.size()){
                carry+=(b[i]-'0');
            }
            res+=(carry%10+'0');
            carry=carry/10;
        }
        if (carry==1){
            res+='1';
        }
        return this->reverseString(res);
    }
};
#endif //CPPVERSION_415_H
