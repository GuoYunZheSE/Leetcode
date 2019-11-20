//
// Created by 郭蕴喆 on 2019/11/20.
//
#ifndef CPPVERSION_199_H
#define CPPVERSION_199_H

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    unordered_map <int,vector<int>>res;
    struct TreeNode{
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode(int x):val(x),left(NULL),right(NULL){}
    };
    vector<int> rightSideView(TreeNode *root);
    void updateDic(int A,int Length);
    void iterTree(TreeNode *node,int currentDepth);
    void test(TreeNode *node);
};
#endif //CPPVERSION_199_H
