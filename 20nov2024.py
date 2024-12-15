#single inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
class Lion(Animal):
    def roar(self):
        print("Lion roaring")
d=Lion()
d.roar()
d.speak()

#multiple inheritance
class Calculation1:
    def Addition(self,x,y):
        return x+y;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Division(self,a,b):
        return a/b;
d=Derived()
print(d.Addition(2,4))
print(d.Multiplication(2,4))
print(d.Division(2,4))

#Multi-level inheritance
class Animal:
    def speak(self):
        print("animal speaking")
class Lion(Animal):
    def roar(self):
        print("lion roaring")
class BabyLion(Lion):
    def eat(self):
        print("eating meat...")
d=BabyLion()
d.roar()
d.speak()
d.eat()


#Hierarchial inheritance[many child class leads to 1 parent class]
#hybrid [multiple inheritance and multilevel inheritance]


#polymorphism{same operator/fncn is used with diff names or forms/tasks}
#1.overloading
#ability of fncn or operator to behave diff depending on the fncn .
#Method or fnccn overloading type of polymor. in which we can define a no. 
#of methods with same name but diff numbers of parameters as well as parameters can be of diff types
def addition(a,b):
    x=a+b
    print(x)
def addition(a,b,c):
    x=a+b+c
    print(x)
#addition(2,5).........it will give error(as python doesnot support method overloading)
addition(2,5,6)


#operator overloading
#use + for addition as well as concatenation strings as + operator is overloaded by int and str class
#with operator overloading a programmer is allowed to provide his own defination for an opetaror for an 
#class by overloading te build in operator:
#hence we are able to perform some specific computation when the operator is applied on 
#clsss object and to apply a standard defination ..when the same op. is appied on built in data type

print(3+2)
print("GHK"+"inno")


#overriding
#means having two methods wit the same name but doing diff tasks. it means that one of the methods overrides the other
class Employee:
    def message(self):
        print("this message is from employee")

class Company(Employee):
    def message(self):
        print("this is comany ingertited employee")


emp=Employee()
emp.message()
comp=Company()
comp.message()

#HYBRID AND MULTILEVEL INHERITANCE
#parent class1
class Employee:
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id

    def display_info(self):
        return f"Name:{self.name},ID:{self.employee_id}"
#parent class2
class Manager():
    def manage_team(self):
        return"Managing team tasks"
#parent class3 inheriting from manager
class Developer(Manager):
    def write_code(self):
        return"Writing code"

#child class inheriting from employee and manager

class SalesExecutive(Employee,Manager):
    def handle_clients(self):
        return"Handling client meetings"



#create instance of child classes
sales_executive=SalesExecutive("Jhon Doe","SE001")
#qa_engineer=QAEngineer("Alice Smith","QA001")

#Accessing methods
print(sales_executive.display_info())
print(sales_executive.manage_team())
print(sales_executive.handle_clients())




#Wap that has a class point define another class location  which has two object location and destination also define a fncn in location that prints the reflection 
#of destination on the x axis

class Point:
 def __init__(self, x, y):
  self.x = x
  self.y = y
  self.x_new = 0
  self.y_new = 0
 def display_point(self):
  print(f'X = {self.x}, Y = {self.y}')
class Location(Point):
 def reflection(self):
  self.y_new = self.y * -1
  self.x_new = self.x
  print(f'X_relected = {self.x_new}, Y_reflected = {self.y_new}')
location = Location(1, 2)
destination = Location(10, 20)
location.display_point()
destination.display_point()
destination.reflection()

#WAP that has classes :-course,department,and  Enrol an student in the course in a particular dept

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.courses = []  # List to hold courses in the department

    def add_course(self, course):
        self.courses.append(course)
        print(f"Course {course.course_name} added to the {self.dept_name} department.")

    def __str__(self):
        return f"Department: {self.dept_name}, Courses: {[course.course_name for course in self.courses]}"


class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.enrollments = []  # List to hold enrolled courses

    def enroll(self, course, department):
        if course in department.courses:
            self.enrollments.append((course, department))
            print(f"Student {self.student_name} enrolled in {course.course_name} ({department.dept_name} department).")
        else:
            print(f"Error: {course.course_name} is not available in the {department.dept_name} department.")

    def __str__(self):
        enrolled_courses = [
            f"{course.course_name} ({dept.dept_name})" for course, dept in self.enrollments
        ]
        return f"Student: {self.student_name} (ID: {self.student_id}), Enrollments: {enrolled_courses}"


# Create departments
cs_department = Department("Computer Science")
math_department = Department("Mathematics")

# Create courses
course1 = Course("Python Programming", "CS101")
course2 = Course("Data Structures", "CS102")
course3 = Course("Linear Algebra", "MATH101")

# Add courses to departments
cs_department.add_course(course1)
cs_department.add_course(course2)
math_department.add_course(course3)

# Create a student
student1 = Student("Alice", "S123")

# Enroll the student in courses
student1.enroll(course1, cs_department)
student1.enroll(course3, cs_department)  # Should show an error
student1.enroll(course3, math_department)

# Display student details
print(student1)



