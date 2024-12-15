# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:07:50 2024

@author: HP
"""

#1 Calculate Area of Circle 
a=int(input("Enter the radius="))
area1=3.14*a*a
print("AREA=",area1)

#2 WAP to print  ones digit of number
a=int(input("Enter the number"))
c=a%10
print("ones digit no.",c)

#3 WAP to find avg of two numbers and there deviation too
Num1=int(input("Enter a number 1:"))
Num2=int(input("Enter a number 2: "))
Avg=(Num1+ Num2)/2
Deviation1=Num1-Avg
Deviation2=Num2-Avg
print("The deviation between Number1 and Avg is",Deviation1)
print("The deviation between Number2 and Avg is",Deviation2)

#4 WAP to covert floating number its corresponding integer 
Floating_Number=float(input("Enter the value"))
integer_value=int(Floating_Number)
print("The value after conversion from float to integer is ",integer_value)

#5 WAP to convert Fahrenheit to Celsius 
Fahrenheit=int(input("Enter the number"))
Celsius=(5/9)*(Fahrenheit-32)
print("Fahrenheit value is",Fahrenheit, "and in Celsius its value is ",Celsius)