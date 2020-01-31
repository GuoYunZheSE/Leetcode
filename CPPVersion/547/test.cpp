//
// Created by 郭蕴喆 on 2020/1/31.
//

#include <gtest/gtest.h>
#include "547.h"

using namespace std;

TEST(FC,t1){
    vector<vector<int>> M({{1,1,0},{1,1,0},{0,0,1}});
    Solution s;
    EXPECT_EQ(2,s.findCircleNum(M));
}
TEST(FC,t2){
    vector<vector<int>> M({{1,1,0},{1,1,1},{0,1,1}});
    Solution s;
    EXPECT_EQ(1,s.findCircleNum(M));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}