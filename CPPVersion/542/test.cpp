//
// Created by 郭蕴喆 on 2020/1/29.
//

#include "542.h"
#include "gtest/gtest.h"
using namespace std;


TEST(_542,t1){
    Solution s;
    vector<vector<int>> nums({{0,0,0},{0,1,0},{0,0,0}});
    EXPECT_EQ(vector<vector<int>> ({{0,0,0},{0,1,0},{0,0,0}}),s.updateMatrix(nums));
}
TEST(_542,t2){
    Solution s;
    vector<vector<int>> nums({{0,0,0},{0,1,0},{1,1,1}});
    EXPECT_EQ(vector<vector<int>> ({{0,0,0},{0,1,0},{1,2,1}}),s.updateMatrix(nums));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}