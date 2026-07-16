# Writing with (with)
with open("notes.txt", "w") as file:
    file.write("Hello, Python!")

# Reading with (with)
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Exercise
with open("greeting.txt", "w") as file:
    file.write("Welcome to Python!")
with open("greeting.txt", "r") as file:
    content = file.read()
    print(content)

# challenge; it will print ABC, the first two line open and write to demo.txt, then the last two line will read from demo.txt, print what it see inside and close automatically.

with open("demo.txt", "w") as file:
    file.write("ABC")

with open("demo.txt", "r") as file:
    print(file.read())