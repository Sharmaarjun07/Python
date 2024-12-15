i=0
sum1=0
sum2=0
M= [182, 162, 114, 134, 154, 155,161,170,124,136,140,127,140,129,132,124,131,173,180,128]
for i in range (len(M)):
    sum1=sum1+M[i]
avg1=sum1/len(M) 
print("Xm=",M)
print("Xm`=",avg1)

for i in range (len(M)):
    x=M[i]-avg1
    sum2=sum2+(x*x)
print("(Xm-Xm`)^2=",sum2)

var=sum2/(len(M)-1)
print("var=",var)
    
    
print("----------------")


j=0
sum3=0
sum4=0
W= [78, 82, 58, 61, 74, 108,81,90,67,58,64,50,74,58,60,54,59,92,83,78]
for j in range (len(W)):
    sum3=sum3+W[j]
avg2=sum3/len(W) 
print("Xw=",W)
print("Xw`=",avg2)

for j in range (len(W)):
    y=W[j]-avg2
    sum4=sum4+(y*y)
print("(Xw-Xw`)^2=",sum4)

var1=sum4/(len(W)-1)
print("var=",var1)

print("----------------")

avgt=0  
for i in range(len(M)):

        avgn = (M[i] - avg1) * (W[i] - avg2)
        print(f"Product of deviations for M[{i}] and W[{j}] = ",avgn)
        avgt += avgn
print("avgn",avgt)

covar=avgt/(len(W)-1)
print("So the Covar is",covar)

print("----------------")
print(var,covar)
print(covar,var1)