class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")

student = Student("Godwin")
student.introduce()

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")
dog.bark()

# Exercise: Create a class called `Person` with attributes `name` and `age`, and a method called `greet` that prints a greeting message including the person's name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person = Person("Godwin", 24)
person.greet()

# Challenge; it will print "Luna, says Meow".
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says Meow!")

cat = Cat("Luna")
cat.meow()