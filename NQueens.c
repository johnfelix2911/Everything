#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    printf("Enter the size:");
    scanf("%d", &n);
    char **p = (char **)malloc(n*sizeof(char *));
    for (int i=0; i<n; i++)
    {
        p[i] = (char *)malloc(20 * sizeof(char));
    }
    printf("Start entering %d strings: \n", n);
    for (int i=0; i<n; i++)
    {
        printf("Enter string number %d:", i+1);
        scanf("%s", p[i]);
    }
    printf("Printing: \n");
    for (int i=0; i<n; i++)
    {
        printf("%s \n", p[i]);
    }
    int *len = (int *)malloc(n * sizeof(int));
    for (int i=0; i<n; i++)
    {
        len[i] = 0;
        for (int j=0; p[i][j]!='\0'; j++)
        {
            len[i]++;
        }
    }
    for (int i=0; i<n; i++)
    {
        printf("%d ", len[i]);
    }
    free(p);
    return 1;
}