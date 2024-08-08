#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *arr[] = {"cat", "dog", "bar", "xyz", "mnp"};
    char *ptr1, *ptr2;
    ptr1 = (arr + 1)[2];
    ptr2 = (*arr+2);
    printf("%s \n", ptr1);
    printf("%s \n", ptr2);
    printf("%d", ptr2-ptr1);
}