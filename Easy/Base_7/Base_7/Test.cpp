#include "Solution.h"
#include <iostream>
using namespace std;
int main() {
	Solution s =Solution();
	while (true)
	{
		int a;
		cin >> a;
		cout << s.convertToBase7(a)<<endl;
	}
}