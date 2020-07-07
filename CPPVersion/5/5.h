//
// Created by 郭蕴喆 on 2020/7/7.
//

#ifndef CPPVERSION_5_H
#define CPPVERSION_5_H

#include <string>
#include <utility>

class Solution {
public:
    std::string s;
    int begin=0;
    int end=0;
    void odd_center(int c){
        if (c<this->s.size()-1){
            if (this->s[c]==this->s[c+1]){
                int left=c;
                int right=c+1;
                while(this->s[left]==this->s[right]){
                    if ((right-left)>(this->end-this->begin)){
                        this->end=right;
                        this->begin=left;
                    }
                    if ((left-1)>=0 && (right+1)<this->s.size()){
                        left-=1;
                        right+=1;
                    } else{
                        break;
                    }
                }
            } else{
                return;
            }
        } else{
            return;
        }
    }

    void even_center(int c){
        if (c>0 && c<this->s.size()){
            if (this->s[c-1]==this->s[c+1]){
                int left=c-1;
                int right=c+1;
                while (this->s[left]==this->s[right]){
                    if((right-left)>(this->end-this->begin)){
                        this->begin=left;
                        this->end=right;
                    }
                    if ((left-1)>=0&&(right+1)<this->s.size()){
                        left-=1;
                        right+=1;
                    } else{
                        break;
                    }
                }
            } else{
                return;
            }
        } else{
            return;
        }
    }
    std::string longestPalindrome(std::string s) {
        if(s.size()<=1){
            return s;
        }
        this->s=s;
        for (int i = 0; i < this->s.size(); ++i) {
            this->even_center(i);
            this->odd_center(i);
        }
        std::string res="";
        for (int i=this->begin;i<=this->end;++i){
            res+=this->s[i];
        }
        return res;
    }
};
#endif //CPPVERSION_5_H
