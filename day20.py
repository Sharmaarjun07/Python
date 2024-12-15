def fn(a,b): #creating a functin.
    c=a+b
    print("sum1",c)
def avg(a,b) :  
     pass #if u leave the fncn with no statement it is mandatory to write this.
a=10
b=20 
fn(a,b)   #callling the fncn

a=40
b=90
fn(a,b)
#day21
#function arguments
def average(e=10,f=4):
    print("Average=",(e+f)/2)
    
average(e=6)   #here it will only consider the second given value of e.
#NEW CODE
def averagee(*numbers): #to store no. in touple
 print(type (numbers))
 sum=0
 for i in numbers:
        sum=sum+i
        return sum/len(numbers)
    
c=averagee(5,6,7,8)
print("averagee=",c)
