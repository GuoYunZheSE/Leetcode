//
// Created by 郭蕴喆 on 2020/3/14.
//

#include "1287.h"
#include "gtest/gtest.h"

using namespace std;

TEST(findSpecialInteger,t1){
    Solution s;
    vector<int> nums({1,2,2,6,6,6,6,7,10});
    EXPECT_EQ(6,s.findSpecialInteger(nums));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}