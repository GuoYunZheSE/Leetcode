//
// Created by 郭蕴喆 on 2021/3/19.
//

#ifndef CPPVERSION_84_H
#define CPPVERSION_84_H
#include <vector>
#include <deque>
class Solution {
public:
    static int max(int a,int b){
        if (a>=b){
            return a;
        } else{
            return b;
        };
    }
    int largestRectangleArea(std::vector<int>& heights) {

        std::deque<int> q;
        q.push_back(-1);
        heights.insert(heights.end(),0);

        int res=0;
        for(std::size_t i = 0; i<heights.size();++i){
            while (q.back()>=0 && heights[int(i)]<heights[q.back()]){
                int height=heights[q.back()];
                q.pop_back();

                int width = int(i) - q.back() - 1;

                res = max(res,width*height);

            }
            q.push_back(int(i));
        }
        return res;
    }
};

#endif //CPPVERSION_84_H
