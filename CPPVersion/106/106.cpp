//
// Created by 郭蕴喆 on 2021/3/31.
//
//朱爽 202066324339
#include <iostream>
#include <iomanip>
using namespace std;int main(){double x1, quantity1, money1;double x2, quantity2, money2, sum, remain, truth;cin >> x1 >> quantity1;cin >> x2 >> quantity2;cin >> sum;money1 = x1 * quantity1;money2 = x2 * quantity2;truth = money1 + money2;remain = sum - truth;cout << "XXX超市购物小票" << endl;cout << "--------------------------------------" << endl;cout << "物品名称\t" << "单价\t" << "数量\t" << "金额" << endl;cout << "花生    \t" << fixed << setprecision(2) << x1 << "\t" << quantity1 << "\t" << money1 << endl;cout << "苹果    \t" << x2 << "\t" << quantity2 << "\t" << money2 << endl;cout << "--------------------------------------" << endl;cout << "已收： ￥" << sum << "元" << endl;cout << "实收： ￥" << truth << "元" << endl;cout << "找零： ￥" << remain << "元";return 0;}

