//
// Created by 郭蕴喆 on 2021/3/22.
//

#include <gtest/gtest.h>
#include "84.h"

using namespace std;

TEST(SWM,t1){
    vector<int> M({2,1,5,6,2,3});
    Solution s;
    EXPECT_EQ(10,s.largestRectangleArea(M));
}

TEST(SWM,t2){
    vector<int> M({2,4});
    Solution s;
    EXPECT_EQ(4,s.largestRectangleArea(M));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
