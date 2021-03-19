//
// Created by 郭蕴喆 on 2021/3/19.
//

#include <gtest/gtest.h>
#include "239.h"

using namespace std;

TEST(SWM,t1){
    vector<int> M({1,3,-1,-3,5,3,6,7});
    Solution s;
    EXPECT_EQ(vector<int>({3,3,5,5,6,7}),s.maxSlidingWindow(M,3));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
