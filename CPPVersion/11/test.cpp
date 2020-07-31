#include <gtest/gtest.h>
#include "11.h"

using namespace std;

TEST(CWMW,t1){
    vector<int> strs({1,8,6,2,5,4,8,3,7});
    Solution s;
    EXPECT_EQ(49,s.maxArea(strs));
}

int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}