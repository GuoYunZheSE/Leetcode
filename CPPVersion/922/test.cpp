//
// Created by 郭蕴喆 on 2020/1/27.
//

#include <gtest/gtest.h>
#include "922.h"

using namespace std;
TEST(SAbP2,t1){
    vector<int> nums({4,2,5,7});
    vector<int> nums2({4,5,2,7});
    Solution s;
    EXPECT_EQ(nums2,s.sortArrayByParityII(nums));
}

int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}