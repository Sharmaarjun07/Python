import time
t = time.strftime('%H:%M:%S')
print(t)
hour = int(time.strftime('%H'))
print(hour)

if (hour > 0 & hour < 12):
    print("Good Morning")
    # day 28
    # "f" String
    name = "arjun"
print(f"hello my name is {name}")
print("___________")
# day 29


def square(n):
    '''Takes in number n,return the square of n'''  # it is a doc string that is used as a code
    print(n**2)


square(5)
print(square.__doc__)  # call the doc string
print("___________")
# day30
#recursion
def factorial(n):
    if (n==0 or n==1):
     return 1
    else:
     return n*factorial(n-1)
print (factorial(4))
print("___________")
def fibonacci_series(n):
    if n<=1:
        return 1
    else:
        return(fibonacci_series(n-1)+fibonacci_series(n-2))
n=10
for i in range(n):
    print(fibonacci_series(i))
print("___________")
#day 31
#sets = in sets the words cannot be repeated and closed in curly brackets
#and there is no gurantee of order 
s={1,2,3,2}
print(s)
print("___________")
#day 32
#operations on set
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2)) #s1+s2
print("___________")
print(s1.intersection(s2)) #s1-s2
print("___________")
print(s1.symmetric_difference(s2)) #except the common value
print("___________")
print(s1.issuperset(s2))
print("___________")
#day 33
#dictionary
dic={"Harry":"Human Being",
     "spoon":"object"
     }
print(dic["Harry"])
print("___________")
dict1={
       344:"harry",
       561:"shubham",
       678:"zakir",
       567:"neha"
       }
print(dict1[567])
print("___________")
#day 34
#dictionary methods
ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.update(ep2)#update the value
print(ep1)
print("___________")
ep1.pop(122)#pop out the value 122
print (ep1)
print("___________")
del ep1[123]
print(ep1)
print("___________")
#day35
#for loop with else in python
for i in range(6):
    print(i)
    if i==4:
     break
else:
    print("Sorry no i")
print("___________")
#day36
#Exception Handling
#using try and except(this is used to run the other half of the code which dont have any error)
a=input("enter the value:")  
print(f"The multiplication table for {a} is")
try: 
 for i in range(1,11):
     print(f"{int(a)} X {i}={int(a)*i}")
except Exception as e: #to write except
 print(e)
print("SOME IMP LINES")
#Similarly
b=input("enter the value:")  
print(f"The multiplication table for {b} is")
try: 
 for i in range(1,11):
     print(f"{int(b)} X {i}={int(b)*i}")
except :
 print("SOME IMP LINES")