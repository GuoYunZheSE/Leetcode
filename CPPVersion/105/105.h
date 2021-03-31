//
// Created by 郭蕴喆 on 2021/3/30.
//

#ifndef CPPVERSION_105_H
#define CPPVERSION_105_H
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
#include <unordered_map>
#include <deque>
class Solution {
public:
    std::unordered_map<int,int> table;
    TreeNode* helper(std::deque<int>& preorder, std::vector<int>& inorder) {
        if (!inorder.empty()){

            int val=preorder.front();
            preorder.pop_front();
            int index=0;
            for (int i = 0; i < inorder.size(); ++i) {
                if (inorder[i]==val){
                    index=i;
                }
            }
            std::vector<int> left_part;
            std::vector<int> right_part;

            for (int i = 0; i < inorder.size(); ++i) {
                if (i<index){
                    left_part.emplace_back(inorder[i]);
                }
                if (i>index){
                    right_part.emplace_back(inorder[i]);
                }
            }
            auto left = helper(preorder,left_part);
            auto right = helper(preorder,right_part);
            auto root = new TreeNode(val,left,right);
            return root;
        }else{
            return nullptr;
        }
    }
    TreeNode* buildTree(std::vector<int>& preorder, std::vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); ++i) {
            this->table.emplace(inorder[i],i);
        }
        std::deque<int> pre;
        for (int & i : preorder){
            pre.emplace_back(i);
        }
        return helper(pre,inorder);
    }
};
#endif //CPPVERSION_105_H
