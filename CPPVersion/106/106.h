//
// Created by 郭蕴喆 on 2021/3/30.
//

#ifndef CPPVERSION_106_H
#define CPPVERSION_106_H

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
#include <deque>
#include <unordered_map>
#include <iostream>
class Solution {
public:
    std::deque<int> post;
    std::unordered_map<int,int> table;

    TreeNode* helper(int start,int end){
        if (start>=end){
            return nullptr;
        }
        int val=this->post.back();
        this->post.pop_back();
        int index= this->table[val];

        TreeNode* right = this->helper(index+1,end);
        TreeNode* left = this->helper(start,index);
        auto* root = new TreeNode(val,left,right);
        std::cout<<"Root: "<<root->val;
        return root;
    }
    TreeNode* buildTree(std::vector<int>& inorder, std::vector<int>& postorder) {
        for (int i=0;i<inorder.size();++i){
            this->table.emplace(inorder[i],i);
        }
        for (int j:postorder){
            this->post.push_back(j);
        }
        TreeNode *root = this->helper(0,inorder.size());
        return root;
    }
};
#endif //CPPVERSION_106_H
