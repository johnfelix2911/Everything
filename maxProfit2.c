#include <stdio.h>

int maxProfit(int* prices, int pricesSize)
{
    int max = 0;
    for (int i=0, j=pricesSize-1; i<j; i++, j--)
    {
        if ((prices[j]-prices[i])>max)
        {
            max = prices[j]-prices[i];
        }
    }
    return max;
}

int main()
{
    int prices[] = {7,6,4,3,1};
    int max = maxProfit(prices, 5);
    printf("%d", max);
    return 1;
}