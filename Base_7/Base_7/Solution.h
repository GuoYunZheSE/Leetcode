#include <string>
using namespace std;
//Runtime: 4 ms, faster than 98.28% of C++ online submissions for Base 7.
class Solution {
public:
	string convertToBase7(int num) {
		string A = "";
		bool mark = false;
		if (num < 0) {
			num = abs(num);
			mark = true;
		}
		while (num>=7)
		{
			A = A + to_string(num % 7);
			num = int(num / 7);
		}
		A = A + to_string(num);
		char temp;
		size_t i, j;
		//size_t概述： size_t 类型定义在cstddef头文件中，该文件是C标准库的头文件stddef.h的C++版。它是一个与机器相关的unsigned整型类型，其大小足以保证存储内存中对象的大小。
		for (j = 0, i = A.size() - 1; j < i; --i, ++j) {
			temp = A[i];
			A[i] = A[j];
			A[j] = temp;
		}
		if (mark) {
			return '-' + A;
		}
		else{
			return A;
		}
	}
};