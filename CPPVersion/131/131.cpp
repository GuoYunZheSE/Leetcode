#include <iostream>

using namespace std;



int main()

{

    int a, b, c, h,j;

    cout << "汉字以多少点阵方式显示，16*16输入16,32*32输入32，依次类推?" << endl;

    cin >> a;

    b = a % 2;

    if (b > 0)

    {

        j = a;//横的元素个数

        c = a - 1;

        h = (a - 1) / 2;

    }

    else c = a - 2, h = ((a - 2) / 2),j=a-1;

    char d;

    cout << "请输入构成汉字的基本字符号是?" << endl;

    cin >> d;

    int e = 1, f = 1, g = 1, i = 1 + h;//e表示第几行  f

    while (e <= a)

    {

        if (e == 1 || e == i || e == a)

        {

            while (f <= j)

            {

                cout << d;

                f = f + 1;

            }

            f = 1;

            cout << endl;

        }

        else

        {

            while (g <= ((c / 2)+1))

            {

                if (g == ((c / 2) + 1))

                {

                    cout << d;

                }

                else cout << " ";

                g = g + 1;

            }

            g = 1;

            cout << endl;

        }

        e = e + 1;

    }

    cout << endl;

}

