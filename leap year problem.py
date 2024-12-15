
i=int(input("Enter the value"))
if i%4==0 or i%100==0:
   print("LEAP YEAR")
else:
   print("Its not an LEAP YEAR")
   
print("____________")
sum=0
n=int(input("Enter the value="))
for i in range (1,n+1):
    sum+=1/(i)
print(sum)