# Creating a class
class Student:
    pass
student1 = Student()
print(student1)

# Giving objects data
class Student:
    def __init__(self, name, age):
        self.name = name # Store this student's name inside this specific object.
        self.age = age
student1 = Student("Godwin", 24)

print(student1.name)
print(student1.age)

# Exercise
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
car1 = Car("Toyota", 2024)

print(car1.brand)
print(car1.year)

# challenge; it will print the dog name, which is Buddy

class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Godwin")
student2 = Student("Sarah")