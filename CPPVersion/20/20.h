//
// Created by 郭蕴喆 on 2020/1/21.
//

#ifndef CPPVERSION_20_H
#define CPPVERSION_20_H

#include <string>
#include <vector>
class Solution {
public:
    std::vector<char> stack_open;
    bool isValid(std::string s) {
        if (s.length()%2!=0){
            return false;
        }
        for(char i : s){
            if (i=='('){
                this->stack_open.push_back('(');
                continue;
            }
            if (i=='{'){
                this->stack_open.push_back('{');
                continue;
            }
            if (i=='['){
                this->stack_open.push_back('[');
                continue;
            }
            if (i==')'){
                if(this->stack_open.empty() || this->stack_open[this->stack_open.size()-1]!='('){
                    return false;
                }
                this->stack_open.pop_back();
                continue;
            }
            if (i==']'){
                if(this->stack_open.empty() || this->stack_open[this->stack_open.size()-1]!='['){
                    return false;
                }
                this->stack_open.pop_back();
                continue;
            }
            if (i=='}'){
                if(this->stack_open.empty() || this->stack_open[this->stack_open.size()-1]!='{'){
                    return false;
                }
                this->stack_open.pop_back();
                continue;
            }
        }
        return this->stack_open.empty();
    }
};
#endif //CPPVERSION_20_H
