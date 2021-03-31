//
// Created by 郭蕴喆 on 2021/3/31.
//

#include <gtest/gtest.h>
#include "106.h"

using namespace std;

TEST(SWM,t1){
    vector<int>postorder = {9,15,7,20,3};
    vector<int>inorder = {9,3,15,20,7};
    Solution S;
    EXPECT_EQ(nullptr,S.buildTree(inorder,postorder));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
