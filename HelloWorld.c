#include <stdio.h>

int main() {
   int m, p, q;

   // Get input for m
   printf("Enter a positive integer m > 1: ");
   scanf("%d", &m);

   // Check if m is valid
   if (m <= 1) {
       printf("Invalid input: m must be a positive integer greater than 1.\n");
       return 1;
   }

   // Calculate 2 * m
   int twice_m = 2 * m;

   // Check for prime decomposition directly within the loop
   for (p = 2; p <= twice_m / 2; p++) {
       int divisibility_count = 0;
       for (int i = 2; i * i <= p; i++) {  // Check for divisibility to determine primeness of p
           if (p % i == 0) {
               divisibility_count++;
               break;
           }
       }
       if (divisibility_count == 0) {  // p is prime
           int divisibility_count_q = 0;
           for (int i = 2; i * i <= twice_m - p; i++) {  // Check for divisibility to determine primeness of q
               if ((twice_m - p) % i == 0) {
                   divisibility_count_q++;
                   break;
               }
           }
           if (divisibility_count_q == 0) {  // q is prime
               q = twice_m - p;
               printf("2 * m = p + q, where p = %d and q = %d\n", p, q);
               return 0;  // Found a decomposition, exit successfully
           }
       }
   }

   // No decomposition found
   printf("No prime decomposition found for 2 * m = %d\n", twice_m);
   return 0;
}
