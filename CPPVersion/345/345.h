//
// Created by 郭蕴喆 on 2019/12/17.
//

#ifndef CPPVERSION_345_H
#define CPPVERSION_345_H

#endif //CPPVERSION_345_H

#include <set>
#include <string>

class Solution {
public:
    std::string reverseVowels(std::string s) {
        if (s.length()<=1){
            return s;
        } else{
            int begin=0;
            int end=s.length();
            std::set<char> vowel({'a', 'e', 'i', 'o', 'u','A','E','I','O','U'});

            while (begin<=end){
                if(vowel.find(s[begin])!=vowel.end()){
                    if(vowel.find(s[end])!=vowel.end()){
                        char temp=s[begin];
                        s[begin]=s[end];
                        s[end]=temp;
                        begin+=1;
                        end-=1;
                    } else{
                        end-=1;
                    }
                } else{
                    begin+=1;
                }
            }
            return s;
        }
    }
};