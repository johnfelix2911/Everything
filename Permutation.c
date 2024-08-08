#include <stdio.h>

int print_seq(int n)
{
    int no_of_permut, temp;
    for (int i=0; i<=n; i++)
    {
        for (int j=0; j<=(n/2); j++)
        {
            for (int k=0; k<=(n/3); k++)
            {
                if (i + 2*j + 3*k == n)
                {
                    int length = i+j+k;
                    int a[length];
                    for (int m=0; m<i; m++)
                    {
                        a[m] = 1;
                    }
                    for (int m=0; m<j; m++)
                    {
                        a[m+i] = 2;
                    }
                    for (int m=0; m<k; m++)
                    {
                        a[m+i+j] = 3;
                    }
                    for (int m=0; m<length; m++)
                    {
                        printf("%d ", a[m]);
                    }
                    printf("\n");
                    for (int m=0; m<length; m++)
                    {
                        for (int q=0; q<length; q++)
                        {
                            if (a[m]!=a[q])
                            {
                                temp = a[m];
                                a[m] = a[q];
                                a[q] = temp;
                                for (int p=0; p<length; p++)
                                {
                                    printf("%d ", a[p]);
                                }
                                printf("\n");
                            }
                        }
                    }
                }
            }
        }
    }
}

int main()
{
    print_seq(8);
}