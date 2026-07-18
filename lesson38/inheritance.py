# Lesson38 - Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name}.")
class Student(Person):
    pass

student = Student("Godwin", 24)
student.greet()

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
student = Student("Godwin", 24, "Computer Science")

# Exercise; 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says Woof! Woof!!")

class Dog(Animal):
    pass
dog = Dog("Buddy")
dog.speak()

# Challenge; it will print "Animal sound"