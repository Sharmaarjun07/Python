#WAp to swap two values using tuple assignment
T1=(1,2,3)
T2=(4,5,6)
print("First tuple=",T1)
print("Second tuple=",T2)
T1,T2=T2,T1
print("\n SWAAPPING")
print("T1=",T1)
print("T2=",T2)
print("______________")

#WAP USing fncn that return a circle whose radius is passed as an argument
def area(R):
    A=(3.14*(R**2))
    return A
def circum(C):
    C=2*(3.14*(R))
    return C
R=int(input("Enter radius of the circle="))
X=area(R)
Y=circum(R)

print("Area of circle",X)
print("Circumfrance of circle",Y)
print("______________")
#seprate the terms before and after the @ using tuple

email=str(input("Enter email="))
local_part, domain_part = email.split('@', 1)
        
# Create tuples for each part..
local_tuple = (local_part,)
domain_tuple = (domain_part,)

print(local_tuple,"@" ,domain_tuple)
  
print("______________")
#WAP that has a nested list to store topper details.Edit the details and reprint the details.
list1=['Arjun','MSc','94']
enter=input("enter=")
if enter=='Name':
       print("Enter the correct Name") 
       new_name=input("Name=")
       list1[0] = new_name
       print(list1)
elif enter=='Sub':
        print("Enter the correct Subject") 
        new_sub=input("Subject=")
        list1[1] = new_sub
        print(list1)
elif enter=='Marks':
        print("Enter the correct Marks") 
        new_marks=input("Marks=")
        list1[2] = new_marks
        print(list1)
else:
    print("Invalid input. Please enter 'Name', 'Sub', or 'Marks'.")