#lists
marks=[3,5,6]
print(type(marks))
print(marks[0])
#23
l=[11,32,3,4]
print(l)
l.append(7)#add the 7 in last of list
print(l)
l.sort()#sort the list in ascending order
print(l)
print (l.index(3))#will give the index value
l.insert(1,899)#insert the 899 on index 1
print(l)
#24
#Tuple
#Tuple value can't be changed
Tup=(12,13,45,5)
print(type(Tup),Tup)
if 13 in Tup:
    print("yes present")
#25
c=("spain","italy","india")
list1=list(c)#to convert the tuple to list if uh want to edit the tuple
list1.append("russia")
c=tuple(list1)#again covert it back to tuple
print(c)

