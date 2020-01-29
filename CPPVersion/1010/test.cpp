//
// Created by 郭蕴喆 on 2020/1/29.
//

#include "1010.h"
#include "gtest/gtest.h"
using namespace std;


TEST(_1010,t1){
    Solution s;
    vector<int> nums({30,20,150,100,40});
    EXPECT_EQ(3,s.numPairsDivisibleBy60(nums));
}
TEST(_1010,t2){
    Solution s;
    vector<int> nums({60,60,60});
    EXPECT_EQ(3,s.numPairsDivisibleBy60(nums));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}