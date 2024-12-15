#day 37
#Finally Keyword
#finally will get executed even if it get returned...used to close the file etc
try:
    l=[1,2,3,4]
    i=int(input("Enter the index value"))
    print(l[i])
except:
    print("Some Error Occured")
finally:
    print("I awlyas get executed")
    
#day 38
#Raising Custom errors
#by using the raise keyword
a=int(input("Enter any value bw 5 and 9="))
print(f"No. entered is={a}")
if (a<5 or a>9):
    raise ValueError("Value should be bw 5 and 9")
#similarly:-FloatingPointError, ImportError,ModuleNotError,MemoryEoor 
#We can make our own error also

