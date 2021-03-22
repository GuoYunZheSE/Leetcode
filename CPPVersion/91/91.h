//
// Created by 郭蕴喆 on 2021/3/22.
//

#ifndef CPPVERSION_91_H
#define CPPVERSION_91_H
#include <string>
#include <vector>
class Solution {
public:
    int numDecodings(std::string s) {
        std::vector<int> bitmap(s.size());
        bitmap.insert(bitmap.begin(),1);
        if (s[0]!='0'){
            bitmap[1]=1;
        }
        for (int i = 2; i<s.size()+1;++i){
            std::string temp1=s.substr(i-1,1);
            std::string temp2=s.substr(i-2,2);

            if (std::stoi(temp1)>0 &&std::stoi(temp1)<=9){
                bitmap[i]+=bitmap[i-1];
            }
            if (std::stoi(temp2)>=10 && std::stoi(temp2)<=26){
                bitmap[i]+=bitmap[i-2];
            }
        }
        return bitmap.back();
    }
};
#endif //CPPVERSION_91_H
