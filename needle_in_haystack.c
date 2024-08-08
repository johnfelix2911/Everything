#include <stdio.h>
#include <stdlib.h>

struct student
{
    char name[10];
    float gpa;
    int roll;
};

int main()
{
    struct student *a = (struct student *)malloc(5 * sizeof(struct student)); 
    for (int i=0; i<5; i++)
    {
        printf("Enter the name of student %d:", i+1);
        scanf("%s", a[i].name);
        printf("Enter the gpa of student %d:", i+1);
        scanf("%f", &a[i].gpa);
        printf("Enter the roll of student %d:", i+1);
        scanf("%d", &a[i].roll);
    }
    printf("Printinng: \n");
    for (int i=0; i<5; i++)
    {
        printf("Student %d: %s, %f, %d \n",i+1, a[i].name, a[i].gpa, a[i].roll);
    }
    free(a);
    return 1;
}