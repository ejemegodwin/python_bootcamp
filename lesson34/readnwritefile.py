file = open("notes.txt", "w")
file.write("Hello, Godwin!")
file.close()

# Reading a file
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()

# Exercise
messages = open("message.txt", "w")
messages.write("Python is awesome!")
messages.close()
message = open("message.txt", "r")
content = message.read()
print(content)
message.close()

# challenge; when this program runs it will first of all creat a file name test.txt, it content will be Hello and World in a new line then close.