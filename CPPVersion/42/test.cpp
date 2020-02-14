//
// Created by 郭蕴喆 on 2020/2/14.
//

#include "42.h"
#include "gtest/gtest.h"

using namespace std;

TEST(Trapping_Rain_Water,t1){
    Solution s;
    vector<int> height({0,1,0,2,0,0,1,3,2,1,2,1});
    EXPECT_EQ(7,s.trap(height));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
