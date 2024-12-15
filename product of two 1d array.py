#WAP To multiply two 1D Array
array1=[1,2,3,4,5]
array2=[6,7,8,9,10]
result=[]

for i in range(len(array1)):
    
        c=array1[i]*array2[i]
        result.append(c)

print("ARRAY1",array1)
print("ARRAY2",array2)
print("RESULT:", result)