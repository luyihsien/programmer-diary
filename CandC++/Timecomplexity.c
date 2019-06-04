#include<stdio.h>
int main()
{
    int n =6;
    int i,s;
    for (int i=1,s=0;i<n;i++)
    {
        for(int j=0;j<i*i;j++)
            {
                s+=j;
                printf("%d\n",j);
            }

    }
    system("pause");
    return 0;
}
