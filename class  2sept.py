for i in range(2,4): 
    for j in range(1,11):
#priniting the loop 
       print(i, "*", j, "=", i*j)
print()
print("______________")
# NESTED LOOP TO PRINT PATTERN 
rows = 5
#outer loop
for i in range(1, rows+1):
#inner loop 
      for j in range(1, i+1): 
          print("*",end="") 
      print('')
print("______________")
   # nested loop to print patterens 
for i in range(1, rows+1):
      for j in range(1, i+1): 
          print(i,end="")

      print('')
print("______________")
# 2nd
n=5
for i in range (1, n+1):
        for k in range(n, i,-1): 
            print(" ", end = '')
        for j in range(1, i+1): 
            print(i, end=' ') 
        print('')
print("______________")
row=5
column=3
for i in range (row):
        print("* "*column) 
   #wap to classify a given no. into prime or composite
   #wap to cal. a factorial of a no.
print("______________")
n=int(input("enter the number="))
flag=0
if n==0 or n==1 :
      print("no. is not  prime")
elif n>1:
    for i in range (2,n):  
        if(n%i)==0: 
          flag=1
    if (flag==1):
        print("non prime")
    else:
      print("prime")     
print("______________") 
facto=1
fact=int(input("enter the value")) 
for i in range (1,fact+1):
  facto=facto*i
print(facto)
print("______________") 
