#Dictionary
# use {} for dictionary
dict={'Name':'Zara','Age':7,'class':'First'}
print("dict['Name']:",dict['Name'])
print("dict['Age']:",dict['Age'])

#updating
dict={'Name':'Zara','Age':7,'class':'First'}
dict['Age']=8
print("dict['Age']:",dict['Age'])

#delete
del dict['Name']
print(dict)

#properties
#it will replace with the last value ..like zwa wil get replaced by zara
dict={'Name':'Zara','Age':7,'Name':'Ankit'}
print(dict)
#to print the length of dictionary
print (len(dict))


#to print the whole dictionary
print("Equivalent string :%s"%str (dict))


#to check the type 
print("TYPE %s"%type(dict))


#to take a specific value frm list
print("Value:%s"%dict.get('Age'))


#to return the list of dict
print("value:%s"%dict.items())


#to find the value
print("value:%s" % dict.setdefault('Age', None))
print(dict)



print("_____________________")


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict1.update(dict2)
print(dict1)

print("____________________")

dict={'a':'time','b':'money','c':'value'}
print(dict)

for key, value in dict.items():
    print(f' {key} ')
   

for key, value in dict.items():
 print(f'{value}')

print("____________________")
#for arranging it in sorted manner

#my_dict = {'b': 2, 'a': 1, 'c': 3}

#sorted =dict(sorted(my_dict.items()))
#print(sorted)
print("____________________")

#armstrong
 # take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")











