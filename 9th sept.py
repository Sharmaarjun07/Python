#Slicing in array
import array as arr
l=[1,2,3,4,5,6,7,8,9,10]
a=arr.array('i',l)
print("Initial Array:")
for i in (a):
    print(i,end=" ")
    Sliced_array=a[3:8]
    print("\nSlicing elements in a range 3-8:")
    print(Sliced_array)
    Sliced_array=a[5:]
    print("\nElements sliced from 5th")
    print(Sliced_array)
    Sliced_array=a[:]
    print("\nPrinting all elements using slice operation")
    print(Sliced_array)


print("___________________________")

#index method
import array
arr=array.array('i',[1,2,3,1,2,5])
print("The new created array is",end="")
for i in range(0,6):
    print(arr[i],end=" ")
print("\r")
print("the index of 1st occurance of  2is:",end=" ")
print(arr.index(2))
print("The index of 1st occurance of 1:",end=" ")
print(arr.index(1))

print("___________________________")

#update the index value
import array 
arr=array.array('i',[1,2,3,4,5,6,7,8])
print("array before updation:",end=" ")
for i in range(0,6):
    print(arr[i],end=" ")
    
print("___________________________")
#count  the value of 2 occured
import array
my_array=array.array('i',[1,2,3,4,5,6,7,3,2,2])
count=my_array.count(2)
print("Number of occurances of 2:",count)

print("___________________________")

#sorting=focus on the size of data like the n. of characters
#Syntax=sorted_list=sorted(unsorted_list,key=len)
def Sorting(lst):
    lst2=sorted(lst,key=len)
    return lst2

lst=["rohan","amy","sapna","abs","aakash","raunak"]
print(Sorting(lst))

print("___________________________")
#Bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
      for j in range(0,n-i-1):
          if arr[j]>arr[j+1]:
              arr[j],arr[j+1]=arr[j+1],arr[j]
          
#Exaple usage
if __name__=="__main__":
    sample_list=[64,34,25,22,12,11,90]
    print("Original list",sample_list)

bubble_sort(sample_list)
print("Sorted list",sample_list)
print("___________________________")

#Tuples
Tuple1=()
print("Initial empty Tuple:")
print(Tuple1)
#creating
Tuple1=('Hello','sam')
print("\nTuple with the use of String:")
print(Tuple1)

list1=[1,2,3,4,5,6]
print("\nTuple using list")
print(tuple(list1))

Tuple1=tuple('sam')
print("\n with the use of fncn:")
print(Tuple1)
      
print("__________________________")
#creating a tuple with mixed data types)

Tuple1=(5,'Welcome',7,'pie')
print("\nTuple with Mixed Datatypes")
print(Tuple1)

#creating a tuple
Tuple1 =(0,1,2,3)
Tuple2=('python','course')
Tuple3=(Tuple1,Tuple2)
print("\nTuplewith nested tuples:")
print(Tuple3)

#creating a tuple
Tuple1=('Sam',)*3 
print("\nTuplewith repetition")
print(Tuple1)

Tuple1=('Sam')
n=5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1=(Tuple1,)
    print(Tuple1)
print("__________________________")

#concatination of tuples
# Tuple unpacking
Tuple1 = ("Sam", "is", "Dancing")
# This Line unpack
# values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking:")
print(a)
print(b)
print(c)

# Concatination of tuples
Tuplel = (0, 1, 2, 3)
TupLe2 = ('Sam', 'is', 'Studying')
Tuple3 = Tuple1 + Tuple2
# Printing first Tuple
print ("Tuple 1: ")
print(Tuple1)
# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)
# Printing Final Tuple
print("\nTuples after Concatenation")
print(Tuple3)

print("__________________________") 
#del()....
#tuples are immutable and by suing del() the whole tuple will get deleted
#Tuple Assignment
def max_min(vals):
    x=max(vals)
    y=min(vals)
    return(x,y)
vals=(99,98,97,89,86)
(max_marks,min_marks)=max_min(vals)
print("Highest Marks=",max_marks)
print("Lowest Marks=",min_marks)
print("__________________________") 
#Printing the tuples
Toppers=(("aarav","BSc",92.0),("chahat","BCA",97))
for i in Toppers:
    print(i)
print("__________________________") 
Topper=("jhanvi",[94,95,97])
print("class Topper:",Topper[0])
print("Higest Scores",Topper[1:])
print("__________________________") 
thisistuple=("apple","banana","cherry")
for i in range(len(thisistuple)):
    print(thisistuple[i])
print("__________________________") 



