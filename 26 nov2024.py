
#SYNTAX ERROR
#it occurs when we violate the rules of python .


#LOGIC ERROR
#it specifies all those type of error in which the program executes but gives incorrect results...it may occur due to  wrong algo. or logic
#to solve a particular program..in some caces logic errors may need to divide by zero or excessing an item in a list where the index of the item 
#is outside the bound of a list in this case logic error leads to run time error that cause the prog to terminate abrupteluy..these type of run type error are called exceptions


#EXCEPTION
#it occurs during the execution of prog. and distrupt the normal flow of the program
#it as an object that represents an error

#HANDLING EXCEPTION
#try block and exccept block
#a criticl operation which can raise exception is placed inside the try block and the code that handles exception is placed under except block
#try:
      #statements
#except(name):
      #statement

#Q1wap to handle the divide by zero exception?
num=int(input("Enter the value of numerator=")) 
denominator=int(input("Enter the value of denominator=")) 
try:   
    q=num/denominator
    print("q=", q)
except ZeroDivisionError:
    print("Denominator cannot be zero")
    
#multiple exception in single block
#an except block may name multiple exception as parenthise exceptions ...so ehat ever exception is raise that except block is executed out of those exceptions

try:   
    num=int(input("  "))
    print(num**2)
except(KeyboardInterrupt,TypeError,ValueError):
    print("Check before prog. terminate")
    
#The Else clause
#try an except block can exceptionally have an else block...ehich when present must follow all except block...


#RAISING EXCEPTIONS
#syntax will be raise[Exception[,args[,traceback]]]
try:
    num=10
    print(num)
    raise ValueError
except:
    print("EXCEPTION OCCURED")

#Instentiating exceptions
#python allows programmers to intentiate excep  ..first before raising it and adds any attribute to it as desired..these attributes is used to give
#additional info about error
#SYNTAX:- except Exception as error obj

try:
      num=10
      print(num)
      raise ValueError
except Exception as errorobj:  
      print(type(errorobj))   
    
#print(errorobj.args)



#FINALLY
 #used to define clean up actions that must be used under all circumstances...alwwys executed before leaving try block   
 #try to finally(Finallly will alwys be executed)
 
 
#assertions
   #an asssertion is an basic check that can be turned on or off when the prog is being tested 
 
#syntax:- assert expression[,arguments]   
    
#Q. WAP that prompts a user to enter a number   and print the square of that number if no number is entered  ..thena keyboard 
#interrupt is genrated
    
try:
    a=int(input("ENTER A VALUE"))
    b=a*a
    print(b)
except (KeyboardInterrupt):
   print("enter value first") 
    
    
#WAP which infinitely print natural numbers ... raise the stop iteration exception after displaying first 20 numbers exit from the program
def display():
    n = 0  # Starting from 0 (natural numbers can start from 1, but let's go with 0 here for clarity)
    while True:
        try:
            n += 1  # Increment the number
            if n == 21:  # After displaying the 20th number, raise StopIteration
                raise StopIteration
            print(n)  # Print the number
        except StopIteration:
            break  # Exit the loop after the 20th number is displayed

# Call the function to display numbers
display()


    
    
    
    
    