//
// Created by 郭蕴喆 on 2019/11/26.
//

#ifndef CPPVERSION_731_H
#define CPPVERSION_731_H

#endif //CPPVERSION_731_H

#include <vector>
#include <tuple>
#include <algorithm>


class MyCalendarTwo {
public:
    std::vector<std::tuple<int,int>> once;
    std::vector<std::tuple<int,int>> twice;

    MyCalendarTwo() = default;

    bool book(int start, int end) {
        for (int i = 0; i < twice.size(); ++i) {
            if (start < std::get<1>(twice[i]) && std::get<0>(twice[i])<end){
                return false;
            }
        }
        for (std::vector<std::tuple<int,int>>::const_iterator it=once.begin();it<this->once.end();it++){
            if(start<std::get<1>(*it)&&std::get<0>(*it)<end){
                this->twice.emplace_back(std::max(start,std::get<0>(*it)),std::min(end,std::get<1>(*it)));
            }
        }
        this->once.emplace_back(start,end);
        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */