#include <stdio.h>

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n)
{
    if (n!=0 && nums1Size!=m && m!=0)
    {
        for (int i=m, j=0; nums1Size!=i; i++, j++)
        {
            nums1[i] = nums2[j];
        }
            int temp;
        for (int i=0; i<nums1Size; i++)
        {
            for (int j=0; j<nums1Size-i; j++)
            {
                if (nums1[j]>nums1[j+1])
                {
                    temp = nums1[j];
                    nums1[j] = nums1[j+1];
                    nums1[j+1] = temp;
                }
            }
        }
    }
    else
    {
        for (int i=0; i<nums1Size; i++)
        {
            nums1[i] = nums2[i];
        }
    }
}

int main()
{
    int prices[] = {7,1,5,3,6,4};
    int max = maxProfit(prices, 6);
    printf("%d", max);
    return 1;
}