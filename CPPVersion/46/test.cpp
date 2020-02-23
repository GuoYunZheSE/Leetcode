//
// Created by 郭蕴喆 on 2020/2/23.
//

#include "46.h"
#include "gtest/gtest.h"

using namespace std;

TEST(Trapping_Rain_Water,t1){
    Solution s;
    vector<int> nums({1,2,3});
    EXPECT_EQ(6,(s.permute(nums)).size());
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
