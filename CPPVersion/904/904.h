//
// Created by 郭蕴喆 on 2020/3/2.
//

#ifndef CPPVERSION_904_H
#define CPPVERSION_904_H

#endif //CPPVERSION_904_H

#include <vector>
#include <unordered_map>
class Solution {
public:
    int totalFruit(std::vector<int> &tree) {
        std::unordered_map<int, int> count;
        int i, j;
        for (i = 0, j = 0; j < tree.size(); ++j) {
            count[tree[j]]++;
            if (count.size() > 2) {
                if (--count[tree[i]] == 0)count.erase(tree[i]);
                i++;
            }
        }
        return j - i;
    }
};
