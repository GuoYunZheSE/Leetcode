#include <gtest/gtest.h>
#include "11.h"

using namespace std;

TEST(CWMW,t1){
    vector<int> strs({1,8,6,2,5,4,8,3,7});
    Solution s;
    EXPECT_EQ(49,s.maxArea(strs));
}

int main(int argc, char ** argv) {
//    testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();  // 执行所有的 test case
    double n=10000000;
    double sum1 = 0;
    double temp1 = n;
    double temp = 1.0;

    for (int i = 1; i < n+1; ++i) {
        cout<<i<<endl;
        temp = int(temp * temp1 / i) % (1000000000 + 7);
        sum1 += int (temp * i) % (1000000000+ 7);
        temp1 -= 1;
    }
    cout<<int(sum1) % (1000000000 + 7);
}