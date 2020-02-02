//
// Created by 郭蕴喆 on 2020/2/2.
//

#ifndef CPPVERSION_1041_H
#define CPPVERSION_1041_H


#include <string>
#include <unordered_map>


class Solution {
public:
    std::unordered_map<char,int> trace{{'N',0},{'S',0},{'E',0},{'W',0}};
    char changeDirection(char curr,char direction){
        char temp[]="NESW";
        int c=0;
        if(curr=='N'){
            c=0;
        }else if(curr=='E'){
            c=1;
        } else if(curr=='S'){
            c=2;
        } else{
            c=3;
        }
        if (direction=='R'){
            return temp[(c+1+4)%4];
        } else{
            return temp[(c-1+4)%4];
        }
    }
    bool check(){
        if(this->trace['N']==this->trace['S']){
            if (this->trace['W']==this->trace['E']){
                return true;
            }
        }
        return false;
    }
    bool isRobotBounded(std::string instructions) {
        char current='N';
        for (int i = 0; i <4 ; ++i) {
            for (char c :instructions){
                if (c=='G'){
                    this->trace[current]+=1;
                    continue;
                } else{
                    current=this->changeDirection(current,c);
                }
            }
            if (this->check()){
                return true;
            }
        }
        return false;
    }
};
#endif //CPPVERSION_1041_H
