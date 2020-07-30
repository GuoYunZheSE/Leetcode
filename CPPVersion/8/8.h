//
// Created by 郭蕴喆 on 2020/7/30.
//

#ifndef CPPVERSION_8_H
#define CPPVERSION_8_H

#include <string>
#include <deque>
#include <cmath>

class Solution {
public:
    int compare_with_ultr(std::deque<char> &res,std::deque<char> &ultr){
        bool return_sum= false;
        bool return_max_size=false;
        if (res.size()<ultr.size()){
            return 1;
        }
        else if (res.size()==ultr.size()){
                for (int i = 0; i <ultr.size() ; ++i) {
                    if (ultr[i]>res[i]){
                        return 1;
                    }
                    if (ultr[i]<res[i]){
                        return -1;
                    }
                }
            return 0;
            }
        else{
            return -1;
            }
    }
    int myAtoi(std::string str) {
        std::deque<char> temp;
        bool find_content= false;
        for (char i : str) {
            if (i==' ' && ! find_content){
                continue;
            } else{
                find_content= true;
                temp.push_back(i);
            }
        }
        bool Positive= true;
        if (temp.empty()){
            return 0;
        }
        if (!(int(temp[0]<=int('9') && int(temp[0])>=int('0')))){
            if (temp[0]=='-'){
                Positive= false;
                temp.pop_front();
            } else{
                if (temp[0]=='+'){
                    temp.pop_front();
                } else{
                    return 0;
                }
            }
        }
        std::deque<char> res;
        bool BeginwithZer0= true;
        for (char i : temp){
            if (!(int(i)<=int('9')&&int(i)>=int('0'))){
                break;
            } else{
                if (i=='0'&&BeginwithZer0){
                    continue;
                } else{
                    BeginwithZer0= false;
                    res.push_back(i);
                }
            }
        }
        int result=0;
        if (Positive){
            std::deque<char> ultr({'2','1','4','7','4','8','3','6','4','7'});
            result =compare_with_ultr(res,ultr);
        } else{
            std::deque<char> ultr({'2','1','4','7','4','8','3','6','4','8'});
            result =compare_with_ultr(res,ultr);
        }
        if (result==1){
            int sum=0;
            int i=0;
            while(!res.empty()) {
                sum+=((int(res.back())-int('0'))*(std::pow(10,i)));
                i+=1;
                res.pop_back();
            }
            if (Positive){
                return sum;
            } else{
                return sum*-1;
            }
        } else{
            if (Positive){
                return 2147483647;
            } else{
                return -2147483648;
            }
        }
    }
};

//class Solution {
//public:
//    int myAtoi(string str) {
//        if(str.empty())return 0;
//        while(str.at(0)==' '){
//            str.erase(str.begin());
//            if (str.empty()) return 0;
//        }
//        stringstream ss(str);
//        int a;
//        if(ss.fail())return 0;
//        ss>>a;
//        if(a>INT_MAX)return INT_MAX;
//        else if(a<INT_MIN)return INT_MIN;
//        else if(a)return a;
//        else return 0;
//    }
//};
#endif //CPPVERSION_8_H
