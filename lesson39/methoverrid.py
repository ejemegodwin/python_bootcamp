# Method Overriding in Python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")
dog = Dog()
dog.speak()  # Output: Woof!

class Cat(Animal):
    def speak(self):
        print("Meow!")
cat = Cat()
cat.speak()  # Output: Meow!

class Bird(Animal):
    def move(self):
        print("Bird flies")
bird = Bird()
bird.move()  # Output: Bird flies

# Exercise;
class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")
cat = Cat()
cat.speak() 

# challenge; it will print "Hello, I am a teacher."