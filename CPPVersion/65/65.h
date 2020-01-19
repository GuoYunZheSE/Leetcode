//
// Created by 郭蕴喆 on 2020/1/19.
//

#ifndef CPPVERSION_65_H
#define CPPVERSION_65_H

#include <string>
#include <tuple>
class Solution {
public:
    int containPoint(const std::string& s){
        int count=0;
        for (char i : s) {
            if (i=='.'){
                count+=1;
            }
        }
        return count;
    }
    int containNumber(const std::string& s){
        int count=0;
        for(char i : s){
            if(int(i)<=57 && int(i)>=48){
                count+=1;
            }
        }
        return count;
    }
    std::tuple<int,bool> contianLetter(const std::string& s){
        int count=0;
        bool FindE= false;
        for(char i : s){
            if (int(i)>=65 && int(i)<=122){
                count+=1;
                if (i=='e'){
                    FindE= true;
                }
            }
        }
        std::tuple<int,bool> res(count,FindE);
        return res;
    }
    int containSign(const std::string& s){
        int count=0;
        for(char i:s){
            if(i=='+'||i=='-'){
                count+=1;
            }
        }
        return count;
    }
    bool isNumber(std::string s) {
        s.erase(0,s.find_first_not_of(' '));
        s.erase(s.find_last_not_of(' ')+1);
        if (s.empty()||s=="."){
            return false;
        }
        for(char i : s){
            if(i==' '){
                return false;
            }
        }
        int letterCount;
        bool FindE;
        std::tuple<int,bool> temp=this->contianLetter(s);
        letterCount=std::get<0>(temp);
        FindE=std::get<1>(temp);
        if(letterCount>=2 || (letterCount==1 && !FindE)){
            return false;
        } else{
            if (FindE){
                std::string base;
                std::string exponent;
                base=s.substr(0,s.find('e'));
                exponent=s.substr(s.find('e')+1,s.length()-1);
                if (base.empty() || exponent.empty()){
                    return false;
                } else{
                    int baseSign=this->containSign(base);
                    int exSign=this->containSign(exponent);
                    if(baseSign>=2 || exSign>=2){
                        return false;
                    } else{
                        if(baseSign==1 &&(!(base[0]=='+'||base[0]=='-')||base.length()==1)){
                            return false;
                        }
                        if (exSign==1 &&(!(exponent[0]=='+'||exponent[0]=='-')||exponent.length()==1)){
                            return false;
                        }
                        if(this->containPoint(base)>1 || this->containPoint(exponent)>0){
                            return false;
                        }
                        if(!this->containNumber(base) || !this->containNumber(exponent)){
                            return false;
                        } else{
                            return !(base.length() == 1 && base[0] == '.');
                        }
                    }
                }
            } else{
                int contSign=this->containSign(s);
                if(!this->containNumber(s)){
                    return false;
                }
                if (contSign>=2){
                    return false;
                } else{
                    if(contSign==1 and (!(s[0]=='+'||s[0]=='-')||s.length()==1)){
                        return false;
                    } else{
                        return this->containPoint(s) <= 1;
                    }
                }
            }
        }
    }
};
#endif //CPPVERSION_65_H
