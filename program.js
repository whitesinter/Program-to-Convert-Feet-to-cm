// This is a Java program which converts the value of feet into cm   
import java.io.*;   
class convert {   
static double Conversion_feet_to_cm(int feet)   
{   
double centimeter;  
centimeter  = 30.48 * feet;    
System.out.printf("Value in Centimeter is: %.2f \n", centimeter);   
return 0;   
}    
public static void main(String args [])   
{   
int feet = 20;   
Conversion_feet_to_cm(feet);   
}  
}  
