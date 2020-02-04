//
// Created by 郭蕴喆 on 2020/2/5.
//

#include "1300.h"
#include "gtest/gtest.h"

using namespace std;

TEST(SMACT,t1){
    Solution s;
    vector<int> nums({4,9,3});
    EXPECT_EQ(3,s.findBestValue(nums,10));
}
TEST(SMACT,t2){
    Solution s;
    vector<int> nums({2,5,3});
    EXPECT_EQ(5,s.findBestValue(nums,10));
}
TEST(SMACT,t3){
    Solution s;
    vector<int> nums({60864,25176,27249,21296,20204});
    EXPECT_EQ(11361,s.findBestValue(nums,56803));
}
TEST(SMACT,t4){
    Solution s;
    vector<int> nums({1547,83230,57084,93444,70879});
    EXPECT_EQ(17422,s.findBestValue(nums,71237));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}