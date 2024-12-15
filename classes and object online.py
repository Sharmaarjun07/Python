class  Car:              #creating class
    color="blue"         #its object
    brand="mercedes"
car1=Car()               #creating object of class
print(car1.color)        #using the class object
print(car1.brand)

#constructor
#__init__
class Student:
    name="Karan"
    def __init__(self):#object created it means,,,and it is an constructor...call itself
        print("adding new student")
        
s1=Student()

#EXAMPLE2
class Student1:
    def __init__(self,fullname):
        self.name=fullname   #step2...name is the new variable made in which value os full name is assigned
        #or we can write self.name=name
        print("hello student")
s2=Student1("RAMAN SHARMA")#step1 raman sharma name will pass to full name in def init constructor
print(s2.name)

#20:40
class Student2:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is:",sum/3)
s3=Student2("Tony", [99,98,97])
s3.get_avg()
#static methods----ont use self keyword
class Student5:
    @staticmethod  # decorator
    def college():
        print("ABC college")
s4=Student5()
s4.college()   
    
    
    
    
    
    
    
    
    
    
    
    