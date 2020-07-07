//
// Created by 郭蕴喆 on 2020/7/1.
//

#ifndef CPPVERSION_43_H
#define CPPVERSION_43_H

#include <string>

std::string multiply(std::string num1, std::string num2) {
    std::string sum(num1.size() + num2.size(), '0');

    for (int i = num1.size() - 1; 0 <= i; --i) {
        int carry = 0;
        for (int j = num2.size() - 1; 0 <= j; --j) {
            int tmp = (sum[i + j + 1] - '0') + (num1[i] - '0') * (num2[j] - '0') + carry;
            sum[i + j + 1] = tmp % 10 + '0';
            carry = tmp / 10;
        }
        sum[i] += carry;
    }

    size_t startpos = sum.find_first_not_of("0");
    if (std::string::npos != startpos) {
        return sum.substr(startpos);
    }
    return "0";
}
#endif //CPPVERSION_43_H
