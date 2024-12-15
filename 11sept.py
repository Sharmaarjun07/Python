#set
#they are unordered, unchangable, unindexed and donot allow duplicate value
#in keyword in set is used to check wether the element is present in the set or not
thisset={"apple","banana","cherry"}
print("banana" in thisset) 
print("_________")
#to add value in set.....can update the value in anywhere 
thisset.add("orange")
print(thisset)
print("_________")
#can update the set
tropical={"pineapple","mango"}
thisset.update(tropical)
print("new=",thisset)
print("__________________________")

#add any iterable
#an update the tuble and list same
thisset1={"apple","banana","cherry1"}
mylist=["kiwi","orange"]
thisset1.update(mylist)
print(thisset1)
print("_________")
#(discard) keyword
thisset.discard("banana")
print(thisset)
print("_________")
#clear method clear all the items present in the set...and (del)..delete the cell completely
#del thisset 
#print(thisset)

print("_________")
#union,#update
#or we can use "|" to join the sets
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)

print(set3)

print("_________")
#intersection()==will keep the duplicates only
set1={"a","b","c"}
set2={1,2,3,"a"}
set3=set1.intersection(set2)
print("_________")
#intersection_update=will not form the new set
set10={"a","b","c"}
set20={1,2,3,"a"}
set10.intersection_update(set20)
print(set10)
print("_________")
print("_________")
#difference()==
set1={"a","b","c"}
set2={1,2,3,"a"}
set3=set1.difference(set2)

print(set3)
print("_________")
#symmetric_difference()==will not print the common things or use just (^)
set1={"a","b","c"}
set2={1,2,3,"a"}
set3=set1.symmetric_difference(set2)

print(set3)
print("_________")
#intersection 
set11={"apple",1,"banana",0,"cherry"}
set22={False,"google",1,"apple",2,True}
set33=set11.intersection(set22)
print(set33)
print("_________")
#to check the set is frozen set or not
{frozenset({1,2}),frozenset({3,4})}
a={3,4,1,2}
c={1,2}
print(c.issubset(a))
print("_________")
print("_______________")
#WAP that creates  two sets of sq and cubes in range 1-10.You have t demonststre update ,remove,add ,clear, function
set1=set()
set2=set()
for i in range(1,11):
    set1.add(i*i)
    set2.add(i*i*i)
    i=+i

print(set1)
print(set2)
print("_______________")
set3={"mango"}
set1.update(set3)#update operation
print(set1)
print("_______________")
set1.remove("mango")#remove fncn
print(set1)
print("_______________")
set1.clear()
print (set1)
print("_______________")
#wap two create sets one in even no. 1-10..and other all composite no.1-20. 
#..demonstrate the use of all ()..
set1=set()
set2=set()
for i in range(1,11):
    if i%2==0:
     set1.add(i)
print(set1)
for num in range(2, 21):  # Start from 2 since 1 is not a composite number
  for j in range(2, int(num**0.5) + 1):
    if num % j == 0:
     set2.add(num)
print(set2)
print("_________________")
#numpy
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(np.__version__)#to check the version
print(type(arr))#to check the type of array.....nd array means n dimensional array
print("_________________")
#0d array
import numpy as np
arr=np.array(42)
print(arr)
#1d array
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)  
print("_________________") 
#2d array
import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)  
print(arr.ndim) #to check the dimension of array
print(arr[0,1])#to access the 1st row and second element
print("_________________")
#3d array
import numpy as np
arr=np.array([[[1,2,3],[5,6,7]],[[9,8,7],[10, 11,12]]])
print(arr)  
print(arr.ndim) 
print(arr[0,1,2])               
print("_________________")

