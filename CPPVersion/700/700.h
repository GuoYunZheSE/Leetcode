//
// Created by 郭蕴喆 on 2020/5/25.
//

#ifndef CPPVERSION_700_H
#define CPPVERSION_700_H

#endif //CPPVERSION_700_H


 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode *ans = nullptr;

    void DFS(TreeNode *cur, int val) {
        if (cur->val == val) {
            this->ans = cur;
        }
        if (cur->val > val && cur->left) {
            this->DFS(cur->left, val);
        }
        if (cur->val < val && cur->right) {
            this->DFS(cur->right, val);
        }
    }

    TreeNode *searchBST(TreeNode *root, int val) {
        if (root == nullptr) {
            return nullptr;
        } else {
            this->DFS(root, val);
            return this->ans;
        }
    }
};