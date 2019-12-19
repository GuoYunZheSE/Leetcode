//
// Created by 郭蕴喆 on 2019/12/19.
//

#include "1110.h"
#include <gtest/gtest.h>
using namespace std;
//struct TreeNode {
//    int val;
//    TreeNode *left;
//    TreeNode *right;
//    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//};
TEST(DNRF,t1){
    TreeNode r(1);
    TreeNode rl(2);
    TreeNode rll(4);
    TreeNode rlr(5);
    TreeNode rr(3);
    TreeNode rrl(6);
    TreeNode rrr(7);
    rr.left=&rrl;
    rr.right=&rrr;
    rl.left=&rll;
    rl.right=&rlr;
    r.right=&rr;
    r.left=&rl;
    vector<int> todel({3,5});
    Solution s;
    s.delNodes(&r,todel);
//    for(vector<TreeNode*>::iterator it=s.roots.begin();it!=s.roots.end();++it){
//        cout<<*it.val;
//    }
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}