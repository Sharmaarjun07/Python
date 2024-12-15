list=[1,2,3,4,5,6,7,8,9,10]
for index,i in enumerate(list):
    print(i,"at index" ,index)
print("_______________")
def square(item):
    squares=[]
    for I in item:
        squares.append(I**2)
    return squares
my_list=[17,52,8]
my_result=square(my_list)
print("list=",my_result)
print("_______________")
def evenodd(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")
evenodd(5)#calling of fncn
print("_______________")
def nameage(name,age):
    print("name=",name)
    print("age=",age)
print("case1")
nameage("suraj",27)
print("case2")
nameage(27,"suraj")
print("_______________")
a=lambda g,h:(g*h)
print(a,(4,5))

#LOCAL AND GLOBAL VARIABLES
var="good"#global
def show():
    global var1
    var1="sunday"#local
show()
print("outside function var1 is",var1)
print("var is",var)
print("____________")


def sub(a,b):
    c=a-b
    print("sub",c)
sub(7,5)
print("__________")
def evenodd(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")
evenodd(5)
print("__________")
def time(h,m):
    tt=(h*60)+m
    print(tt,"mins")
h=int(input("Enter hour time"))
m=int(input("Enter min time"))
time(h,m)
print("__________")
#wap to swap two numbers
a=10
b=20
c=a
b=c
print(b)
print(a)
print("__________")
amount=int(input("enter the amount"))
time=int(input("enter the time"))
age=int(input("enter the age"))
if age>=60:
    Sim=(amount*12*time)/100
else:
    Sim=(amount*10*time)/100
    
print("simple interest",Sim)
print("Total amount=",amount+Sim)

