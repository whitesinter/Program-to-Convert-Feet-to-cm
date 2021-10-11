# This is a Python program which converts centimeter length to feet and Inches   
      
centimeter=int(input("Enter the height in centimeters:"))  
#convert centimeter to inches  
inches = 0.394 * centimeter  
#convert centimeter to feet  
feet = 0.0328 * centimeter  
     
print("The length in feet",round(feet,2))  
print("The length in inches",round(inches,2))  
