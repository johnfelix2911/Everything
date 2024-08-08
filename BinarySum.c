#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void BinarySum11(char* a, char* b)
{
    int l1 = strlen(a);
    int l2 = strlen(b);
    int l, s=0, flag; 
    if (l1>l2)
    {
        l = l1;
        flag = 1;
    }
    else if  (l1<l2)
    {
        l = l2;
        flag = 0;
    }
    else
    {
        l = l2;
        flag = -1;
    }
    char* sum = (char* )malloc(l*sizeof(char));
    if (flag==1)
    {
        b = realloc(b, l*sizeof(char));
    }
    else if (flag==0)
    {
        a = realloc(a, l*sizeof(char));
    }
    if (flag==0)
    {
        for (int i=l1-1; i>=0; i--)
        {
            a[i+l2-l1] = a[i];
        }
        for (int i=0; i<(l2-l1); i++)
        {
            a[i] = '0';
        }
    }
    else if (flag==1)
    {
        for (int i=l2-1; i>=0; i--)
        {
            b[i+l2-l1] = b[i];
        }
        for (int i=0; i<(l1-l2); i++)
        {
            b[i] = '0';
        }
    }
    for (int i=l-1; i>=0; i++)
    {
        if (a[i]=='1' && b[i]=='1')
        {
            if (s==1)
            {
                sum[i] = '1';
            }
            else
            {
                sum[i] = '0';
            }            
        }
        else if (a[i]=='1' && b[i]=='0')
        {
            if (s==1)
            {
                sum[i] = '0';
            }
            else
            {
                sum[i] = '1';
            }
        }
        else
        {
            if (s==1)
            {
                sum[i] = '1';
            }
            else
            {
                sum[i] = '0';
            }
        }
    }
    if (s==1)
    {
        sum = realloc(sum, (l+1)*sizeof(char));
        for (int i=l; i>0; i--)
        {
            sum[i] = sum[i-1];
        }
        sum[0] = '1';
        printf("%s", sum);
    }
    else
    {
        printf("%s", sum);
    }
}

int main()
{
    char a[] = "111";
    char b[] = "10";
    BinarySum11(a, b);
    return 1;
}