#include <stdio.h>

int maxProfit(int* prices, int pricesSize)
{
    int maxpos = 0, minpos = 0, cond=0;
    for (int i=0; i<pricesSize; i++)
    {
        if (prices[i]<prices[i+1])
        {
            cond = 1;
        }
    }
    if (cond==0)
    {
        return 0;
    }
    while (cond)
    {
        for (int i=0; i<pricesSize; i++)
        {
            if (prices[i]>prices[maxpos])
            {
                maxpos = i;
            }
            else if (prices[i]<prices[minpos])
            {
                minpos = i;
            }
        }
        if (maxpos>minpos)
        {
            return prices[maxpos]-prices[minpos];
        }
        else if (maxpos == minpos)
        {
            return 0;
        }
    }
}

int main()
{
    int prices[] = {3,2,6,5,0,3};
    int max = maxProfit(prices, 6);
    printf("%d", max);
    return 1;
}