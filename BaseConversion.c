#include <stdio.h>

void basconv(int n, int b)
{
    int r = n%b;
    int q = n/b;
    if (q==0)
    {
        printf("(%d", r);
    }
    else
    {
        basconv(q, b);
        printf(",%d",r);
    }
}

int main()
{
    int n, b;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("Enter the value of b: ");
    scanf("%d", &b);
    basconv(n, b);
    printf(")_%d", b);
}