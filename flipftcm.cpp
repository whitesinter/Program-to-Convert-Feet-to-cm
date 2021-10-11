#include <stdio.h>
double convert(int centimeter){
   double inch = 0.3937 * centimeter;
   double feet = 0.0328 * centimeter;
   printf ("Inches is: %.2f \n", inch);
   printf ("Feet is: %.2f", feet);
   return 0;
}
// Driver Code
int main() {
   int centimeter = 20;
   convert(centimeter);
   return 0;
}
