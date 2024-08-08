#include <stdio.h>

int main()
{
    int a[4][4] = {1, 2, 3, 4, 5, 6, 7, 7, 5, 6, 7, 8, 7, 6, 5, 4};
    for (int i=0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
    return 1;
}