//
// Created by 郭蕴喆 on 2020/2/25.
//

#include "47.h"
#include "gtest/gtest.h"

using namespace std;

TEST(PermutationsII,t1){
    Solution s;
    vector<int> nums({1,2,1});
    EXPECT_EQ(3,(s.permuteUnique(nums)).size());
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
