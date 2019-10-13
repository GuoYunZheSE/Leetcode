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
		//size_t������ size_t ���Ͷ�����cstddefͷ�ļ��У����ļ���C��׼���ͷ�ļ�stddef.h��C++�档����һ���������ص�unsigned�������ͣ����С���Ա�֤�洢�ڴ��ж���Ĵ�С��
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