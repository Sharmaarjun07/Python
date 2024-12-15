#Write a program to calculate the distance between two points.
#import the lib of math to do Sq.rt
import math
# made the function 
def dis(x,y,x1,y1):
   d=math.sqrt((x-x1)**2+(y-y1)**2)
   return d
#made another fncn to import the values
def main():
 x=float(input("Enter value of x="))
 y=float(input("Enter value of y="))
 x1=float(input("Enter value of x1="))
 y1=float(input("Enter value of y1="))
# Calculate distance
 d=dis(x, y, x1, y1)
 print(f"The distance between the points ({x}, {y}) and ({x1}, {y1}) is {d:.2f}")
 #calling the main fncn  to take the input value first
main()





