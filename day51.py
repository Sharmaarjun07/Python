#day 51
#Seek() Tell() 
from functools import reduce#import reduce

with open('day41.py','r')as f:
     print(type(f))
     f.seek(10)# Move to the 10th byte in the file by ignoring them
     print(f.tell())
     data=f.read(5)#read the 5 elements of file
     print(data)
 
print("_______________________")   
with open('day41.py','w')as f:
    f.write('Helo World!!')
    f.truncate(5)#give the limit to file that only 5 characters can be included
with open('day41.py','r')as f:
    print(f.read())
print("_______________________")
    
    
#lambda fncn 
double=lambda x:x**2
print(double(5))   
#or
avg=lambda x,y:(x+y)/2
print(avg(3,4))
 
#day53
#Map, Filter and Reduce
def cube(x):
    return x*x*x
l=[1,2,4,6,4,3]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)
#or we can do simple use of  map
newl=list(map(cube,l))#CUBE is the name of function ...and l is the list on which u want to perform fncn
print(newl)           #we have to give a fncn

#FILTER ....it is used as a filter
def filter_fncn(a):
    return a>2
newnewl=list(filter(filter_fncn,l))
print(newnewl)


#REDUCE
numbers=[1,2,3,4,5]
def mysum(x,y):
    return x+y

sum=reduce(mysum,numbers)#first add 1+2...then add the sum of 1&2 i.e 3 in 3..then add 6 in 4
print(sum)#and give output as 15
print("__________________")
#day56
#procedural programming...that we have done so far...made functions and call them
#object-oriented programing...simple and easy to use by making classes and objects and link
#it with real time entities

#day 57
#classes AND objects
class person: #create a class
    name="Harry"
    occupation="Software Developer"
  
    def info(self):#made a fncn in class...and self argument is imp to give
     print(f"{self.name} is a {self.occupation}")#call everytime a.name and b.name
    
a=person() #calling the class
b=person()
c=person()
a.name="Shubham"
a.occupation="Accountant"
b.name="Ramesh"
b.occupation="Doctor"
c.name="harsh"
c.occupation="Soldier"
a.info()
b.info()
c.info()
print("__________________")

#day58
#Constructor
#def __init__(self):
    #when we call a fncn the constructor in it always get called
class Person:
    def __init__(self,n,o):#CONSTRUCTOR...and the (self,n,o) are the arguments
        print("HEllo")
        self.name=n
        self.occ=o
        
    def info(self):#FUNCTION
        print(f"{self.name} is a {self.occ}")
a=Person("HArry","Developer")
b=Person("Divya","HR")
a.info() 
b.info()  

print("__________________")

#day59
#Decorators =>@greet
def greet(fx):
    def mfx():
        print("GOOD MORINING")#every time call first this 
        fx()#call the fncn
        print("THANKS FOR USING THIS FNCN")#everytime at last call
    return mfx
@greet
def hello():
    print("HELLO EVERYONE")

hello()
print("__________________")
   
#day 60
#Getters and Setters
#Getters are methods that are used to aceess the values of an objects properties
# @property is used to declare getter
 


#INHERITANCE
class Employee:#main class
    def __init__(self,name,id):#constructor
     self.name=name
     self.id=id
 
    def showDetails(self):#fncn
        print(f"The name of the Employee:{self.name} its ID is {self.id}")

class programmer(Employee):#sub class ...inherit properties of parent class
    def showlanguage(self):#fncn
        print("The default lang is Python")
e1=Employee("Rohan", 420)
e1.showDetails()#calling the fncn of parent class
e2=Employee("Gangan", 122)#always use these values
e2.showDetails()#calling the fncn
e2=programmer("Harry",345)
e2.showlanguage()#calling the fncn from child class

#day62
#Access Modifiers



















