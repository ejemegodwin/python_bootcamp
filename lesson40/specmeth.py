# Special Methods in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

    def __len__(self):
        return self.age

person = Person("Godwin", 24)
print(person)  # Output: Person(Name: Godwin, Age: 24)
print(len(person))  # Output: 24

# Another example
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"{self.brand} ({self.year})"
car = Car("Toyota", 2024)
print(car)  # Output: Toyota (2024)

# Exercise: Create a class called `Book` with attributes `title` and `author`, and implement the `__str__` method to return a string representation of the book in the format "Title by Author".
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("Atomic Habits", "James Clear")
print(book) 

# Challenge: it will print "Buddy"