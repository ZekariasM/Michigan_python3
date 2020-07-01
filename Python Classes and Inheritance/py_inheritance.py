# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class
# Create a class named `Person`, with firstname and lastname properties, and a `printname` method:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
		
    def printname(self):
        print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

x = Person("Zeki", "Mulu")
x.printname()

print("XXXXXXXXXXXXXXXXXXXXXXXXX")

# Create a Child Class
#########################

class Student(Person):
    pass

x = Student("Alemu", "Chala")
x.printname()

print("XXXXXXXXXXXXXXXXXXXXXXXXX")

#############################
# Add the __init__() Function
#############################

# We want to add the __init__() function to the child class (instead of the `pass` keyword).
























