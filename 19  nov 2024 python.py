class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def enterMarks(self):
        for i in range(3):
            m = int(input(f"Enter marks of {self.name} in subject {i + 1}: "))
            self.marks.append(m)

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


# Creating instances of the Student class
s1 = Student("Anisha")
s1.enterMarks()

s2 = Student("Jay")
s2.enterMarks()

# Displaying the details
s1.display()
s2.display()
#Wap with class employee that keeps a track of the numbers of employees  in an organisation and also stores there name, designation 
#and salary details,initialsise that with zero and update count 
class Employee:
    count = 0  # Class variable to track the number of employees

    def __init__(self, name, desi, salary):
        self.name = name
        self.desi = desi
        self.salary = salary
        Employee.count += 1  # Increment count when a new employee is created

    def display(self):
        # Display employee details
        print(f"Name: {self.name}, Designation: {self.desi}, Salary: {self.salary}")

    def display_count(self):
        # Access the class variable `count` using self
        print(f"Total number of employees: {Employee.count}")


# Create employee instances
emp1 = Employee("John", "Software Engineer", 50000)
emp2 = Employee("Smith", "Data Scientist", 60000)
emp3 = Employee("Johnson", "Product Manager", 75000)

# Display individual employee details
emp1.display()
emp2.display()
emp3.display()

# Display total number of employees using an instance
emp1.display_count()  # Can be called from any instance



#wap that has a class circle use a class variable to define the value constatnt pi(3.14). then use this class variabe to calculate area 
#and circumfrance of a circle with specified radius.

class Circle:
    # Class variable for the constant value of pi
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius  # Instance variable for the circle's radius

    def calculate_area(self):
        # Formula: Area = π * r^2
        return Circle.pi * self.radius ** 2

    def calculate_circumference(self):
        # Formula: Circumference = 2 * π * r
        return 2 * Circle.pi * self.radius


# Example usage
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

# Calculate and display area and circumference
area = circle.calculate_area()
circumference = circle.calculate_circumference()

print(f"Circle with radius {radius}:")
print(f"Area = {area:.2f}")
print(f"Circumference = {circumference:.2f}")

#wap an menu driven prog. that keeps record of books and generals available in lib.
#create a class book make constructor (02)
#fncn:- read(TITLE ,AUTHOR, PRICE) and display(PRINT TITLE AUTHOR AND PRICE)
#call read and display




























